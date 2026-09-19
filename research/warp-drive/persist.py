#!/usr/bin/env python3
"""
persist.py -- HOW LONG MAY THE NEGATIVE MASS LAST?

antigravity.py closed on "the corridor needs the INTEGRAL negative, not the
integrand", and ruled out the one source of negative mass M had proposed.
qei.py evaluated Fewster-Osterbrink Theorem 4.3 and found the STATE-INDEPENDENT
piece of the proved bound scales as tau^-4.

NEITHER ASKED THE QUESTION THE TWO OF THEM TOGETHER MAKE OBVIOUS.  A corridor
needs its negative mass to LAST -- for at least the time light takes to cross
the mouth, since nothing can traverse faster than that inside the throat.  And
a quantum energy inequality does not bound negative energy at all; it bounds
negative energy BY HOW LONG IT LASTS.  So the two quantities are the same
quantity, and they have never been compared in this tree.

THEY ARE COMPARED HERE, AND THE RESULT REFRAMES THE WALL.

===============================================================================
1. THE BOUND, IN THE FORM USED, AND WHAT IS DROPPED FROM IT
===============================================================================

The Ford-Roman SCALING bound for a massless field in four dimensions:

        |rho|  <=  hbar / (c^3 T^4)

The numerical coefficient is dropped.  For Lorentzian sampling the minimally
coupled coefficient is 3/(32 pi^2) = 9.5e-3, so DROPPING IT IS GENEROUS TO THE
CORRIDOR BY TWO ORDERS -- keeping it would make the permitted mass ~100x
smaller still.  Every deficit reported below is therefore a FLOOR.

WHAT IS NOT DONE HERE, stated rather than hidden:

    (a) This is the scaling form, not qei.py's proved Theorem 4.3.  It carries
        no xi.  So this pass DOES NOT CLOSE THE STATE-DEPENDENT ESCAPE; it
        measures the size of the hole that escape would have to fill.
    (b) A QEI bounds a SAMPLED energy density along a timelike geodesic.
        Treating a static shell's volume-integrated mass as if it were such a
        sample is a heuristic, and it is the same heuristic the Ford-Roman
        wormhole literature uses.  Recorded as a heuristic.
    (c) The curved-space term QC[f] of qei.py section 1 is again absent, and
        again does not vanish here.

===============================================================================
2. THE TWO CLOCKS
===============================================================================

The mouth is mouth.py's: R = 1.524 m, the radius of a ten-foot doorway, fixed
by M's own assumption.  Its required mass is closeout.py's, M = R c^2/(2G).

    T_CROSS   = R/c                    how long the corridor must hold
    T_ALLOWED = (hbar/(c^3 rho))^(1/4) how long the bound permits that density

with rho = M c^2/V and V = (4/3) pi R^3, so rho = 3 c^4/(8 pi G R^2) and

        T_ALLOWED(R) = ( 8 pi hbar G R^2 / (3 c^7) )^(1/4)   proportional to R^(1/2)
        T_CROSS(R)   = R/c                                   proportional to R

THE BOUND DOES NOT FORBID THE DENSITY.  IT FORBIDS THE DURATION.  The density
the corridor needs is permitted -- for a while.  The while is too short.

===============================================================================
3. THE FOURTH-POWER IDENTITY
===============================================================================

Two deficits can be quoted, and they are not independent.  Compare masses at
fixed duration (one light crossing), or compare durations at fixed density:

        GAP_MASS(R)     = M_required(R) / M_allowed(R, T = R/c)
        GAP_DURATION(R) = T_CROSS(R) / T_ALLOWED(R)

Because both masses occupy the SAME volume, their ratio is the ratio of the
densities, and rho_allowed goes as T^-4.  Hence, exactly:

        GAP_MASS  =  GAP_DURATION^4

This is an identity, not a coincidence, and it is checked below to machine
precision over fifteen orders of magnitude in R.  It also fixes both exponents
at once:

        GAP_DURATION  proportional to  R^(1/2)
        GAP_MASS      proportional to  R^2

===============================================================================
4. BIGGER IS STRICTLY WORSE, AND THAT IS NEW HERE
===============================================================================

    GAP_MASS(R) = 3 R^2 / (8 pi l_P^2)

Every other wall in this thread has been scale-free or has REWARDED shrinking
the object only by shrinking the reach with it -- closeout.py's aspect ratio
Lambda/2 is scale-invariant to 1e-15 over sixteen orders, and kugelblitz.py's
E x R is scale-free.  THIS ONE IS THE FIRST THAT PUNISHES SIZE OUTRIGHT.  You
cannot buy your way past it with a bigger installation; a bigger installation
is quadratically further away.

===============================================================================
5. THE CROSSOVER, AND WHY LAMBDA IS ABSENT FROM IT
===============================================================================

Setting GAP_MASS = 1:

        R_cross = sqrt(8 pi/3) l_P = 2.894 l_P

LAMBDA IS NOT IN IT, and the cancellation is worth stating because the ladder
does contain Lambda.  The ladder gives M = Delta d c^2/(G Lambda) and the
aspect ratio gives Delta d = Lambda R/2; substituting, Lambda cancels and
M = R c^2/(2G).  So the crossover radius is a Lambda-INDEPENDENT statement even
though it is reached through a Lambda-dependent exchange rate -- verified
directly below by recomputing it through the ladder at three values of Lambda.

That crossover is three Planck lengths.  It is the fourth crossover in this
thread that exists and is never reached.

===============================================================================
6. WHAT THIS DOES AND DOES NOT SETTLE
===============================================================================

DOES:  the corridor's negative-mass requirement fails the Ford-Roman scaling
bound not by a little and not at some sizes, but at every size above a few
Planck lengths, by a deficit that grows as R^2, and the deficit quoted is a
floor because the bound's own coefficient was dropped in the corridor's favour.

DOES NOT:  close Fewster-Osterbrink's state-dependent piece.  That remains the
one open escape, and its size is now quantified rather than gestured at.

NOTHING IS REPAIRED.  A finding is recorded.
"""

