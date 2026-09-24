#!/usr/bin/env python3
r"""
xigate.py -- PUSHING THE T = 1 ROUTE, AND FINDING THAT ITS GATE IS AN EXCHANGE
RATE RATHER THAN A WALL.

M: "Push on the T=1 route."

The non-minimal route is the only door in this tree that OVERSHOOTS on
magnitude -- by about 1200x -- and its gate was recorded as the hierarchy
problem: Barcelo-Visser need |phi| > M_red / sqrt(xi), so at the Higgs VEV the
required coupling is xi = 9.78e31 = (v/M_red)^-2 exactly, more than 1e27 above
the value Higgs inflation uses. That framing is right and it is not the whole
statement.

    THE 1e27 SHORTFALL BELONGS TO THE HIGGS, NOT TO THE ROUTE.
    AND WHAT REPLACES IT IS AN EXACT TRADE, NOT A WALL.

    python3 xigate.py             the reading
    python3 xigate.py --selftest  fixtures

===============================================================================
1. THE GATE CLOSES AT THE GUT SCALE, ON A COUPLING ALREADY IN USE
===============================================================================

xi_required = (M_red / phi)^2 falls as the square of the field scale, and the
Higgs VEV is small.  Seat the scalar higher and the coupling needed collapses:

    field scale                phi (GeV)     xi required     vs Higgs inflation
    Higgs VEV (electroweak)     2.46e+02      9.78e+31          5.8e+27
    1 TeV                       1.00e+03      5.93e+30          3.5e+26
    see-saw / intermediate      1.00e+11      5.93e+14          3.5e+10
    **GUT scale**               2.00e+16      **1.48e+04**      **0.87**
    reduced Planck mass         2.44e+18      1.00e+00          5.9e-05

**AT THE GUT SCALE THE REQUIRED COUPLING IS 1.48e4 -- 0.87 TIMES THE xi THAT
HIGGS INFLATION ALREADY USES, I.E. BELOW IT.**  Not an exotic value, not a tuned
one, a number already in the cosmology literature for a different purpose.

    CORRECTED (DOCKET 63, ruling F9).  The first draft pinned its own
    XI_HIGGS_INFLATION = 1e4 while higgs.py pins 1.7e4 for the same named
    constant (Bezrukov-Shaposhnikov, NAMED-NOT-READ) -- two values for one
    constant -- and against 1e4 it called the GUT requirement "ONE AND A HALF
    TIMES" Higgs inflation's.  The constant is now IMPORTED from higgs.py, so
    the last column above is against 1.7e4 and the ratio is 0.87.  The first
    pin is kept as XI_HIGGS_INFLATION_AS_FIRST_PINNED, withdrawn.  THE FINDING
    DOES NOT MOVE: the GUT-scale requirement is within a factor of two of a
    coupling already in use, now from below instead of above.  HBAR_C was also
    retyped here (:119 of the first draft); it is now higgs.HBAR_C / GEV_IN_J.  The gate is
the hierarchy problem only because the Higgs sits sixteen orders below the Planck
scale; a field that does not sit there does not inherit it.

===============================================================================
2. AND THE THROAT CLOSES AT THE SAME PLACE, EXACTLY
===============================================================================

At the gate xi phi^2 = M_red^2, so the effective Planck scale IS the field
scale and the geometry is modified at the field's own Compton length.  Which
means the coupling you can reach and the throat you get are not independent:

    field scale        xi required     throat (m)     in Planck lengths
    Higgs VEV           9.78e+31        8.0e-19         5.0e+16
    see-saw             5.93e+14        2.0e-27         1.2e+08
    GUT scale           1.48e+04        9.9e-33         6.1e+02
    reduced Planck      1.00e+00        8.1e-35         5.0e+00

    AND THE RELATION IS EXACT, TO EVERY DIGIT TESTED:

            xi_required  =  (throat / l_P)^2 / (8 pi)

verified at five scales spanning sixteen orders, ratio 1.000000 at each.  The
8 pi is not fitted: it is M_Planck^2 / M_red^2, the same factor that separates
the two Planck masses, entering because the gate is written in one and the
throat in the other.

===============================================================================
3. WHAT THAT MEANS, AND IT IS NEITHER THE GOOD NEWS NOR THE BAD ONE ALONE
===============================================================================

**THE GATE IS AN EXCHANGE RATE.**  A reachable coupling is buyable, and the
price is throat size, one for one, at a fixed rate of 8 pi.  You cannot pay it
down: every order of magnitude you gain in xi costs half an order in throat
radius, forever, because both are the same function of phi.

So the T = 1 route is not blocked by the hierarchy problem.  It is blocked by
the fact that ITS TWO REQUIREMENTS ARE THE SAME REQUIREMENT SEEN TWICE.  At the
only field scale where the coupling is ordinary, the throat is six hundred
Planck lengths.

**AND THIS IS scale.py's THEOREM ARRIVING FROM A NEW DIRECTION.**  That file
proved every route in this tree crosses the feasibility line within two orders
of l_P, and proved the convergence INEVITABLE rather than deep.  The T = 1 route
was the one candidate that overshot, and pushing it produces the same crossing,
now with an exact coefficient rather than a coincidence.  A prediction the tree
made before this route was pushed, confirmed by pushing it.

WHAT WOULD ACTUALLY MOVE IT, stated so the negative is useful.  The trade is
exact given BV's gate and the identification of the throat with the field's
Compton length.  Breaking it needs one of:
  * a gate that is not phi^2 > kappa/xi -- a different non-minimal structure,
    not a different value in this one;
  * a throat set by something other than the field scale, which means a second
    scale in the problem that the single-field ansatz does not have;
  * a mechanism that localises a high-scale VEV, since a GUT-scale field is
    cosmological and uniform and nothing here can put one where a throat is
    wanted.
None of those is a number to compute. Each is a different model.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not claim the route is open.**  The coupling becomes ordinary and the
throat becomes Planckian at the same field scale, which is a relocation of the
obstruction and not a removal of it.

**It does not claim the route is closed either.**  Unlike the T = 0 census,
nothing here is a theorem forbidding the configuration; the trade follows from
one gate and one identification, and section 3 names exactly what would break it.

**It does not treat the GUT-scale field as available.**  A high-scale VEV is
uniform and cosmological. That the gate opens there says nothing about being
able to put one anywhere.
"""

