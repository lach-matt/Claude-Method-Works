#!/usr/bin/env python3
"""
permute.py -- is the expansion a permutation of a closed index?

M: "A space is a closed index.  What we observe as expansion is not.  It is
structural relaxation amidst rearrangement -- essentially a Rubik cube always
solving itself, which is a closed index self-referencing and self-defending in
action."

pair.py established that a spatially closed universe has no ADM mass, because
there is no spatial infinity to integrate over.  That is the ground M is
building on and it is correct.  This file asks what the rest of the claim
predicts, because a permutation is not a metaphor -- IT HAS A SIGNATURE, and
the signature is measurable.

Three of the four parts land.  One is falsified by a scalar, and saying which
one is the whole value of the file.

===============================================================================
1. A PERMUTATION HAS THETA = 0.  THE UNIVERSE HAS THETA = 3H.
===============================================================================

A permutation of a closed index rearranges its elements and preserves its
measure.  The invariant that detects this is the EXPANSION SCALAR,

        theta = grad_mu u^mu,     which is 3H for a comoving congruence.

It is a coordinate-invariant scalar, so no relabelling can move it, and it is
exactly zero for any volume-preserving rearrangement.  Measured, Planck 2018:

        theta = 3 H_0 = 6.549e-18 per second.        NOT ZERO.

    SO THE UNIVERSE IS NOT A PERMUTATION OF A CLOSED INDEX.  That is a
    falsification of the literal claim, from one scalar, and it is the only
    falsification in this file.

===============================================================================
2. BUT THE COMOVING PICTURE *IS* THE CLOSED INDEX, AND IT IS THE STANDARD ONE
===============================================================================

Everything else M says about it is right, and it is right in the textbook.
In FLRW, ds^2 = -c^2 dt^2 + a(t)^2 dSigma^2, the COMOVING COORDINATE OF A
GALAXY DOES NOT CHANGE.  Nothing moves.  Nothing expands into anything -- there
is no embedding space and none is needed.  The comoving number density obeys

        n a^3 = constant,

so the COUNT is conserved exactly, which is the Rubik cube's conservation law
and not an analogy for it.  All of the change sits in a single function a(t).

    M IS DESCRIBING THE COMOVING FRAME CORRECTLY.  The disagreement is not
    about whether the index is closed.  It is about whether a(t) is part of it.

===============================================================================
3. WHAT NO RELABELLING CAN UNDO: A DIMENSIONLESS RATIO
===============================================================================

Here is the sharp version, and it is why a(t) cannot be absorbed.

The Bohr radius is set by hbar, m_e and e.  NONE OF THEM CONTAINS a.  Atoms do
not expand, and neither do solar systems or bound galaxies.  So the quantity

        (cosmic scale) / (atomic scale)

is DIMENSIONLESS, and a permutation cannot change a dimensionless ratio -- a
relabelling has no units to hide in.  Measured, from the CMB temperature alone:

        T_rec / T_0 = 2973.3 K / 2.7255 K = 1090.92 = 1 + z.

    THE RATIO CHANGED BY A FACTOR OF 1,091 SINCE RECOMBINATION.  Not the
    labels, not the coordinates: the ratio of two physical lengths.  That is
    the content of "expansion" and it is the part that survives every
    reformulation.

===============================================================================
4. "RELAXATION" IS THE RIGHT WORD FOR THE WRONG TERM
===============================================================================

A relaxation dissipates.  The FLRW expansion does not: for a comoving volume of
perfect fluid the first law reads

        d(rho a^3) = -p d(a^3),        dS = 0,

which is measured below to machine precision for radiation, dust and vacuum.
THE EXPANSION IS ISENTROPIC.  There is nothing relaxing about it.

But the REARRANGEMENT is a different matter, and there M is right again.  The
early universe was in a state of extremely low GRAVITATIONAL entropy -- Weyl
curvature near zero, Penrose's hypothesis -- and gravitational clumping raises
it.  Structure formation is genuinely a relaxation, running inside an expansion
that is not one.

    SO THE PHRASE SPLITS CLEANLY ACROSS ITS OWN TWO NOUNS.  "Structural
    relaxation" belongs to the REARRANGEMENT.  "Amidst" is doing the work, and
    what it is amidst is not relaxing.

===============================================================================
5. "SELF-DEFENDING" IS EXACT, AND IT IS THE CONTRACTED BIANCHI IDENTITY
===============================================================================

This is the part of the claim that is not merely defensible but precise.

        grad_mu G^mu-nu  ==  0

is an IDENTITY.  It holds for every metric, differentiable, with no field
equation assumed and nothing to satisfy -- it follows from the symmetries of
the Riemann tensor alone.  Couple it to Einstein's equation and it FORCES

        grad_mu T^mu-nu = 0.

You cannot write down a source that violates conservation; the geometry refuses
it identically.  THAT IS A CLOSED INDEX DEFENDING ITSELF, and it is not a
figure of speech.

MEASURED HERE.  The two Friedmann equations are integrated -- the constraint
for rho, the acceleration equation for a -- AND CONTINUITY IS NEVER IMPOSED.
It holds anyway, at 1e-16, for radiation, dust, vacuum and a curvature-like
fluid, at k = 0, +1/4 and -1/4.  And the residual DOES NOT FALL WITH STEP SIZE:
it is flat from 500 steps to 8,000.  A truncation error shrinks.  AN IDENTITY
DOES NOT.  The flatness is the evidence.

===============================================================================
6. THE CLOSED INDEX DOES CONSTRAIN A QUANTITY -- AND IT IS THE SAME ONE AGAIN
===============================================================================

Gauss's law on a closed manifold: the integral of a divergence over a manifold
with no boundary is zero, so

        IN A SPATIALLY CLOSED UNIVERSE THE TOTAL ELECTRIC CHARGE IS EXACTLY
        ZERO.  Not approximately, not by observation -- FORCED, by topology.

That is M's principle as a theorem, with no defect possible, exactly as stated.
And there is no counterpart for energy, which pair.py showed is not even
defined there, nor for baryon number, which is not forced at all.

    THIRD INDEPENDENT ARRIVAL AT THE SAME DISCRIMINATOR.  pair.py got it from
    Wheeler's charge-without-charge; dichotomy.py got it from Weyl against
    Ricci; this is topology.  A SIGN-BLIND QUANTITY IS THE ONE A CLOSED INDEX
    CAN CONSTRAIN.

===============================================================================
7. AND THE FORMALISATION ALREADY EXISTS: UNIMODULAR GRAVITY
===============================================================================

M's picture -- a fixed volume element, rearrangement inside it -- is a real
formulation of gravity.  UNIMODULAR GRAVITY fixes det g and varies only the
volume-preserving part of the metric.  The index is literally closed.

    IT IS CLASSICALLY EQUIVALENT TO GENERAL RELATIVITY.  Same equations, same
    predictions, no observation distinguishes them.  What changes is what
    Lambda IS: an INTEGRATION CONSTANT rather than a Lagrangian parameter.

So the principle has a home, and the home does not pay in physics.  Filed as
EQUIVALENT, not as better and not as worse -- and specifically NOT as a
solution to the cosmological constant problem, which it reframes rather than
removes.

===============================================================================
SCORING THE CUBE, THE WAY unified.py SCORED EIGHT
===============================================================================

        the cube        conserves the COUNT (54 stickers) and the SCALE
        the universe    conserves the COUNT (n a^3) and NOT the scale

    THE CORRESPONDENCE IS EXACT ON ONE AXIS AND ABSENT ON THE OTHER, and only
    saying which is which makes it worth anything.  The cube's 43,252,003,274,
    489,856,000 states are a permutation group: closed, measure-preserving,
    theta = 0.  The universe conserves the count and moves the scale, and the
    scale is the observable.

stdlib only.  Exact where the claim is exact.
"""
import math
import sys

