#!/usr/bin/env python3
"""
supply.py -- converting the transition's cost into something that can be
supplied, and what that conversion actually costs.

THE QUESTION: phase1.py prices the transition in KILOGRAMS -- 1.349e26 kg per
metre contracted.  What must be applied to the mathematics to pay in
ELECTRICITY, or in charge manipulation, instead?

THE ANSWER IS SHORTER THAN THE QUESTION: the conversion is already inside the
equation, and applying it again buys nothing.

===============================================================================
S0 -- THE CONVERSION IS ALREADY DONE
===============================================================================

        Delta d  =  Lambda * (G/c^4) * E

        G/c^4  =  8.26272e-45 m/J
        c^4/G  =  1.21026e+44 N        <- THE PLANCK FORCE

    G/c^4 = (G/c^2)/c^2.  E = mc^2 IS NOT SOMETHING YOU APPLY TO THE
    TRANSITION EQUATION; IT IS ALREADY THERE.  Paying in joules rather than
    kilograms is paying the same bill in another currency at a rate that has
    already been applied.

        1.21237e43 J per metre contracted  =  22.6 EARTH MASS-ENERGIES PER
                                              METRE.

    The whole cost of this project is one sentence: SPACETIME IS STIFF TO THE
    TUNE OF 1.2e44 NEWTONS, and c^4/G is the only constant in it.

===============================================================================
S1 -- THE SUPPLY FORM DOES NOT CHANGE THE MAGNITUDE.  ONLY THE SIGN MATTERS.
===============================================================================

Einstein's equation charges the same rate for every form of stress-energy.
Mass, field, charge, binding, vacuum -- G_{mu nu} = 8 pi T_{mu nu} does not ask
where T came from.  So the supply form changes the LOGISTICS (energy can be
beamed; mass must be assembled and held) and NOT THE MAGNITUDE.

    WHAT IT COULD CHANGE IS THE SIGN, AND THAT IS THE ONLY THING WORTH ASKING
    A SUPPLY ROUTE.  The rest of this file asks exactly that, four times.

===============================================================================
S2 -- ELECTRICITY ADDS POSITIVE ENERGY.  MORE POWER MAKES IT WORSE.
===============================================================================

Classical electromagnetic stress-energy is POSITIVE-DEFINITE:

        u  =  eps0 E^2 / 2  +  B^2 / 2 mu0   >=  0   ALWAYS

There is no classical field configuration with negative energy density, at any
field strength, in any geometry.  Driving harder adds positive mass, lengthens
the corridor, and moves the answer the wrong way.

The only negative electromagnetic energy is the QUANTUM VACUUM -- Casimir --
and it depends on GEOMETRY, not on power:

        u_C(d)  =  - pi^2 hbar c / (720 d^4)

    NO APPLIED FIELD APPEARS IN IT.  So the two terms do not compete on equal
    footing: one is fixed by the gap, the other grows as the square of whatever
    you apply.  Setting them equal gives the field that CANCELS the only
    negative energy in the apparatus:

        d          u_Casimir (J/m^3)     E_cancel (V/m)
        1 nm       -4.3338e+08           9.8940e+09
        10 nm      -4.3338e+04           9.8940e+07
        100 nm     -4.3338e+00           9.8940e+05
        1 um       -4.3338e-04           9.8940e+03

    AT A TEN-NANOMETRE GAP THE CANCELLING FIELD IS 9.9e7 V/m, WHICH IS BELOW
    THE DIELECTRIC BREAKDOWN OF A SOLID (~1e8 V/m) AND SEVEN ORDERS BELOW A
    FOCUSED ULTRASHORT LASER (~1e14 V/m).

    So "charge manipulation" at any interesting power destroys the only
    negative energy present, and destroys it before the apparatus even breaks
    down.  This is not a magnitude complaint.  It is the wrong sign, applied
    enthusiastically.

===============================================================================
S3 -- CHARGE CANNOT SUPPLY THE SIGN
===============================================================================

The Reissner-Nordstrom potential Phi = -M/r + Q^2/2r^2 has a positive term, and
it looks like the handle.  It is not, for two independent reasons:

    * Phi > 0 requires r < Q^2/2M, and charge.py measures that region HIDDEN
      inside the horizon at EVERY Q.
    * The Einstein-Maxwell positive energy theorem (Gibbons-Hull; Witten) gives
      Q <= M for any asymptotically flat solution.  The charge term can never
      dominate outside a horizon.  It is a theorem, not a limit of technique.

    WHAT CHARGE DOES SUPPLY IS THE SEAT, and charge.py already found that.
    A conjugate point needs T_kk > 0, which is what ordinary fields have.
    Charge is on the right side of the seat and the wrong side of the sign.

===============================================================================
S4 -- AND NO ASSEMBLY GIVES NET NEGATIVE MASS
===============================================================================

Binding energy is genuinely negative: a bound system weighs less than its
parts.  It is the most promising-looking route and it is bounded the same way.

        chemical binding        ~ 1e-9 of rest mass
        nuclear binding         ~ 1e-2
        accretion onto Kerr     ~ 0.42, the theoretical maximum

    Every one of them is a FRACTION of a positive rest mass you had to bring.
    The net stays positive, and that is not an accident of the examples --
    IT IS THE POSITIVE MASS THEOREM, which says exactly that no assembly of
    matter satisfying the energy conditions has negative total mass.

    THE FOUR ROUTES A SUPPLY QUESTION CAN TAKE -- field, charge, binding,
    vacuum -- ARE BOUNDED BY THE SAME THEOREM, EXCEPT THE LAST, WHICH IS
    BOUNDED BY hbar.  There is no fifth.

===============================================================================
S5 -- THE EFFICIENCY THE MATHEMATICS DEMANDS, AND IT EXCEEDS ONE
===============================================================================

Write the honest chain, with a conversion efficiency eta = |E_negative| /
E_supplied:

        Delta d  =  Lambda * (G/c^4) * eta * E_supplied

Solve for eta at a human budget.  To contract four light years by one per cent
using the WORLD'S ANNUAL ENERGY PRODUCTION (6.0e20 J):

        eta  >  7.6e36

    ETA MUST EXCEED ONE BY THIRTY-SIX ORDERS.  More negative energy out than
    energy in, which no conversion permits at any efficiency.

    AND EVEN AT eta = 1 -- perfect, thermodynamically impossible, every joule
    becoming a joule of negative energy -- the requirement is 4.59e57 J, the
    entire mass-energy of 2.6e10 SUNS.  Efficiency is not the problem.  The
    problem is c^4/G, and no conversion touches it.

===============================================================================
S6 -- SO THE LEVER IS GEOMETRY, NOT POWER -- AND THREE ROUTES AGREE WHERE
===============================================================================

The Casimir density goes as d^-4 while the requirement for a fractional
contraction eps goes as 1/b^2, so the ratio closes as b shrinks:

        |u_C| / u_required  =  pi^2 Lambda l_P^2 / (720 eps b^2)

  at eps = 1 %, b = 1 m:  3.6e-69       -- sixty-nine orders short
  it reaches unity at:    b = 6.0e-35 m = 3.7 PLANCK LENGTHS

    AND THAT AGREES WITH TWO INDEPENDENT MEASUREMENTS ALREADY IN THE TREE:
    corridor.py's Casimir seat crossing at 0.132 l_P and gjw.py's unity
    separation at 0.0934 l_P.  THREE DIFFERENT QUANTITIES -- a contraction, a
    seat and a coupling -- ALL CROSSING WITHIN TWO ORDERS OF THE PLANCK LENGTH.

    That is the answer to "what must we apply".  Not a bigger supply and not a
    better conversion: THE ONLY FREE VARIABLE IS THE GAP, and the gap has to
    reach the Planck scale, where this theory does not apply and nobody's does.

stdlib only.
"""
import math, sys