import math
import sys

import higgs as H

HBAR_C_GEV_M = H.HBAR_C / H.GEV_IN_J  # GeV*m -- imported, no longer retyped
L_PLANCK = 1.616255e-35             # m, CODATA                    NAMED-NOT-READ

SCALES = [
    ("Higgs VEV (electroweak)", None),      # filled from higgs.py
    ("1 TeV", 1e3),
    ("see-saw / intermediate", 1e11),
    ("GUT scale", 2e16),
    ("reduced Planck mass", None),          # filled from higgs.py
]
# DOCKET 63 F9.  ONE NAMED CONSTANT, ONE VALUE: imported from its owner.
XI_HIGGS_INFLATION = H.XI_HIGGS_INFLATION          # 1.7e4, NAMED-NOT-READ there
#: The first draft's own pin for the same constant.  WITHDRAWN, kept.
XI_HIGGS_INFLATION_AS_FIRST_PINNED = 1e4
XI_HIGGS_INFLATION_WITHDRAWAL_REASON = (
    "two values for one named constant: higgs.py pins 1.7e4 "
    "(Bezrukov-Shaposhnikov); this file's 1e4 is withdrawn and the constant "
    "imported.  The GUT-scale xi_required(2e16) = 1.48e4 is then 0.87x Higgs "
    "inflation's, not 'one and a half times'.")
GUT_SCALE_GEV = 2e16


def scales():
    out = []
    for nm, v in SCALES:
        if nm.startswith("Higgs VEV"):
            v = H.vev()
        elif nm.startswith("reduced"):
            v = H.reduced_planck_gev()
        out.append((nm, v))
    return out


def xi_required(phi):
    """(M_red/phi)^2 -- imported from the seated instrument, not reimplemented."""
    return H.xi_required(phi)


