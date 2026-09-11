#!/usr/bin/env python3
"""
wormhole.py -- THE FORK, TAKEN.  M chose the throat.

entsym.py put a fork and declined to choose it: a throat supplies the two
systems entanglement needs, and makes the object a wormhole.  M: "if wormhole
makes sense for this, then let's run with it.  It seems to me that what we are
looking at currently is the ability to create and contain a stable wormhole."

This file prices that architecture against the corridor.  ONE LARGE WIN, ONE
REVERSAL OF AN EARLIER ANSWER, AND ONE SCOPE DECISION THAT IS M'S TO MAKE.

===============================================================================
1. THE WIN, AND IT IS STRUCTURAL: COST DOES NOT SCALE WITH DISTANCE
===============================================================================

        CORRIDOR   cost proportional to the DISTANCE SHORTENED
                   1.3489e26 kg per metre, so one per cent off four light
                   years is 5.1048e40 kg = 2.567e10 SOLAR MASSES.

        WORMHOLE   cost proportional to the THROAT RADIUS, and to NOTHING
                   ELSE.  M ~ r_0 c^2/(8 pi G), independent of how far apart
                   the mouths are.

        throat r_0       M_exotic (kg)      Earth masses
        1 um             5.3579e+19         8.97e-06
        1 m              5.3579e+25         8.97          <- ANY separation
        10 m             5.3579e+26         89.7
        3 km             1.6074e+29         2.69e+04

    A ONE-METRE THROAT COSTS ABOUT NINE EARTH MASSES, WHETHER THE MOUTHS ARE A
    METRE APART OR FOUR LIGHT YEARS APART.  Against the corridor's 2.567e10
    solar masses for one per cent of Alpha Centauri, that is 15.0 ORDERS, and
    the ratio grows without limit with the distance.

    THIS IS WHY THE LITERATURE WORKS ON WORMHOLES AND NOT ON CORRIDORS, and
    phase1's own complaint -- "a saving that does not scale with the journey is
    not a faster journey" -- is exactly what the throat fixes.

===============================================================================
2. BUT IT REVERSES contain.py.  A WORMHOLE WANTS TO BE LARGE.
===============================================================================

Kuhfittig (arXiv:2409.16184) eq. (32), the radial tension at the throat:

        tau(r_0)  =  c^4 / (8 pi G r_0^2)

        r_0          tau (Pa)         dyn/cm^2
        1 m          4.8155e+42       4.8155e+43
        10 m         4.8155e+40       4.8155e+41     <- his "~5e41 (10 m/r_0)^2"
        3 km         5.3505e+35       5.3505e+36     <- neutron-star centre

    BOTH OF HIS FIGURES REPRODUCE HERE.  And the exponent is the point: TAU
    GOES AS 1/r_0^2, so shrinking the throat makes the tension WORSE.  His own
    conclusion, and he is a wormhole advocate: "Morris-Thorne wormholes could
    only exist on very large scales."

        contain.py CONCLUDED THAT MINIATURE WAS FORCED.  THAT WAS THE
        CORRIDOR'S ANSWER AND IT DOES NOT TRANSFER.  For a corridor the
        quantum ceiling lets a smaller core hold more mass; for a throat the
        tension diverges as it shrinks.  THE TWO ARCHITECTURES WANT OPPOSITE
        SIZES, and M's "contain in miniature" belongs to the one we just left.

===============================================================================
3. AND THE REQUIREMENT IS THE ONE WE ALREADY HAD, TO A FACTOR OF 2 pi^2
===============================================================================

        seatindex.py   T_kk required   =  pi c^4/(4 G l^2)   = 9.5053e43 / l^2
        wormhole       tau at throat   =  c^4/(8 pi G r_0^2) = 4.8155e42 / r_0^2

        ratio = 19.739209        2 pi^2 = 19.739209        EXACT

    THE SAME 2 pi^2 as entangle.py's holographic excess and, times three,
    spec.py's collapse ratio -- currency.py reconciled those two and this is
    the third face of the same constant.

        THE WORMHOLE IS NOT A NEW PHYSICS PROBLEM.  IT IS THE SAME
        REQUIREMENT IN A GEOMETRY THAT SPENDS IT BETTER.

===============================================================================
4. WHAT THE THROAT REOPENS
===============================================================================

    ENTANGLEMENT.  Two boundaries exist now, so entsym.py's obstruction lifts:
        there are two subsystems for the symmetric relation to relate.

    GJW APPLIES DIRECTLY rather than by analogy.  Their O_L O_R coupling has
        its two boundaries, and their bank-loan theorem and traversal window
        become live constraints on THIS object instead of a borrowed example.

    AND MTY REOPENS AS A RISK.  anecscope.py closed the Morris-Thorne-Yurtsever
        construction on structure -- no throat, no two ends to age
        differentially.  THAT CLOSURE IS NOW GONE.  The known mitigation is
        GJW's own: their coupling breaks the H_L - H_R Killing symmetry and
        "fixes the relative time coordinate between them, excluding the
        possibility of having closed time-like curves".  Live, not fatal, and
        no longer answerable by "we have no throat".

===============================================================================
5. THE SCOPE DECISION, AND IT IS M'S
===============================================================================

Kuhfittig is a wormhole advocate and his section 7 still says this:

    "The most important conclusion for our purposes is that Phi'(r) = 0 is
     outside this range, so that the resulting wormhole solution CANNOT BE
     COMPATIBLE WITH QUANTUM FIELD THEORY.  This also applies to the wormhole
     solutions in Ref. [3]."

    Ref. [3] IS MORRIS AND THORNE.  So the canonical zero-tidal-force
    traversable wormhole is incompatible with QFT in CLASSICAL GENERAL
    RELATIVITY, said by someone arguing for wormholes.

His escape, and the escapes in the neighbouring literature, all leave GR:

        f(R) MODIFIED GRAVITY -- his sections 6 and 8, on the ground that "the
            estimates of the local curvature needed to apply Inequality (26)
            come from Einstein's theory, not from the modified theory".  That
            is an argument that the QI DERIVATION does not transfer, not a
            demonstration that the bound is absent.  WEAK, AND FLAGGED AS WEAK.

        NONCOMMUTATIVE GEOMETRY -- his section 9, smearing the source.

    BOTH CHANGE THE THEORY.  M's standing constraint is "everything we claim is
    accurate and true" and "true and proven in its math".  Adopting f(R) or a
    noncommutative background is a decision to prove something in a DIFFERENT
    THEORY, and it should be taken deliberately or not at all.

        WITHIN CLASSICAL GR THE THROAT BUYS GEOMETRY, NOT PERMISSION.  Cost
        stops scaling with distance -- which is real, large, and the reason to
        take the fork -- and the exotic source is exactly as unavailable as it
        was.

stdlib only.  seatindex.py supplies the seating coefficient this file matches
to 2 pi^2; phase1.py the corridor's exchange rate.
"""
import math, sys