C, G = 2.99792458e8, 6.67430e-11
HBAR, EPS0, MU0 = 1.054571817e-34, 8.8541878128e-12, 1.25663706212e-6
HBARC = HBAR * C
LAMBDA = 9.982529                     # phase1.lam(), the seated geometry
SOLAR_MASS, EARTH_MASS = 1.98892e30, 5.9722e24
LIGHT_YEAR = 9.4607e15
WORLD_ANNUAL_J = 6.0e20               # ~600 EJ, order of magnitude
L_PLANCK = math.sqrt(HBAR * G / C ** 3)


# ------------------------------------------------------ S0: the conversion

def planck_force():
    """c^4/G = 1.21e44 N.  The only constant in the transition's cost."""
    return C ** 4 / G


def metres_per_joule():
    """G/c^4 = (G/c^2)/c^2 -- E = mc^2 is ALREADY INSIDE the coupling."""
    return G / C ** 4


def joules_per_metre(lam=LAMBDA):
    return C ** 4 / (G * lam)


def earth_energies_per_metre(lam=LAMBDA):
    return joules_per_metre(lam) / (EARTH_MASS * C * C)


def conversion_already_applied(tol=1e-12):
    """G/c^4 == (G/c^2)/c^2.  Checked, because the whole point rests on it."""
    return abs(metres_per_joule() - (G / C ** 2) / C ** 2) <= tol * metres_per_joule()


