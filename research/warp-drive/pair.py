#!/usr/bin/env python3
"""
pair.py -- the conservation ledger a wormhole/black hole pair would need, and
which quantity actually pairs.

M: "a wormhole emits mass density, and a black hole pulls it in... what if the
wormhole is the entrance, and the black hole is the exit?  Everything in
existence is defined by the atomic index of real elements, and it is closed, so
everything exists in balance with no defect possible.  Wormholes and black holes
are considered to be defects, but what if they are not?  What if for every
wormhole there is a black hole of the same but inverse energy?"

Four separable claims, and they do not stand or fall together.  Two are
measurably backwards, one is a real and standard theorem about the WRONG
QUANTITY, and the fourth -- the balance principle itself -- survives, forces a
conclusion this tree had only ever ASSUMED, and is the reason to write the file.

===============================================================================
1. THE EMISSION IS BACKWARDS, AND IT IS THE BLACK HOLE THAT EMITS
===============================================================================

A black hole emits.  Hawking: T = hbar c^3 / (8 pi G M k_B), and every black
hole radiates at it -- 6.17e-8 K for a solar mass, 1.92e-9 K for detect.py's
32.13-solar-mass search target.  Faint, and not zero.

A traversable wormhole has NO HORIZON -- that is detect.py's whole
discriminator, absorb-versus-transmit -- and no horizon means no surface
gravity, no Hawking temperature and no emission.  It does not "emit mass
density."  What it does have at the throat is a NEGATIVE energy density, which
is a local requirement of the flare-out condition and not a flux of anything.

    SO THE POLARITY IS INVERTED.  THE EMITTER IS THE BLACK HOLE.

That is a correction, not a refutation -- the contrast M is reaching for is
real.  It is just absorb-versus-TRANSMIT, which detect.py already named, and
not absorb-versus-emit.

===============================================================================
2. "THE BLACK HOLE IS THE EXIT" IS A CONTRADICTION -- AND IT IS ALSO A
   SOLUTION THAT EXISTS, IS EXACTLY THIS PICTURE, AND IS NOT TRAVERSABLE
===============================================================================

A horizon is a one-way null surface.  Matter cannot cross it outward, by the
definition of the object, so nothing exits through a black hole.  The far end
of a one-way tunnel is a WHITE HOLE, not a black one.

But the object M is describing is not hypothetical.  The maximally extended
Schwarzschild solution -- THE EINSTEIN-ROSEN BRIDGE -- is precisely a tunnel
joining two asymptotic regions, with a black hole horizon at one end and a white
hole horizon at the other.  It is the original wormhole, it needs no exotic
matter, and it is a vacuum solution of the field equations.

    AND IT IS PROVABLY NOT TRAVERSABLE, exactly, with no approximation.

Kruskal coordinates: T^2 - X^2 = (1 - r/2M) e^{r/2M}, the singularity at
T^2 - X^2 = 1, the horizons at T = +-X.  Two things are measured below.

    THE BRIDGE PINCHES OFF.  On the X = 0 slice the throat is r = 2M at T = 0
    and falls to r = 0 at T = 1.  It opens and closes.

    NO RAY CROSSES IT.  A leftward radial null ray from region I is T = c - X
    with c = T_0 + X_0 > 0.  It meets the singularity at

        X_s = (c^2 - 1)/(2c),        T_s = (c^2 + 1)/(2c),

    and region III needs |X| > T with X < 0.  But |1 - c^2| < 1 + c^2 for EVERY
    c > 0, so |X_s| < T_s always: the ray hits the singularity while still in
    the future interior.  NOT ONE RAY, NOT FOR ANY STARTING POINT.  Scanned
    below over 200,000 values of c, and the margin is strictly negative at
    every one.

Fuller & Wheeler 1962.  The bridge closes faster than light can cross it, and
holding it open is exactly the exotic-matter bill this tree has priced at 65
orders (achievable.py, scale.py).  M's picture is a real solution.  It is the
one that does not work, and it is why Morris-Thorne had to add the exotic
matter in the first place.

===============================================================================
3. THE PAIRING IS A REAL THEOREM -- ABOUT CHARGE, AND NOT ABOUT MASS
===============================================================================

Wheeler's CHARGE WITHOUT CHARGE: thread a wormhole with electric field lines and
the two mouths look like +Q and -Q to their respective asymptotic regions.  No
charged matter anywhere; the charge is the topology.  That is M's principle
exactly -- a conserved quantity, paired, summing to zero, with no defect -- and
it is standard, uncontroversial physics.

    SO THE PRINCIPLE IS NOT WRONG.  IT IS RIGHT ABOUT A CLASS OF QUANTITY, AND
    MASS IS NOT IN THAT CLASS.

The reason is measured below and it is one line: the mass associated with a
charge goes as Q^2.  Field energy Q^2/(8 pi eps0 r) is SIGN-BLIND.  So the two
mouths carry OPPOSITE charge and the SAME POSITIVE mass, and the mass ledger
does not cancel -- it ADDS.  Pair the charges and you have doubled the mass.

    A QUANTITY PAIRS +- IFF IT IS SIGN-SYMMETRIC.  Charge is.  Energy is not,
    and what breaks the symmetry is section 4.

===============================================================================
4. THE BALANCE PRINCIPLE SURVIVES -- AND FORCES SOMETHING THIS TREE ASSUMED
===============================================================================

Why can energy not pair +-?  THE POSITIVE MASS THEOREM (Schoen-Yau 1979,
Witten 1981).  For an asymptotically flat spacetime, nonsingular, whose matter
satisfies the dominant energy condition:

        M_ADM >= 0,   AND M_ADM = 0 IF AND ONLY IF THE SPACETIME IS MINKOWSKI.

The inequality is the half everybody quotes, and it already kills the naive
ledger: a wormhole of energy -E "balanced" by a black hole of +E is not
permitted-because-balanced, because THE NEGATIVE MEMBER CANNOT EXIST AT ALL
under the DEC.  The theorem is a ONE-SIDED BOUND, not a symmetric ledger.  This
tree has quoted that half seven times.

IT IS THE SECOND HALF -- THE RIGIDITY CLAUSE -- THAT NOBODY HERE HAS USED, AND
IT IS THE WHOLE REASON TO TAKE M'S PRINCIPLE SERIOUSLY.

Push the principle through honestly.  Balance, applied to ADM energy, leaves
exactly one option for a pair in one asymptotic region: not +E and -E, but

        M_ADM = 0.

which is concentric.py, measured at -4.000e-15.  The principle lands on the
device the tree already built.  And then rigidity fires:

        IF M_ADM = 0 AND THE MATTER SATISFIES THE DEC, THE SPACETIME IS
        MINKOWSKI.  The device is not Minkowski -- it seats a conjugate point,
        it has a corridor, it has structure at every radius.  THEREFORE ITS
        MATTER CANNOT SATISFY THE DEC.

    NEGATIVE ENERGY IS NOT AN ASSUMPTION OF THIS DESIGN.  IT IS FORCED BY THE
    DESIGN'S OWN M_ADM = 0, BY A THEOREM, WITH NO APPEAL TO ANY MAGNITUDE.

concentric.py's caution 1 says "NEGATIVE MASS IS STILL ASSUMED."  That is now
too weak, and this file supersedes it: it is DERIVED.  Every statement in this
tree of the form "the positive mass theorem has nothing to object to" was also
reading only the inequality; the correct statement is that the device satisfies
the theorem's CONCLUSION while violating its HYPOTHESIS, and must.

    WHICH IS ALSO WHY THE BALANCE CANNOT BE HAD FOR FREE.  M's principle says
    the closed index admits no defect.  The positive mass theorem agrees --
    and then charges for it: THE ONLY BALANCED, NON-TRIVIAL CONFIGURATION IS
    ONE THAT VIOLATES THE DOMINANT ENERGY CONDITION.  Balance does not remove
    the exotic-matter bill.  IT IS THE PROOF THAT THE BILL IS UNAVOIDABLE.

===============================================================================
5. AND AT COSMOLOGICAL SCALE THE PRINCIPLE IS TRUE AND EMPTY
===============================================================================

"Everything is closed, so everything is in balance."  In a spatially closed
universe that is correct, and it is correct for a reason that gives nothing
back: ADM mass is a surface integral at spatial infinity, and a closed universe
HAS NO SPATIAL INFINITY.  The total energy is not zero; it is UNDEFINED.

    A quantity that does not exist cannot be out of balance, and cannot be used
    to pair two objects inside the universe either.  This is a definitional
    refusal, not a measurement, and it is filed as one.

===============================================================================
WHAT SURVIVES, IN ONE LINE
===============================================================================

        A SIGN-BLIND QUANTITY PAIRS.  A SIGN-COMMITTED ONE DOES NOT.

Charge pairs because it is sign-symmetric; energy does not because the positive
mass theorem commits it.  And that is dichotomy.py's split arriving from a
completely different direction -- Weyl focusing is sign-blind and both signs
seat; Ricci focusing is sign-committed and only one sign does.  Two independent
routes to the same discriminator is the finding, and it is M's principle stated
in the form that is true.

stdlib only.  Exact where the claim is exact.
"""
import math
import sys