C, G = 2.99792458e8, 6.67430e-11
MSUN, MEARTH, LY = 1.98892e30, 5.9722e24, 9.4607e15
LAMBDA = 9.982529


# ------------------------------------------------- 1: cost, and how it scales

def corridor_mass(dd_metres, lam=LAMBDA):
    """Proportional to the DISTANCE shortened."""
    return dd_metres * C ** 2 / (G * lam)


def throat_mass(r0):
    """M ~ r_0 c^2/(8 pi G).  Proportional to the THROAT, and nothing else."""
    return r0 * C ** 2 / (8.0 * math.pi * G)


def cost_scales_with_distance(architecture):
    return architecture == "corridor"


def advantage_at(dd_metres=0.01 * 4.0 * LY, r0=1.0):
    return corridor_mass(dd_metres) / throat_mass(r0)


def advantage_grows_with_distance():
    """The corridor's bill grows with the trip; the throat's does not."""
    return advantage_at(0.10 * 4.0 * LY) > advantage_at(0.01 * 4.0 * LY)


# --------------------------------------- 2: and it reverses contain.py

def throat_tension(r0):
    """Kuhfittig eq. (32): tau = c^4/(8 pi G r_0^2).  Diverges as r_0 -> 0."""
    return C ** 4 / (8.0 * math.pi * G * r0 * r0)