# --------------------------------- S2: electricity adds positive energy

def u_applied(E_field=0.0, B_field=0.0):
    """Classical EM energy density.  POSITIVE-DEFINITE at every field."""
    return 0.5 * EPS0 * E_field ** 2 + B_field ** 2 / (2.0 * MU0)


def u_casimir(d):
    """-pi^2 hbar c / 720 d^4.  Depends on the GAP, and on no applied field."""
    return -(math.pi ** 2) * HBARC / (720.0 * d ** 4)


def u_net(d, E_field=0.0, B_field=0.0):
    return u_casimir(d) + u_applied(E_field, B_field)


def cancelling_field(d):
    """The applied E that zeroes the Casimir dip.  Below breakdown at 10 nm."""
    return math.sqrt(2.0 * abs(u_casimir(d)) / EPS0)


def more_power_is_worse(d=1.0e-8, lo=0.0, hi=1.0e6):
    """d(u_net)/d(applied field) > 0 always.  Measured, not argued."""
    return u_net(d, hi) > u_net(d, lo)


BREAKDOWN_SOLID = 1.0e8               # V/m, dielectric breakdown, order
LASER_FOCUSED = 1.0e14                # V/m, focused ultrashort pulse, order


def breakdown_beats_casimir(d=1.0e-8):
    """At a realistic gap, ordinary breakdown fields already cancel it."""
    return BREAKDOWN_SOLID > cancelling_field(d)


# ------------------------------------------- S3 / S4: the sign, four routes

# (route, supplies the sign?, what bounds it)
ROUTES = (
    ("classical E and B fields", False,
     "T_00 = (eps0 E^2 + B^2/mu0)/2 >= 0, POSITIVE-DEFINITE at every field"),
    ("charge / Reissner-Nordstrom", False,
     "Q <= M by the Einstein-Maxwell positive energy theorem, and the "
     "Phi > 0 region is hidden inside the horizon at every Q (charge.py)"),
    ("binding energy", False,
     "genuinely negative but bounded by a fraction of the positive rest mass "
     "brought -- 1e-9 chemical, 1e-2 nuclear, 0.42 Kerr accretion. The net "
     "stays positive, which IS the positive mass theorem"),
    ("quantum vacuum: Casimir, squeezed", True,
     "the ONLY route that supplies the sign, and it is bounded by hbar rather "
     "than by the positive mass theorem: |rho| <~ hbar c / L^4"),
)


def routes_supplying_the_sign():
    return [r[0] for r in ROUTES if r[1]]


def only_one_route():
    """Four routes, one sign.  And it is the one bounded by hbar."""
    return len(routes_supplying_the_sign()) == 1


BINDING_FRACTIONS = (("chemical", 1e-9), ("nuclear", 1e-2), ("Kerr accretion", 0.42))


def binding_ever_net_negative():
    """No: every fraction is < 1 of a positive rest mass.  Positive mass theorem."""
    return any(f >= 1.0 for _n, f in BINDING_FRACTIONS)