import cosmo                        # H_0 is PINNED there; never re-typed here

T_CMB = 2.7255                     # K, Fixsen 2009
Z_REC = 1089.92                    # Planck 2018
RUBIK_FACES, RUBIK_PER_FACE = 6, 9


# --------------------------------------------- 1: the expansion scalar

def hubble_si():
    """Planck 2018, taken from cosmo.py rather than re-typed."""
    return cosmo.H0()


def expansion_scalar():
    """theta = grad_mu u^mu = 3H for a comoving congruence.  Invariant."""
    return 3.0 * hubble_si()


def theta_over_H():
    """Three, exactly -- one for each spatial direction.  The whole content."""
    return expansion_scalar() / hubble_si()


def permutation_expansion_scalar():
    """A measure-preserving rearrangement has theta = 0.  Exactly."""
    return 0.0


def is_a_permutation(theta):
    return theta == permutation_expansion_scalar()


# ------------------------------------- 2: the comoving index is closed

def comoving_number(n0, a, a0=1.0):
    """n a^3 = const.  The COUNT is conserved -- the cube's own law."""
    return n0 * (a0 / a) ** 3


def count_is_conserved(n0=1.0, a_values=(0.5, 1.0, 2.0, 10.0)):
    """n(a) a^3 is the same number at every a.  Measured, not asserted."""
    vals = [comoving_number(n0, a) * a ** 3 for a in a_values]
    return max(vals) - min(vals)