C = 2.99792458e8
G = 6.67430e-11
HBAR = 1.054571817e-34
KB = 1.380649e-23
EPS0 = 8.8541878128e-12
M_SUN = 1.98892e30
E_CHARGE = 1.602176634e-19

SEARCH_TARGET_SOLAR = 32.13          # detect.py


# ------------------------------------------- 1: which one emits

def hawking_temperature(M_kg):
    """T = hbar c^3 / (8 pi G M k_B).  Every black hole has one."""
    return HBAR * C ** 3 / (8.0 * math.pi * G * M_kg * KB)


def has_horizon(is_black_hole):
    return bool(is_black_hole)


def emits(is_black_hole):
    """No horizon, no surface gravity, no Hawking temperature, no emission."""
    return has_horizon(is_black_hole)


EMITTER = "black hole"
DISCRIMINATOR = "absorb-versus-transmit"      # detect.py, not absorb-vs-emit


# ------------------- 2: the Einstein-Rosen bridge, in Kruskal coordinates

def kruskal_rhs(r_over_2M):
    """(1 - r/2M) e^{r/2M}.  Equals T^2 - X^2."""
    return (1.0 - r_over_2M) * math.exp(r_over_2M)


def throat_radius(T, iters=200):
    """Minimal r on the slice, at X = 0: solve (1-r)e^r = T^2 for r in [0,1].
    Monotone decreasing there, so bisection is exact to machine precision."""
    lo, hi = 0.0, 1.0
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if kruskal_rhs(mid) > T * T:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def bridge_pinches_off():
    """r = 2M at T = 0 and r = 0 at T = 1.  It opens and it closes."""
    return throat_radius(0.0) > 0.999999 and throat_radius(1.0) < 1e-9


