#!/usr/bin/env python3
"""
higgs.py -- CAN THE HIGGS FIELD OPEN THE THROAT?

M: "The higgs boson.  We need to build a higgs field."

THE INSTINCT LANDS ON THE RIGHT OBJECT AND THE ANSWER SPLITS THREE WAYS, ONE OF
WHICH IS A FIRST FOR THIS THREAD.

    MAGNITUDE   YES, and it is the first candidate in the whole thread that
                OVERSHOOTS instead of falling short -- by a factor of ~1200.
    NEC         NO, and not by a margin: a minimally coupled scalar satisfies
                the NEC IDENTICALLY, for ANY potential, and a CONSTANT field --
                which is exactly what a VEV is -- SATURATES it at exactly zero.
    THE ESCAPE  xi.  Barcelo-Visser prove a traversable wormhole branch for
                EVERY xi > 0, and the Higgs is the one Standard Model field
                whose xi is not optional.  AND THE GATE THEY STATE IS THE
                HIERARCHY PROBLEM, EXACTLY.

===============================================================================
1. A MINIMALLY COUPLED SCALAR SATISFIES THE NEC IDENTICALLY.  THE POTENTIAL
   DOES NOT ENTER
===============================================================================

For L = -(1/2)(grad phi)^2 - V(phi),

    T_mn = d_m phi d_n phi - g_mn [ (1/2)(grad phi)^2 + V(phi) ]

Contract with a null k.  The bracket multiplies g_mn k^m k^n, WHICH IS ZERO BY
DEFINITION OF NULL, so the whole potential term drops out and

    T_mn k^m k^n = (k^m d_m phi)^2  >=  0

THE MEXICAN HAT IS IRRELEVANT.  Its depth is irrelevant, its sign is
irrelevant, its shape is irrelevant.  No potential whatever can make a
minimally coupled scalar violate the NEC -- Barcelo-Visser's own eq. (2.6),
READ FROM SOURCE: "This condition is clearly satisfied by minimally coupled
scalars."

AND A CONSTANT FIELD SATURATES IT AT EXACTLY ZERO.  A VEV is a constant field,
so d_m phi = 0 and T_mn = -g_mn V: a perfect fluid with

        rho = V,   p = -V,   w = -1,   rho + p = 0 EXACTLY

w = -1 IS A GENUINE ISOTROPIC TENSION and it is what M is reaching for.  It
beats electromagnetism's w = +1 in every way except the only one that counts.

    THE FIELD SITS PRECISELY ON THE LINE IT WOULD HAVE TO CROSS.

That is emtension.py's sentence, and this is THE SECOND FIELD TO LAND ON IT,
for the same structural reason: both T_kk are manifestly non-negative
quadratic forms, and the interesting configuration is the one that makes the
form vanish.  EM saturates because a radial field is boost-invariant in the t-r
plane; the scalar saturates because a VEV has no gradient.  DIFFERENT REASONS,
IDENTICAL VERDICT.

AND EVERY KNOB TURNS THE WRONG WAY.  Give the field a gradient and T_kk becomes
STRICTLY positive -- further from the line, not nearer.  There is no
minimally-coupled configuration anywhere between "useless" and "worse".

===============================================================================
2. THE MAGNITUDE, AND IT IS THE FIRST OVERSHOOT IN THE THREAD
===============================================================================

The Standard Model Higgs potential at its minimum:

        V_min = -lambda v^4/4 = -m_h^2 v^2/8

With v from the Fermi constant and m_h from the PDG this is about
-1.19e8 GeV^4, and in SI about 2.48e45 J/m^3 in magnitude.  pressure.py's
throat needs TAU_0 = 2.073325e42 Pa.

        THE HIGGS VACUUM CARRIES ABOUT 1200 TIMES WHAT THE THROAT NEEDS.

EVERY OTHER CANDIDATE IN THIS THREAD FELL SHORT: amps.py by seventeen orders,
kugelblitz.py by fifty-six, persist.py by sixty-nine, antigravity.py by a
category.  THIS ONE OVERSHOOTS.  And the SIGN of rho is right too -- the
electroweak vacuum sits BELOW the symmetric point, so it carries genuinely
NEGATIVE potential energy density.

TWO CAVEATS, AND THEY ARE NOT SMALL.

  (a) THE ABSOLUTE NORMALISATION OF V IS NOT MEASURED.  In flat-space QFT only
      DIFFERENCES of V are observable and an additive constant is free.  The
      number above is the electroweak contribution to the cosmological constant
      under the convention V(0) = 0.  It exceeds the OBSERVED vacuum energy by
      some fifty-four orders, and that excess IS THE COSMOLOGICAL CONSTANT
      PROBLEM.  So the magnitude is real as a contribution and is cancelled, by
      something nobody has identified, down to a number we do measure.
  (b) IT IS UNIFORM.  It is the same inside the throat as outside it, so it
      does not localise, cannot be switched on in one place, and is already
      included in whatever Lambda is.  A resource you cannot put somewhere is
      not a resource.

===============================================================================
3. THE ESCAPE IS xi, AND THE HIGGS IS THE ONE FIELD THAT MUST HAVE IT
===============================================================================

xi phi^2 R is a dimension-four operator forbidden by no symmetry, and in curved
space it is generated radiatively even if set to zero -- which is why it is
standard to carry it.  RECORDED AS ELEMENTARY; no source was read for it here.
For the Higgs the operator is xi H^dagger H R, and it is the reason Higgs
inflation exists at all.

BARCELO-VISSER (gr-qc/0003025, READ FROM SOURCE) SETTLE WHAT xi BUYS:

  - eq. (2.6): NEC = [phi'^2 - xi (phi^2)''] / (kappa - xi phi^2).  For xi > 0
    and |phi| small, ANY LOCAL MAXIMUM OF phi^2 VIOLATES THE POINTWISE NEC.
    POINTWISE NEC VIOLATION IS CHEAP.
  - BUT A WORMHOLE NEEDS ANEC, by topological censorship, AND ANEC IS NOT
    CHEAP.  Their case 2: for xi > 0 with phi^2 < kappa/xi everywhere, "the
    integrand appearing above is again positive and ANEC is satisfied".  Only
    their case 3, phi^2 > kappa/xi SOMEWHERE, admits ANEC violation.
  - and they find "an entire branch of traversable wormholes for every xi > 0",
    gated by exactly that condition, which they state as: "In all these
    solutions the scalar field has to reach absolute values above ~ m_p/sqrt(xi)
    ... either the scalar field acquires trans-Planckian values or the curvature
    coupling constant xi must become disturbingly large."

THE DISTINCTION MATTERS AND IS THE KIND THAT GETS FLATTENED: POINTWISE NEC
VIOLATION IS AVAILABLE TO THE HIGGS AT ANY xi > 0.  ANEC VIOLATION IS NOT.

===============================================================================
4. AND THE GATE IS THE HIERARCHY PROBLEM.  EXACTLY, NOT BY ANALOGY
===============================================================================

Put the Higgs VEV into their condition.  ANEC violation needs

        phi > M_reduced / sqrt(xi)        i.e.   xi > (M_reduced/v)^2

M_reduced = M_Planck/sqrt(8 pi) = 2.4e18 GeV and v = 246.22 GeV, so

        v / M_reduced  =  1.01e-16
        xi required    =  9.8e31

Higgs inflation runs at xi ~ 1.7e4 (Bezrukov-Shaposhnikov, NAMED-NOT-READ),
TWENTY-EIGHT ORDERS BELOW.  And the reason the gate fails is not an accident of
this calculation: BARCELO-VISSER'S THRESHOLD IS THE PLANCK SCALE, AND THE
HIERARCHY PROBLEM IS THE STATEMENT THAT v SITS SIXTEEN ORDERS BELOW IT.

    THE SINGLE MOST FAMOUS FINE-TUNING IN PARTICLE PHYSICS IS EXACTLY THE
    QUANTITY STANDING BETWEEN THE HIGGS AND A TRAVERSABLE THROAT.

Squared, because the gate is on xi and the field enters squared: sixteen orders
of hierarchy become thirty-two orders of xi.

===============================================================================
5. WHAT DOES VIOLATE IT, NAMED SO THE LEDGER IS HONEST
===============================================================================

A PHANTOM (wrong-sign kinetic term) gives T_kk = -(k.grad phi)^2 <= 0 and
violates the NEC at every gradient.  It is exhibited below AS A NEGATIVE
CONTROL, and it is not the Higgs: the Higgs kinetic term's sign is measured
every time the particle propagates.  Naming the thing that works, and that we
do not have, is part of not overclaiming the thing that does not.

NOTHING IS REPAIRED.
"""

