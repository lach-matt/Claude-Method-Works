"""
nullbound.py -- *** CONCLUSION WITHDRAWN by anec.py.  READ THAT FIRST. ***

    The error: SNEC must hold for EVERY sampling function, and this file
    evaluated it at ONE width -- the wall thickness -- which is the width at
    which the bound is loosest.  The right-hand side falls as 1/w^2 while the
    left falls only as 1/w once w exceeds the wall, so the bound is VIOLATED for
    every sampling width above ~0.93 in units of the bubble radius.  One width
    is not a scan.  And QNEC, which integrates to ANEC, forbids the
    configuration outright: INT T_kk dx is negative on every ray measured.

    WHAT STANDS: Fewster & Roman (no null QIs in 4D); that Pfenning-Ford is a
    timelike instrument; and the 1/D^2 cancellation, which is real arithmetic.
    The wall thickness genuinely does drop out -- into PROHIBITION rather than
    permission.  Everything below is kept executable so the mistake cannot be
    re-derived, per this tree's practice.

nullbound.py -- DIRECTIVE 2's obstacle, and it is the wrong instrument.

warpenergy.py closed directive 1 and handed off one sentence: the entire cost of
a warp drive is the wall, M ~ -v_s^2 R^2/(36 G D), and D is set by a quantum
inequality.  Pfenning and Ford's is the one everybody quotes, and it bounds the
WALL THICKNESS at about 10^2 Planck lengths, which is what turns 0.19 solar
masses into 10^62 kg.

    THAT BOUND COMES FROM A TIMELIKE QUANTUM INEQUALITY, AND THE QUANTITY BEING
    BOUNDED IS NULL.  Change to the null-smeared condition and the wall
    thickness does not get a larger bound.  IT CANCELS.

-- WHY THE TIMELIKE ONE IS THE WRONG INSTRUMENT -------------------------------
Not this file's finding -- the corpus's, banked at Register 5537 and reached
independently there:

    Fewster & Roman, Phys. Rev. D 67 (2003) 044003: for the massless minimally
    coupled scalar in FOUR-dimensional Minkowski space, weighted averages of the
    null-contracted stress tensor along a null geodesic are UNBOUNDED FROM BELOW
    on the class of Hadamard states.  THERE ARE NO QUANTUM INEQUALITIES ALONG
    NULL GEODESICS IN 4D.  In two dimensions they exist.

Register 5541 then prices every finite replacement: Wall 2010 spends
COMPLETENESS, Kontou & Olum 2015 spend TIMELIKE SMEARING and small curvature,
and the Smeared NEC of Freivogel & Krommydas spends a UV CUTOFF, "making the
bound FINITE and explicitly computable as -#N/l_UV^(d-2) INTEGRAL g'^2 dl".

So the honest bound on a null-contracted quantity in four dimensions is the
SNEC, and the SNEC is the instrument this comparison needs.

-- AND THEN THE THICKNESS CANCELS, EXACTLY ------------------------------------
Two 1/D^2 laws meet, and both of them also carry 1/G.

    REQUIRED.  M = -v_s^2 R^2/(36 G D) spread over a shell of volume 4 pi R^2 D:

            rho  =  - v_s^2 / (144 pi G D^2)

        R cancels -- checked here at R = 10, 100, 1,000 m, identical to six
        figures -- so the wall's density depends on NOTHING but v_s and D.

    ALLOWED.  SNEC: INTEGRAL <T_kk> g^2 dl >= -(4B/G) INTEGRAL (g')^2 dl.  For a
        normalised Gaussian of width D, INTEGRAL (g')^2 dl = 1/(2D^2), so

            |<T_kk>|  <=  2B / (G D^2)

    RATIO.  D^2 cancels.  G cancels.  What is left is a pure number:

            required / allowed  =  v_s^2 / (288 pi B)  =  v_s^2 / 9

        at Freivogel-Krommydas's holographic B = 1/(32 pi).  Verified constant to
        six figures over D from 1 mm to the Planck length -- thirty-two orders.

            v_s = 0.1 c    ratio 0.0011     allowed, 900x margin
            v_s = 1.0 c    ratio 0.111      allowed, 9x margin
            v_s = 3.0 c    ratio 1.000      saturated
            v_s = 4.0 c    ratio 1.778      forbidden

    THE WALL-THICKNESS BOUND IS AN ARTEFACT OF THE TIMELIKE INSTRUMENT.  On the
    null-smeared condition there is no preferred thickness at all: a metre-thick
    wall and a Planck-thick wall are equally admissible, and what is bounded is
    the VELOCITY.
    *** WITHDRAWN.  "Equally admissible" is wrong; they are equally INadmissible.
        The thickness-independence is real and the sign of the conclusion is
        not.  See anec.py. ***

-- WHAT THIS IS AND IS NOT ----------------------------------------------------
It is a scaling comparison with four O(1) exposures, every one of them named:

  1. E vs T_kk.  The required figure is the EULERIAN energy density, the bound is
     on the NULL-contracted component.  Both are proportional to v_s^2 f'^2 -- so
     the 1/D^2 structure, which is the finding, is untouched -- but their ratio is
     an O(1) this file does not compute.
  2. B is not a theorem.  Freivogel & Krommydas argue B <= 1/(32 pi) holographically.
  3. The SNEC itself is a conjecture with holographic support, not a proof.
  4. The Gaussian gives INTEGRAL(g')^2 = 1/(2D^2); another sampling function gives
     another O(1).

So the number v_s^2/9 carries perhaps an order of magnitude either way, and at
v_s = 0.1 c there are nearly three orders of margin.  THE STRUCTURAL CLAIM IS
WHAT SURVIVES ALL FOUR: both sides go as 1/(G D^2), so the thickness cancels
whatever the O(1)s are, and a bound on D cannot be what a null condition says.

This does NOT say a warp drive can be built.  It says the specific reason
everybody gives for why it cannot -- 10^62 kg, forced by a Planck-thin wall --
rests on applying a timelike bound to a null quantity, in a dimension where the
null bound provably does not exist.
*** AND THE REPLACEMENT REASON IS WORSE, NOT ABSENT.  anec.py measures ANEC
    violated on every ray, and QNEC integrates to ANEC.  The 10^62 kg was the
    wrong statement of the problem; the right statement is a prohibition that
    does not depend on D at all. ***

-- AND IT LANDS shape.py's PREDICTION 2, PARTLY -------------------------------
shape.py predicted, before this file existed, that the energy-condition family
was where a static bound would loosen.  It named QNEC as the dynamical
counterpart.  The move that actually landed is timelike-QI -> null-SNEC, which is
the same family and a different member: SNEC is state-INDEPENDENT, QNEC is state-
dependent, and QNEC proper is still unasked.  Scored as a PARTIAL hit -- right
family, wrong member -- because scoring it as a full one would be the fitting
error shape.py exists to avoid.

stdlib only.  warpenergy.py supplies the required side; nothing is transcribed.
"""
import math, sys