def throat_m(phi):
    """The field's Compton length. At the gate xi phi^2 = M_red^2, so the
    effective Planck scale IS the field scale and this is where the geometry
    is modified."""
    return HBAR_C_GEV_M / phi


def trade(phi):
    """(throat/l_P)^2 / (8 pi) -- equals xi_required(phi) exactly."""
    return (throat_m(phi) / L_PLANCK) ** 2 / (8 * math.pi)


def report():
    print("=" * 74)
    print("THE T = 1 GATE IS AN EXCHANGE RATE, NOT A WALL")
    print("=" * 74)
    print()
    print("1. THE GATE CLOSES AT THE GUT SCALE, ON A COUPLING ALREADY IN USE.")
    print("   xi_required = (M_red/phi)^2, and the Higgs VEV is simply small.")
    print("   %-26s %-12s %-13s %s" % ("field scale", "phi (GeV)", "xi required",
                                       "vs Higgs inflation"))
    for nm, phi in scales():
        xi = xi_required(phi)
        print("   %-26s %-12.3e %-13.3e %.1e" % (nm, phi, xi, xi / XI_HIGGS_INFLATION))
    print()
    print("   AT THE GUT SCALE THE COUPLING NEEDED IS %.2fx THE ONE HIGGS INFLATION"
          % (xi_required(GUT_SCALE_GEV) / XI_HIGGS_INFLATION))
    print("   ALREADY USES (xi = %.1e, imported from higgs.py; the first draft's"
          % XI_HIGGS_INFLATION)
    print("   own 1e4 pin, which gave '1.5x', is WITHDRAWN -- DOCKET 63 F9).")
    print("   The 1e27 shortfall belongs to the Higgs, not the route:")
    print("   the gate is the hierarchy problem only because the Higgs sits sixteen")
    print("   orders below the Planck scale, and another field need not.")
    print()

    print("2. AND THE THROAT CLOSES AT THE SAME PLACE, EXACTLY.")
    print("   %-26s %-13s %-13s %s" % ("field scale", "xi required", "throat (m)",
                                       "in Planck lengths"))
    for nm, phi in scales():
        print("   %-26s %-13.3e %-13.3e %.2e"
              % (nm, xi_required(phi), throat_m(phi), throat_m(phi) / L_PLANCK))
    print()
    print("   THE RELATION IS EXACT:   xi_required = (throat / l_P)^2 / (8 pi)")
    worst = max(abs(xi_required(p) / trade(p) - 1.0) for _, p in scales())
    print("   checked at %d scales over sixteen orders; worst deviation %.2e"
          % (len(scales()), worst))
    print("   The 8 pi is M_Planck^2 / M_red^2, not a fit -- the gate is written")
    print("   in one Planck mass and the throat in the other.")
    print()

    print("3. SO THE GATE IS AN EXCHANGE RATE.")
    print("   A reachable coupling is buyable and the price is throat size, one")
    print("   for one, at a fixed rate. It cannot be paid down: xi and the throat")
    print("   are the same function of phi. At the only field scale where the")
    print("   coupling is ordinary, the throat is %.0f Planck lengths."
          % (throat_m(2e16) / L_PLANCK))
    print()
    print("   AND THIS IS scale.py's THEOREM ARRIVING FROM A NEW DIRECTION. That")
    print("   file proved every route crosses the line within two orders of l_P,")
    print("   and proved the convergence INEVITABLE. T = 1 was the one candidate")
    print("   that overshot; pushing it produces the same crossing, now with an")
    print("   exact coefficient instead of a coincidence.")
    print()
    print("   WHAT WOULD MOVE IT -- none of them a number, each a different model:")
    print("     * a gate that is not phi^2 > kappa/xi;")
    print("     * a throat set by something other than the field scale, which")
    print("       means a second scale the single-field ansatz does not have;")
    print("     * a way to LOCALISE a high-scale VEV, which is cosmological and")
    print("       uniform, and which nothing here can put where a throat is wanted.")
    return 0


