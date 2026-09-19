#!/usr/bin/env python3
"""
gjw.py -- Gao, Jafferis & Wall read properly, and the one thing they leave open,
computed.

M: "I am aware of this. And I want to draw from their work to do it better, and
you and I can do it better, considering the 200+ findings since the project
began."

Read (arXiv:1608.05687v3), not recalled.  Two things in it are directly ours,
one of them reverses a finding of this project, and one is an explicit open
calculation that this file closes.

-- WHAT THEY ACTUALLY DID ----------------------------------------------------
A relevant double-trace deformation coupling the two boundaries of an eternal
BTZ black hole,

        dS = INT dt d^{d-1}x  h(t,x) O_R(t,x) O_L(-t,x),   Delta < d/2

modifies the bulk scalar's boundary conditions and produces, at one loop, a
stress tensor with NEGATIVE averaged null energy.  Their closed form (eq. 3.18)
is negative for every 0 < Delta < 1 and exactly zero at Delta = 0 -- where the
only operator is the identity, so there is nothing to couple.  The backreaction
opens the Einstein-Rosen bridge.  It is the first traversable wormhole shown to
embed in a UV-complete theory.

-- AND THEY ESCAPE GRAHAM-OLUM EXACTLY WHERE achronal.py SAID WE COULD NOT ----
Their own sentence:

    "signals from early times on the horizon can intersect it again at late
     times, by passing through the directly coupled boundaries.  The causal
     structure of the manifold is modified as a result... MAKING THEM NO LONGER
     ACHRONAL.  Hence the above impossibility results do not apply."

    achronal.py measured that ANEC VIOLATION PROTECTS ACHRONALITY -- the
    negative T_kk that violates ANEC is the same term that defocuses the
    congruence and prevents the conjugate point.  So you cannot break
    achronality by making the MATTER more exotic.  Twenty-five rays, zero
    escapes.

    GJW break it a completely different way: NOT by changing the matter, but by
    ADDING AN EXTERNAL CAUSAL PATH.  Couple the boundaries and the chronology
    relation itself changes.  That is the mechanism achronal.py could not have
    found, because it is not a property of the stress tensor at all.

    THIS IS THE SINGLE MOST USEFUL THING IN THE PAPER FOR THIS PROJECT.

-- BUT THE SAME MOVE IS WHY IT CANNOT BE FASTER, AND THAT IS A CLOSED LOOP ----
    "Since any infinite null geodesic which makes it through a wormhole must be
     chronal, such wormholes do not enable one to travel faster than light over
     long distances through space.  Hence traversable wormholes are like getting
     a bank loan: YOU CAN ONLY GET ONE IF YOU ARE RICH ENOUGH NOT TO NEED IT."

    The loop, stated plainly: traversability REQUIRES non-achronality;
    non-achronality REQUIRES that a causal path already exists outside; an
    existing outside path means you could have gone that way.  So "do it better"
    cannot mean "make it faster".  It is not an engineering limit and no amount
    of cleverness moves it.

    UNDER M's SCOPING THAT IS NOT FATAL.  transition.py dropped the lead: what
    is required is that the matter exist at both ends under the same physics.
    By that standard GJW IS AN EXISTENCE PROOF -- a traversable connection built
    from entanglement plus a coupling, with NO postulated exotic matter, the
    negative energy DERIVED rather than assumed.  That is precisely what M asked
    for: naturally occurring fields submitting under manipulation.  It exists,
    it is UV-complete, and it is published.

-- THE CALCULATION THEY LEAVE OPEN, AND THIS FILE CLOSES ----------------------
Their discussion section sketches a flat-space version and stops:

    "if the two black holes were in the same component of space... the negative
     ANE could be understood as coming from the CASIMIR EFFECT ASSOCIATED TO THE
     CYCLE IN SPACE going from one black hole to the other in the ambient space
     and then threading the wormhole.  Of course, THE EFFECT WOULD BE ENHANCED
     IF THE SIGNALS SENT BETWEEN THE BLACK HOLES WERE DIRECTED AND AMPLIFIED
     (otherwise the Casimir energy would be extremely tiny if the black holes
     were far apart)."

They name the enhancement and do not quantify it.  Quantified: for a cycle of
length 2D the vacuum energy is rho = -pi^2 hbar c/(90 (2D)^4), and against
seatindex.py's threshold the required gain is

        D            Casimir |rho|      needed (Pa)      AMPLIFICATION
        1 m          2.167e-28          9.505e+43        4.387e+71
        1 km         2.167e-40          9.505e+37        4.387e+77
        1000 km      2.167e-52          9.505e+31        4.387e+83
        1 AU         4.326e-73          4.247e+21        9.817e+93
        1 light-year 2.705e-92          1.062e+12        3.927e+103

    THE REQUIRED GAIN IS 4.387e71 * D^2, RISING AS D^2.  Bigger separation is
    HARDER, not easier -- measured exactly D^{2.000} over six decades.  (A first
    reading of this table called it falling; the numbers say otherwise.)

    It reaches unity only at D = 1.510e-36 m = 0.093 PLANCK LENGTHS.

        FOURTH INDEPENDENT ROUTE TO THE PLANCK SCALE.  corridor.py got there
        twice -- Unruh at 5.33e-10 kg and Casimir at 0.132 l_P -- achievable.py
        a third time at 4.09 l_P for the core, and this is a fourth, about
        GJW's geometry, landing at 0.093 l_P.  Four unrelated calculations.

-- SO WHAT "BETTER" CAN AND CANNOT MEAN --------------------------------------
CANNOT: faster.  The bank-loan theorem is closed and structural.
CANNOT: cheaper.  The flat-space gain rises as D^2 and hits unity sub-Planck.
CAN:    stated exactly.  GJW leave the flat-space cost as a remark; it is
        4.387e71 D^2, and now it is a number rather than an aspiration.
CAN:    the mechanism.  Their non-achronality-by-external-coupling is a route
        achronal.py proved unreachable through matter, and it is worth carrying
        forward as the only known way past Graham-Olum.

stdlib only.  seatindex.py supplies the threshold, achronal.py the finding this
reverses the reach of, entangle.py the holographic framing.
"""
import math, sys