import math
import sys

import ladder

c = ladder.c
G = ladder.G
HBAR = ladder.HBAR
LAMBDA = ladder.LAMBDA
L_PLANCK = ladder.L_PLANCK
M_EARTH = ladder.M_EARTH

T_PLANCK = L_PLANCK / c

R_MOUTH = 1.524                      # mouth.py: ten-foot doorway, radius in m

FR_COEFFICIENT_DROPPED = True        # section 1
BOUND_IS_SCALING_FORM = True         # section 1(a)
STATE_DEPENDENT_PIECE_STILL_OPEN = True
SAMPLING_IS_HEURISTIC = True         # section 1(b)
QC_TERM_STILL_ABSENT = True          # section 1(c)
NOTHING_IS_REPAIRED = True


def volume(R):
    return (4.0 / 3.0) * math.pi * R ** 3


def rho_allowed(T):
    """Ford-Roman scaling bound on |rho|, coefficient dropped."""
    return HBAR / (c ** 3 * T ** 4)


def mass_allowed(R, T):
    """Mass-equivalent of the largest negative energy density permitted for T."""
    return rho_allowed(T) * volume(R) / (c * c)


def mass_allowed_light_crossing(R):
    """mass_allowed(R, R/c), in closed form.  Falls as 1/R."""
    return (4.0 * math.pi / 3.0) * HBAR / (c * R)


def mass_required(R):
    """closeout.py's mass for a mouth of radius R.  Rises as R."""
    return R * c * c / (2.0 * G)


def mass_required_via_ladder(R, lam=LAMBDA):
    """The same mass reached through the Lambda-bearing exchange rate.

    Delta d = lam R/2 (aspect ratio), then M = Delta d c^2/(G lam).  Lambda
    must cancel; that it does is checked, not assumed.
    """
    delta_d = lam * R / 2.0
    return delta_d * c * c / (G * lam)


def rho_required(R):
    return mass_required(R) * c * c / volume(R)


def t_cross(R):
    return R / c


def t_allowed(R):
    """Longest time the bound permits the REQUIRED density to stand."""
    return (HBAR / (c ** 3 * rho_required(R))) ** 0.25


def gap_mass(R):
    return mass_required(R) / mass_allowed_light_crossing(R)


def gap_mass_closed(R):
    """3 R^2 / (8 pi l_P^2) -- the same number without going through masses."""
    return 3.0 * R * R / (8.0 * math.pi * L_PLANCK ** 2)


def gap_duration(R):
    return t_cross(R) / t_allowed(R)