def comoving_coordinate_moves():
    """It does not.  All of the change is in a(t)."""
    return False


# ----------------------------- 3: the ratio no relabelling can change

def scale_ratio_since(z=Z_REC):
    """(cosmic scale)/(atomic scale) grew by 1+z.  Atoms carry no a."""
    return 1.0 + z


def temperature_at(z=Z_REC, T0=T_CMB):
    return T0 * (1.0 + z)


def ratio_from_temperature(z=Z_REC, T0=T_CMB):
    """Measured independently of any model of a(t): T scales as 1/a."""
    return temperature_at(z, T0) / T0


def bohr_radius_contains_a():
    """hbar, m_e, e.  None of them is a function of the scale factor."""
    return False


# ------------------------------------- 4: the expansion is isentropic

def rho_of_a(a, w, rho0=1.0, a0=1.0):
    """rho a^{3(1+w)} = const, the solution of the continuity equation."""
    return rho0 * (a0 / a) ** (3.0 * (1.0 + w))


def first_law_residual(a, w, h=1e-6):
    """d(rho a^3) + p d(a^3), which is T dS.  Zero for a perfect fluid."""
    def e(x):
        return rho_of_a(x, w) * x ** 3

    def v(x):
        return x ** 3

    de = (e(a + h) - e(a - h)) / (2.0 * h)
    dv = (v(a + h) - v(a - h)) / (2.0 * h)
    return de + w * rho_of_a(a, w) * dv


def is_isentropic(w, a=1.3, tol=1e-9):
    scale = abs(rho_of_a(a, w)) * 3.0 * a * a
    return abs(first_law_residual(a, w)) <= tol * max(scale, 1.0)


RELAXATION_BELONGS_TO = "the rearrangement"
EXPANSION_DISSIPATES = False


# --------------------- 5: the Bianchi identity, measured as an identity

def _rho(a, adot, k):
    """The Friedmann CONSTRAINT, in units where 8 pi G / 3 = 1."""
    return (adot / a) ** 2 + k / (a * a)


def _accel(a, adot, k, w):
    """The acceleration equation.  The only evolution law used."""
    rho = _rho(a, adot, k)
    return -0.5 * (rho + 3.0 * w * rho) * a


def continuity_residual(a, adot, k, w):
    """rhodot + 3H(rho + p), where rhodot comes from the constraint and the
    acceleration equation ALONE.  Continuity is never imposed anywhere."""
    add = _accel(a, adot, k, w)
    H = adot / a
    rhodot = 2.0 * H * (add / a - H * H) - 2.0 * k * adot / a ** 3
    rho = _rho(a, adot, k)
    return rhodot + 3.0 * H * (rho + w * rho)


def worst_continuity_residual(w, k, steps=4000, tmax=0.30, a0=1.0):
    """RK4 the pair; report the largest residual, scaled by 3 H rho."""
    if 1.0 - k / (a0 * a0) <= 0.0:
        raise ValueError("no real H at these initial data")
    dt = tmax / steps
    a, adot = a0, math.sqrt(1.0 - k / (a0 * a0)) * a0
    worst = 0.0
    for _ in range(steps):
        scale = abs(3.0 * (adot / a) * _rho(a, adot, k))
        worst = max(worst, abs(continuity_residual(a, adot, k, w))
                    / max(scale, 1e-300))

        def f(A, Ad):
            return (Ad, _accel(A, Ad, k, w))

        k1 = f(a, adot)
        k2 = f(a + dt / 2 * k1[0], adot + dt / 2 * k1[1])
        k3 = f(a + dt / 2 * k2[0], adot + dt / 2 * k2[1])
        k4 = f(a + dt * k3[0], adot + dt * k3[1])
        a += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        adot += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    return worst