# ------------------------------------- S5: the efficiency the maths demands

def energy_for_contraction(dd_metres, eta=1.0, lam=LAMBDA):
    """E_supplied = Delta d * c^4 / (G Lambda eta)."""
    return dd_metres * C ** 4 / (G * lam * eta)


def required_eta(dd_metres, budget_joules, lam=LAMBDA):
    """Solve the chain for eta.  If this exceeds 1, no conversion suffices."""
    return energy_for_contraction(dd_metres, 1.0, lam) / budget_joules


def eta_exceeds_unity(dd_metres=0.01 * 4.0 * LIGHT_YEAR,
                      budget_joules=WORLD_ANNUAL_J):
    return required_eta(dd_metres, budget_joules) > 1.0


# ------------------------------------------- S6: the lever is geometry

def casimir_over_required(b, eps=0.01, lam=LAMBDA):
    """|u_C| / u_required = pi^2 Lambda l_P^2 / (720 eps b^2).

    The requirement for a FRACTIONAL contraction eps goes as 1/b^2 while the
    Casimir density goes as 1/b^4, so the ratio closes as the gap shrinks.
    """
    return (math.pi ** 2) * lam * L_PLANCK ** 2 / (720.0 * eps * b * b)


def casimir_unity_gap(eps=0.01, lam=LAMBDA):
    """The b at which the ratio reaches one."""
    return math.sqrt((math.pi ** 2) * lam * L_PLANCK ** 2 / (720.0 * eps))


def unity_gap_in_planck_lengths(eps=0.01):
    return casimir_unity_gap(eps) / L_PLANCK


CORRIDOR_CROSSING_LP = 0.132          # corridor.py, the Casimir SEAT crossing
GJW_CROSSING_LP = 0.0934              # gjw.py, the unity SEPARATION