def crossover_radius():
    return math.sqrt(8.0 * math.pi / 3.0) * L_PLANCK


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  constants")
    print("      %-38s %20.6e m" % ("Planck length", L_PLANCK))
    print("      %-38s %20.6e s" % ("Planck time", T_PLANCK))
    print("      %-38s %20.6e" % ("Lambda", LAMBDA))
    print()
    print("  the mouth (mouth.py, ten feet across)")
    print("      %-38s %20.6f m" % ("radius R", R_MOUTH))
    print("      %-38s %20.6e kg" % ("mass required", mass_required(R_MOUTH)))
    print("      %-38s %20.6f" % ("  in Earth masses",
                                  mass_required(R_MOUTH) / M_EARTH))
    print("      %-38s %20.6e kg/m^3" % ("density required",
                                         rho_required(R_MOUTH) / (c * c)))
    print("      %-38s %20.6e J/m^3" % ("energy density required",
                                        rho_required(R_MOUTH)))
    print()
    print("  the two clocks")
    print("      %-38s %20.6e s" % ("must hold for  (R/c)", t_cross(R_MOUTH)))
    print("      %-38s %20.6e s" % ("may hold for   (Ford-Roman)",
                                    t_allowed(R_MOUTH)))
    print("      %-38s %20.6e" % ("  ratio allowed/needed",
                                  t_allowed(R_MOUTH) / t_cross(R_MOUTH)))
    print("      %-38s %20.6e" % ("  in Planck times, allowed",
                                  t_allowed(R_MOUTH) / T_PLANCK))
    print()
    print("  the two masses, at one light crossing")
    print("      %-38s %20.6e kg" % ("required", mass_required(R_MOUTH)))
    print("      %-38s %20.6e kg" % ("permitted",
                                     mass_allowed_light_crossing(R_MOUTH)))
    print("      %-38s %20.6e" % ("  deficit", gap_mass(R_MOUTH)))
    print("      %-38s %20.2f" % ("  orders of magnitude",
                                  math.log10(gap_mass(R_MOUTH))))
    print()
    print("  the fourth-power identity")
    print("      %-38s %20.6e" % ("GAP_DURATION", gap_duration(R_MOUTH)))
    print("      %-38s %20.6e" % ("GAP_DURATION^4", gap_duration(R_MOUTH) ** 4))
    print("      %-38s %20.6e" % ("GAP_MASS", gap_mass(R_MOUTH)))
    print("      %-38s %20.3e" % ("  relative disagreement",
                                  abs(gap_duration(R_MOUTH) ** 4
                                      - gap_mass(R_MOUTH)) / gap_mass(R_MOUTH)))
    print()
    print("  scaling -- bigger is strictly worse")
    print("      %-14s %16s %16s %16s" % ("R (m)", "GAP_MASS",
                                          "GAP_DURATION", "GAP_MASS/R^2"))
    for e in range(-10, 6, 2):
        R = 10.0 ** e
        print("      %-14.0e %16.6e %16.6e %16.6e"
              % (R, gap_mass(R), gap_duration(R), gap_mass(R) / (R * R)))
    print()
    print("  the crossover, and Lambda's absence from it")
    Rx = crossover_radius()
    print("      %-38s %20.6e m" % ("R_cross", Rx))
    print("      %-38s %20.6f" % ("  in Planck lengths", Rx / L_PLANCK))
    print("      %-38s %20.6f" % ("  sqrt(8 pi/3)", math.sqrt(8 * math.pi / 3)))
    print("      %-38s %20.6e" % ("  GAP_MASS there", gap_mass(Rx)))
    for lam in (1.0, LAMBDA, 1000.0):
        m = mass_required_via_ladder(R_MOUTH, lam)
        print("      via ladder at Lambda = %10.4f  %20.6e kg" % (lam, m))
    print()
    print("  what the deficit would cost the escape")
    print("      the state-dependent piece must supply a factor of %.4e"
          % gap_mass(R_MOUTH))
    print("      and the Ford-Roman coefficient 3/(32 pi^2) = %.4e was DROPPED,"
          % (3.0 / (32.0 * math.pi ** 2)))
    print("      so the true requirement is larger by 1/that = %.4e"
          % (32.0 * math.pi ** 2 / 3.0))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The bound does not forbid the density.  It forbids the duration.")
    print("  Bigger is strictly worse, quadratically, and that is the first")
    print("  wall in this thread that punishes size.")
    print()