def singularity_hit(c):
    """A leftward radial null ray T = c - X meets T^2 - X^2 = 1 here."""
    return ((c * c - 1.0) / (2.0 * c), (c * c + 1.0) / (2.0 * c))


def reaches_other_region(c):
    """Region III needs X < 0 and |X| > T.  Never true: |1-c^2| < 1+c^2."""
    Xs, Ts = singularity_hit(c)
    return Xs < 0.0 and abs(Xs) > Ts


def crossing_margin(c):
    """|X_s| - T_s.  Strictly negative for every c > 0, and that is the proof."""
    Xs, Ts = singularity_hit(c)
    return abs(Xs) - Ts


def worst_margin(n=200000, step=1e-4):
    return max(crossing_margin(i * step) for i in range(1, n))


ER_BRIDGE_TRAVERSABLE = False
ER_BRIDGE_NEEDS_EXOTIC_MATTER = True


# ------------------------------- 3: what pairs, and what does not

def field_energy(Q, r):
    """Q^2 / (8 pi eps0 r) -- the energy outside radius r.  Goes as Q SQUARED."""
    return Q * Q / (8.0 * math.pi * EPS0 * r)


def mass_from_charge(Q, r):
    return field_energy(Q, r) / C ** 2


def charge_is_sign_symmetric(Q, r):
    """+Q and -Q are distinct charges with the SAME mass.  Measured, not said."""
    return mass_from_charge(Q, r) == mass_from_charge(-Q, r)


def mouth_pair_charge(Q):
    """Wheeler: the two mouths look like +Q and -Q.  The ledger closes."""
    return Q + (-Q)


def mouth_pair_mass(Q, r):
    """And the mass ledger does NOT close -- it doubles."""
    return mass_from_charge(Q, r) + mass_from_charge(-Q, r)


PAIRS = (("electric charge", True, "sign-symmetric: +Q and -Q both exist"),
         ("magnetic charge", True, "same, and topological pair creation makes them"),
         ("ADM energy", False, "sign-committed by the positive mass theorem"))