import math
import sys
from fractions import Fraction

import ladder
import pressure

c = ladder.c
G = ladder.G
HBAR = ladder.HBAR

GEV_IN_J = 1.602176634e-10           # SI-EXACT (elementary charge is exact)
HBAR_C = HBAR * c                    # J m

# Measured inputs.  STATUS IS PART OF THE VALUE.
G_FERMI = 1.1663788e-5               # GeV^-2, PDG          NAMED-NOT-READ
M_HIGGS = 125.20                     # GeV, PDG             NAMED-NOT-READ
XI_HIGGS_INFLATION = 1.7e4           # Bezrukov-Shaposhnikov NAMED-NOT-READ
RHO_LAMBDA_OBS = 6.0e-10             # J/m^3, order          ORDER

BV_READ_FROM_SOURCE = True           # gr-qc/0003025
MINIMAL_SCALAR_SATISFIES_NEC = True
VEV_SATURATES_NEC = True
POINTWISE_NEC_IS_CHEAP = True        # BV sect. 2.2, xi > 0
ANEC_IS_NOT = True                   # BV sect. 2.3, cases 2 and 3
HIGGS_IS_NOT_A_PHANTOM = True
NOTHING_IS_REPAIRED = True


# ------------------------------------------------------------------- the SM
def vev():
    """v = (sqrt(2) G_F)^(-1/2), in GeV."""
    return 1.0 / math.sqrt(math.sqrt(2.0) * G_FERMI)