def three_routes_agree(tol_orders=2.0):
    """A contraction, a seat and a coupling -- all within two orders of l_P."""
    vals = (unity_gap_in_planck_lengths(), CORRIDOR_CROSSING_LP, GJW_CROSSING_LP)
    return math.log10(max(vals) / min(vals)) < tol_orders


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

    print("S0 -- THE CONVERSION IS ALREADY INSIDE THE EQUATION")
    near("c^4/G, the Planck force (N)", planck_force(), 1.21026e44, 1e-5)
    near("G/c^4 (m/J)", metres_per_joule(), 8.26272e-45, 1e-5)
    chk("G/c^4 == (G/c^2)/c^2 -- E=mc^2 is already there",
        conversion_already_applied(), True)
    near("joules per metre contracted", joules_per_metre(), 1.21237e43, 1e-5)
    near("  = Earth mass-energies per metre", earth_energies_per_metre(), 22.588, 1e-4)

    print("\nS2 -- ELECTRICITY ADDS POSITIVE ENERGY.  MORE POWER IS WORSE.")
    chk("classical EM density is non-negative at 1e14 V/m",
        u_applied(1.0e14) >= 0.0, True)
    chk("d(u_net)/d(applied field) > 0", more_power_is_worse(), True)
    for d in (1.0e-9, 1.0e-8):
        near("cancelling field at d = %.0e m (V/m)" % d, cancelling_field(d),
             9.8940e9 if d == 1.0e-9 else 9.8940e7, 1e-4)
    chk("ordinary dielectric breakdown already cancels it at 10 nm",
        breakdown_beats_casimir(), True)
    near("  a focused laser exceeds the cancelling field by", 
         LASER_FOCUSED / cancelling_field(1.0e-8), 1.0107e6, 1e-3)

    print("\nS3 / S4 -- FOUR ROUTES, AND ONLY ONE SUPPLIES THE SIGN")
    for n, s, why in ROUTES:
        print("      %-28s %-5s %s" % (n, "YES" if s else "no", why[:40]))
    chk("routes that supply the sign", routes_supplying_the_sign(),
        ["quantum vacuum: Casimir, squeezed"])
    chk("exactly one", only_one_route(), True)
    chk("binding energy ever nets negative", binding_ever_net_negative(), False)
    print("      and the other three are bounded by the SAME theorem -- the")
    print("      positive mass theorem.  The fourth is bounded by hbar instead.")

    print("\nS5 -- THE EFFICIENCY DEMANDED, AND IT EXCEEDS ONE")
    dd = 0.01 * 4.0 * LIGHT_YEAR
    near("energy at eta = 1 for 1 % of 4 ly (J)", energy_for_contraction(dd), 4.5878e57, 1e-4)
    near("  in solar mass-energies", energy_for_contraction(dd) / (SOLAR_MASS * C * C),
         2.5667e10, 1e-4)
    near("eta required against world annual energy", required_eta(dd, WORLD_ANNUAL_J),
         7.6463e36, 1e-4)
    chk("eta must exceed 1 -- no conversion suffices", eta_exceeds_unity(), True)
    print("      Efficiency is not the problem.  c^4/G is, and no conversion")
    print("      touches it.")

    print("\nS6 -- SO THE LEVER IS GEOMETRY, AND THREE ROUTES AGREE WHERE")
    near("Casimir over required at b = 1 m, eps = 1 %", casimir_over_required(1.0),
         3.5729e-69, 1e-3)
    near("the gap at which it reaches unity (m)", casimir_unity_gap(), 5.9774e-35, 1e-3)
    near("  in Planck lengths", unity_gap_in_planck_lengths(), 3.6982, 1e-3)
    print("      corridor.py's seat crossing   %.4f l_P" % CORRIDOR_CROSSING_LP)
    print("      gjw.py's unity separation     %.4f l_P" % GJW_CROSSING_LP)
    chk("three different quantities, all within two orders of l_P",
        three_routes_agree(), True)

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE CONVERSION IS ALREADY DONE.  G/c^4 = (G/c^2)/c^2, so E = mc^2
  is not something you apply to the transition equation -- it is
  already inside the coupling.  Paying in joules instead of kilograms
  is the same bill in another currency at a rate already applied:
  1.212e43 J per metre, which is 22.6 Earth mass-energies per metre.

  SO THE SUPPLY FORM CHANGES THE LOGISTICS AND NOT THE MAGNITUDE.
  The only thing worth asking a supply route is whether it supplies
  the SIGN, and four routes exist.  Classical fields cannot: EM
  stress-energy is positive-definite at every field strength.  Charge
  cannot: Q <= M is a theorem and the Phi > 0 region is hidden at
  every Q.  Binding cannot: it is always a fraction of a positive
  rest mass, which is the positive mass theorem restated.  Only the
  QUANTUM VACUUM can, and it is bounded by hbar rather than by that
  theorem.

  AND CHARGE MANIPULATION IS ACTIVELY HARMFUL, WHICH IS THE SHARPEST
  THING HERE.  The Casimir density depends on the GAP and on no
  applied field, while the field you apply contributes positively as
  its square.  At a ten-nanometre gap the field that CANCELS the
  Casimir dip is 9.9e7 V/m -- below the dielectric breakdown of a
  solid, and a million times below a focused laser.  Applying charge
  destroys the only negative energy in the apparatus before the
  apparatus even breaks down.

  EFFICIENCY CANNOT RESCUE IT.  Against the world's annual energy
  production, eta would have to exceed 1 by thirty-six orders -- more
  negative energy out than energy in.  And at a perfect eta = 1 the
  requirement is still the mass-energy of 26 billion suns.

  WHAT IS LEFT IS THE GAP.  The requirement falls as 1/b^2 and the
  Casimir density rises as 1/b^4, so the ratio closes -- at
  b = 3.7 Planck lengths.  corridor.py put its seat crossing at
  0.132 l_P and gjw.py its coupling at 0.0934 l_P.  THREE DIFFERENT
  QUANTITIES, ALL CROSSING WITHIN TWO ORDERS OF THE PLANCK LENGTH.

  That is the answer.  Not a bigger supply, not a better conversion:
  the only free variable is the gap, and it has to reach a scale
  where this theory does not apply and nobody's does.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
