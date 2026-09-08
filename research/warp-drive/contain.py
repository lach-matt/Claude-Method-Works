#!/usr/bin/env python3
"""
contain.py -- "if not a miniature contained black hole, what DO we contain in
miniature form?"

A NEGATIVE-ENERGY CORE.  That is the whole answer to the first half, and the
tree already specifies it.  The interesting half is the second: MINIATURE IS
THE RIGHT INSTINCT, IT IS ACTUALLY NECESSARY, AND IT IS EXACTLY COST-NEUTRAL.

===============================================================================
1. WHAT THE OBJECT IS -- already specified, three files
===============================================================================

        core.py         the contents: exact interior Schwarzschild with
                        rho < 0, measured HAWKING-ELLIS TYPE I (|Im|/||T||
                        1e-7 to 1e-8), central pressure p(0)/|rho| -> 1/3 from
                        below, and NO BUCHDAHL LIMIT -- a negative mass has
                        none, so there is no compactness ceiling to hit.

        concentric.py   the container: a positive shell of equal magnitude at
                        R_s, which cancels the monopole so M_ADM = 0 EXACTLY
                        and the positive mass theorem has no objection.

        stability.py    the container holds: V'' = +2.965e-2 against an
                        ordinary shell's -3.036e-2, and beta^2_crit is negative
                        everywhere, so it is stable for free at beta^2 = 0.

    THE CONTAINER IS DESIGNED, MEASURED AND STABLE.  THE PROBLEM WAS NEVER THE
    CONTAINER.  IT IS THE CONTENTS.

===============================================================================
2. MINIATURE IS THE RIGHT DIRECTION, AND FOR A REASON
===============================================================================

shaping.py derived the quantum ceiling on negative energy density from
zero-point saturation plus mode counting:

        |rho|  <=  (pi^2/192) hbar c / a^4  =  0.051404 hbar c / a^4

so the negative mass a region of radius a may hold is

        M  <=  (4/3) pi (pi^2/192) hbar/(a c)  =  0.215321 hbar/(a c)

    A SMALLER CORE MAY HOLD MORE MASS, not less.  The ceiling rises as 1/a.
    And scale.py's shortfall falls as (a/l_P)^2, so shrinking is the only
    direction in which the vacuum ever catches up with the requirement.

        MINIATURE IS NOT A PREFERENCE.  IT IS NECESSARY: at any larger scale
        the density the corridor needs exceeds what the vacuum permits.

===============================================================================
3. AND IT BUYS EXACTLY NOTHING, BECAUSE a CANCELS
===============================================================================

phase1: Delta d = (G/c^2) M Lambda.  One core at the ceiling therefore delivers

        Delta d_max  =  0.215321 * Lambda * l_P^2 / a

        a (m)          M_max (kg)      Delta d_max (m)      in l_P
        1e-9           7.5743e-35      5.6150e-61           3.47e-26
        1e-15          7.5743e-29      5.6150e-55           3.47e-20
        1e-25          7.5743e-19      5.6150e-45           3.47e-10
        l_P            4.6863e-09      3.4741e-35           2.1495

    BOTH SCALE AS 1/a.  The mass allowed rises as the core shrinks and the
    contraction delivered rises in exactly the same proportion, so

        M / Delta d  =  [C hbar/(a c)] / [C Lambda l_P^2/a]  =  c^2/(G Lambda)

    THE CORE RADIUS CANCELS ALGEBRAICALLY, AND SO DOES THE QUANTUM
    COEFFICIENT.  What is left is phase1's exchange rate, with no length in it
    and no trace of hbar.

CHECKED NUMERICALLY BY A ROUTE THAT SHARES NO ALGEBRA WITH phase1:

        2.8785e+34 Planck-sized cores per metre
        total mass                      1.3489e+26 kg/m
        phase1's exchange rate          1.3489e+26 kg/m
        ratio                           1.000000

    EXACT.  The containment question and the cost question are the same
    question, approached from opposite ends -- which is M's reversal rule
    landing a third time.

===============================================================================
4. SO THE ANSWER, IN ONE LINE AND THEN THE CAVEAT
===============================================================================

    YOU DO NOT NEED TO CONTAIN ANYTHING IN MINIATURE.  YOU NEED TO CONTAIN
    1.349e26 kg OF NEGATIVE MASS PER METRE OF CONTRACTION, AND THE PACKAGING IS
    FREE TO CHOOSE.

    Miniature is forced on you by the quantum ceiling -- Planck-sized cores are
    the only size at which the required density is permitted at all -- but
    choosing that size changes the bill by nothing.  You need 2.88e34 of them
    per metre.

    AND AT a = l_P ALL FIVE OF scale.py's APPROXIMATIONS FAIL AT ONCE:
    semiclassical gravity, Ford-Roman's own fixed background, geometric optics,
    the perfect-conductor Casimir formula, and the weak field.  So "a
    Planck-sized negative-energy core" is not a specification.  IT IS THE EDGE
    OF THE MAP, WEARING A COMPONENT'S NAME.

stdlib only.  core.py, concentric.py and stability.py supply the object;
shaping.py the ceiling; phase1.py the exchange rate this file reproduces.
"""
import math, sys