def selftest():
    fails = []

    def chk(label, got, want, tol=None):
        ok = (abs(got - want) <= tol) if tol is not None else (got == want)
        print("  [%s] %-56s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-56s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("persist.py --selftest")
    print()

    # ------------------------------------------------------------------ forms
    # mass_allowed_light_crossing must equal mass_allowed(R, R/c) exactly
    for R in (1e-9, 1.0, R_MOUTH, 1e6):
        chkrel("closed form = mass_allowed(R, R/c) at R=%g" % R,
               mass_allowed_light_crossing(R), mass_allowed(R, t_cross(R)),
               1e-12)

    # gap_mass closed form
    for R in (1e-20, 1e-3, R_MOUTH, 1e9):
        chkrel("gap_mass closed form at R=%g" % R,
               gap_mass_closed(R), gap_mass(R), 1e-12)

    # ------------------------------------------------ the fourth-power identity
    for e in range(-10, 6):
        R = 10.0 ** e
        chkrel("GAP_MASS = GAP_DURATION^4 at R=1e%d" % e,
               gap_duration(R) ** 4, gap_mass(R), 1e-9)

    # -------------------------------------------------------------- exponents
    # GAP_MASS goes as R^2, GAP_DURATION as R^(1/2)
    chkrel("GAP_MASS(10R)/GAP_MASS(R) = 100", gap_mass(10.0) / gap_mass(1.0),
           100.0, 1e-12)
    chkrel("GAP_DURATION(100R)/GAP_DURATION(R) = 10",
           gap_duration(100.0) / gap_duration(1.0), 10.0, 1e-12)
    # and it really is monotone increasing -- bigger is worse, not better
    chk("gap_mass strictly increases with R",
        all(gap_mass(10.0 ** e) < gap_mass(10.0 ** (e + 1))
            for e in range(-20, 20)), True)

    # NEGATIVE CONTROL: an R^3 law would also increase, so monotonicity alone
    # is not the claim.  The exponent is.
    chk("the exponent is 2, not 3",
        abs(math.log10(gap_mass(1e3) / gap_mass(1.0)) - 6.0) < 1e-9, True)

    # -------------------------------------------------------------- crossover
    Rx = crossover_radius()
    chkrel("gap_mass = 1 at the crossover", gap_mass(Rx), 1.0, 1e-12)
    chkrel("gap_duration = 1 at the crossover", gap_duration(Rx), 1.0, 1e-9)
    chkrel("crossover in Planck lengths is sqrt(8 pi/3)",
           Rx / L_PLANCK, math.sqrt(8.0 * math.pi / 3.0), 1e-12)
    chk("and it is never reached by a doorway", Rx < R_MOUTH, True)

    # LAMBDA CANCELS: the ladder route gives the same mass at any Lambda
    base = mass_required(R_MOUTH)
    for lam in (1e-6, 1.0, LAMBDA, 1e6):
        chkrel("ladder mass is Lambda-free at Lambda=%g" % lam,
               mass_required_via_ladder(R_MOUTH, lam), base, 1e-12)
    # and the crossover has no Lambda in it at all
    chk("crossover_radius takes no Lambda",
        "lam" not in crossover_radius.__code__.co_varnames, True)

    # ------------------------------------------------------------- the mouth
    chk("the mouth is mouth.py's", R_MOUTH, 1.524)
    chkrel("mass required matches closeout.py", mass_required(R_MOUTH),
           1.026102e27, 1e-6)

    # ------------------------------------------------- the scope, kept narrow
    chk("this is the scaling form, not Theorem 4.3", BOUND_IS_SCALING_FORM, True)
    chk("the coefficient was dropped, in the corridor's favour",
        FR_COEFFICIENT_DROPPED, True)
    chk("so every deficit here is a floor",
        3.0 / (32.0 * math.pi ** 2) < 1.0, True)
    chk("the state-dependent escape is NOT closed",
        STATE_DEPENDENT_PIECE_STILL_OPEN, True)
    chk("the sampling step is a heuristic", SAMPLING_IS_HEURISTIC, True)
    chk("the QC term is still absent", QC_TERM_STILL_ABSENT, True)
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