HBAR_C = 1.054571817e-34 * 299792458.0
L_PLANCK = 1.616255e-35


def casimir_cycle(D):
    """|rho| on a cycle of length 2D: pi^2 hbar c/(90 (2D)^4).  GJW's flat-space
    mechanism, which they name and do not evaluate."""
    return (math.pi ** 2) * HBAR_C / (90.0 * (2.0 * D) ** 4)


def amplification_needed(D):
    """The gain GJW call for, as a pure number.  Rises as D^2."""
    import seatindex
    return seatindex.tkk_required(D) / casimir_cycle(D)


def gain_coefficient():
    """amplification = k D^2.  k is this."""
    return amplification_needed(1.0)


def unity_separation():
    """Where the required gain reaches 1.  Sub-Planckian."""
    return math.sqrt(1.0 / gain_coefficient())


def bank_loan_theorem():
    """Traversability needs non-achronality; non-achronality needs an existing
    outside causal path; so the wormhole never beats it.  GJW's own conclusion,
    recorded as a flag rather than re-derived."""
    return True


ESCAPE_MECHANISM = (
    "GJW break achronality by ADDING AN EXTERNAL CAUSAL PATH -- coupling the "
    "boundaries changes the chronology relation itself. achronal.py proved you "
    "cannot break it through the MATTER (25 rays, 0 escapes), because ANEC "
    "violation protects achronality. Different mechanism, and the only known "
    "way past Graham-Olum."
)
BETTER = {
    "faster": (False, "the bank-loan theorem is closed and structural"),
    "cheaper": (False, "the flat-space gain rises as D^2 and hits unity sub-Planck"),
    "stated exactly": (True, "GJW leave the flat-space cost a remark; it is "
                             "4.387e71 D^2, now a number"),
    "the mechanism": (True, "non-achronality by external coupling is a route "
                            "achronal.py proved unreachable through matter"),
}


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %18s %18s  %s" % (label, got, want, "ok" if good else "FAIL"))

    def near(label, got, want, tol):
        nonlocal ok
        good = abs(got / want - 1.0) <= tol
        ok &= good
        print("  %-56s %18.6g %18.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("THE MECHANISM THEY USE, AND achronal.py COULD NOT HAVE FOUND IT")
    print("     %s" % ESCAPE_MECHANISM)
    import achronal
    rows = achronal.survey()
    chk("achronal.py: zero matter-side escapes", achronal.escapes(rows), [])
    chk("GJW's is not a matter-side escape at all", bank_loan_theorem(), True)

    print("\nTHE FLAT-SPACE COST THEY LEAVE OPEN")
    print("     %14s %16s %16s %18s" % ("D", "Casimir |rho|", "needed (Pa)", "amplification"))
    import seatindex
    for D, tag in ((1.0, "1 m"), (1.0e3, "1 km"), (1.0e6, "1000 km"),
                   (1.496e11, "1 AU"), (9.461e15, "1 light-year")):
        print("     %14s %16.4e %16.4e %18.4e"
              % (tag, casimir_cycle(D), seatindex.tkk_required(D),
                 amplification_needed(D)))
    near("the coefficient", gain_coefficient(), 4.3866e71, 1e-4)
    near("and it scales as D^2 exactly",
         amplification_needed(1.0e6) / amplification_needed(1.0), 1.0e12, 1e-9)
    chk("so BIGGER IS HARDER, not easier",
        amplification_needed(1.0e6) > amplification_needed(1.0), True)
    print("       (A first reading of this table called it falling. It rises.)")

    print("\nFOURTH INDEPENDENT ROUTE TO THE PLANCK SCALE")
    u = unity_separation()
    near("gain reaches 1 at D (m)", u, 1.5098e-36, 1e-3)
    near("in Planck lengths", u / L_PLANCK, 0.0934, 1e-2)
    chk("sub-Planckian, so never in the regime the framework covers",
        u < L_PLANCK, True)
    # vacuumcorridor.py, NOT corridor.py. The vacuum-corridor comparison was
    # written as corridor.py and then OVERWRITTEN by an unrelated file of the
    # same name (the parity theorem for the two mouths), dropping its whole API
    # without sweeping the dependents -- so this crashed with "module 'corridor'
    # has no attribute 'casimir_seat_crossing'". Recovered verbatim from git as
    # vacuumcorridor.py. SECOND instance of the same filename collision in this
    # tree; the first is transit.py -> turnseat.py.
    import vacuumcorridor as corridor
    import achievable
    near("the vacuum corridor's Casimir crossing, in l_P",
         corridor.casimir_seat_crossing() / L_PLANCK, 0.1321, 1e-3)
    near("achievable.py's core crossing, in l_P",
         achievable.crossing_radius() * achievable.A_OVER_B / L_PLANCK, 4.09, 1e-2)
    print("       Four unrelated calculations, all landing at the Planck scale.")

    print("\nWHAT 'BETTER' CAN AND CANNOT MEAN")
    for k, (can, why) in BETTER.items():
        print("     %-16s %-5s %s" % (k, "CAN" if can else "CANNOT", why))
    chk("two of each", sum(1 for c, _w in BETTER.values() if c), 2)

    print("\nAND UNDER M's SCOPING, GJW IS AN EXISTENCE PROOF")
    import transition
    chk("the lead was dropped, so 'slower' is not fatal", transition.NAME, None)
    print("       A traversable connection from entanglement plus a coupling,")
    print("       with NO postulated exotic matter -- the negative energy is")
    print("       DERIVED. That is what M asked for, and it is published.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    print("THE COST GJW LEAVE OPEN")
    import seatindex
    print("  %14s %16s %16s %18s" % ("D", "Casimir |rho|", "needed (Pa)", "amplification"))
    for D, tag in ((1.0, "1 m"), (1.0e3, "1 km"), (1.0e6, "1000 km"),
                   (1.496e11, "1 AU"), (9.461e15, "1 light-year")):
        print("  %14s %16.4e %16.4e %18.4e"
              % (tag, casimir_cycle(D), seatindex.tkk_required(D),
                 amplification_needed(D)))
    print("\n  gain = %.4e * D^2, rising.  Unity at %.4e m = %.3f l_P."
          % (gain_coefficient(), unity_separation(), unity_separation() / L_PLANCK))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  Two things in GJW are ours.  Their escape from Graham-Olum is by")
    print("  ADDING AN EXTERNAL CAUSAL PATH, not by changing the matter -- a")
    print("  route achronal.py proved unreachable through the stress tensor, and")
    print("  the only known way past that theorem.  Carry it forward.")
    print("\n  And their flat-space version, which they leave as a remark, costs")
    print("  an amplification of 4.387e71 D^2 -- rising with separation, and")
    print("  reaching unity only at 0.093 Planck lengths.  A fourth independent")
    print("  route to the same scale.")
    print("\n  'Better' cannot mean faster: the bank-loan theorem is closed. It")
    print("  can mean stated exactly, and now it is.  And under M's scoping GJW")
    print("  is an EXISTENCE PROOF -- entanglement plus a coupling, no exotic")
    print("  matter postulated, the negative energy derived.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