def selftest():
    ok = True

    def chk(name, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("xigate selftest")
    # The seated gate, imported not copied.
    chk("the Higgs-VEV gate is the seated 9.78e31",
        xi_required(H.vev()) / 9.7829068836e31, 1.0, 1e-9)
    chk("and it IS the hierarchy squared, as higgs.py proves",
        xi_required(H.vev()) * (H.vev() / H.reduced_planck_gev()) ** 2, 1.0, 1e-12)

    # The push: the GUT scale brings it to a coupling already in use.
    chk("at the GUT scale the coupling needed is about 1.48e4",
        xi_required(GUT_SCALE_GEV) / 1e4, 1.48, 0.02)
    # DOCKET 63 F9: ONE named constant, ONE value, imported from its owner.
    chk("XI_HIGGS_INFLATION is higgs.py's, not a second pin",
        XI_HIGGS_INFLATION is H.XI_HIGGS_INFLATION, True)
    chk("  and it is 1.7e4", XI_HIGGS_INFLATION, 1.7e4)
    chk("HBAR_C is imported from higgs.py, not retyped",
        HBAR_C_GEV_M, H.HBAR_C / H.GEV_IN_J)
    chk("  and it agrees with the first draft's typed 1.973269804e-16",
        HBAR_C_GEV_M, 1.973269804e-16, 1e-24)
    # RE-PINNED.  Against the imported 1.7e4 the GUT requirement is 0.872x,
    # BELOW Higgs inflation's.  The first draft asserted 1 < ratio < 2 against
    # its own 1e4 (ratio 1.48); that fixture moved and is withdrawn.
    chk("the GUT requirement is 0.872x Higgs inflation's (re-pinned)",
        xi_required(GUT_SCALE_GEV) / XI_HIGGS_INFLATION, 0.8722, 1e-4)
    chk("which is within a factor of two of it, from below",
        0.5 < xi_required(GUT_SCALE_GEV) / XI_HIGGS_INFLATION < 1.0, True)
    chk("WITHDRAWN fixture: against the first pin 1e4 it was 1.48x",
        xi_required(GUT_SCALE_GEV) / XI_HIGGS_INFLATION_AS_FIRST_PINNED,
        1.4827, 1e-4)
    # the docstring's vs-Higgs-inflation column, reproduced
    for phi, want in ((H.vev(), 5.7547e27), (1e3, 3.4888e26), (1e11, 3.4888e10),
                      (H.reduced_planck_gev(), 5.8824e-5)):
        chk("docstring column at phi = %.3g" % phi,
            xi_required(phi) / XI_HIGGS_INFLATION / want, 1.0, 1e-4)
    chk("so the 1e27 shortfall is the HIGGS's, not the route's",
        xi_required(H.vev()) / xi_required(GUT_SCALE_GEV) > 1e27, True)

    # THE TRADE, and it is the finding.
    worst = max(abs(xi_required(p) / trade(p) - 1.0) for _, p in scales())
    chk("xi_required = (throat/l_P)^2 / 8pi, at every scale", worst < 1e-6, True)
    # 1e-6, not tighter: the residual is the CODATA precision of l_P against
    # M_red, not a fitted coefficient. Pinning below that would pin the constants.
    chk("the constant is 8 pi and not fitted",
        (throat_m(1e10) / L_PLANCK) ** 2 / xi_required(1e10) / (8 * math.pi), 1.0, 1e-6)

    # And the trade cannot be paid down: both are powers of phi.
    a, b = 1e10, 1e12
    chk("a 100x higher field buys 1e4 in xi", xi_required(a) / xi_required(b), 1e4, 1.0)
    chk("and costs exactly 100x in throat", throat_m(a) / throat_m(b), 100.0, 1e-9)

    # Where it lands, which is scale.py's crossing.
    chk("at the GUT scale the throat is a few hundred Planck lengths",
        100 < throat_m(2e16) / L_PLANCK < 1000, True)
    chk("and at M_red it is single-digit Planck lengths",
        1 < throat_m(H.reduced_planck_gev()) / L_PLANCK < 10, True)

    print("xigate selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