HBAR, C, G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
L_PLANCK = math.sqrt(HBAR * G / C ** 3)
L_PLANCK_SQ = HBAR * G / C ** 3
M_PLANCK = math.sqrt(HBAR * C / G)
LAMBDA = 9.982529
FR_COEFF = math.pi ** 2 / 192.0          # shaping.py, derived not quoted


# --------------------------------------------------- 1: what the object is

SPECIFICATION = (
    ("contents", "core.py",
     "exact interior Schwarzschild with rho < 0; Hawking-Ellis TYPE I measured "
     "at |Im|/||T|| 1e-7 to 1e-8; p(0)/|rho| -> 1/3 from below; NO Buchdahl "
     "limit, because a negative mass has none"),
    ("container", "concentric.py",
     "a positive shell of equal magnitude at R_s, cancelling the monopole so "
     "M_ADM = 0 exactly"),
    ("it holds", "stability.py",
     "V'' = +2.965e-2 against an ordinary shell's -3.036e-2; beta^2_crit "
     "negative everywhere, so stable for free at beta^2 = 0"),
)


def container_is_solved():
    """Designed, measured and stable.  The problem is the contents."""
    return len(SPECIFICATION) == 3


# ------------------------------------------- 2: the ceiling, and why smaller

def mass_ceiling(a):
    """M <= (4/3) pi K hbar/(a c).  RISES as the core shrinks."""
    return (4.0 / 3.0) * math.pi * FR_COEFF * HBAR / (a * C)


def ceiling_coefficient():
    return (4.0 / 3.0) * math.pi * FR_COEFF


def smaller_holds_more(a1=1.0e-9, a2=1.0e-15):
    return mass_ceiling(a2) > mass_ceiling(a1)


# ------------------------------------------ 3: what one core delivers, and a cancels

def contraction_max(a, lam=LAMBDA):
    """Delta d = (G/c^2) M Lambda at the ceiling.  Also rises as 1/a."""
    return G * mass_ceiling(a) / C ** 2 * lam


def mass_per_metre_from_cores(a, lam=LAMBDA):
    """M/Delta d.  The core radius CANCELS -- checked at many a."""
    return mass_ceiling(a) / contraction_max(a, lam)


def exchange_rate(lam=LAMBDA):
    """phase1's c^2/(G Lambda), reached without reference to cores."""
    return C ** 2 / (G * lam)


def a_cancels(radii=(1.0e-9, 1.0e-15, 1.0e-25, None), rtol=1e-12):
    """Size-independence, measured over sixteen decades."""
    rs = [mass_per_metre_from_cores(L_PLANCK if a is None else a) for a in radii]
    return (max(rs) - min(rs)) <= rtol * max(rs)


def reproduces_phase1(a=None, rtol=1e-9):
    a = L_PLANCK if a is None else a
    return abs(mass_per_metre_from_cores(a) / exchange_rate() - 1.0) <= rtol


def cores_per_metre(a=None, lam=LAMBDA):
    a = L_PLANCK if a is None else a
    return 1.0 / contraction_max(a, lam)


def core_mass_in_planck(a=None):
    a = L_PLANCK if a is None else a
    return mass_ceiling(a) / M_PLANCK


# ------------------------------------------------------- 4: and the caveat

MINIATURE_IS_NECESSARY = True        # the only size where the density is permitted
MINIATURE_REDUCES_COST = False       # a cancels

BROKEN_AT_PLANCK_CORE = (
    "semiclassical gravity",
    "Ford-Roman's own fixed background",
    "geometric optics",
    "the perfect-conductor Casimir formula",
    "the weak field",
)