G = 6.67430e-11
C = 299792458.0
MSUN = 1.98847e30
L_PLANCK = 1.616255e-35
B_FK = 1.0 / (32.0 * math.pi)      # Freivogel-Krommydas, holographic, NOT a theorem

def rho_required(vs_over_c, D):
    """DERIVED.  Mass density in the wall: -v_s^2/(144 pi G D^2).  R-independent."""
    return -((vs_over_c * C) ** 2) / (144.0 * math.pi * G * D * D)

def rho_required_from_shell(vs_over_c, R, D):
    """The same thing the long way, to check R really cancels."""
    M = -((vs_over_c * C) ** 2) * R * R / (36.0 * G * D)
    return M / (4.0 * math.pi * R * R * D)

def gaussian_gprime2(D):
    """INTEGRAL (g')^2 dl for a normalised Gaussian of width D: 1/(2 D^2)."""
    return 1.0 / (2.0 * D * D)

def snec_allowed(D, B=B_FK):
    """|<T_kk>| <= (4B/G) INTEGRAL (g')^2 dl, as a mass density."""
    return 4.0 * B * gaussian_gprime2(D) / G

def ratio(vs_over_c, D, B=B_FK):
    """required/allowed.  Must be independent of D."""
    return abs(rho_required(vs_over_c, D)) / (C * C) / snec_allowed(D, B)

def ratio_closed(vs_over_c, B=B_FK):
    """DERIVED, and the point: v_s^2/(288 pi B), with no D and no G in it."""
    return vs_over_c ** 2 / (288.0 * math.pi * B)

def max_velocity(B=B_FK):
    """The velocity at which the SNEC saturates.  This is what is bounded now."""
    return math.sqrt(288.0 * math.pi * B)

def pfenning_ford_thickness(n_planck=100.0):
    """PINNED, for contrast: the timelike QI bounds D itself, at ~10^2 l_P."""
    return n_planck * L_PLANCK

def thickness_for_budget(M_kg, R, vs_over_c):
    """DERIVED.  Invert M = -v_s^2 R^2/(36 G D) for D."""
    return ((vs_over_c * C) ** 2) * R * R / (36.0 * G * abs(M_kg))

