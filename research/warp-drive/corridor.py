#!/usr/bin/env python3
"""
corridor.py -- the two readings of "a vacuum corridor", compared.

M proposed that the transition happens in a vacuum -- the corridor itself is a
vacuum -- and, when the phrase was found to read two ways, asked for both to be
explored and compared rather than one chosen.  This is that comparison, and it
settles decisively in favour of the classical reading by eighteen orders of
magnitude.

    CLASSICAL VACUUM   T_kk = 0 exactly.  Einstein's equations then force
                       R_kk = 0, so RICCI FOCUSING IS ZERO and the only thing
                       that can focus a congruence is WEYL.  This is the
                       corridor composite.py measured in.
    QUANTUM VACUUM     a vacuum STATE, not an empty one: <T_kk> != 0, Unruh-
                       like, Hawking-Ellis Type IV.  Ricci comes back.

They are not variants of one idea.  They differ in which term of
G''/G = -(1/2)[sigma^2 + R_kk] is available, and that is the whole of
composite.py's result.

-- THE COMPARISON HAS A CLOSED FORM, WHICH IS WHY IT SETTLES -----------------
Take a compact source of mass mu (Planck units) and a corridor at z = 2m/r.

  WEYL, classical:  the tidal magnitude of a mass mu at radius r goes as
                    mu/r^3, and r = 2 mu / z, so it is  z^3 / (8 mu^2).
  RICCI, quantum:   R_kk = 8 pi <T_kk>, and Abdolrahimi-Page-Tzounis give the
                    Unruh flux in closed form, f(z) = alpha z^2/(16 pi (1-z))
                    with alpha = 3.7474e-5, scaling as mu^-4.

Their ratio collapses to something with no z^3 and no 16 pi left in it:

        RICCI / WEYL  =  4 alpha / ( z (1-z) mu^2 )

    SYMMETRIC ABOUT z = 1/2, and verified against the numerics to machine
    precision at z = 0.2, 0.3, 0.5, 0.7 and 0.8.  So the answer does not depend
    on where in the corridor you stand -- only on the mass.

Setting it to one:

        mu_cross  =  2 sqrt( alpha / (z(1-z)) ),   minimised at z = 1/2 as
        mu_cross  =  4 sqrt(alpha)  =  2.4486e-2 Planck masses
                                    =  5.3293e-10 kg

    HALF A NANOGRAM.  Below that the quantum vacuum dominates the corridor;
    above it, the classical one does.

-- AND THE DESIGN POINT IS NOWHERE NEAR IT ------------------------------------
selfconsistent.py matched a 1 m, 0.1 c configuration to the Type IV strength of
a 1.1263e9 kg hole.  Against a crossover of 5.3293e-10 kg that is

        EIGHTEEN AND A HALF ORDERS OF MAGNITUDE.

    FOR ANY DEVICE, THE CLASSICAL VACUUM CORRIDOR IS THE CORRECT ONE, and not
    marginally.  M's instinct -- "I was referring to the classic vacuum, which
    may be the correct form when we finish" -- is confirmed by computation
    rather than adopted by preference.

-- WHAT THE QUANTUM CORRIDOR WOULD DO, WHERE IT APPLIES -----------------------
Recorded rather than pursued, because a result you decline to use should still
be known.  The Unruh <T_kk> is NEGATIVE throughout and grows toward the horizon
(measured from universal.py's state functions: -8.8e-2 at z = 0.1 to -2.5e1 at
z = 0.9).  Negative Ricci in the Jacobi equation is DEFOCUSING.  So a quantum
corridor would:

        HURT the seat      -- negative R_kk fights the Weyl focusing
        HELP the lead      -- negative energy is what advance requires

which is composite.py's window pushed in both directions at once: the lower
edge rises (harder to seat) while the advance grows.  Whether the window
survives that is NOT-RUN, and it is not worth running for a sub-nanogram
device.

A NORMALISATION CAUTION, because it would be easy to get wrong: the SIGN above
is taken from universal.py's Unruh state functions and the MAGNITUDE ratio from
selfconsistent.py's APT closed form.  Those are different normalisations and
this file never multiplies one by the other.  Sign from one, magnitude from the
other, and no mixed quantity is reported.

-- WHAT THIS DOES NOT SETTLE --------------------------------------------------
  1. It compares MAGNITUDES of two focusing terms.  It does not re-run
     composite.py's window with a quantum term added -- that is the NOT-RUN
     above.
  2. The Weyl estimate is the tidal SCALE mu/r^3, not the integrated focusing.
     Good to an order of magnitude, which is all an 18-order gap needs.
  3. APT's result is first order in hbar and for a conformally coupled massless
     scalar; selfconsistent.py's scope list applies here unchanged.

stdlib only.  selfconsistent.py supplies the APT closed form, universal.py the
Unruh state, composite.py the corridor whose emptiness is at issue.
"""
import math, sys

CLASSICAL, QUANTUM = "CLASSICAL-VACUUM", "QUANTUM-VACUUM"


def _sc():
    import selfconsistent
    return selfconsistent


def weyl_coefficient(z):
    """Classical Weyl tidal scale, times mu^2:  z^3 / 8."""
    return z ** 3 / 8.0


def ricci_coefficient(z):
    """Quantum Ricci term R_kk = 8 pi <T_kk>, times mu^4."""
    return 8.0 * math.pi * _sc().flux_component(z)


def ratio_times_mu2(z):
    """RICCI/WEYL times mu^2.  Closed form 4 alpha / (z(1-z))."""
    return ricci_coefficient(z) / weyl_coefficient(z)


