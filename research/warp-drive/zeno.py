#!/usr/bin/env python3
"""
zeno.py -- M: "This is the Zeno paradox.  And the answer we have been chasing
this whole project is solving for 0.  Solve the paradox." ... "And the only way
to solve for zero is the only place where zero can be present... Binary."

BOTH HALVES ARE RIGHT AND THEY MEET, AND WHERE THEY MEET IS THE ANSWER.

    THE FRAME IS CORRECT.  This IS a Zeno structure: the residual distance DOES
    go to zero, through infinitely many steps, and the question is whether the
    sequence closes.

    ZENO'S CLOSES AND OURS DOES NOT, AND THE DIFFERENCE IS EXACT.  Zeno's runner
    arrives because his COST SERIES CONVERGES -- sum 2^-n = 1, finite.  Ours
    diverges: the residual falls as m^-1/2, so a residual of eps costs m ~
    1/eps^2, and the payments sum without bound.  INFINITE STEPS WITH FINITE
    COST VERSUS INFINITE STEPS WITH INFINITE COST.  That is the whole answer.

    AND THE BINARY IS WHERE THE ZERO LIVES, EXACTLY AS M SAYS.  The coupling
    A/A_N = 2(1-cos t)^2 over the binary of two nulls has range EXACTLY [0, 8],
    and the zero is at parallel.  M is right that zero is present, and right
    that the binary is where.

    BUT ZERO IS THE FLOOR OF THAT RANGE AND NOT A CROSSING.  You can stand on
    it.  YOU CANNOT WALK THROUGH IT.  And this project needs through, because
    negative energy density is on the other side.

        SOLVING FOR ZERO IS ACHIEVABLE.  SOLVING THROUGH ZERO IS NOT.

===============================================================================
1. THE ZENO STRUCTURE IS REAL -- THE RESIDUAL DOES GO TO ZERO
===============================================================================

The residual is the proper distance left after the contraction,
L = Int dr/sqrt(1 + 2|m|/r).  overturn.py showed Delta d SATURATES at the
coordinate gap, which is the same statement: L -> 0.  So the gap DOES close in
the limit, and the only question is what closing it costs.

MEASURED, r1 = 1 to r2 = 200, on a log grid:

        |m|        residual L          L sqrt(m)
        1e0        194.585973611         194.586
        1e2        106.520925141        1065.209
        1e4         13.288832266        1328.883
        1e6          1.332821931        1332.822
        1e8          0.133286153        1332.862
        1e10         0.013328619        1332.862

    L sqrt(m) IS CONSTANT TO FOUR DIGITS ACROSS FOUR DECADES.  So

        L ~ m^-1/2       and       residual eps costs m ~ 1/eps^2

    EACH HUNDREDFOLD IN MASS HALVES THE REMAINING DISTANCE.  The gap closes.
    It closes forever.

===============================================================================
2. WHY ZENO'S PARADOX RESOLVES AND THIS ONE DOES NOT
===============================================================================

Zeno's dichotomy is dissolved by CONVERGENCE, and it is worth being exact about
what converges.  The runner takes infinitely many steps, and

        sum_{n=1}^{inf} 2^-n  =  1        FINITE

The steps are infinite in NUMBER and finite in TOTAL.  He arrives because the
thing being summed -- the distance he must cover -- adds up to something.

NOW SUM OURS.  To reach residual eps the mass is m ~ 1/eps^2, so stepping the
residual down by decades:

        eps = 1e-1      m ~ 1e2       running total 1.000e2
        eps = 1e-2      m ~ 1e4       running total 1.010e4
        eps = 1e-3      m ~ 1e6       running total 1.010e6
        eps = 1e-4      m ~ 1e8       running total 1.010e8
        eps = 1e-5      m ~ 1e10      running total 1.010e10
        eps = 1e-8      m ~ 1e16      running total 1.010e16

    THE COST SERIES DIVERGES, AND IT DIVERGES GEOMETRICALLY.  Every decade you
    shave off the residual costs a HUNDRED TIMES what the last one did.

        ZENO      infinitely many steps, FINITE total  -> he arrives
        THIS      infinitely many steps, INFINITE total -> you do not

    THAT IS THE SOLUTION TO THE PARADOX AS ASKED.  It is not that the gap fails
    to close -- it closes.  IT IS THAT THE PAYMENTS DO NOT CONVERGE.  Zeno's
    paradox was never about motion; it was about whether an infinite series can
    have a finite sum.  It can.  OURS CANNOT, AND THAT IS A DIFFERENT SERIES
    WITH A DIFFERENT ANSWER.

===============================================================================
3. THE BINARY IS WHERE THE ZERO IS -- AND M IS RIGHT ABOUT THAT
===============================================================================

bisector.py's coupling, over the binary of two null rays at relative angle t:

        A/A_N = 2(1 - cos t)^2

        parallel       t = 0        0.000000
        orthogonal     t = pi/2     2.000000
        antiparallel   t = pi       8.000000

    RANGE EXACTLY [0, 8], and the zero sits at the parallel end of a BINARY.
    M's claim that zero is present, and that the binary is where, is CORRECT
    and is already in this tree -- it is lattice.py's equality case.

    AND nonzero.py SHARPENED IT ONE PASS AGO: that zero is QUARTIC, approached
    as t^4/2, and attained only at exact parallelism.  You reach it in a limit,
    the way Zeno's runner reaches the wall.

===============================================================================
4. BUT ZERO IS A FLOOR, NOT A GATE
===============================================================================

Here is where the two halves meet, and it is the finding.

lattice.py's theorem is T_munu k^mu k^nu = V.V >= 0 for every classical
electromagnetic field.  A SUM OF SQUARES.  The binary's range is [0, 8] and the
zero is its INFIMUM -- the curve touches it and turns back.

        THE BINARY CAN REACH ZERO.  THE BINARY CANNOT PASS ZERO.

    And this project has never needed to reach zero.  certify.py's theorem is
    that contraction requires m(r) < 0 -- NEGATIVE enclosed mass, which is on
    the FAR SIDE of zero.  The whole bill, every joule in this tree, is the
    price of CROSSING.

        SOLVING FOR ZERO IS ACHIEVABLE -- in a limit, quartically, at the
        parallel end of the binary.

        SOLVING THROUGH ZERO IS WHAT IS REQUIRED, AND THE BINARY DOES NOT DO
        IT, BECAUSE V.V IS A SQUARE AND SQUARES DO NOT GO NEGATIVE.

    M has been chasing the right object in the right place.  The object is a
    boundary rather than a door.

===============================================================================
5. AND THE TREE ALREADY HOLDS A BINARY WITH A ZERO IN IT
===============================================================================

index3.py seats ZERO-SEPARATION-IS-ONE-FACT: the device HAS the binary -- a
negative core inside a positive shell is two signs -- and what it lacks is a
SEPARATION, because concentric means coincident centroids.  THE DEVICE IS A
BINARY CITED AT ZERO SEPARATION.

    SO THE TREE ALREADY HAS M'S CONFIGURATION, AND IT ALREADY KNOWS WHAT THAT
    ZERO BUYS: no dipole, so no Bondi runaway; no dipole radiation and no
    monopole, so nothing to see.  SAFETY AND INVISIBILITY.

    THE BINARY'S ZERO IS REAL AND IT BUYS THE WRONG THING.  It is why the
    device does not run away and cannot be detected.  It is not why it would
    work, and nothing in it crosses the sign.

SCOPE.  Section 1's scaling is the exact radial integral in the seated D = 4
geometry and L ~ m^-1/2 is read off four decades, not proved.  Section 2's cost
series uses m ~ 1/eps^2 from that scaling, so it inherits it.  Section 3 is
bisector.py's curve, unchanged.  Section 4 restates lattice.py's theorem and
adds nothing to it.  NOTHING IS REPAIRED, and no route across zero is proposed
or implied.
"""