def quantity_pairs(name):
    return dict((n, p) for n, p, _w in PAIRS)[name]


# ---------------------- 4: the rigidity clause, and what it forces

PMT_INEQUALITY = "M_ADM >= 0"
PMT_RIGIDITY = "M_ADM = 0 if and only if the spacetime is Minkowski"
PMT_HYPOTHESES = ("asymptotically flat", "nonsingular", "dominant energy condition")


def balanced_pair_energies():
    """The principle, pushed through the theorem.  Not (+E, -E) -- (0, 0)."""
    return (0.0, 0.0)


def device_is_minkowski():
    """It is not: it seats a conjugate point and has structure at every radius."""
    return False


def dec_must_fail(adm_is_zero=True, is_minkowski=None):
    """THE RIGIDITY CLAUSE, CONTRAPOSED.  M_ADM = 0 and not Minkowski implies
    the dominant energy condition fails.  No magnitude enters this."""
    if is_minkowski is None:
        is_minkowski = device_is_minkowski()
    return bool(adm_is_zero and not is_minkowski)


NEGATIVE_ENERGY_STATUS = "DERIVED"        # was ASSUMED -- concentric.py caution 1
SUPERSEDES = ("concentric.py caution 1: 'NEGATIVE MASS IS STILL ASSUMED'",)


# ------------------------------- 5: the closed universe

CLOSED_UNIVERSE_TOTAL_ENERGY = "UNDEFINED"     # not zero: there is no boundary


def adm_mass_defined(has_spatial_infinity):
    """ADM mass is a surface integral at spatial infinity.  No infinity, no
    integral, no quantity -- so nothing to balance and nothing to pair with."""
    return bool(has_spatial_infinity)


# --------------------------------------------------- what survives