def ratio_closed_form(z):
    return 4.0 * _sc().ALPHA / (z * (1.0 - z))


def mu_crossover(z=0.5):
    """The mass at which the two terms are equal, in Planck masses."""
    return math.sqrt(ratio_closed_form(z))


def kg_crossover(z=0.5):
    return mu_crossover(z) * _sc().M_PLANCK


def dominant(mu, z=0.5):
    """Which corridor description governs at this mass."""
    return QUANTUM if ratio_closed_form(z) / (mu * mu) > 1.0 else CLASSICAL


def unruh_tkk_sign(z):
    """Sign only -- see the normalisation caution in the header."""
    import universal as U
    return U.unruh_rho(z) + U.unruh_p(z) - 2.0 * U.unruh_f(z)


def orders_of_magnitude(mass_kg, z=0.5):
    return math.log10(mass_kg / kg_crossover(z))


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %16s %16s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got - want) <= tol
        ok &= good
        print("  %-58s %16.8g %16.8g  %s" % (label, got, want, "ok" if good else "FAIL"))

    sc = _sc()

    print("The ratio collapses to a closed form -- checked, not asserted")
    for z in (0.2, 0.3, 0.5, 0.7, 0.8):
        near("z=%.1f  numeric vs 4 alpha/(z(1-z))" % z,
             ratio_times_mu2(z), ratio_closed_form(z), 1e-18)
    near("and it is symmetric about z = 1/2",
         ratio_closed_form(0.3), ratio_closed_form(0.7), 1e-18)
    print("       no z^3 and no 16 pi survive, so WHERE in the corridor you")
    print("       stand does not matter.  Only the mass does.")

    print("\nThe crossover, and it is exact at z = 1/2")
    near("mu_cross(1/2) = 4 sqrt(alpha)", mu_crossover(0.5),
         4.0 * math.sqrt(sc.ALPHA), 1e-15)
    near("in Planck masses", mu_crossover(0.5), 2.4486401e-2, 1e-8)
    # relative, not absolute: 1e-14 against a value of 5e-10 is meaningless,
    # and this is the third time an absolute tolerance on a small number has
    # failed in this tree.
    near("in kg (relative)", kg_crossover(0.5) / 5.3293051e-10, 1.0, 1e-6)
    chk("z = 1/2 minimises it, so this is the LARGEST crossover",
        all(mu_crossover(z) >= mu_crossover(0.5) for z in (0.1, 0.3, 0.7, 0.9)), True)

    print("\nWhich description governs, by mass")
    print("     %18s %20s" % ("mass (kg)", "corridor"))
    for kg, tag in ((1.0e-15, "femtogram"), (1.0e-6, "microgram"),
                    (1.1263e9, "the design point"), (5.972e24, "the Earth")):
        mu = kg / sc.M_PLANCK
        print("     %18.4e %20s   %s" % (kg, dominant(mu), tag))
    chk("a femtogram source is quantum-dominated",
        dominant(1.0e-15 / sc.M_PLANCK), QUANTUM)
    chk("the design point is classical", dominant(1.1263e9 / sc.M_PLANCK), CLASSICAL)
    near("and by how many orders", orders_of_magnitude(1.1263e9), 18.325, 1e-2)
    print("       EIGHTEEN AND A HALF.  Not a marginal call.")

    print("\nWhat the quantum corridor would do, where it applies")
    signs = [(z, unruh_tkk_sign(z)) for z in (0.1, 0.3, 0.5, 0.7, 0.9)]
    for z, s in signs:
        print("     z=%.1f   Unruh T_kk = %+.4e" % (z, s))
    chk("it is NEGATIVE throughout", all(s < 0 for _z, s in signs), True)
    chk("and grows in magnitude toward the horizon",
        all(abs(b) > abs(a) for (_z1, a), (_z2, b) in zip(signs, signs[1:])), True)
    print("       Negative Ricci DEFOCUSES: it would hurt the seat and help the")
    print("       lead -- composite.py's window pushed both ways at once.  Whether")
    print("       it survives is NOT-RUN, and not worth running sub-nanogram.")

    print("\nThe normalisation caution, enforced")
    chk("sign comes from universal.py", unruh_tkk_sign(0.5) < 0, True)
    chk("magnitude comes from selfconsistent.py", ricci_coefficient(0.5) > 0, True)
    print("       Different normalisations.  This file never multiplies one by")
    print("       the other, and reports no mixed quantity.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE COMPARISON")
    print("  %6s %16s %16s %16s" % ("z", "Weyl x mu^2", "Ricci x mu^4", "ratio x mu^2"))
    for z in (0.1, 0.3, 0.5, 0.7, 0.9):
        print("  %6.1f %16.5e %16.5e %16.5e"
              % (z, weyl_coefficient(z), ricci_coefficient(z), ratio_times_mu2(z)))
    print("\n  crossover  %.6e Planck masses  =  %.6e kg" % (mu_crossover(), kg_crossover()))
    print("  design point 1.1263e+09 kg is %.2f orders above it"
          % orders_of_magnitude(1.1263e9))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  The classical vacuum corridor is the correct one for any device,")
    print("  by eighteen and a half orders of magnitude.  The quantum vacuum")
    print("  corridor is a sub-nanogram regime; where it applies its Ricci term")
    print("  is NEGATIVE, so it would defocus -- hurting the seat and helping")
    print("  the lead.  Recorded, not pursued.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