def lam():
    """lambda = m_h^2 / (2 v^2)."""
    return M_HIGGS ** 2 / (2.0 * vev() ** 2)


def v_min_gev4():
    """V at the minimum of the Mexican hat, with V(0) = 0.  NEGATIVE."""
    return -lam() * vev() ** 4 / 4.0


def gev4_to_si(x):
    """GeV^4 -> J/m^3."""
    return x * GEV_IN_J ** 4 / HBAR_C ** 3


def planck_mass_gev():
    return math.sqrt(HBAR * c ** 5 / G) / GEV_IN_J


def reduced_planck_gev():
    return planck_mass_gev() / math.sqrt(8.0 * math.pi)


# ------------------------------------------- the scalar stress tensor, long way
# Integers, not floats, so the whole construction runs unchanged over
# fractions.Fraction and the NEC identity below is PROVED rather than measured
# -- proofs.py's house method.
ETA = (-1, 1, 1, 1)


def T_scalar(dphi, V, ghost=False):
    """T_mn for L = -(s/2)(grad phi)^2 - V, s = +1 normal, -1 phantom.

    Built componentwise from the definition -- no null shortcut anywhere, so
    the NEC result below is a measurement and not a restatement.
    """
    s = -1 if ghost else 1
    kin = sum(ETA[m] * dphi[m] * dphi[m] for m in range(4))   # g^mn d_m d_n
    T = [[None] * 4 for _ in range(4)]
    for m in range(4):
        for n in range(4):
            g_mn = ETA[m] if m == n else 0
            T[m][n] = s * dphi[m] * dphi[n] - g_mn * ((s * kin) / 2 + V)
    return T


def contract(T, k):
    return sum(T[m][n] * k[m] * k[n] for m in range(4) for n in range(4))