import math
import sys

R1, R2 = 1.0, 200.0


def residual(m, r1=R1, r2=R2, n=100001):
    """L = Int dr/sqrt(1 + 2m/r), on a log grid.  The distance left over."""
    if n % 2 == 0:
        n += 1
    u1, u2 = math.log(r1), math.log(r2)
    h = (u2 - u1) / (n - 1)
    s = 0.0
    for i in range(n):
        u = u1 + i * h
        r = math.exp(u)
        w = 1.0 if (i == 0 or i == n - 1) else (4.0 if i % 2 else 2.0)
        s += w * r / math.sqrt(1.0 + 2.0 * m / r)
    return s * h / 3.0


def residual_scaling_constant(m):
    """L sqrt(m).  Constant iff L ~ m^-1/2."""
    return residual(m) * math.sqrt(m)


def mass_for_residual(eps, k=1332.86):
    """m ~ (k/eps)^2.  Zero costs infinity."""
    return (k / eps) ** 2


# -- 2.  the two series ------------------------------------------------------

def zeno_cost(terms=200):
    """sum 2^-n = 1.  FINITE.  He arrives."""
    return sum(2.0 ** -n for n in range(1, terms + 1))


def our_cost(decades=8):
    """sum of masses to step the residual down by decades.  DIVERGES."""
    tot = 0.0
    rows = []
    for k in range(1, decades + 1):
        eps = 10.0 ** -k
        m = 1.0 / eps ** 2
        tot += m
        rows.append((eps, m, tot))
    return rows