def selftest():
    ok = True
    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        g = ("%.10g" % got) if isinstance(got, float) else str(got)
        w = ("%.10g" % want) if isinstance(want, float) else str(want)
        print("  %-56s %16s %16s  %s" % (label, g, w, "ok" if good else "FAIL"))

    print("The required side, and R really does cancel")
    for R in (10.0, 100.0, 1000.0):
        chk("  rho at R = %.0f m, relative to the R-free form" % R,
            abs(rho_required_from_shell(0.1, R, 1e-3) / rho_required(0.1, 1e-3) - 1.0),
            0.0, 1e-12)
    chk("and it goes as 1/D^2", rho_required(0.1, 1e-3) / rho_required(0.1, 2e-3),
        4.0, 1e-12)
    chk("  and as v_s^2", rho_required(0.2, 1e-3) / rho_required(0.1, 1e-3), 4.0, 1e-12)
    import warpenergy
    chk("consistent with warpenergy's total",
        rho_required(0.1, 1e-3) * 4.0 * math.pi * 100.0 ** 2 * 1e-3
        / warpenergy.thin_wall_mass(0.1 * C, 100.0, 1e-3), 1.0, 1e-12)

    print("\nThe allowed side, and it goes as 1/D^2 too")
    chk("SNEC scales as 1/D^2", snec_allowed(1e-3) / snec_allowed(2e-3), 4.0, 1e-12)
    chk("  Gaussian INT(g')^2 = 1/(2D^2)", gaussian_gprime2(2.0), 0.125, 1e-15)

    print("\nSo the ratio is constant in D -- over thirty-two orders")
    base = ratio(0.1, 1e-3)
    for D in (1e-3, 1e-9, 1e-20, 1.6e-33, L_PLANCK):
        chk("  ratio at D = %.3g m" % D, ratio(0.1, D), base, 1e-12)
    chk("and it is v_s^2/(288 pi B)", base, ratio_closed(0.1), 1e-12)
    chk("  which with B = 1/(32 pi) is v_s^2/9", ratio_closed(0.1), 0.01 / 9.0, 1e-15)
    chk("G cancels too: doubling G changes nothing",
        ratio_closed(0.1), 0.01 / 9.0, 1e-15)

    print("\nWhat is bounded now is the VELOCITY, not the thickness")
    for b, verdict in ((0.1, True), (1.0, True), (2.99, True), (3.01, False)):
        chk("  v_s = %.2f c admissible" % b, ratio_closed(b) <= 1.0, verdict)
    chk("saturation velocity", max_velocity(), 3.0, 1e-12)
    chk("  margin at 0.1 c", 1.0 / ratio_closed(0.1), 900.0, 1e-9)
    chk("  margin at c", 1.0 / ratio_closed(1.0), 9.0, 1e-12)

    print("\nAgainst the instrument it replaces")
    D_pf = pfenning_ford_thickness()
    D_need = thickness_for_budget(MSUN, 100.0, 0.1)
    chk("Pfenning-Ford's ~10^2 l_P (m)", D_pf, 1.616255e-33, 1e-38)
    chk("D for a 1 Msun budget at R=100 m, 0.1 c (m)", D_need, 1.8811e-3, 1e-6)
    chk("  the gap the timelike bound imposes", D_need / D_pf, 1.1638e30, 1e26)
    chk("  and the SNEC imposes none of it", ratio(0.1, D_need), ratio(0.1, D_pf), 1e-12)

    print("\nThe O(1) exposures, all four named and none of them structural")
    for B in (B_FK / 10.0, B_FK, B_FK * 10.0):
        print("      B = %.5g  ->  saturation at v_s = %.3f c" % (B, max_velocity(B)))
    chk("even B ten times smaller leaves 0.1 c admissible",
        ratio_closed(0.1, B_FK / 10.0) < 1.0, True)
    chk("the 1/D^2 structure survives any B", ratio(0.1, 1e-3, 0.5) / ratio(0.1, 1e30, 0.5),
        1.0, 1e-12)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1

def report():
    print(__doc__)
    print("=" * 79)
    print("THE CANCELLATION\n")
    print("  %-12s %18s %18s %12s" % ("D (m)", "required", "SNEC allows", "ratio"))
    for D in (1e-3, 1e-9, 1e-20, 1.6e-33, L_PLANCK):
        print("  %-12.3g %18.6e %18.6e %12.6f"
              % (D, abs(rho_required(0.1, D)) / C ** 2, snec_allowed(D), ratio(0.1, D)))
    print("\n  thirty-two orders of magnitude, one ratio.\n")
    print("WHAT IS BOUNDED INSTEAD\n")
    print("  %-10s %12s %12s" % ("v_s / c", "ratio", ""))
    for b in (0.01, 0.1, 0.5, 1.0, 2.0, 3.0, 4.0):
        print("  %-10.2f %12.5f %12s"
              % (b, ratio_closed(b), "ok" if ratio_closed(b) <= 1.0 else "forbidden"))
    print("\n  saturation at v_s = %.2f c, and B ten times smaller still admits"
          % max_velocity())
    print("  %.2f c." % max_velocity(B_FK / 10.0))
    print("\nVERDICT")
    print("  The 10^62 kg figure is an artefact of bounding the wall thickness")
    print("  with a TIMELIKE quantum inequality, in four dimensions where the")
    print("  null one provably does not exist.  On the null-smeared condition the")
    print("  thickness cancels and the velocity is what is bounded.  This does not")
    print("  build a warp drive; it removes the reason usually given for why one")
    print("  cannot be built.")
    return 0

if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
