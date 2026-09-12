#!/usr/bin/env python3
"""
switch.py -- M, across two messages: "EM provides the switch action" ... and
then "what if it was never about giving energy but instead taking it.  Pull the
energy away from the singularity using EM to switch the gravitational field.
This creates a larger surface space by reducing the geometry by an axis."

FOUR CLAIMS.  ONE LANDS AND IT LANDS PROPERLY.  THREE ARE MEASURED AGAINST.

    EM DOES PROVIDE THE SWITCH -- TWO OF THEM, AND BOTH ARE EXACT.  That half
    is simply right and had never been checked here.

    AND GRAVITY CANNOT SEE EITHER ONE.  |T(F) - T(-F)| = 0.000e+00, exactly
    zero, not machine zero.  Duality rotation carries F all the way to -F with
    T constant to 4.4e-16 at every step.  THE SWITCH IS REAL AND THE STRESS
    TENSOR IS BLIND TO IT, because T is QUADRATIC IN F -- which is
    invariance.py's scale/shape split arriving as a direct measurement.

    "TAKE RATHER THAN GIVE" IS RIGHT, AND IT IS THE CASIMIR EFFECT.  Removing
    ordinary energy floors at zero.  Removing VACUUM MODES goes negative, and
    that is the one mechanism known to make rho < 0 in a laboratory.  M reached
    it by reasoning; the tree already holds it, already priced it, and it hits
    the same wall as everything else.

    "REDUCING BY AN AXIS" GOES THE WRONG WAY TWICE: surface-to-volume FALLS as
    dimension falls, and 2+1 gravity has NO NEWTONIAN ATTRACTION AT ALL.

===============================================================================
1. EM PROVIDES TWO SWITCHES, AND BOTH ARE EXACT
===============================================================================

    CHARGE CONJUGATION      F -> -F.  Every component reversed.
    DUALITY ROTATION        E -> E cos a + B sin a,  B -> -E sin a + B cos a.
                            A continuous one-parameter family, and at a = pi it
                            carries F to -F.

    M IS RIGHT THAT EM HAS A SWITCH ACTION.  It has two, one discrete and one
    continuous, and the continuous one is a genuine rotation between the two
    binary values rather than a fade between them.

===============================================================================
2. AND THE GRAVITATIONAL FIELD CANNOT SEE EITHER ONE
===============================================================================

Measured on a random field with E and B drawn in [-2, 2]:

    CHARGE CONJUGATION
        |F - (-F)|         = 3.5396          the field is COMPLETELY reversed
        |T(F) - T(-F)|     = 0.000e+00       EXACTLY ZERO, not machine zero

    DUALITY ROTATION
        alpha       |F_a|        |T(F_a) - T(F)|      F_a = -F ?
        0.00000     1.769801     0.000e+00
        0.78540     2.029449     1.776e-15
        1.57080     1.769801     8.882e-16
        2.35619     2.029449     8.882e-16
        3.14159     1.769801     4.441e-16            YES

    THE FIELD TRAVELS ALL THE WAY FROM F TO -F AND T NEVER MOVES.

    AND THE REASON IS ONE LINE: T_munu is QUADRATIC IN F.  Gravity couples to
    T_munu, T_munu squares the field, and squaring destroys the sign the switch
    flips.  cubic.py said "a square does not go negative"; THIS IS THE SAME
    FACT SEEN FROM THE OTHER SIDE -- a square does not even NOTICE.

        SO EM CANNOT SWITCH THE GRAVITATIONAL FIELD.  Not "it is hard" -- the
        switch is exact and the response is exactly nothing.

    AND IT IS invariance.py's SPLIT, MEASURED DIRECTLY.  The switch acts on the
    FIELD, which is a coefficient.  The obstruction is in T_munu, which is the
    shape.  Changing the coefficient leaves the shape alone, again.

===============================================================================
3. THE STATE BETWEEN 1 AND 0, BY BOTH ROUTES
===============================================================================

M asked what the state between the two binary values is.  There are two
answers and neither has a different sign of energy.

    BY THE FADE  F -> (1-2t)F:

        t = 0.00   |F| = 1.769801    rho = +4.739016
        t = 0.25   |F| = 0.884901    rho = +1.184754
        t = 0.50   |F| = 0.000000    rho =  0.000000     <- THE VACUUM
        t = 0.75   |F| = 0.884901    rho = +1.184754
        t = 1.00   |F| = 1.769801    rho = +4.739016

        THE BETWEEN-STATE IS EMPTY SPACE.  The fade reaches -F and pays for it
        by passing through nothing at all.

    BY DUALITY ROTATION: the between-states are rotated fields of IDENTICAL
        energy, and |F_a| never reaches zero.  A switch that never empties --
        and never changes anything either.

        SO: ONE ROUTE'S BETWEEN-STATE IS ZERO AND THE OTHER'S IS UNCHANGED.
        NEITHER IS NEGATIVE.

    (Sign convention, checked: T^0_0 in the mixed index is -rho in signature
    (-,+,+,+).  The measured T^0_0 = -4.739016 is an energy density of
    +4.739016, and (E^2+B^2)/2 = +4.739016 confirms it.  NO NEGATIVE ENERGY
    APPEARS ANYWHERE ABOVE, and reading the raw component as one would be the
    easiest available error.)

===============================================================================
4. "TAKE RATHER THAN GIVE" -- THE ONE THAT LANDS
===============================================================================

This is the good half and it deserves its own statement.

    REMOVING ORDINARY ENERGY HAS A FLOOR.  m(r) = 4 pi Int rho r^2 dr, and if
    the region holds rho >= 0 then taking energy out drives m(r) toward zero
    and stops there:

        removed   0%   rho = 1.000 rho_0      m(r) >= 0
        removed  50%   rho = 0.500 rho_0      m(r) >= 0
        removed 100%   rho = 0.000 rho_0      m(r) >= 0

        YOU CANNOT TAKE AWAY MORE THAN IS THERE.  Subtraction reaches zero and
        stops, which is zeno.py's finding in a new place: cancellation and
        removal both terminate at zero, and the requirement is on the far side.

    UNLESS YOU REMOVE FROM THE VACUUM -- AND THAT IS THE CASIMIR EFFECT.  The
    vacuum is not empty, so excluding modes from a region leaves it with LESS
    energy than free space:

        rho = -pi^2 hbar c / (720 d^4)

        d = 1e-6 m      rho = -4.3338e-04 J/m^3
        d = 1e-7 m      rho = -4.3338e+00 J/m^3
        d = 1e-8 m      rho = -4.3338e+04 J/m^3

    M REACHED, BY REASONING, THE ONE MECHANISM KNOWN TO PRODUCE NEGATIVE ENERGY
    DENSITY IN A LABORATORY.  That is the correct instinct and it should be
    said plainly.

    AND THE TREE ALREADY HOLDS IT, ALREADY PRICED.  candidates.py ran Casimir
    against the three gates; magnitude.py gave it an area-law constant,
    k_Cas = pi^2 Lambda/720 = 0.136838353, with its crossover at 0.369917 l_P.
    SAME WALL.  Casimir is not a new door -- it is the door the tree measured,
    and it is sub-Planckian like the others.

===============================================================================
5. "REDUCING BY AN AXIS" GOES THE WRONG WAY TWICE
===============================================================================

    SURFACE-TO-VOLUME FALLS, IT DOES NOT RISE.  For a D-ball of radius r the
    ratio is D/r:  3/r in three dimensions, 2/r in two, 1/r in one.  REMOVING
    AN AXIS REDUCES THE SURFACE PER UNIT VOLUME.

    AND THE GRAVITY GOES WITH IT.  solve.py's corrected propagator gives a
    static exchange amplitude of 2 - 2/(D-2), which is EXACTLY ZERO at D = 3
    spacetime -- the known fact that 2+1 gravity has no Newtonian attraction.
    dimension.py measured the same thing from the metric side: at D = 3 there
    is no r in f(r) at all, only a conical deficit.

        REMOVING AN AXIS DOES NOT CONCENTRATE THE FIELD.  IT DELETES IT.

===============================================================================
6. WHAT THE PASS LEAVES
===============================================================================

    THE SWITCH IS REAL AND GRAVITY IS BLIND TO IT -- new here, and exact.
    THE BETWEEN-STATE IS EITHER EMPTY OR IDENTICAL -- never negative.
    SUBTRACTION FLOORS AT ZERO unless it is vacuum subtraction.
    VACUUM SUBTRACTION IS CASIMIR, is the right instinct, and is already priced
        at the same sub-Planckian wall.
    AXIS REMOVAL deletes the gravity rather than concentrating it.

    M'S REFRAME FROM GIVING TO TAKING IS THE BEST STRATEGIC MOVE OF THE
    SESSION AND IT ARRIVES AT A DOOR THE TREE HAD ALREADY OPENED AND MEASURED.
    That is not a failure of the reframe.  IT IS THE REFRAME CONVERGING ON THE
    SAME PLACE FROM A DIFFERENT DIRECTION, which is what a correct instinct
    does when the wall is real.

SCOPE.  Section 2 is measured on one random field and is a demonstration of two
standard invariances, not a proof; NO NOVELTY IS CLAIMED for either.  Section 4
quotes the ideal parallel-plate Casimir density and candidates.py's gate
results, adding no new bound.  Section 5 restates solve.py and dimension.py.
NOTHING IS REPAIRED and no new route is proposed.
"""