def tension_in_dyn_cm2(r0):
    return throat_tension(r0) * 10.0


NEUTRON_STAR_CENTRE_PA = 5.35e35          # his r_0 = 3 km comparison


def smaller_throat_is_worse(a=1.0, b=10.0):
    return throat_tension(a) > throat_tension(b)


def wants_to_be_large():
    """tau ~ 1/r_0^2.  contain.py's 'miniature' was the CORRIDOR's answer."""
    return smaller_throat_is_worse()


# ------------------------------- 3: the same requirement, to a factor of 2 pi^2

def seating_coefficient():
    import seatindex
    return seatindex.T_COEFF                      # pi c^4/(4G)


def throat_coefficient():
    return C ** 4 / (8.0 * math.pi * G)


def coefficient_ratio():
    return seating_coefficient() / throat_coefficient()


def ratio_is_two_pi_squared(rtol=1e-9):
    return abs(coefficient_ratio() - 2.0 * math.pi ** 2) <= rtol * 2.0 * math.pi ** 2


# ------------------------------------------------- 4: what the throat reopens

REOPENED = (
    ("entanglement", "two boundaries exist, so entsym.py's obstruction lifts"),
    ("GJW", "applies DIRECTLY rather than by analogy; bank-loan and traversal "
            "window become live constraints on this object"),
    ("MTY", "RISK REOPENED -- anecscope.py closed it on 'no throat, no two ends "
            "to age differentially', and that closure is gone"),
)


def mty_still_closed_on_structure():
    """No.  The structural closure was the absence of a throat."""
    return False


MTY_MITIGATION = ("GJW's coupling breaks the H_L - H_R Killing symmetry and "
                  "fixes the relative time coordinate, excluding CTCs")


# --------------------------------------------------- 5: the scope decision

KUHFITTIG_ON_GR = ("Phi'(r) = 0 is outside this range, so that the resulting "
                   "wormhole solution CANNOT BE COMPATIBLE WITH QUANTUM FIELD "
                   "THEORY.  This also applies to the wormhole solutions in "
                   "Ref. [3]")           # Ref. [3] is Morris & Thorne

ESCAPES = (
    ("f(R) modified gravity", False,
     "on the ground that the QI's curvature estimates 'come from Einstein's "
     "theory, not from the modified theory' -- an argument that the DERIVATION "
     "does not transfer, not that the bound is absent.  WEAK"),
    ("noncommutative geometry", False,
     "smearing the source; an intrinsic modification of spacetime"),
)


def any_escape_stays_in_gr():
    return any(in_gr for _n, in_gr, _w in ESCAPES)


THROAT_BUYS = "geometry, not permission"