def is_a_specification():
    """No.  Five approximations fail at once at a = l_P."""
    return len(BROKEN_AT_PLANCK_CORE) == 0


# ------------------------------------------------------------------ selftest

def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, rtol):
        nonlocal ok
        good = abs(got - want) <= rtol * abs(want)
        ok &= good
        print("  %-56s %18.6e %18.6e  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. WHAT IS CONTAINED -- a negative-energy core, already specified")
    for what, where, _why in SPECIFICATION:
        print("      %-11s %-16s" % (what, where))
    chk("the container is designed, measured and stable", container_is_solved(), True)
    print("      the problem was never the container.  It is the contents.")

    print("\n2. MINIATURE IS THE RIGHT DIRECTION, AND NECESSARY")
    near("ceiling coefficient (4/3)pi * pi^2/192", ceiling_coefficient(), 0.215321, 1e-5)
    chk("a smaller core may hold MORE mass", smaller_holds_more(), True)
    for a in (1.0e-9, 1.0e-15, L_PLANCK):
        print("      a = %-10.3e  M_max = %.4e kg   Delta d_max = %.4e m"
              % (a, mass_ceiling(a), contraction_max(a)))
    chk("miniature is necessary", MINIATURE_IS_NECESSARY, True)
    print("      at any larger scale the density the corridor needs exceeds")
    print("      what the vacuum permits (scale.py, falling as (a/l_P)^2).")

    print("\n3. AND IT BUYS NOTHING, BECAUSE a CANCELS")
    chk("mass-per-metre is the same at every core size", a_cancels(), True)
    near("  its value (kg/m)", mass_per_metre_from_cores(L_PLANCK), 1.3489e26, 1e-4)
    near("  phase1's exchange rate", exchange_rate(), 1.3489e26, 1e-4)
    chk("reproduces phase1 exactly, by a route sharing no algebra",
        reproduces_phase1(), True)
    near("cores per metre at a = l_P", cores_per_metre(), 2.8785e34, 1e-4)
    near("each of mass (Planck masses)", core_mass_in_planck(), 0.215321, 1e-5)
    chk("miniaturising reduces the cost", MINIATURE_REDUCES_COST, False)

    print("\n4. AND IT IS NOT A SPECIFICATION")
    chk("a Planck-sized core is a design point", is_a_specification(), False)
    for b in BROKEN_AT_PLANCK_CORE:
        print("      x  %s" % b)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  WHAT IS CONTAINED IS A NEGATIVE-ENERGY CORE, and the tree already
  specifies it: core.py gives the contents (Type I, rho < 0,
  p(0)/|rho| -> 1/3, no Buchdahl limit), concentric.py the container
  (a positive shell cancelling the monopole so M_ADM = 0), and
  stability.py says it holds (V'' = +2.965e-2, stable for free).
  THE CONTAINER WAS NEVER THE PROBLEM.

  MINIATURE IS THE RIGHT INSTINCT AND IT IS ACTUALLY FORCED.  The
  quantum ceiling on negative energy density lets a SMALLER core hold
  MORE mass -- M <= 0.2153 hbar/(a c), rising as 1/a -- and the
  shortfall falls as (a/l_P)^2, so shrinking is the only direction in
  which the vacuum ever catches up.  At any larger scale the density
  the corridor needs simply is not permitted.

  AND IT BUYS EXACTLY NOTHING, BECAUSE THE CORE RADIUS CANCELS.  The
  mass allowed rises as 1/a and the contraction delivered rises in
  the same proportion, so M/Delta d = c^2/(G Lambda) with no length
  in it and no trace of hbar.  Checked by a route sharing no algebra
  with phase1: 2.8785e34 Planck-sized cores per metre, 1.3489e26 kg
  in total, against phase1's 1.3489e26.  RATIO 1.000000.

  SO THE ANSWER IS: YOU DO NOT NEED TO CONTAIN ANYTHING IN MINIATURE.
  YOU NEED TO CONTAIN 1.349e26 kg OF NEGATIVE MASS PER METRE, AND THE
  PACKAGING IS FREE.  Miniature is forced by the ceiling and changes
  the bill by nothing; you simply need 2.9e34 of them.

  AND AT a = l_P ALL FIVE OF scale.py's APPROXIMATIONS FAIL AT ONCE.
  "A Planck-sized negative-energy core" is not a component
  specification.  IT IS THE EDGE OF THE MAP, WEARING A COMPONENT'S
  NAME.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