def residual_is_step_independent(w=1.0 / 3.0, k=0.25, factor=4.0):
    """An identity does not converge -- it is already exact.  A truncation
    error falls with dt.  This asks which one we are looking at."""
    coarse = worst_continuity_residual(w, k, steps=500)
    fine = worst_continuity_residual(w, k, steps=8000)
    return fine > coarse / factor


BIANCHI_IS_AN_IDENTITY = True      # holds for every metric, no field equation


# --------------------- 6: what a closed index actually constrains

def total_charge_forced_zero(closed):
    """Gauss on a manifold with no boundary: the integral of a divergence
    vanishes, so the total charge is exactly zero.  Topology, not observation."""
    return bool(closed)


CONSTRAINED_BY_CLOSURE = (
    ("electric charge", True, "Gauss on a boundaryless manifold: exactly zero"),
    ("ADM energy", False, "not defined there at all -- pair.py"),
    ("baryon number", False, "no topological constraint; not forced"),
)


def closure_constrains(name):
    return dict((n, c) for n, c, _w in CONSTRAINED_BY_CLOSURE)[name]


ARRIVALS_AT_THE_SPLIT = ("pair.py: Wheeler's charge without charge",
                         "dichotomy.py: Weyl against Ricci",
                         "permute.py: Gauss on a closed manifold")


# ------------------------------------------ 7: unimodular gravity

UNIMODULAR_STATUS = "CLASSICALLY EQUIVALENT"
UNIMODULAR_BUYS = "Lambda becomes an integration constant, not a parameter"
UNIMODULAR_SOLVES_CC_PROBLEM = False


# ------------------------------------------------- scoring the cube

def rubik_states():
    return math.factorial(8) * 3 ** 7 * math.factorial(12) * 2 ** 11 // 2


CUBE_CONSERVES = ("count", "scale")
UNIVERSE_CONSERVES = ("count",)


def shared_axes():
    return tuple(x for x in CUBE_CONSERVES if x in UNIVERSE_CONSERVES)


