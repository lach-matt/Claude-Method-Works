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
exactly zero for any volume-preserving rearrangement.  Inferred under
base-LCDM, Planck 2018 (H_0 = 67.36 +- 0.54, which Planck calls 'inferred
(model-dependent)', in 3.6-4.4 sigma tension with local measurements):

        theta = 3 H_0 = 6.549e-18 per second.        NOT ZERO.

(At SH0ES's 73.04 it reads 7.101e-18; the value moves by 8.4 %, its sign
does not.)  Modelling a permutation of a closed index as a measure-preserving
flow is this file's own step: the identity supplies only 'volume-preserving
=> theta = 0'.  And theta = 3H is the expansion of the large-scale comoving,
fundamental-observer congruence -- the homogeneity-scale hypothesis; inside
bound structures the matter flow has theta ~ 0.

    SO THE UNIVERSE IS NOT A PERMUTATION OF A CLOSED INDEX -- on the
    large-scale comoving flow.  That is a falsification of the literal claim,
    from one scalar, and it is the only falsification in this file.

===============================================================================
2. BUT THE COMOVING PICTURE *IS* THE CLOSED INDEX, AND IT IS THE STANDARD ONE
===============================================================================

Everything else M says about it is right, and it is right in the textbook.
In FLRW, ds^2 = -c^2 dt^2 + a(t)^2 dSigma^2, the COMOVING COORDINATE OF A
GALAXY DOES NOT CHANGE -- 'in the absence of peculiar motion' (Baumann
0907.5424 pp.15-16).  Real galaxies have it: the Sun moves at 371 km/s against
the comoving frame, a drift of about 0.41 comoving Mpc per Gyr.  On the
idealised comoving congruence nothing moves.  Nothing expands into anything --
there is no embedding space and none is needed.  For a species with a
conserved number current (no creation, annihilation, merger or decay) moving
with that congruence, the comoving number density obeys

        n a^3 = constant,

so the COUNT of that species is conserved exactly, which is the Rubik cube's
conservation law and not an analogy for it.  All of the change sits in a
single function a(t).

    M IS DESCRIBING THE COMOVING FRAME CORRECTLY.  The disagreement is not
    about whether the index is closed.  It is about whether a(t) is part of it.

===============================================================================
3. WHAT NO RELABELLING CAN UNDO: A DIMENSIONLESS RATIO
===============================================================================

Here is the sharp version, and it is why a(t) cannot be absorbed.

The Bohr radius is set by hbar, m_e and e.  NONE OF THEM CONTAINS a -- given
the hypothesis that hbar, m_e and alpha have been constant since z_*.  Atoms do
not expand, and neither do solar systems or bound galaxies.  So the quantity

        (cosmic scale) / (atomic scale)

is DIMENSIONLESS, and a permutation cannot change a dimensionless ratio -- a
relabelling has no units to hide in.  With T scaling as 1/a (free-streaming
FLRW photons, no injection) and z_* = 1089.92 +- 0.25 -- a DERIVED parameter of
Planck 2018's base-LCDM fit to TT,TE,EE+lowE+lensing with T_0 held fixed, not a
reading of the CMB temperature alone:

        T_rec / T_0 = 2973.3 K / 2.7255 K = 1090.92 = 1 + z.

(T_rec here is computed as T_0 (1 + z), so the ratio is 1 + z for any T_0.)
z_* is last scattering, which Planck calls recombination; hydrogen is
half-ionised earlier, at z ~ 1275.  Across Planck's columns 1 + z_* stays
within 1088.8 - 1091.3.

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

which is checked below for radiation, dust and vacuum -- the continuity
solution rho_of_a tested against its own equation by central difference
(relative residuals up to 4.8e-11 against a tolerance of 1e-9), an identity
check rather than a measurement of a physical system.  dS = 0 further needs a
Gibbs relation in local equilibrium with mu dN = 0.  ON THOSE HYPOTHESES THE
EXPANSION IS ISENTROPIC, and there is nothing relaxing about it; a
bulk-viscous fluid (T dS/dt = 9 zeta H^2 a^3 > 0) or a decay between fluids
would dissipate.

But the REARRANGEMENT is a different matter, and there M is right again on a
named hypothesis.  Penrose's Weyl curvature hypothesis -- a conjecture, hedged
in his own words ('very roughly', 'something like'), that the Weyl curvature
vanishes at any INITIAL singularity -- reads the early state as one of low
gravitational entropy; the near-FLRW early universe used here is the weaker
claim.  No agreed measure of gravitational entropy exists, and whether
clumping raises it depends on the measure and regime: normalised Weyl ratios
and the Clifton-Ellis-Tavakol measure rise in the linear growing mode, while
plain C^2 ~ a^-4 falls there.  On such a measure structure formation reads as
a relaxation, running inside an expansion that is not one.

    SO THE PHRASE SPLITS CLEANLY ACROSS ITS OWN TWO NOUNS.  "Structural
    relaxation" belongs to the REARRANGEMENT.  "Amidst" is doing the work, and
    what it is amidst is not relaxing.

===============================================================================
5. "SELF-DEFENDING" IS EXACT, AND IT IS THE CONTRACTED BIANCHI IDENTITY
===============================================================================

This is the part of the claim that is not merely defensible but precise.

        grad_mu G^mu-nu  ==  0

is an IDENTITY.  It holds for the Levi-Civita (torsion-free, metric-compatible)
curvature of every metric smooth enough for grad G to exist (C^3 suffices),
with no field equation assumed and nothing to satisfy.  It is the
twice-contracted DIFFERENTIAL Bianchi identity (Carroll gr-qc/9712019 eqs.
3.88-3.96), not a consequence of the algebraic Riemann symmetries alone: a
tensor with all of them can carry div G != 0, and torsion or non-metricity
break it.  Couple it to Einstein's equation and it FORCES

        grad_mu T^mu-nu = 0.

A source that violates conservation can be written down, but G = 8 pi G T then
has no solution: on every solution T is 'automatically conserved' (Carroll
p.117) -- locally and covariantly, not as an integral energy law.  THAT IS A
CLOSED INDEX DEFENDING ITSELF, and it is not a figure of speech.

COMPUTED HERE.  The two Friedmann equations are integrated -- the constraint
for rho, the acceleration equation for a -- AND CONTINUITY IS NEVER IMPOSED.
It holds anyway, at 1e-16, for radiation, dust, vacuum and a w = -2/3 fluid,
at k = 0, +1/4 and -1/4.  And the residual DOES NOT FALL WITH STEP SIZE: it is
flat from 500 steps to 8,000.  That flatness holds by construction: the
residual vanishes as an algebraic function of each phase-space point (a, adot),
so the trajectory never enters it.  It is what the identity predicts; it
cannot by itself tell an identity from truncation error.

===============================================================================
6. THE CLOSED INDEX DOES CONSTRAIN A QUANTITY -- AND IT IS THE SAME ONE AGAIN
===============================================================================

Gauss's law on a closed manifold: the integral of a divergence over a manifold
with no boundary is zero, so

        IN A SPATIALLY CLOSED UNIVERSE THE TOTAL ELECTRIC CHARGE IS EXACTLY
        ZERO.  Not approximately -- FORCED, by topology, given two hypotheses:
        the Maxwell Gauss constraint of a massless photon, and an untwisted
        bundle (no charge-conjugation holonomy).

The first is itself observational: m_gamma is bounded, not shown zero, and
under a Proca mass a uniform net charge on T^3 is an exact solution; a
C-twisted bundle carries net charge too.  On those hypotheses that is M's
principle as a theorem, with no defect possible, exactly as stated.  ADM
energy is not defined there (pair.py: no spatial infinity); whether the total
energy is 'undefined' or zero is a contested convention, since ADT/Killing
charges, the on-shell Hamiltonian and pseudotensors give zero.  pair.py now
COMPUTES that split: CLOSED_UNIVERSE_ADM_ENERGY = UNDEFINED,
CLOSED_UNIVERSE_HAMILTONIAN_ENERGY = 0.0 on shell (its named prescription
H_HAM), so CLOSED_UNIVERSE_TOTAL_ENERGY = CONTESTED.  The contrast with
charge is therefore a contrast with the ADM energy only: for expanding closed
FRW there is no timelike Killing field, but on pair.py's Hamiltonian
prescription the constraint forces the total to zero much as Gauss forces the
charge, and on a static closed background the perturbative conserved energy
is forced to zero by topology too (Deser-Brill 1973).  (CORRECTED, DOCKET 67
follow-up: this read "The contrast with charge holds for expanding closed
FRW", written before pair.py computed the Hamiltonian total.)  Baryon number is not
forced, given no gauged U(1) acting on B or B-L with a massless untwisted
boson (in the SM U(1)_B is anomalous and cannot be gauged); and the SM does
not conserve B at all, only B-L.  Topology does not fix B's value; it
quantises it (an integer degree in the Skyrme realisation) and locks its
anomalous changes to Chern-Simons winding, Delta B = 3 Delta N_CS.

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

    GIVEN CONSERVED T^mu-nu -- an additional hypothesis in unimodular
    gravity (2603.14718 p.2), automatic for matter from a diffeomorphism-
    invariant action -- IT IS CLASSICALLY EQUIVALENT TO GENERAL RELATIVITY.
    Same classical field equations, so no classical observation
    distinguishes them.  What changes is what Lambda IS: an INTEGRATION
    CONSTANT rather than a Lagrangian parameter.  Without conservation
    Lambda may vary, and the theories are recorded as differing at the
    quantum and perturbative levels (Bufalo et al. 2015, Fabris et al.
    2023, as restated there).

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

===============================================================================
CORRECTED (DOCKET 67)
===============================================================================

Wording only; no verdict, flag or computed number moved.  As first written
this file said: theta was 'Measured, Planck 2018' (H_0 is a base-LCDM
inference); the comoving coordinate does not change and the count is
conserved, with no peculiar-motion or conserved-species hypothesis; the
ratio was 'Measured, from the CMB temperature alone' and 'independently of
any model of a(t)' (z_* is a base-LCDM derived parameter, and the check
returns 1 + z for any T_0); the first-law check was 'measured to machine
precision' and the expansion 'ISENTROPIC' unqualified; Penrose's conjecture
was printed as fact and 'clumping raises it' with no measure; w = -2/3 was
called 'curvature-like' (curvature is w = -1/3; -2/3 is wall-like); Bianchi
held 'for every metric, differentiable ... from the symmetries of the Riemann
tensor alone' and 'You cannot write down a source that violates
conservation'; 'The flatness is the evidence'; total charge zero 'not by
observation' with m_gamma = 0 and the untwisted bundle unnamed; 'no
counterpart for energy' and 'total energy not even defined'; baryon number
had 'no topological constraint'; unimodular gravity was equivalent with 'no
observation distinguishes them' and no conservation clause; 'Measured, not
asserted' stood on a tautology; and the 'Hubble time cross-check' is an
identity for every H_0.  Several checks below compare a DECLARED constant
with itself (comoving_coordinate_moves, BIANCHI_IS_AN_IDENTITY,
total_charge_forced_zero, RELAXATION_BELONGS_TO, the unimodular constants);
they are labelled so.
"""
import math
import sys

import cosmo                        # H_0 is PINNED there; never re-typed here

T_CMB = 2.7255                     # K, Fixsen 2009
Z_REC = 1089.92                    # Planck 2018 Table 2 z_* (last scattering),
                                   # +- 0.25; a base-LCDM DERIVED parameter,
                                   # 'total systematic ... around 0.5 sigma'
                                   # (Table 1 caption).  Named REC by
                                   # convention; x_e = 0.5 falls at z ~ 1275.
RUBIK_FACES, RUBIK_PER_FACE = 6, 9


# --------------------------------------------- 1: the expansion scalar

def hubble_si():
    """Planck 2018 (base-LCDM inferred), taken from cosmo.py, not re-typed."""
    return cosmo.H0()


def expansion_scalar():
    """theta = grad_mu u^mu = 3H for the comoving FLRW congruence, on the
    homogeneity scale.  Invariant."""
    return 3.0 * hubble_si()


def theta_over_H():
    """Three, exactly, for isotropic expansion in three spatial dimensions
    (anisotropic: theta = H1 + H2 + H3).  The whole content."""
    return expansion_scalar() / hubble_si()


def permutation_expansion_scalar():
    """A measure-preserving rearrangement has theta = 0.  Exactly.  DECLARED:
    that a permutation of a closed index is such a flow is this file's own
    modelling step, returned as a constant."""
    return 0.0


def is_a_permutation(theta):
    return theta == permutation_expansion_scalar()


# ------------------------------------- 2: the comoving index is closed

def comoving_number(n0, a, a0=1.0):
    """n a^3 = const for a species with a conserved number current.  The
    COUNT is conserved -- the cube's own law."""
    return n0 * (a0 / a) ** 3


def count_is_conserved(n0=1.0, a_values=(0.5, 1.0, 2.0, 10.0)):
    """n(a) a^3 is the same number at every a.  An identity check, not a
    measurement: comoving_number is defined as n0 (a0/a)^3, so the product is
    n0 a0^3 identically and the spread is float rounding.  (As first written:
    'Measured, not asserted'.)"""
    vals = [comoving_number(n0, a) * a ** 3 for a in a_values]
    return max(vals) - min(vals)


def comoving_coordinate_moves():
    """It does not, for a free body with no peculiar motion.  DECLARED, not
    computed.  All of the change is in a(t)."""
    return False


# ----------------------------- 3: the ratio no relabelling can change

def scale_ratio_since(z=Z_REC):
    """(cosmic scale)/(atomic scale) grew by a factor 1+z.  Atoms carry no a."""
    return 1.0 + z


def temperature_at(z=Z_REC, T0=T_CMB):
    return T0 * (1.0 + z)


def ratio_from_temperature(z=Z_REC, T0=T_CMB):
    """Identically 1 + z for every T0: temperature_at computes T_rec as
    T0 (1 + z), so this returns its input.  T scales as 1/a is assumed
    (free-streaming FLRW photons, no injection), and Z_REC is a base-LCDM
    derived parameter.  (As first written: 'Measured independently of any
    model of a(t)'.)"""
    return temperature_at(z, T0) / T0


def bohr_radius_contains_a():
    """hbar, m_e, e.  None of them is a function of the scale factor --
    the named hypothesis that hbar, m_e and alpha are constant since z_*.
    DECLARED, not computed."""
    return False


# ------------------------------------- 4: the expansion is isentropic

def rho_of_a(a, w, rho0=1.0, a0=1.0):
    """rho a^{3(1+w)} = const, the solution of the continuity equation."""
    return rho0 * (a0 / a) ** (3.0 * (1.0 + w))


def first_law_residual(a, w, h=1e-6):
    """d(rho a^3) + p d(a^3), which is T dS given a Gibbs relation in local
    equilibrium with mu dN = 0.  Zero for a perfect fluid."""
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


RELAXATION_BELONGS_TO = "the rearrangement"   # DECLARED literal, on Penrose's
                                              # conjecture and a chosen measure
EXPANSION_DISSIPATES = False   # perfect fluid in equilibrium, as modelled here


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


BIANCHI_IS_AN_IDENTITY = True      # DECLARED: Levi-Civita curvature of a C^3
                                   # metric, no field equation; not computed


# --------------------- 6: what a closed index actually constrains

def total_charge_forced_zero(closed):
    """Gauss on a manifold with no boundary: the integral of a divergence
    vanishes, so the total charge is exactly zero -- for a massless photon on
    an untwisted bundle.  DECLARED: returns bool(closed); the theorem is not
    computed here, and the checks that read it check this constant."""
    return bool(closed)


CONSTRAINED_BY_CLOSURE = (
    ("electric charge", True,
     "Gauss on a boundaryless manifold (m_gamma = 0, untwisted): exactly zero"),
    ("ADM energy", False, "not defined there at all -- pair.py (the TOTAL "
     "energy is CONTESTED there: Hamiltonian 0 on shell, pair.py)"),
    ("baryon number", False,
     "not forced (no massless gauged U(1) on B or B-L); topology quantises B"),
)


def closure_constrains(name):
    return dict((n, c) for n, c, _w in CONSTRAINED_BY_CLOSURE)[name]


ARRIVALS_AT_THE_SPLIT = ("pair.py: Wheeler's charge without charge",
                         "dichotomy.py: Weyl against Ricci",
                         "permute.py: Gauss on a closed manifold")


# ------------------------------------------ 7: unimodular gravity

UNIMODULAR_STATUS = "CLASSICALLY EQUIVALENT"
UNIMODULAR_BUYS = "Lambda becomes an integration constant, not a parameter"
UNIMODULAR_SOLVES_CC_PROBLEM = False   # the tree's reading of a divided
# literature: Smolin 2009 addresses the vacuum-energy problem while the value
# of Lambda stays a free constant -- 'reframes rather than removes' is the
# fuller statement.  Equivalence and the integration-constant status assume
# conserved T.  Declared constants; not derived here.


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
    near("Hubble time it implies, Gyr (unit identity, any H_0)",
         1.0 / hubble_si() / (1e9 * 365.25 * 86400.0), cosmo.hubble_time_gyr(),
         1e-6)
    near("theta / H is three exactly -- one per spatial direction",
         theta_over_H(), 3.0, 1e-15)
    print("       theta = %.4e /s" % th)
    chk("theta of a measure-preserving rearrangement (declared)",
        permutation_expansion_scalar(), 0.0)
    chk("is the universe a permutation of a closed index",
        is_a_permutation(th), False)
    print("       ONE SCALAR, AND IT IS INVARIANT.  That is the falsification,")
    print("       and it is the only one in this file.")

    print("\n2. BUT THE COMOVING PICTURE IS THE CLOSED INDEX, AND IT IS STANDARD")
    chk("comoving coordinate changes, no peculiar motion (declared)",
        comoving_coordinate_moves(), False)
    near("spread in n a^3 across a factor of 20 in a", count_is_conserved(), 0.0)
    print("       AN IDENTITY OF THE DEFINITION: for a conserved species the COUNT")
    print("       is conserved exactly -- the cube's own law.  All the change sits")
    print("       in a(t).")

    print("\n3. WHAT NO RELABELLING CAN UNDO: A DIMENSIONLESS RATIO")
    chk("does the Bohr radius contain the scale factor",
        bohr_radius_contains_a(), False)
    print("       T_rec = %.1f K against T_0 = %.4f K" % (temperature_at(), T_CMB))
    near("T_rec/T_0 (T_rec computed as T_0(1+z): an identity)",
         ratio_from_temperature(),
         scale_ratio_since())
    near("and that is 1 + z", scale_ratio_since(), 1.0 + Z_REC)
    print("       A DIMENSIONLESS RATIO CHANGED BY A FACTOR OF 1,091 (z_* derived")
    print("       under base-LCDM).  A permutation has no")
    print("       units to hide in and cannot move one.")

    print("\n4. THE PERFECT-FLUID EXPANSION IS ISENTROPIC -- 'RELAXATION' IS THE")
    print("   WRONG TERM (identity check of the continuity solution)")
    for w, name in ((1.0 / 3.0, "radiation"), (0.0, "dust"), (-1.0, "vacuum"),
                    (-2.0 / 3.0, "w=-2/3 (wall)")):
        chk("  d(rho a^3) + p d(a^3) = 0 for %s" % name, is_isentropic(w), True)
    chk("does the expansion dissipate", EXPANSION_DISSIPATES, False)
    chk("so 'structural relaxation' belongs to (declared)",
        RELAXATION_BELONGS_TO,
        "the rearrangement")
    print("       On Penrose's Weyl curvature conjecture and a measure on which")
    print("       clumping raises gravitational entropy, clumping reads as a")
    print("       relaxation -- running inside an expansion that is not one.")
    print("       The phrase splits on its own nouns.")

    print("\n5. 'SELF-DEFENDING' IS THE CONTRACTED BIANCHI IDENTITY, MEASURED")
    print("     continuity is NEVER imposed; only the constraint and the")
    print("     acceleration equation are used.  It holds anyway:")
    for w, name in ((1.0 / 3.0, "radiation"), (0.0, "dust"), (-1.0, "vacuum"),
                    (-2.0 / 3.0, "w=-2/3 (wall)")):
        for k in (0.0, 0.25, -0.25):
            r = worst_continuity_residual(w, k)
            good = r < 1e-13
            ok &= good
            print("       w=%+.4f %-15s k=%+.2f   residual %.3e  %s"
                  % (w, name, k, r, "ok" if good else "FAIL"))
    print("     and it does NOT fall with step size -- by construction, since the")
    print("     residual vanishes pointwise in (a, adot):")
    for n in (500, 2000, 8000):
        print("       steps = %5d   residual = %.3e"
              % (n, worst_continuity_residual(1.0 / 3.0, 0.25, steps=n)))
    chk("residual is step-size independent (pointwise, by construction)",
        residual_is_step_independent(), True)
    chk("Bianchi (Levi-Civita, C^3) an identity (declared constant)",
        BIANCHI_IS_AN_IDENTITY, True)

    print("\n6. AND A CLOSED INDEX DOES CONSTRAIN ONE QUANTITY EXACTLY")
    for name, c, why in CONSTRAINED_BY_CLOSURE:
        print("     %-18s %-12s %s" % (name, "FORCED" if c else "not forced", why))
    print("     (the baryon row is asserted data; only charge and ADM are checked)")
    chk("closed universe forces total charge to zero (declared)",
        total_charge_forced_zero(True), True)
    chk("an open one does not", total_charge_forced_zero(False), False)
    chk("closure constrains electric charge", closure_constrains("electric charge"), True)
    chk("closure constrains ADM energy", closure_constrains("ADM energy"), False)
    import pair
    chk("  pair.py: ADM UNDEFINED, Hamiltonian 0, total CONTESTED (computed there)",
        (pair.CLOSED_UNIVERSE_ADM_ENERGY, pair.CLOSED_UNIVERSE_HAMILTONIAN_ENERGY,
         pair.CLOSED_UNIVERSE_TOTAL_ENERGY), ("UNDEFINED", 0.0, "CONTESTED"))
    chk("independent arrivals at the sign-blind split",
        len(ARRIVALS_AT_THE_SPLIT), 3)
    for a in ARRIVALS_AT_THE_SPLIT:
        print("       %s" % a)

    print("\n7. AND THE FORMALISATION EXISTS: UNIMODULAR GRAVITY")
    # declared constants compared with themselves; no derivation runs here
    chk("status against GR (declared; assumes conserved T)", UNIMODULAR_STATUS,
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
         "comoving coordinates fixed absent peculiar motion; n a^3 conserved"
         " for a conserved species"),
        ("the expansion is a permutation", "FALSIFIED",
         "theta = 3H_0 = %.3e /s on the large-scale comoving flow, invariant,"
         " and a measure-preserving flow has 0" % expansion_scalar()),
        ("it is a structural relaxation", "SPLIT",
         "the perfect-fluid expansion is isentropic; the REARRANGEMENT relaxes"
         " (declared, on Penrose's conjecture)"),
        ("self-referencing, self-defending", "EXACT",
         "the contracted Bianchi identity (Levi-Civita); continuity holds"
         " pointwise at 1e-16"),
        ("no defect possible in a closed index", "TRUE FOR CHARGE",
         "Gauss on a boundaryless manifold (m_gamma = 0, untwisted) forces"
         " total Q = 0"),
    )
    print("  %-34s %-16s %s" % ("claim", "verdict", "why"))
    for c, v, w in rows:
        print("  %-34s %-16s %s" % (c, v, w))
    print("\n" + "=" * 79)
    print("""VERDICT

  FOUR CLAIMS, AND ONLY ONE FAILS.  A permutation of a closed index is
  measure-preserving, so its expansion scalar is exactly zero -- and
  theta = grad_mu u^mu is a coordinate-invariant scalar, inferred under
  base-LCDM at 3 H_0 = 6.549e-18 per second on the large-scale comoving
  flow.  No relabelling moves it.  THE EXPANSION IS NOT A PERMUTATION,
  and that is the one falsification here.

  EVERYTHING ELSE ABOUT THE INDEX IS RIGHT, AND IT IS THE TEXTBOOK.
  Absent peculiar motion, a galaxy's comoving coordinate does not
  change.  Nothing expands into anything; there is no embedding space
  and none is wanted.  The count of a conserved species is conserved
  exactly, n a^3 = const -- which is the cube's own
  conservation law and not an analogy for it.  All of the change sits
  in one function.

  WHAT CANNOT BE ABSORBED IS A DIMENSIONLESS RATIO.  The Bohr radius is
  set by hbar, m_e and e, none of which contains a (given constant
  hbar, m_e and alpha); atoms do not expand.  So (cosmic scale)/(atomic
  scale) is a pure number, and it changed by a factor of 1,090.92 since
  recombination -- 1 + z_*, Planck's base-LCDM derived last-scattering
  redshift, with T scaling as 1/a.  A permutation has no units to hide
  in and cannot move a pure number.  THAT IS THE CONTENT OF THE WORD EXPANSION.

  'RELAXATION' IS THE RIGHT WORD FOR THE WRONG TERM.  For a perfect
  fluid in local equilibrium the FLRW expansion is isentropic:
  d(rho a^3) = -p d(a^3) exactly, no dissipation, nothing relaxing.
  But on Penrose's Weyl curvature hypothesis -- a hedged conjecture
  about the initial singularity -- and on a measure under which
  clumping raises gravitational entropy (normalised Weyl ratios, the
  CET measure in the linear growing mode; plain C^2 falls there),
  STRUCTURE FORMATION reads as a relaxation -- running inside an
  expansion that is not one.  The phrase splits across its own two
  nouns, and 'amidst' is doing the work.

  AND 'SELF-DEFENDING' IS NOT A FIGURE OF SPEECH -- IT IS THE
  CONTRACTED BIANCHI IDENTITY.  grad_mu G^mu-nu == 0 holds for the
  Levi-Civita curvature of every C^3 metric with no field equation
  assumed, and coupling it to Einstein's equation FORCES local
  conservation of the source: a T that violates it has no solution.
  Computed: integrate the two Friedmann equations and never impose
  continuity, and continuity holds at 1e-16 for four fluids at three
  curvatures, and the residual does not fall with step size -- because
  it vanishes pointwise in (a, adot), which is the identity at work and
  holds by construction.

  THE CLOSED INDEX ALSO CONSTRAINS EXACTLY ONE QUANTITY, AND IT IS THE
  SAME ONE AGAIN.  Gauss's law on a manifold with no boundary forces
  TOTAL ELECTRIC CHARGE TO BE EXACTLY ZERO in a spatially closed
  universe -- forced by topology, given a massless photon and an
  untwisted bundle.  ADM energy is not defined there; the TOTAL energy
  is CONTESTED (pair.py computes it: ADM UNDEFINED, the closed-FRW
  Hamiltonian 0 on shell under its named prescription), and on a static
  closed background Deser-Brill forces the Killing energy to zero too.
  (CORRECTED, DOCKET 67 follow-up: this read "for expanding closed FRW
  there is no energy counterpart".)
  Baryon number is not forced, absent a massless gauged U(1) on B or
  B-L.  Third independent arrival at the split:
  A SIGN-BLIND QUANTITY IS WHAT A CLOSED INDEX CAN CONSTRAIN.

  AND THE PICTURE HAS A REAL FORMULATION.  Unimodular gravity fixes
  det g and varies only the volume-preserving part -- a literally
  closed index -- and, given conserved T, it is CLASSICALLY EQUIVALENT
  to general relativity.  Lambda becomes an integration constant rather
  than a Lagrangian parameter.  That reframes the cosmological constant
  problem; it does not solve it, and no classical observation separates
  the two theories while T is conserved.

  SCORING THE CUBE THE WAY unified.py SCORED EIGHT: the cube conserves
  the COUNT and the SCALE; the universe conserves the COUNT and not the
  scale.  EXACT ON ONE AXIS, ABSENT ON THE OTHER -- and the scale is
  the axis we observe.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