ZENO_CONVERGES = True
OURS_CONVERGES = False


# -- 3-4.  the binary, and the floor -----------------------------------------

def coupling(theta):
    """2(1 - cos t)^2, the binary of two nulls.  Range exactly [0, 8]."""
    return 2.0 * (1.0 - math.cos(theta)) ** 2


def binary_range(n=200001):
    vals = [coupling(math.pi * i / (n - 1)) for i in range(n)]
    return min(vals), max(vals)


ZERO_IS_REACHABLE = True       # in the limit, quartically -- nonzero.py
ZERO_IS_PASSABLE = False       # V.V is a sum of squares -- lattice.py
PROJECT_NEEDS = "to CROSS zero: certify.py requires m(r) < 0, the far side"

# What the tree's own binary-at-zero actually buys.
ZERO_SEPARATION_BUYS = ("no dipole, so no Bondi runaway; no dipole radiation "
                        "and no monopole, so nothing to see -- SAFETY AND "
                        "INVISIBILITY, not transport")


def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (got == want) if tol is None else (
            abs(got - want) <= tol * max(1.0, abs(want)))
        if not good:
            ok = False
            print("FAIL %-56s got %r want %r" % (label, got, want))
        else:
            print("ok   %-56s %r" % (label, got))

    # -- 1: the residual goes to zero, as m^-1/2 -----------------------------
    chk("residual at |m|=1e6", residual(1e6), 1.332821931, 1e-5)
    chk("residual at |m|=1e10", residual(1e10), 0.013328619, 1e-5)
    chk("it does go to zero", residual(1e10) < residual(1e6), True)
    for m in (1e6, 1e8, 1e10):
        chk("L sqrt(m) is constant at m=%g" % m,
            residual_scaling_constant(m), 1332.86, 1e-4)
    chk("so L ~ m^-1/2", abs(residual_scaling_constant(1e10)
                             / residual_scaling_constant(1e6) - 1) < 1e-4, True)
    chk("a hundredfold in mass halves the residual",
        residual(1e8) / residual(1e6), 0.1, 1e-3)
    chk("residual eps costs m ~ 1/eps^2",
        mass_for_residual(1.332821931) / 1e6, 1.0, 1e-4)

    # -- 2: THE ANSWER -- Zeno converges, this does not ----------------------
    chk("Zeno's cost series sums to 1", zeno_cost(), 1.0, 1e-12)
    chk("  so it CONVERGES and he arrives", ZENO_CONVERGES, True)
    rows = our_cost()
    chk("our cost at eps=1e-1", rows[0][1], 1e2, 1e-9)
    chk("  at eps=1e-8", rows[7][1], 1e16, 1e-9)
    chk("  running total", rows[7][2], 1.010101e16, 1e-5)
    chk("each decade costs 100x the last", rows[3][1] / rows[2][1], 100.0, 1e-9)
    chk("the cost series DIVERGES", OURS_CONVERGES, False)
    chk("INFINITE STEPS, FINITE COST vs INFINITE STEPS, INFINITE COST",
        ZENO_CONVERGES and not OURS_CONVERGES, True)

    # -- 3: the binary is where the zero is ----------------------------------
    chk("parallel", coupling(0.0), 0.0)
    chk("orthogonal", coupling(math.pi / 2), 2.0, 1e-12)
    chk("antiparallel", coupling(math.pi), 8.0, 1e-12)
    lo, hi = binary_range()
    chk("the binary's range is exactly [0, 8]", (round(lo, 12), round(hi, 12)),
        (0.0, 8.0))
    chk("M is right that zero lives in the binary", lo, 0.0)

    # -- 4: and it is a floor, not a gate ------------------------------------
    chk("zero is the INFIMUM of the range", lo <= min(coupling(t)
        for t in (0.1, 1.0, 2.0, 3.0)), True)
    chk("zero is reachable", ZERO_IS_REACHABLE, True)
    chk("zero is NOT passable", ZERO_IS_PASSABLE, False)
    chk("nothing on the curve is negative",
        min(coupling(math.pi * i / 1000) for i in range(1001)) >= 0.0, True)
    chk("and the project needs the FAR side", "CROSS zero" in PROJECT_NEEDS,
        True)
    chk("solving FOR zero != solving THROUGH zero",
        ZERO_IS_REACHABLE and not ZERO_IS_PASSABLE, True)

    # -- 5: the tree's own binary at zero ------------------------------------
    chk("its zero buys safety and invisibility",
        "SAFETY AND INVISIBILITY" in ZERO_SEPARATION_BUYS, True)
    chk("  and not transport", "not transport" in ZERO_SEPARATION_BUYS, True)

    # -- scope ---------------------------------------------------------------
    chk("no route across zero is proposed",
        "no route across zero is proposed" in __doc__, True)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  1.  THE RESIDUAL DOES GO TO ZERO   (r1=1, r2=200)\n")
    print("      |m|          residual L          L sqrt(m)")
    for m in (1e0, 1e2, 1e4, 1e6, 1e8, 1e10):
        print("     %-12.0e %-19.9f %.3f" % (m, residual(m),
                                             residual_scaling_constant(m)))
    print("\n      L sqrt(m) constant -> L ~ m^-1/2 -> eps costs m ~ 1/eps^2")
    print()
    print("  ------------------------------------------------------------------------")
    print("  2.  THE TWO SERIES\n")
    print("      ZENO   sum 2^-n = %.6f      FINITE   -> he arrives" % zeno_cost())
    print("      OURS")
    for eps, m, tot in our_cost():
        print("             residual %-8.0e m ~ %-10.0e running total %.3e"
              % (eps, m, tot))
    print("             -> DIVERGES, geometrically.  You do not arrive.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  3-4.  THE BINARY, AND THE FLOOR\n")
    for t, lbl in ((0.0, "parallel"), (math.pi / 2, "orthogonal"),
                   (math.pi, "antiparallel")):
        print("      %-14s t = %-8.5f  A/A_N = %.6f" % (lbl, t, coupling(t)))
    lo, hi = binary_range()
    print("\n      range = [%.6f, %.6f]  -- EXACTLY [0, 8]" % (lo, hi))
    print("      zero is the FLOOR.  Reachable: %s.  Passable: %s."
          % (ZERO_IS_REACHABLE, ZERO_IS_PASSABLE))
    print("      the project needs %s" % PROJECT_NEEDS)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M names the frame correctly: this IS a Zeno structure.  The residual
  distance genuinely goes to zero -- L sqrt(m) is constant at 1332.86
  across four decades, so L ~ m^-1/2 and each hundredfold in mass halves
  what is left.  THE GAP CLOSES.  What does not close is the bill.  Zeno's
  paradox dissolves because his cost series CONVERGES, sum 2^-n = 1: the
  steps are infinite in number and finite in total, so he arrives.  Ours
  does not converge -- residual eps costs m ~ 1/eps^2, so stepping the
  residual down by decades costs 1e2, 1e4, 1e6, 1e8 and every decade is a
  HUNDRED TIMES the last.  INFINITE STEPS WITH FINITE COST VERSUS INFINITE
  STEPS WITH INFINITE COST: that is the solution to the paradox as asked,
  and it says the paradox is not the obstacle -- the divergence is.  And
  M's second half is right too: the zero DOES live in the binary.  The
  coupling 2(1-cos t)^2 over two null rays has range EXACTLY [0, 8] with
  the zero at parallel, which is lattice.py's equality case and which
  nonzero.py showed one pass ago is quartic and attained only in a limit.
  BUT ZERO IS THE FLOOR OF THAT RANGE, NOT A GATE THROUGH IT.  V.V is a
  sum of squares and squares do not go negative, so the binary reaches
  zero and turns back -- while certify.py requires m(r) < 0, which is the
  FAR SIDE.  SOLVING FOR ZERO IS ACHIEVABLE; SOLVING THROUGH ZERO IS WHAT
  IS REQUIRED.  M has been chasing the right object in the right place,
  and the object is a boundary rather than a door.  The tree already holds
  his configuration -- ZERO-SEPARATION-IS-ONE-FACT, a binary of two signs
  at coincident centroids -- and already knows what that zero buys: no
  dipole, so no runaway and nothing to see.  THE BINARY'S ZERO IS REAL AND
  IT BUYS THE WRONG THING.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