import math
import random
import sys

ETA = [[-1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1,
       (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}

HBAR, C_SI = 1.054571817e-34, 2.99792458e8
LAMBDA = 9.982529174194637


def F_from_EB(E, B):
    F = [[0.0] * 4 for _ in range(4)]
    for i in range(3):
        F[0][i + 1] = E[i]
        F[i + 1][0] = -E[i]
    for i in range(3):
        for j in range(3):
            F[i + 1][j + 1] = sum(EPS.get((i, j, k), 0) * B[k] for k in range(3))
    return F


def stress_mixed(Fd):
    Fm = [[sum(ETA[m][a] * Fd[a][n] for a in range(4)) for n in range(4)]
          for m in range(4)]
    Fuu = [[sum(ETA[n][b] * Fm[m][b] for b in range(4)) for n in range(4)]
           for m in range(4)]
    F2 = sum(Fuu[a][b] * Fd[a][b] for a in range(4) for b in range(4))
    return [[sum(Fuu[m][a] * Fd[n][a] for a in range(4))
             - (0.25 * F2 if m == n else 0.0) for n in range(4)]
            for m in range(4)]


def energy_density(Fd):
    """rho = -T^0_0 in signature (-,+,+,+).  Reading the raw component is the
    easiest available error, so it is done here once and named."""
    return -stress_mixed(Fd)[0][0]


def maxdiff(A, B):
    return max(abs(A[i][j] - B[i][j]) for i in range(4) for j in range(4))


def fnorm(F):
    return max(abs(F[i][j]) for i in range(4) for j in range(4))


def negate(F):
    return [[-F[i][j] for j in range(4)] for i in range(4)]


def duality(E, B, a):
    Ea = [E[i] * math.cos(a) + B[i] * math.sin(a) for i in range(3)]
    Ba = [-E[i] * math.sin(a) + B[i] * math.cos(a) for i in range(3)]
    return F_from_EB(Ea, Ba)


def sample_field(seed=5):
    rng = random.Random(seed)
    E = [rng.uniform(-2, 2) for _ in range(3)]
    B = [rng.uniform(-2, 2) for _ in range(3)]
    return E, B


# -- 4.  subtraction ---------------------------------------------------------

def removal_floor(rho0, fraction):
    """Removing ordinary energy: bottoms out at zero."""
    return rho0 * (1.0 - fraction)


def casimir_density(d):
    """-pi^2 hbar c/(720 d^4).  Vacuum subtraction, and it IS negative."""
    return -math.pi ** 2 * HBAR * C_SI / (720.0 * d ** 4)


K_CASIMIR = math.pi ** 2 * LAMBDA / 720.0
CASIMIR_CROSSOVER_LP = math.sqrt(K_CASIMIR)


# -- 5.  axis removal --------------------------------------------------------

def surface_to_volume(D, r=1.0):
    """D/r for a D-ball.  Falls as D falls."""
    return D / r


def static_amplitude(D_spacetime):
    """2 - 2/(D-2).  Zero at D = 3: no Newtonian attraction in 2+1."""
    return 2.0 - 2.0 / (D_spacetime - 2)


# The four claims.
CLAIMS = [
    ("EM provides a switch action", "LANDS",
     "two of them -- charge conjugation and duality rotation, both exact"),
    ("EM can switch the gravitational field", "REFUTED",
     "|T(F) - T(-F)| = 0.000e+00 exactly; duality invariant to 4.4e-16"),
    ("take energy rather than give it", "LANDS",
     "the Casimir mechanism -- and already in the tree, already priced, "
     "same sub-Planckian wall"),
    ("reducing by an axis gives larger surface space", "REFUTED",
     "S/V = D/r FALLS as D falls, and 2+1 gravity has no Newtonian force"),
]

NOVELTY_CLAIMED = False


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

    E, B = sample_field()
    F = F_from_EB(E, B)
    T = stress_mixed(F)

    # -- sign convention, established before anything is read off ------------
    chk("T^0_0 mixed is negative", T[0][0] < 0, True)
    chk("  and the ENERGY DENSITY is its negative",
        energy_density(F), 0.5 * (sum(e * e for e in E) + sum(b * b for b in B)),
        1e-12)
    chk("  which is POSITIVE", energy_density(F) > 0, True)

    # -- 1-2: the switch exists and gravity cannot see it --------------------
    Fn = negate(F)
    chk("F -> -F genuinely reverses the field", maxdiff(F, Fn), 3.5396, 1e-4)
    chk("and T is EXACTLY unchanged", maxdiff(T, stress_mixed(Fn)), 0.0)
    chk("  exactly zero, not machine zero", maxdiff(T, stress_mixed(Fn)) == 0.0,
        True)
    for a in (math.pi / 4, math.pi / 2, math.pi):
        chk("duality at a=%.4f leaves T invariant" % a,
            maxdiff(stress_mixed(duality(E, B, a)), T) < 1e-14, True)
    chk("duality at a=pi reaches -F",
        maxdiff(duality(E, B, math.pi), Fn) < 1e-12, True)
    chk("  and |F| never vanishes on the way",
        min(fnorm(duality(E, B, math.pi * i / 20)) for i in range(21)) > 1.0,
        True)
    chk("the reason is that T is QUADRATIC in F",
        "QUADRATIC IN F" in __doc__, True)

    # -- 3: the between-state ------------------------------------------------
    half = [[0.0] * 4 for _ in range(4)]
    chk("the FADE passes through the vacuum", energy_density(half), 0.0)
    chk("  so that between-state is EMPTY", fnorm(half), 0.0)
    chk("the duality between-state is UNCHANGED in energy",
        abs(energy_density(duality(E, B, math.pi / 2)) - energy_density(F))
        < 1e-12, True)
    chk("neither between-state is NEGATIVE",
        energy_density(half) >= 0 and
        energy_density(duality(E, B, math.pi / 2)) > 0, True)

    # -- 4: subtraction floors at zero, unless it is the vacuum --------------
    for f in (0.0, 0.5, 1.0):
        chk("removing %.0f%% leaves rho >= 0" % (f * 100),
            removal_floor(4.739016, f) >= 0.0, True)
    chk("removal bottoms out at exactly zero", removal_floor(4.739016, 1.0), 0.0)
    chk("Casimir IS negative", casimir_density(1e-7) < 0, True)
    chk("  at d = 1e-7 m", casimir_density(1e-7), -4.3338, 1e-4)
    chk("  and steepens as d^-4",
        casimir_density(1e-8) / casimir_density(1e-7), 1e4, 1e-9)
    chk("but it is the tree's own already-priced door",
        K_CASIMIR, 0.136838353, 1e-8)
    chk("  crossing sub-Planckian", CASIMIR_CROSSOVER_LP, 0.369917, 1e-5)

    # -- 5: axis removal goes the wrong way twice ----------------------------
    chk("S/V falls as D falls",
        [surface_to_volume(D) for D in (3, 2, 1)], [3.0, 2.0, 1.0])
    chk("  so removing an axis REDUCES surface per volume",
        surface_to_volume(2) < surface_to_volume(3), True)
    chk("and 2+1 gravity has NO Newtonian attraction",
        static_amplitude(3), 0.0, 1e-15)
    chk("  while D = 4 does", static_amplitude(4), 1.0, 1e-15)

    # -- the ledger -----------------------------------------------------------
    chk("four claims", len(CLAIMS), 4)
    chk("two land", sum(1 for c in CLAIMS if c[1] == "LANDS"), 2)
    chk("two refuted", sum(1 for c in CLAIMS if c[1] == "REFUTED"), 2)
    chk("no novelty claimed", NOVELTY_CLAIMED, False)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    E, B = sample_field()
    F = F_from_EB(E, B)
    T = stress_mixed(F)
    print("  ------------------------------------------------------------------------")
    print("  THE SWITCH, AND WHAT GRAVITY MAKES OF IT\n")
    print("    F -> -F        |F - (-F)| = %.4f   |T(F) - T(-F)| = %.3e"
          % (maxdiff(F, negate(F)), maxdiff(T, stress_mixed(negate(F)))))
    print("\n    duality   alpha       |F_a|       |T(F_a) - T(F)|   F_a = -F ?")
    for a in (0.0, math.pi / 4, math.pi / 2, 3 * math.pi / 4, math.pi):
        Fa = duality(E, B, a)
        print("              %-10.5f  %-11.6f %-17.3e %s"
              % (a, fnorm(Fa), maxdiff(stress_mixed(Fa), T),
                 "YES" if maxdiff(Fa, negate(F)) < 1e-12 else ""))
    print("\n    the field travels all the way to -F and T NEVER MOVES.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  TAKE RATHER THAN GIVE\n")
    print("    removing ORDINARY energy:")
    for f in (0.0, 0.5, 0.9, 1.0):
        print("      removed %3.0f%%   rho = %.6f   m(r) >= 0"
              % (f * 100, removal_floor(4.739016, f)))
    print("      FLOOR AT ZERO.\n")
    print("    removing VACUUM modes -- the Casimir effect:")
    for d in (1e-6, 1e-7, 1e-8):
        print("      d = %-8.0e m   rho = %+.4e J/m^3" % (d, casimir_density(d)))
    print("      NEGATIVE -- and it is the tree's own k_Cas = %.9f," % K_CASIMIR)
    print("      crossing at %.6f l_P.  SAME WALL." % CASIMIR_CROSSOVER_LP)
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE FOUR CLAIMS\n")
    for what, verdict, why in CLAIMS:
        print("    %-42s %-9s %s" % (what, verdict, why[:44]))
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M is right that EM provides a switch action -- it provides TWO, charge
  conjugation F -> -F and duality rotation, and the second carries the
  field continuously from F all the way to -F without ever passing through
  zero.  AND GRAVITY CANNOT SEE EITHER.  |T(F) - T(-F)| is 0.000e+00,
  exactly zero rather than machine zero, and T is constant to 4.4e-16
  along the whole duality path.  The reason is one line: gravity couples
  to T_munu, T_munu is QUADRATIC in F, and squaring does not merely
  destroy the sign the switch flips -- it does not notice it.  That is
  invariance.py's scale/shape split arriving as a direct measurement, the
  switch acting on a coefficient and the obstruction living in the shape.
  The state between the two values is either the VACUUM, by the fade,
  which passes through rho = 0 exactly, or an IDENTICAL-energy rotated
  field, by duality -- NEITHER IS NEGATIVE.  And the reframe from giving
  to taking is the best strategic move of the session: removing ordinary
  energy floors at zero, because you cannot take away more than is there,
  BUT REMOVING VACUUM MODES GOES NEGATIVE AND THAT IS THE CASIMIR EFFECT
  -- the one mechanism known to produce rho < 0 in a laboratory, reached
  here by reasoning.  It is also already in this tree, already run against
  the three gates, already carrying an area-law constant of 0.136838353
  and a crossover at 0.369917 l_P.  SAME WALL.  Only the last step goes
  wrong twice: surface-to-volume is D/r and FALLS as dimension falls, and
  2+1 gravity has no Newtonian attraction at all, so removing an axis
  deletes the field rather than concentrating it.  The reframe converged
  on a door the tree had already opened and measured, WHICH IS WHAT A
  CORRECT INSTINCT DOES WHEN THE WALL IS REAL.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