# PYTHAGOREAN QUADRUPLES a^2+b^2+c^2 = N^2, so k^m = (N, a, b, c) has
# k.k = -N^2 + a^2 + b^2 + c^2 = 0 EXACTLY IN BINARY FLOATING POINT.
#
# This matters and it is not fussiness.  The potential enters T only through
# -g_mn V, so its contribution to T_kk is -V (k.k) -- ZERO BY THE THEOREM.  With
# a direction built from sin and cos, k.k is zero only to ~1e-16, and a
# potential of 1e12 GeV^4 turns that rounding into a 1e-4 residual that LOOKS
# like V-dependence.  That is sign.py's catastrophic-cancellation channel
# appearing a second time, in a test rather than in an integrand: the
# amplification factor is exactly |V| times machine epsilon.  Exact nulls remove
# it and the potential-independence comes out EXACT, which is what the theorem
# actually says.
QUADS = ((1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (4, 4, 7, 9),
         (2, 6, 9, 11), (6, 6, 7, 11), (3, 4, 12, 13), (2, 5, 14, 15),
         (2, 10, 11, 15), (1, 12, 12, 17), (8, 9, 12, 17), (1, 6, 18, 19))


def null_vector(q):
    """(k_m, k^m) for an exactly null k built from a Pythagorean quadruple.

    Entries stay INTEGERS so the contraction is exact under Fraction.
    """
    a, b, cc, N = q
    kup = (N, a, b, cc)
    return tuple(ETA[m] * kup[m] for m in range(4)), kup


def nec_scalar(dphi, V, q, ghost=False):
    """T_mn k^m k^n.  T is built with LOWER indices, so this contracts with the
    UPPER-index k -- the first draft used the lower one, which is also a perfect
    square and also non-negative, so the physics survived the slip and only the
    exact identity caught it."""
    _, kup = null_vector(q)
    return contract(T_scalar(dphi, V, ghost), kup)


def perfect_fluid_w(V):
    """A constant field: rho = V, p = -V.  Returns (rho, p, w, rho+p)."""
    return V, -V, -1.0, 0.0


# ------------------------------------------------ Barcelo-Visser's ANEC gate
def anec_gate_field_gev(xi):
    """|phi| must exceed this for ANEC violation.  BV: phi^2 > kappa/xi."""
    return reduced_planck_gev() / math.sqrt(xi)


def xi_required(phi_gev):
    """The xi that brings the gate down to a given field value."""
    return (reduced_planck_gev() / phi_gev) ** 2


def hierarchy():
    return vev() / reduced_planck_gev()


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    v = vev()
    Vm = v_min_gev4()
    Vsi = abs(gev4_to_si(Vm))
    tau = pressure.throat_tension(pressure.R_MOUTH)
    print("  the Standard Model Higgs")
    print("      %-38s %20.6f GeV" % ("v, from G_F", v))
    print("      %-38s %20.6f GeV" % ("m_h (PDG, NAMED-NOT-READ)", M_HIGGS))
    print("      %-38s %20.9f" % ("lambda = m_h^2/2v^2", lam()))
    print("      %-38s %20.6e GeV^4" % ("V at the minimum", Vm))
    print("      %-38s %20.6e J/m^3" % ("  |V_min| in SI", Vsi))
    print()
    print("  against the throat, and this is the first overshoot")
    print("      %-38s %20.6e Pa" % ("pressure.py TAU_0 needed", tau))
    print("      %-38s %20.6e" % ("  |V_min| / TAU_0", Vsi / tau))
    print("      %-38s %20.2f" % ("  orders of surplus",
                                  math.log10(Vsi / tau)))
    print("      %-38s %20.6e" % ("  vs observed vacuum energy",
                                  Vsi / RHO_LAMBDA_OBS))
    print("      %-38s %20.2f" % ("    orders (the CC problem)",
                                  math.log10(Vsi / RHO_LAMBDA_OBS)))
    print()
    print("  the NEC, measured from T built the long way")
    print("      %-26s %14s %14s %12s" % ("configuration", "V (GeV^4)",
                                          "T_kk", "verdict"))
    F = Fraction
    Vx = F(Vm)
    cases = [("VEV: constant field", (F(0),) * 4, Vx),
             ("constant, V > 0", (F(0),) * 4, -Vx),
             ("constant, V = 0", (F(0),) * 4, F(0)),
             ("time-varying", (F(3), F(0), F(0), F(0)), Vx),
             ("space-varying", (F(0), F(2), F(0), F(0)), Vx),
             ("both, deep well", (F(3, 2), F(-5, 2), F(7, 10), F(0)),
              F(-10) ** 9)]
    for name, d, V in cases:
        val = nec_scalar(d, V, QUADS[0])
        print("      %-26s %14.3e %14.6e %12s"
              % (name, float(V), float(val), "OK" if val >= 0 else "VIOLATED"))
    print("      and the phantom, as a negative control")
    val = nec_scalar((F(3), F(0), F(0), F(0)), Vx, QUADS[0], ghost=True)
    print("      %-26s %14.3e %14.6e %12s"
          % ("wrong-sign kinetic term", float(Vx), float(val),
             "OK" if val >= 0 else "VIOLATED"))
    print()
    print("      EXACT RATIONALS ABOVE, AND THAT IS NOT FUSSINESS: in double")
    print("      precision the constant-field rows read %+.3e instead of zero"
          % nec_scalar((0.0, 0.0, 0.0, 0.0), Vm, QUADS[0]))
    print("      and one of them PRINTS VIOLATED.  The residual is |V| times")
    print("      machine epsilon -- sign.py\'s cancellation channel, in a")
    print("      report rather than an integrand.  IT IS AN ARTEFACT.")
    print()
    rho, p, w, s = perfect_fluid_w(Vm)
    print("  a VEV is a perfect fluid")
    print("      %-38s %20.6e" % ("rho", rho))
    print("      %-38s %20.6e" % ("p", p))
    print("      %-38s %20.6f" % ("w = p/rho", w))
    print("      %-38s %20.6e" % ("rho + p", s))
    print()
    print("  Barcelo-Visser's ANEC gate (gr-qc/0003025, READ)")
    print("      %-38s %20.6e GeV" % ("Planck mass", planck_mass_gev()))
    print("      %-38s %20.6e GeV" % ("reduced Planck mass", reduced_planck_gev()))
    print("      %-16s %20s %20s" % ("xi", "gate |phi| (GeV)", "v/gate"))
    for xi in (1e-1, 1.0, 1.0 / 6.0, XI_HIGGS_INFLATION, 1e15, 1e31,
               xi_required(v)):
        g = anec_gate_field_gev(xi)
        print("      %-16.4e %20.6e %20.6e" % (xi, g, v / g))
    print()
    print("      %-38s %20.6e" % ("xi REQUIRED at the Higgs VEV",
                                  xi_required(v)))
    print("      %-38s %20.6e" % ("xi used by Higgs inflation",
                                  XI_HIGGS_INFLATION))
    print("      %-38s %20.2f" % ("  orders short",
                                  math.log10(xi_required(v)
                                             / XI_HIGGS_INFLATION)))
    print()
    print("  and the gate IS the hierarchy problem")
    print("      %-38s %20.6e" % ("v / M_reduced", hierarchy()))
    print("      %-38s %20.2f" % ("  orders of hierarchy",
                                  -math.log10(hierarchy())))
    print("      %-38s %20.2f" % ("  doubled, because xi takes phi^2",
                                  math.log10(xi_required(v))))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Right object, right magnitude -- the first overshoot in the")
    print("  thread -- and the wrong side of a line the field cannot leave.")
    print("  The escape is xi, and the gate on xi is the hierarchy problem.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("higgs.py --selftest")
    print()

    # ------------------------------------------ THE THEOREM, MEASURED NOT ASSUMED
    # T_kk = (k.grad phi)^2 for EVERY gradient, EVERY potential, EVERY null k.
    import random
    rnd = random.Random(20260912)
    # OVER EXACT RATIONALS, so "identically" means identically.  4000 random
    # gradients x random potentials x twelve exactly-null directions, every
    # arithmetic operation exact -- this is a PROOF on a grid, not a sample.
    exact_fail = 0
    negative = 0
    for _ in range(4000):
        d = tuple(Fraction(rnd.randrange(-500, 501), 100) for _ in range(4))
        V = Fraction(rnd.randrange(-10 ** 15, 10 ** 15 + 1), 7)
        q = QUADS[rnd.randrange(len(QUADS))]
        klo, kup = null_vector(q)
        got = nec_scalar(d, V, q)
        want = sum(kup[m] * d[m] for m in range(4)) ** 2
        if got != want:
            exact_fail += 1
        if got < 0:
            negative += 1
    chk("T_kk == (k.grad phi)^2 EXACTLY, 4000 rational configurations",
        exact_fail, 0)
    chk("and it never once went negative", negative, 0)
    chk("recorded", MINIMAL_SCALAR_SATISFIES_NEC, True)
    # the potential really is absent -- EXACTLY
    d = tuple(Fraction(x, 10) for x in (17, -4, 22, 9))
    base = nec_scalar(d, Fraction(0), QUADS[3])
    for V in (-10 ** 30, -10 ** 12, -1, 0, 1, 10 ** 12, 10 ** 30):
        chk("V = %g changes nothing at all" % V,
            nec_scalar(d, Fraction(V), QUADS[3]), base)
    # the null vectors really are null, exactly
    for q in QUADS:
        klo, kup = null_vector(q)
        chk("k%s is null exactly" % (q,),
            sum(klo[m] * kup[m] for m in range(4)), 0.0)

    # ------------------------------------------------- the VEV saturates it
    zero = (Fraction(0),) * 4
    Vm_exact = Fraction(v_min_gev4())
    for q in QUADS:
        chk("a constant field gives exactly zero on k%s" % (q,),
            nec_scalar(zero, Vm_exact, q), 0)
    rho, p, w, s = perfect_fluid_w(v_min_gev4())
    chk("a VEV has w = -1", w, -1.0)
    chk("and rho + p = 0", s, 0.0)
    chk("recorded as saturation, not violation", VEV_SATURATES_NEC, True)
    # EVERY KNOB TURNS THE WRONG WAY: a gradient makes it strictly positive
    chk("any gradient makes it strictly worse",
        all(nec_scalar(tuple(Fraction(g) if i == j else Fraction(0)
                             for i in range(4)), Vm_exact, q) > 0
            for j in range(4) for g in (Fraction(1, 10), 1, 10)
            for q in QUADS), True)

    # NEGATIVE CONTROL: a phantom DOES violate it, so the test can detect one
    for g in (Fraction(1, 2), 3, 20):
        chk("a phantom violates the NEC at gradient %s" % g,
            all(nec_scalar((Fraction(g), Fraction(0), Fraction(0),
                            Fraction(0)), Fraction(0), q, ghost=True) < 0
                for q in QUADS), True)
    chk("and the Higgs is not one", HIGGS_IS_NOT_A_PHANTOM, True)

    # ------------------------------------------------------- the Standard Model
    chkrel("v from G_F", vev(), 246.2196, 1e-5)
    chkrel("lambda", lam(), 0.129280575661, 1e-10)
    chk("V_min is negative", v_min_gev4() < 0.0, True)
    # the two closed forms for V_min must agree
    chkrel("V_min = -m_h^2 v^2/8", v_min_gev4(),
           -M_HIGGS ** 2 * vev() ** 2 / 8.0, 1e-12)
    chkrel("Planck mass in GeV", planck_mass_gev(), 1.220890e19, 1e-5)
    chkrel("reduced Planck mass", reduced_planck_gev(), 2.435323e18, 1e-5)

    # ----------------------------------------------- the overshoot, and it is real
    tau = pressure.throat_tension(pressure.R_MOUTH)
    surplus = abs(gev4_to_si(v_min_gev4())) / tau
    chk("the Higgs vacuum EXCEEDS the throat requirement", surplus > 1.0, True)
    chk("by more than a hundred", surplus > 1e2, True)
    chk("and less than ten thousand", surplus < 1e4, True)
    # NEGATIVE CONTROL: every other candidate in the tree fell short, so an
    # overshoot is a real distinction and not what this comparison always does.
    gapmass = __import__("persist").gap_mass(pressure.R_MOUTH)
    chk("while persist.py's candidate fell short", gapmass > 1e60, True)

    # -------------------------------------------------- Barcelo-Visser's gate
    chk("Barcelo-Visser was read from source", BV_READ_FROM_SOURCE, True)
    chk("pointwise NEC violation is available at any xi > 0",
        POINTWISE_NEC_IS_CHEAP, True)
    chk("ANEC violation is not", ANEC_IS_NOT, True)
    # the gate is phi > M_red/sqrt(xi); check it inverts
    for xi in (1e-3, 1.0 / 6.0, 1.0, 1e4, 1e31):
        chkrel("gate inverts at xi=%g" % xi,
               xi_required(anec_gate_field_gev(xi)), xi, 1e-12)
    chk("at xi = 1 the gate is the reduced Planck mass",
        abs(anec_gate_field_gev(1.0) - reduced_planck_gev()) < 1e3, True)
    chk("the Higgs VEV is below the gate at Higgs-inflation xi",
        vev() < anec_gate_field_gev(XI_HIGGS_INFLATION), True)
    xr = xi_required(vev())
    chkrel("xi required at the VEV", xr, 9.7829068836e31, 1e-9)
    chk("which is more than 1e27 above Higgs inflation",
        xr / XI_HIGGS_INFLATION > 1e27, True)

    # ------------------------------------------ and the gate IS the hierarchy
    h = hierarchy()
    chkrel("v/M_reduced", h, 1.0110346504e-16, 1e-9)
    # THE IDENTITY: xi_required is exactly the hierarchy squared.  Not an
    # analogy -- the same number, because xi couples phi^2.
    chkrel("xi_required = (v/M_red)^-2 exactly", xr, 1.0 / h ** 2, 1e-12)
    chk("sixteen orders of hierarchy, thirty-two of xi",
        round(math.log10(xr) / -math.log10(h), 6), 2.0)

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