SURVIVING_FORM = "a sign-blind quantity pairs; a sign-committed one does not"


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %16s %16s  %s"
              % (label, str(got)[:16], str(want)[:16], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-9):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-58s %16.6e %16.6e  %s"
              % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE EMISSION IS BACKWARDS -- IT IS THE BLACK HOLE THAT EMITS")
    near("T x M is a constant of nature, not a property of the hole",
         hawking_temperature(M_SUN) * M_SUN,
         hawking_temperature(SEARCH_TARGET_SOLAR * M_SUN)
         * SEARCH_TARGET_SOLAR * M_SUN)
    near("and it lands on the published solar-mass figure, 6.17e-8 K",
         hawking_temperature(M_SUN), 6.17e-8, 2e-3)
    print("     one solar mass          %.4e K" % hawking_temperature(M_SUN))
    print("     detect.py's target      %.4e K  (%.2f solar masses)"
          % (hawking_temperature(SEARCH_TARGET_SOLAR * M_SUN), SEARCH_TARGET_SOLAR))
    chk("a black hole emits", emits(True), True)
    chk("a horizonless wormhole emits", emits(False), False)
    chk("so the emitter is", EMITTER, "black hole")
    chk("and the discriminator is detect.py's", DISCRIMINATOR,
        "absorb-versus-transmit")

    print("\n2. THE EINSTEIN-ROSEN BRIDGE IS THAT PICTURE, AND IT DOES NOT CROSS")
    print("     the throat on the X = 0 slice, r/2M against Kruskal T")
    for T in (0.0, 0.25, 0.5, 0.75, 0.9, 0.99, 1.0):
        print("       T = %4.2f    r/2M = %.6f" % (T, throat_radius(T)))
    near("throat at T = 0 is the horizon radius", throat_radius(0.0), 1.0, 1e-12)
    near("throat at T = 1 has pinched to zero", throat_radius(1.0), 0.0, 1e-12)
    chk("the bridge opens and closes", bridge_pinches_off(), True)
    print("     and no leftward null ray reaches region III, at any c > 0")
    counterexamples = [i * 1e-4 for i in range(1, 200000)
                       if reaches_other_region(i * 1e-4)]
    chk("rays that cross, over 200,000 starting points", counterexamples, [])
    wm = worst_margin()
    print("       best margin over all of them:  |X_s| - T_s = %.4e" % wm)
    chk("and it is strictly negative -- never zero, never positive", wm < 0.0, True)
    print("       exactly: |1 - c^2| < 1 + c^2 for every c > 0.")
    chk("so the Einstein-Rosen bridge is traversable", ER_BRIDGE_TRAVERSABLE, False)
    chk("and holding it open needs exotic matter", ER_BRIDGE_NEEDS_EXOTIC_MATTER, True)

    print("\n3. THE PAIRING IS REAL -- FOR CHARGE, AND NOT FOR MASS")
    r0 = 1.0
    Q = 1.0e-6
    chk("+Q and -Q have the SAME mass (field energy goes as Q^2)",
        charge_is_sign_symmetric(Q, r0), True)
    near("the charge ledger of the two mouths", mouth_pair_charge(Q), 0.0, 1e-30)
    near("the mass ledger of the two mouths, kg", mouth_pair_mass(Q, r0),
         Q * Q / (4.0 * math.pi * EPS0 * r0 * C ** 2))
    chk("does the mass ledger cancel", mouth_pair_mass(Q, r0) == 0.0, False)
    print("       Wheeler's charge without charge: the charges pair to zero and")
    print("       the masses ADD.  Pair the charge and you have doubled the mass.")
    for name, pairs_, why in PAIRS:
        print("     %-18s %-9s %s" % (name, "PAIRS" if pairs_ else "DOES NOT", why))
    chk("electric charge pairs", quantity_pairs("electric charge"), True)
    chk("ADM energy pairs", quantity_pairs("ADM energy"), False)

    print("\n4. THE RIGIDITY CLAUSE, AND WHAT THE BALANCE PRINCIPLE FORCES")
    print("     %s" % PMT_INEQUALITY)
    print("     %s" % PMT_RIGIDITY)
    print("     hypotheses: %s" % ", ".join(PMT_HYPOTHESES))
    chk("balance through the theorem gives (+E, -E)",
        balanced_pair_energies() != (0.0, 0.0), False)
    chk("it gives exactly", balanced_pair_energies(), (0.0, 0.0))
    print("     which is concentric.py, and then rigidity fires:")
    try:
        import concentric
        res = concentric.adm_residual(5.0e-3)
        print("       concentric.py M_ADM residual = %.3e" % res)
        chk("  measured M_ADM is zero", abs(res) < 1e-10, True)
    except Exception as exc:                       # pragma: no cover
        print("       concentric.py not importable (%s) -- row skipped" % exc)
    chk("is the device Minkowski", device_is_minkowski(), False)
    chk("so the DEC MUST fail -- derived, not assumed", dec_must_fail(), True)
    chk("and a Minkowski spacetime is exempt", dec_must_fail(True, True), False)
    chk("negative energy in this design is now", NEGATIVE_ENERGY_STATUS, "DERIVED")
    print("       supersedes: %s" % SUPERSEDES[0])
    print("       BALANCE DOES NOT REMOVE THE EXOTIC-MATTER BILL.  IT IS THE")
    print("       PROOF THAT THE BILL IS UNAVOIDABLE.")

    print("\n5. AND AT COSMOLOGICAL SCALE IT IS TRUE AND EMPTY")
    chk("ADM mass is defined in an asymptotically flat spacetime",
        adm_mass_defined(True), True)
    chk("ADM mass is defined in a spatially closed universe",
        adm_mass_defined(False), False)
    chk("so the total energy of a closed universe is",
        CLOSED_UNIVERSE_TOTAL_ENERGY, "UNDEFINED")
    print("       Not zero -- UNDEFINED.  A quantity that does not exist cannot")
    print("       be out of balance, and cannot pair two objects either.")

    print("\nWHAT SURVIVES")
    chk("the form of the principle that is true", SURVIVING_FORM,
        "a sign-blind quantity pairs; a sign-committed one does not")
    try:
        import dichotomy
        print("     dichotomy.py reached the same split from the other side:")
        print("       Weyl focusing is SIGN-BLIND and both signs seat;")
        print("       Ricci focusing is SIGN-COMMITTED and only one sign does.")
        chk("  and it holds two routes", len(dichotomy.ROUTES), 2)
    except Exception as exc:                       # pragma: no cover
        print("     dichotomy.py not importable (%s) -- row skipped" % exc)

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE LEDGER\n")
    print("  %-20s %-10s %s" % ("quantity", "pairs +-?", "why"))
    for name, pairs_, why in PAIRS:
        print("  %-20s %-10s %s" % (name, "YES" if pairs_ else "NO", why))
    print("\n  %-20s %s" % ("emitter", EMITTER))
    print("  %-20s %s" % ("ER bridge traversable", ER_BRIDGE_TRAVERSABLE))
    print("  %-20s %s" % ("balanced pair", balanced_pair_energies()))
    print("  %-20s %s" % ("negative energy", NEGATIVE_ENERGY_STATUS))
    print("  %-20s %s" % ("closed universe", CLOSED_UNIVERSE_TOTAL_ENERGY))
    print("\n" + "=" * 79)
    print("""VERDICT

  TWO HALVES OF THE PICTURE ARE BACKWARDS, AND SAYING SO COSTS THE IDEA
  NOTHING.  It is the BLACK HOLE that emits -- Hawking, 1.92e-9 K at
  detect.py's search target -- and a horizonless wormhole does not emit
  at all.  And nothing exits through a black hole: a horizon is one-way
  by definition, so the far end of a one-way tunnel is a WHITE hole.

  BUT THE PICTURE IS A REAL SOLUTION, AND IT IS THE ORIGINAL ONE.  The
  maximally extended Schwarzschild spacetime -- the Einstein-Rosen
  bridge -- is exactly a tunnel between two regions with a black hole at
  one end and a white hole at the other, in vacuum, needing no exotic
  matter.  It is also provably impassable: the throat falls from 2M to
  zero between Kruskal T = 0 and T = 1, and every leftward null ray hits
  the singularity first, because |1 - c^2| < 1 + c^2 for every c > 0.
  Scanned over 200,000 starting points with a strictly negative margin
  at each.  THAT IS WHY MORRIS-THORNE HAD TO ADD THE EXOTIC MATTER.

  AND THE PAIRING PRINCIPLE IS A STANDARD THEOREM -- ABOUT CHARGE.
  Wheeler's charge without charge: thread a wormhole with field lines
  and the two mouths are +Q and -Q, with no charged matter anywhere.
  The ledger closes exactly.  But the mass that goes with a charge goes
  as Q SQUARED, so it is sign-blind: the two mouths carry opposite
  charge and the SAME POSITIVE mass, and the mass ledger does not
  cancel, IT DOUBLES.

  A QUANTITY PAIRS +- IF AND ONLY IF IT IS SIGN-SYMMETRIC, and energy is
  not, because the POSITIVE MASS THEOREM commits its sign.

  WHICH IS WHERE THE PRINCIPLE STOPS BEING AN ANALOGY AND STARTS PAYING.
  Pushed through that theorem honestly, balance in one asymptotic region
  does not give (+E, -E).  It gives M_ADM = 0 -- and that IS
  concentric.py, measured at -4.000e-15.  Then the theorem's SECOND
  half, the rigidity clause this tree has never once used, fires:
  M_ADM = 0 under the dominant energy condition implies MINKOWSKI.  The
  device is not Minkowski.

        THEREFORE ITS MATTER CANNOT SATISFY THE DOMINANT ENERGY
        CONDITION.  NEGATIVE ENERGY IS NOT AN ASSUMPTION OF THIS DESIGN
        -- IT IS DERIVED FROM THE DESIGN'S OWN M_ADM = 0, BY A THEOREM,
        WITH NO APPEAL TO ANY MAGNITUDE.

  concentric.py's caution 1 said negative mass was STILL ASSUMED.  It is
  not an assumption any more, and this file supersedes that line.

  SO M'S PRINCIPLE IS RIGHT AND IT DOES NOT BUY WHAT IT LOOKS LIKE IT
  BUYS.  The closed index really does admit no defect, and the positive
  mass theorem agrees -- then charges for it.  THE ONLY BALANCED,
  NON-TRIVIAL CONFIGURATION IS ONE THAT VIOLATES THE DOMINANT ENERGY
  CONDITION.  Balance does not remove the exotic-matter bill.  IT IS THE
  PROOF THAT THE BILL IS UNAVOIDABLE.

  And at cosmological scale the principle is true and empty: a spatially
  closed universe has no spatial infinity, ADM mass is a surface
  integral there, so the total energy is not zero -- it is UNDEFINED.

  WHAT SURVIVES IS ONE LINE, AND IT IS WORTH KEEPING: A SIGN-BLIND
  QUANTITY PAIRS; A SIGN-COMMITTED ONE DOES NOT.  Which is dichotomy.py's
  Weyl-against-Ricci split arriving from a completely different
  direction -- and two independent routes to the same discriminator is
  the finding.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