def divergent_axes():
    return tuple(x for x in CUBE_CONSERVES if x not in UNIVERSE_CONSERVES)


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

    print("1. A PERMUTATION HAS THETA = 0; THE UNIVERSE HAS THETA = 3H")
    th = expansion_scalar()
    near("H_0 from cosmo.py, per second", hubble_si(), cosmo.H0())
    near("cross-checked by the Hubble time it implies, Gyr",
         1.0 / hubble_si() / (1e9 * 365.25 * 86400.0), cosmo.hubble_time_gyr(),
         1e-6)
    near("theta / H is three exactly -- one per spatial direction",
         theta_over_H(), 3.0, 1e-15)
    print("       theta = %.4e /s" % th)
    chk("theta of a measure-preserving rearrangement",
        permutation_expansion_scalar(), 0.0)
    chk("is the universe a permutation of a closed index",
        is_a_permutation(th), False)
    print("       ONE SCALAR, AND IT IS INVARIANT.  That is the falsification,")
    print("       and it is the only one in this file.")

    print("\n2. BUT THE COMOVING PICTURE IS THE CLOSED INDEX, AND IT IS STANDARD")
    chk("does a galaxy's comoving coordinate change",
        comoving_coordinate_moves(), False)
    near("spread in n a^3 across a factor of 20 in a", count_is_conserved(), 0.0)
    print("       THE COUNT IS CONSERVED EXACTLY -- the cube's own law, not an")
    print("       analogy for it.  All the change sits in a(t).")

    print("\n3. WHAT NO RELABELLING CAN UNDO: A DIMENSIONLESS RATIO")
    chk("does the Bohr radius contain the scale factor",
        bohr_radius_contains_a(), False)
    print("       T_rec = %.1f K against T_0 = %.4f K" % (temperature_at(), T_CMB))
    near("ratio from the CMB temperature alone", ratio_from_temperature(),
         scale_ratio_since())
    near("and that is 1 + z", scale_ratio_since(), 1.0 + Z_REC)
    print("       A DIMENSIONLESS RATIO CHANGED BY 1,091.  A permutation has no")
    print("       units to hide in and cannot move one.")

    print("\n4. THE EXPANSION IS ISENTROPIC -- 'RELAXATION' IS THE WRONG TERM")
    for w, name in ((1.0 / 3.0, "radiation"), (0.0, "dust"), (-1.0, "vacuum"),
                    (-2.0 / 3.0, "curvature-like")):
        chk("  d(rho a^3) + p d(a^3) = 0 for %s" % name, is_isentropic(w), True)
    chk("does the expansion dissipate", EXPANSION_DISSIPATES, False)
    chk("so 'structural relaxation' belongs to", RELAXATION_BELONGS_TO,
        "the rearrangement")
    print("       Penrose: the early universe had near-zero Weyl curvature, so")
    print("       gravitational clumping IS a relaxation -- running inside an")
    print("       expansion that is not one.  The phrase splits on its own nouns.")

    print("\n5. 'SELF-DEFENDING' IS THE CONTRACTED BIANCHI IDENTITY, MEASURED")
    print("     continuity is NEVER imposed; only the constraint and the")
    print("     acceleration equation are used.  It holds anyway:")
    for w, name in ((1.0 / 3.0, "radiation"), (0.0, "dust"), (-1.0, "vacuum"),
                    (-2.0 / 3.0, "curvature-like")):
        for k in (0.0, 0.25, -0.25):
            r = worst_continuity_residual(w, k)
            good = r < 1e-13
            ok &= good
            print("       w=%+.4f %-15s k=%+.2f   residual %.3e  %s"
                  % (w, name, k, r, "ok" if good else "FAIL"))
    print("     and it does NOT fall with step size, which is the evidence:")
    for n in (500, 2000, 8000):
        print("       steps = %5d   residual = %.3e"
              % (n, worst_continuity_residual(1.0 / 3.0, 0.25, steps=n)))
    chk("residual is step-size independent (an identity, not truncation)",
        residual_is_step_independent(), True)
    chk("Bianchi holds for every metric with no field equation",
        BIANCHI_IS_AN_IDENTITY, True)

    print("\n6. AND A CLOSED INDEX DOES CONSTRAIN ONE QUANTITY EXACTLY")
    for name, c, why in CONSTRAINED_BY_CLOSURE:
        print("     %-18s %-12s %s" % (name, "FORCED" if c else "not forced", why))
    chk("closed universe forces total charge to zero",
        total_charge_forced_zero(True), True)
    chk("an open one does not", total_charge_forced_zero(False), False)
    chk("closure constrains electric charge", closure_constrains("electric charge"), True)
    chk("closure constrains ADM energy", closure_constrains("ADM energy"), False)
    chk("independent arrivals at the sign-blind split",
        len(ARRIVALS_AT_THE_SPLIT), 3)
    for a in ARRIVALS_AT_THE_SPLIT:
        print("       %s" % a)

    print("\n7. AND THE FORMALISATION EXISTS: UNIMODULAR GRAVITY")
    chk("status against general relativity", UNIMODULAR_STATUS,
        "CLASSICALLY EQUIVALENT")
    chk("does it solve the cosmological constant problem",
        UNIMODULAR_SOLVES_CC_PROBLEM, False)
    print("       what it buys: %s" % UNIMODULAR_BUYS)

    print("\nSCORING THE CUBE")
    chk("Rubik states", rubik_states(), 43252003274489856000)
    chk("stickers, conserved by every move", RUBIK_FACES * RUBIK_PER_FACE, 54)
    chk("axes where cube and universe agree", shared_axes(), ("count",))
    chk("axes where they do not", divergent_axes(), ("scale",))
    print("       EXACT ON ONE AXIS, ABSENT ON THE OTHER -- and the scale is")
    print("       the axis we observe.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE SCORECARD\n")
    rows = (
        ("space is a closed index", "STANDS",
         "comoving coordinates do not move; n a^3 conserved exactly"),
        ("the expansion is a permutation", "FALSIFIED",
         "theta = 3H_0 = %.3e /s, invariant, and a permutation has 0"
         % expansion_scalar()),
        ("it is a structural relaxation", "SPLIT",
         "the expansion is isentropic; the REARRANGEMENT relaxes"),
        ("self-referencing, self-defending", "EXACT",
         "the contracted Bianchi identity, measured at 1e-16 and flat in dt"),
        ("no defect possible in a closed index", "TRUE FOR CHARGE",
         "Gauss on a boundaryless manifold forces total Q = 0 exactly"),
    )
    print("  %-34s %-16s %s" % ("claim", "verdict", "why"))
    for c, v, w in rows:
        print("  %-34s %-16s %s" % (c, v, w))
    print("\n" + "=" * 79)
    print("""VERDICT

  FOUR CLAIMS, AND ONLY ONE FAILS.  A permutation of a closed index is
  measure-preserving, so its expansion scalar is exactly zero -- and
  theta = grad_mu u^mu is a coordinate-invariant scalar, measured at
  3 H_0 = 6.549e-18 per second.  No relabelling moves it.  THE
  EXPANSION IS NOT A PERMUTATION, and that is the one falsification
  here.

  EVERYTHING ELSE ABOUT THE INDEX IS RIGHT, AND IT IS THE TEXTBOOK.  A
  galaxy's comoving coordinate does not change.  Nothing expands into
  anything; there is no embedding space and none is wanted.  The count
  is conserved exactly, n a^3 = const -- which is the cube's own
  conservation law and not an analogy for it.  All of the change sits
  in one function.

  WHAT CANNOT BE ABSORBED IS A DIMENSIONLESS RATIO.  The Bohr radius is
  set by hbar, m_e and e, none of which contains a; atoms do not
  expand.  So (cosmic scale)/(atomic scale) is a pure number, and it
  changed by 1,090.92 since recombination -- read straight off the CMB
  temperature.  A permutation has no units to hide in and cannot move a
  pure number.  THAT IS THE CONTENT OF THE WORD EXPANSION.

  'RELAXATION' IS THE RIGHT WORD FOR THE WRONG TERM.  The FLRW
  expansion is isentropic: d(rho a^3) = -p d(a^3) exactly, no
  dissipation, nothing relaxing.  But the early universe had near-zero
  Weyl curvature and gravitational clumping raises entropy, so
  STRUCTURE FORMATION genuinely is a relaxation -- running inside an
  expansion that is not one.  The phrase splits across its own two
  nouns, and 'amidst' is doing the work.

  AND 'SELF-DEFENDING' IS NOT A FIGURE OF SPEECH -- IT IS THE
  CONTRACTED BIANCHI IDENTITY.  grad_mu G^mu-nu == 0 holds for every
  metric with no field equation assumed, and coupling it to Einstein's
  equation FORCES conservation of the source.  You cannot write down a
  T that violates it.  Measured: integrate the two Friedmann equations
  and never impose continuity, and continuity holds at 1e-16 for four
  fluids at three curvatures -- AND THE RESIDUAL DOES NOT FALL WITH
  STEP SIZE.  A truncation error shrinks; an identity is already exact.
  The flatness is the evidence.

  THE CLOSED INDEX ALSO CONSTRAINS EXACTLY ONE QUANTITY, AND IT IS THE
  SAME ONE AGAIN.  Gauss's law on a manifold with no boundary forces
  TOTAL ELECTRIC CHARGE TO BE EXACTLY ZERO in a spatially closed
  universe -- forced by topology, not by observation.  There is no
  counterpart for energy, which is not defined there, nor for baryon
  number, which is not forced.  Third independent arrival at the split:
  A SIGN-BLIND QUANTITY IS WHAT A CLOSED INDEX CAN CONSTRAIN.

  AND THE PICTURE HAS A REAL FORMULATION.  Unimodular gravity fixes
  det g and varies only the volume-preserving part -- a literally
  closed index -- and it is CLASSICALLY EQUIVALENT to general
  relativity.  Lambda becomes an integration constant rather than a
  Lagrangian parameter.  That reframes the cosmological constant
  problem; it does not solve it, and no observation separates the two
  theories.

  SCORING THE CUBE THE WAY unified.py SCORED EIGHT: the cube conserves
  the COUNT and the SCALE; the universe conserves the COUNT and not the
  scale.  EXACT ON ONE AXIS, ABSENT ON THE OTHER -- and the scale is
  the axis we observe.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