# ---------------------------------------------------------------------------
# THE SCOPE DECISION, MADE.  2026-09-11.
#
# This flag was None from the day this file was written, and asserted None in
# its own selftest so that nobody -- me included -- could resolve it quietly by
# letting an instrument drift into modified gravity and calling the result
# proven.  gaps.py classified it as the SINGLE DECISION-grade gap in the whole
# census: the one gap that was not a computation, a search or a conjecture, and
# the only one that was M's rather than anyone's to calculate.
#
# THREE ASSERTIONS IN A ROW LANDED ON IT before it was made:
#   orient.py     black bounces as VACUUM solutions of metric theories in four
#                 and higher dimensions (arXiv:2608.02771) -- a throat inside a
#                 horizon with NO exotic matter, but not in GR
#   emtension.py  a black bounce sourced by NON-MINIMALLY COUPLED linear
#                 electrodynamics (arXiv:2608.08208) -- xi =/= 0 is the one
#                 published route past w = 1, and non-minimal is outside GR
#   emtension.py  and the reason: linear minimally-coupled EM is PINNED at
#                 w = 1 by a symmetry, so nothing inside GR can cross it
#
# M CHOSE.  MODIFIED GRAVITY COUNTS.
#
# WHAT THAT DOES AND DOES NOT DO, because a decision is not a result:
#   IT DOES     turn the corridor from a PROHIBITION into a BILL.  Inside GR
#               certify.py's m < 0 is a theorem and expose.py found no exposed
#               positive-mass instance in 3.5e6 sampled points; outside GR the
#               same geometry is a vacuum solution and there is no exotic
#               matter to buy.  The question becomes what CONSTRUCTION costs,
#               and nobody has computed that.
#   IT DOES NOT make anything proven.  Every result derived under this scope
#               is CONDITIONAL ON IT and must say so.  A scope choice is a
#               declaration about what will be argued, not evidence.
#   IT DOES NOT retroactively license anything already recorded.  Findings
#               seated before this date were derived in GR and stay GR.
# ---------------------------------------------------------------------------
SCOPE_CHOSEN_HERE   = "modified gravity counts"   # M's constraint, M's decision
SCOPE_CHOSEN_BY     = "M"
SCOPE_CHOSEN_ON     = "2026-09-11"
SCOPE_IS_A_RESULT   = False    # a declaration about what will be argued
RESULTS_UNDER_SCOPE_ARE_CONDITIONAL = True
SCOPE_LICENSES_EARLIER_FINDINGS     = False


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

    print("1. THE WIN -- cost stops scaling with distance")
    near("corridor, 1 % off 4 ly (kg)", corridor_mass(0.01 * 4.0 * LY), 5.1048e40, 1e-4)
    print("      %10s %16s %14s" % ("throat r0", "M_exotic (kg)", "Earth masses"))
    for r in (1.0e-6, 1.0, 10.0, 3000.0):
        print("      %10.4g %16.4e %14.4g" % (r, throat_mass(r), throat_mass(r) / MEARTH))
    near("one-metre throat, in Earth masses", throat_mass(1.0) / MEARTH, 8.9714, 1e-4)
    near("advantage over the corridor at 1 % of 4 ly", advantage_at(), 9.528e14, 1e-3)
    chk("and the advantage GROWS with distance", advantage_grows_with_distance(), True)
    chk("corridor cost scales with distance", cost_scales_with_distance("corridor"), True)
    chk("throat cost scales with distance", cost_scales_with_distance("wormhole"), False)

    print("\n2. BUT IT REVERSES contain.py -- a throat wants to be LARGE")
    for r in (1.0, 10.0, 3000.0):
        print("      r0 = %-8.4g tau = %.4e Pa = %.4e dyn/cm^2"
              % (r, throat_tension(r), tension_in_dyn_cm2(r)))
    near("Kuhfittig's ~5e41 dyn/cm^2 at 10 m", tension_in_dyn_cm2(10.0), 4.8155e41, 1e-3)
    near("and neutron-star centre at 3 km", throat_tension(3000.0),
         NEUTRON_STAR_CENTRE_PA, 1e-2)
    chk("a smaller throat is worse", smaller_throat_is_worse(), True)
    chk("so the architecture wants to be large", wants_to_be_large(), True)
    print("      contain.py's 'miniature is forced' was the CORRIDOR's answer.")
    print("      THE TWO ARCHITECTURES WANT OPPOSITE SIZES.")

    print("\n3. AND THE REQUIREMENT IS THE ONE WE ALREADY HAD")
    near("seatindex T_kk coefficient", seating_coefficient(), 9.5053e43, 1e-4)
    near("throat tension coefficient", throat_coefficient(), 4.8155e42, 1e-4)
    near("ratio", coefficient_ratio(), 2.0 * math.pi ** 2, 1e-9)
    chk("exactly 2 pi^2", ratio_is_two_pi_squared(), True)
    print("      the same constant as entangle.py's holographic excess and,")
    print("      times three, spec.py's collapse ratio.  Same problem, better")
    print("      geometry -- not a new one.")

    print("\n4. WHAT THE THROAT REOPENS")
    for n, why in REOPENED:
        print("      %-14s %s" % (n, why[:58]))
    chk("MTY still closed on structure", mty_still_closed_on_structure(), False)
    print("      mitigation: %s" % MTY_MITIGATION[:60])

    print("\n5. THE SCOPE DECISION, AND IT IS M'S")
    print("      Kuhfittig, a wormhole ADVOCATE, on classical GR:")
    print("        \"%s\"" % KUHFITTIG_ON_GR[:64])
    print("        ...and Ref. [3] is MORRIS AND THORNE.")
    for n, in_gr, why in ESCAPES:
        print("      %-24s in GR: %-5s %s" % (n, in_gr, why[:34]))
    chk("any escape stays inside GR", any_escape_stays_in_gr(), False)
    chk("the scope is now CHOSEN", SCOPE_CHOSEN_HERE, "modified gravity counts")
    chk("  by whom", SCOPE_CHOSEN_BY, "M")
    chk("  and when", SCOPE_CHOSEN_ON, "2026-09-11")
    chk("  a choice is not a result", SCOPE_IS_A_RESULT, False)
    chk("  results under it are CONDITIONAL", RESULTS_UNDER_SCOPE_ARE_CONDITIONAL, True)
    chk("  and it licenses nothing already seated", SCOPE_LICENSES_EARLIER_FINDINGS, False)
    chk("within classical GR the throat buys", THROAT_BUYS, "geometry, not permission")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE FORK IS WORTH TAKING, AND FOR ONE REASON THAT IS LARGE AND
  STRUCTURAL: A THROAT'S COST DOES NOT SCALE WITH DISTANCE.  The
  corridor charges 1.3489e26 kg per metre shortened, so one per cent
  off Alpha Centauri is 2.567e10 solar masses.  A one-metre throat
  costs about nine Earth masses whether the mouths are a metre apart
  or four light years apart -- 15.0 orders, and the ratio grows
  without limit with the distance.  phase1's own complaint, that a
  saving which does not scale with the journey is not a faster
  journey, is exactly what the throat fixes.

  BUT IT REVERSES AN ANSWER GIVEN TWO PASSES AGO.  The throat tension
  is c^4/(8 pi G r_0^2) and DIVERGES AS THE THROAT SHRINKS --
  4.8e42 Pa at a metre, and only at about three kilometres does it
  fall to the pressure at the centre of a neutron star.  contain.py
  concluded that miniature was forced; that was the CORRIDOR's answer,
  where the quantum ceiling lets a smaller core hold more mass.  THE
  TWO ARCHITECTURES WANT OPPOSITE SIZES.

  AND THE REQUIREMENT IS THE ONE WE ALREADY HAD.  The throat
  coefficient and seatindex's seating coefficient differ by EXACTLY
  2 pi^2 -- the same constant as entangle.py's holographic excess and,
  times three, spec.py's collapse ratio.  The wormhole is not a new
  physics problem; it is the same requirement in a geometry that
  spends it better.

  THE THROAT ALSO REOPENS WHAT IT WAS MISSING.  Entanglement has its
  two subsystems, GJW applies directly rather than by analogy -- and
  MTY comes back as a live risk, because anecscope.py closed it on
  "no throat", and there is a throat now.  GJW's own coupling is the
  known mitigation.

  AND ONE DECISION IS M'S, NOT MINE.  Kuhfittig, arguing FOR
  wormholes, says the zero-tidal-force solution -- Morris and Thorne's
  own -- cannot be compatible with quantum field theory in classical
  GR.  Every escape in that literature leaves General Relativity:
  f(R) modified gravity, on the weak ground that the QI derivation
  does not transfer, or a noncommutative background.  Against a
  standing constraint of "true and proven in its math", adopting
  either is a decision to prove something in a DIFFERENT THEORY.

  WITHIN CLASSICAL GR, THE THROAT BUYS GEOMETRY AND NOT PERMISSION.
  The distance scaling is fixed, which is real and worth having.  The
  exotic source is exactly as unavailable as it was.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
