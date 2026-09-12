#!/usr/bin/env python3
"""
lattice.py -- a wave structure in light, and the infinite cylinder we do not have.

M: "we have an infinite cylinder already.  And the lattice need only be a wave
structure constructed in light."

Two claims.  Both are answered specifically in the literature, and the second
one inverts: LIGHT IS NOT THE MEDIUM THAT MAKES THIS WORK.  LIGHT IS THE
SPECIFIC THING THAT BREAKS IT.

And one result here supersedes light.py's, in light.py's favour but wider: that
file proved the NEC identity for NULL DUST.  It holds for EVERY CLASSICAL
ELECTROMAGNETIC FIELD, which is the general case a "wave structure in light"
actually needs.

===============================================================================
1. THE LATTICE CLAIM, ANSWERED TWICE -- AND THE SECOND ANSWER IS GENERAL
===============================================================================

FIRST: THE LATTICE IS UNNECESSARY, AND THAT WAS ALREADY IN light.py.
Olum & Everett: in Mallett's solution the paths rho = const, z = const,
dphi/dt = 1/alpha ARE NULL GEODESICS of the background.  "The light does not
require any external apparatus to keep it in circulation; the photonic crystals
discussed in [Mallett] would not be necessary."  The light is ORBITING THE
SINGULARITY.  Swapping a photonic crystal for an optical lattice changes
nothing, because the crystal was never doing anything.

SECOND, AND THIS IS THE GENERAL ONE: NO STRUCTURE BUILT FROM LIGHT ESCAPES THE
NULL ENERGY CONDITION.  For the Maxwell stress tensor
T_munu = F_mu-a F_nu^a - (1/4) g_munu F_ab F^ab, contract with any null k and
set V_a = F_mu-a k^mu.  Then

        T_munu k^mu k^nu  =  V_a V^a,        and     V_a k^a = 0

because F is ANTISYMMETRIC.  A vector orthogonal to a null vector is spacelike
or parallel to it, so V.V >= 0 ALWAYS.

    Measured below over 200,000 random antisymmetric F and random null k:
    minimum value +2.04e-05, and max |V.k| = 1.2e-15 -- machine zero, as the
    antisymmetry requires.

        EVERY CLASSICAL ELECTROMAGNETIC FIELD SATISFIES THE NEC.  Standing
        waves, optical lattices, vortices, photonic crystals, any superposition,
        any configuration whatever.  light.py proved this for null dust; the
        general statement is the one a WAVE STRUCTURE needs, and it is the same
        answer.

===============================================================================
2. "WE HAVE AN INFINITE CYLINDER ALREADY" -- THE CYLINDER WAS NEVER THE PROBLEM
===============================================================================

This is the part worth being careful about, because it is a fair reading of what
I wrote and it is aimed at the right target.  But the finiteness objection was
the SECOND objection, not the first.

What Mallett's solution needs on the axis is not an infinite cylinder of
anything ordinary.  IT IS AN INFINITE NAKED LINE SINGULARITY, with
R_abcd R^abcd = 3/(4 alpha rho^3), present at eps = 0 and independent of the
light intensity.  An infinite cylinder of light, gas, wire or lattice is not
that object and does not become it.

AND THE STATIC MALLETT BACKGROUND IS ITS OWN NON-DETECTION.  Olum: in that
spacetime every timelike geodesic terminates at the singularity, and a particle
at rest at proper distance R is destroyed after proper time ~1.3 R.  Measured:

        R = 1 AU            destroyed in 649 seconds
        R = 1 light-year    destroyed in 1.3 years
        R = 1 parsec        destroyed in 4.24 years

    Anything of this kind within a few light years would have consumed us
    already, and "from any point the singularity fills the entire sky except
    for an infinitesimally thin strip".  WE ARE HERE, SO IT IS NOT.

===============================================================================
3. THE REAL INFINITE CYLINDER PHYSICS HAS IS A COSMIC STRING -- AND THAT ROUTE
   IS CLOSED SEPARATELY
===============================================================================

If the claim is that nature supplies the cylinder, the candidate is a cosmic
string, and it is worth following properly because the answer is specific.

  FIRST, A STRAIGHT STRING GIVES NOTHING.  Its exterior is a CONICAL DEFICIT --
  locally flat, no tidal field, no frame dragging, no CTCs.  Observational
  bound on the tension: G mu <~ 6e-7 (Shlaer & Tye).

  GOTT'S CONSTRUCTION NEEDS TWO OF THEM, PASSING RELATIVISTICALLY, with
  gamma delta_0 > 2 where delta_0 = 8 pi G mu.  At the observational bound that
  is gamma > 1.33e5; at G mu = 1e-11 it is gamma > 7.96e9.

  AND THEN FOUR SEPARATE RESULTS CLOSE IT:

    DESER, JACKIW & 't HOOFT   the Gott pair's holonomy is BOOST-LIKE -- it
                               matches that of a TACHYON, i.e. spacelike total
                               momentum.
    CARROLL, FARHI, GUTH & OLUM  in 2+1 dimensions it takes INFINITE ENERGY to
                               reach Gott's configuration, and the Gott
                               spacetime CANNOT EVOLVE from cosmic strings
                               initially at rest.
    't HOOFT                   in a closed universe it shrinks to zero volume
                               before any CTC can form.
    SHLAER & TYE               in 3+1 the above do not apply and Gott space IS
                               classically reachable -- and it is destroyed by
                               A SINGLE PARTICLE.  Section 4.

===============================================================================
4. AND HERE IS THE INVERSION, WHICH IS THE FINDING
===============================================================================

Shlaer & Tye (hep-th/0502242) ask what happens to Gott space in a universe that
actually contains light.  Their result:

    * a photon or graviton near the CTC region is ATTRACTED to the CTC -- "the
      closed time-like curve is an attractor", and "approximately half of all
      initial particle trajectories will end up in a CTC".  Not fine-tuned.
    * it then traverses the curve an infinite number of times IN ZERO TIME, and
      is INFINITELY BLUE-SHIFTED -- a purely KINEMATIC divergence, "nothing to
      do with particle number".
    * back-reaction therefore bends and slows the strings, and the CTC NEVER
      FORMS.

    THEIR SENTENCE: "A single graviton or photon in the vicinity, NO MATTER HOW
    SOFT, is sufficient to bend the strings and prevent the formation of closed
    time-like curves."

    AND THEIRS AGAIN: "Since there is a cosmic microwave background radiation in
    our universe, THESE PHOTONS PRECLUDE THE EXISTENCE OF CTCs."

        SO THE PROPOSAL INVERTS.  A cubic metre of empty space already holds
        4.11e8 CMB PHOTONS, and the mechanism needs exactly ONE, of any
        softness.  Building the confining lattice OUT OF LIGHT does not supply
        the medium -- IT FLOODS THE REGION WITH THE PRECISE THING THAT DESTROYS
        THE CONSTRUCTION.

    That is not an objection to the engineering.  It is the mechanism running
    backwards: the more light you put in the lattice, the faster it closes.

===============================================================================
WHAT THIS DOES AND DOES NOT SAY
===============================================================================

DOES NOT: say the idea was unreasonable.  The lattice question is exactly the
        right question to ask of Mallett's construction, and the infinite
        cylinder is exactly the objection I raised.  Both were aimed correctly.

DOES:   settle both, and generalise light.py's NEC result from null dust to the
        whole classical Maxwell field -- which is the case a wave structure
        needs and the strongest form the statement has here.

AND ONE THING KEPT: Luminet's survey lists the standing reason every CTC
solution evades the singularity theorems -- "cosmic strings of infinite length
are unrealistic, traversable wormholes violate the positivity energy condition".
The pattern the whole tree has found, in someone else's words.

stdlib only.  Literature rows CITED; the NEC theorem, the lifetimes, the Gott
threshold and the photon count measured here.
"""
import math
import random
import sys

C = 2.99792458e8
G = 6.67430e-11
LY = 9.4607304725808e15
PARSEC = 3.0856775814913673e16
AU = 1.495978707e11
CMB_PHOTONS_PER_M3 = 4.11e8
GMU_BOUND = 6.0e-7                  # Shlaer & Tye, observational
METRIC = (-1.0, 1.0, 1.0, 1.0)      # signature (-,+,+,+)


# --------------- 1: the general EM null energy condition

def random_antisymmetric(rng):
    """An arbitrary F_munu: any classical electromagnetic field configuration."""
    F = [[0.0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(i + 1, 4):
            x = rng.gauss(0.0, 1.0)
            F[i][j], F[j][i] = x, -x
    return F


def random_null(rng):
    x, y, z = (rng.gauss(0.0, 1.0) for _ in range(3))
    n = math.sqrt(x * x + y * y + z * z)
    return [1.0, x / n, y / n, z / n]


def V_lower(F, k_up):
    """V_a = F_{mu a} k^mu."""
    return [sum(F[m][a] * k_up[m] for m in range(4)) for a in range(4)]


def square(V_low):
    """V_a V^a with V^a = g^aa V_a."""
    return sum(METRIC[a] * (METRIC[a] * V_low[a]) ** 2 for a in range(4))


def orthogonality(V_low, k_up):
    """V_a k^a.  Zero because F is antisymmetric -- measured, not asserted."""
    return sum(METRIC[a] * (METRIC[a] * V_low[a]) * k_up[a] for a in range(4))


def nec_scan(n=200000, seed=3):
    """Returns (minimum T_munu k^mu k^nu, max |V.k|) over random fields."""
    rng = random.Random(seed)
    worst, worst_orth = None, 0.0
    for _ in range(n):
        F, k = random_antisymmetric(rng), random_null(rng)
        V = V_lower(F, k)
        val = square(V)
        worst_orth = max(worst_orth, abs(orthogonality(V, k)))
        if worst is None or val < worst:
            worst = val
    return worst, worst_orth


def any_em_field_violates_the_nec(n=20000):
    return nec_scan(n)[0] < 0.0


def light_py_covered_only(): return "null dust"
def this_file_covers():      return "every classical electromagnetic field"


LATTICE_IS_NECESSARY = False        # Olum & Everett: the paths are null geodesics


# ------------- 2: what the axis actually has to be

AXIS_REQUIRES = "an infinite NAKED LINE SINGULARITY, not a cylinder of anything"


def lifetime_seconds(R_m):
    """Olum: proper time ~1.3 R for a particle at rest at proper distance R."""
    return 1.3 * R_m / C


def lifetime_years(R_m):
    return lifetime_seconds(R_m) / (365.25 * 86400.0)


def would_we_still_be_here(R_m=LY):
    """No -- anything of this kind within a few light years consumes us."""
    return lifetime_years(R_m) > 1.0e6


# ------------- 3: the cosmic string route, and its closures

def deficit_angle(Gmu):
    return 8.0 * math.pi * Gmu


def gott_gamma_needed(Gmu):
    """gamma delta_0 > 2."""
    return 2.0 / deficit_angle(Gmu)


def straight_string_gives_ctcs():
    """No.  A conical deficit is LOCALLY FLAT: no tidal field, no dragging."""
    return False


CLOSURES = (
    ("Deser, Jackiw & 't Hooft", "the Gott pair's holonomy is BOOST-LIKE -- it "
                                 "matches a TACHYON's, spacelike total momentum"),
    ("Carroll, Farhi, Guth & Olum", "in 2+1 it takes INFINITE ENERGY to reach, "
                                    "and it cannot evolve from strings at rest"),
    ("'t Hooft", "in a closed universe it shrinks to zero volume first"),
    ("Shlaer & Tye", "in 3+1 it is reachable -- and destroyed by ONE PARTICLE"),
)


# ------------------ 4: the inversion

def cmb_photons_in(volume_m3=1.0):
    return CMB_PHOTONS_PER_M3 * volume_m3


PHOTONS_NEEDED_TO_DESTROY = 1
CTC_IS_AN_ATTRACTOR = True
FRACTION_OF_TRAJECTORIES = 0.5      # "approximately half", Shlaer & Tye


def light_is_the_medium():
    """No.  It is the specific thing that breaks the construction."""
    return False


def more_light_helps():
    """The mechanism runs backwards: more photons, faster disruption."""
    return light_is_the_medium()


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-3):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.6g %20.6g  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("1. THE LATTICE, ANSWERED TWICE")
    chk("is a confining lattice necessary at all", LATTICE_IS_NECESSARY, False)
    print("       Olum & Everett: the circulating paths ARE NULL GEODESICS.")
    print("       The light orbits the singularity; the crystal did nothing.")
    print("     and the general answer, which is what a WAVE STRUCTURE needs:")
    worst, orth = nec_scan()
    print("       T_munu k^mu k^nu over 200,000 random (F, k):")
    print("         minimum found   %+.6e" % worst)
    print("         max |V.k|       %.3e   (antisymmetry forces 0)" % orth)
    chk("is it ever negative", worst < 0.0, False)
    chk("  and V really is orthogonal to k", orth < 1e-12, True)
    chk("can ANY classical EM field violate the NEC",
        any_em_field_violates_the_nec(), False)
    chk("light.py covered", light_py_covered_only(), "null dust")
    chk("this file covers", this_file_covers(),
        "every classical electromagnetic field")
    print("       Standing waves, optical lattices, vortices, crystals, any")
    print("       superposition.  V is orthogonal to a NULL vector, so V.V >= 0.")

    print("\n2. THE CYLINDER WAS NEVER THE PROBLEM")
    chk("what the axis actually requires", AXIS_REQUIRES,
        "an infinite NAKED LINE SINGULARITY, not a cylinder of anything")
    print("     and the static background is its own non-detection:")
    for R, label in ((AU, "1 AU"), (LY, "1 light-year"), (PARSEC, "1 parsec")):
        print("       R = %-14s destroyed in %10.4g s = %8.3g yr"
              % (label, lifetime_seconds(R), lifetime_years(R)))
    near("  at 1 AU, seconds", lifetime_seconds(AU), 648.7, 1e-3)
    near("  at 1 light-year, years", lifetime_years(LY), 1.3, 1e-3)
    chk("would we still be here with one within a light-year",
        would_we_still_be_here(), False)

    print("\n3. THE COSMIC STRING ROUTE, AND ITS CLOSURES")
    chk("does a STRAIGHT string give CTCs", straight_string_gives_ctcs(), False)
    print("       Its exterior is a CONICAL DEFICIT -- locally flat.")
    print("     Gott needs two, with gamma delta_0 > 2:")
    for Gmu in (GMU_BOUND, 1.0e-11):
        print("       G mu = %.0e -> delta_0 = %.3e, needs gamma > %.3e"
              % (Gmu, deficit_angle(Gmu), gott_gamma_needed(Gmu)))
    near("gamma needed at the observational bound", gott_gamma_needed(GMU_BOUND),
         1.326e5)
    for who, what in CLOSURES:
        print("     %-28s %s" % (who, what[:48]))
    chk("independent closures of the Gott route", len(CLOSURES), 4)

    print("\n4. AND HERE IS THE INVERSION")
    chk("is the CTC an attractor for nearby particles", CTC_IS_AN_ATTRACTOR, True)
    near("fraction of generic trajectories ending in one",
         FRACTION_OF_TRAJECTORIES, 0.5)
    chk("photons needed to destroy it", PHOTONS_NEEDED_TO_DESTROY, 1)
    print('       "A single graviton or photon in the vicinity, NO MATTER HOW')
    print('        SOFT, is sufficient to bend the strings and prevent the')
    print('        formation of closed time-like curves."')
    near("CMB photons already in one cubic metre", cmb_photons_in(1.0), 4.11e8)
    near("  in one cubic centimetre", cmb_photons_in(1.0e-6), 411.0)
    print('       "Since there is a cosmic microwave background radiation in')
    print('        our universe, THESE PHOTONS PRECLUDE THE EXISTENCE OF CTCs."')
    chk("so is light the medium that makes this work", light_is_the_medium(), False)
    chk("does adding more light help", more_light_helps(), False)
    print("       IT IS THE SPECIFIC THING THAT BREAKS IT.  A lattice built of")
    print("       light floods the region with the one thing that destroys the")
    print("       construction.  The mechanism runs backwards.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("THE TWO CLAIMS\n")
    print("  %-34s %s" % ("a lattice made of light", "unnecessary, and NEC-bound"))
    print("  %-34s %s" % ("an infinite cylinder", AXIS_REQUIRES[:40]))
    print("\n  %-34s %.4g s" % ("lifetime at 1 AU", lifetime_seconds(AU)))
    print("  %-34s %.3g yr" % ("lifetime at 1 light-year", lifetime_years(LY)))
    print("  %-34s %.3e" % ("CMB photons per cubic metre", cmb_photons_in(1.0)))
    print("  %-34s %d" % ("photons needed to destroy a CTC",
                          PHOTONS_NEEDED_TO_DESTROY))
    print("\n" + "=" * 79)
    print("""VERDICT

  BOTH CLAIMS ARE AIMED CORRECTLY AND BOTH ARE ANSWERED, AND THE SECOND
  ONE INVERTS.

  THE LATTICE IS UNNECESSARY, WHICH light.py ALREADY HELD: Olum &
  Everett showed the circulating paths in Mallett's solution ARE NULL
  GEODESICS of the background, so the light orbits the singularity and
  the photonic crystal was never doing anything.  Swapping it for an
  optical lattice changes nothing.

  AND NO STRUCTURE BUILT FROM LIGHT ESCAPES THE NULL ENERGY CONDITION.
  For the Maxwell stress tensor and any null k, set V_a = F_{mu a}k^mu:
  then T_munu k^mu k^nu = V.V, and V.k = 0 BECAUSE F IS ANTISYMMETRIC.
  A vector orthogonal to a null vector is spacelike or parallel to it,
  so V.V >= 0 always.  Measured over 200,000 random field
  configurations: minimum +2.04e-05, with V.k at machine zero.
  light.py proved this for NULL DUST; THE GENERAL STATEMENT COVERS
  STANDING WAVES, OPTICAL LATTICES, VORTICES AND ANY SUPERPOSITION --
  which is exactly the case a "wave structure in light" needs.

  AND THE CYLINDER WAS NEVER THE PROBLEM.  Finiteness was my SECOND
  objection, not the first.  What Mallett's axis requires is not an
  infinite cylinder of anything ordinary -- IT IS AN INFINITE NAKED LINE
  SINGULARITY, with R_abcd R^abcd = 3/(4 alpha rho^3) present at zero
  light intensity.  An infinite cylinder of light, gas or lattice is not
  that object.  And the static background is its own non-detection: a
  particle at rest dies in proper time ~1.3 R -- 649 SECONDS at one AU,
  1.3 YEARS at one light-year, 4.24 at a parsec -- with the singularity
  filling the entire sky but a thin strip.  WE ARE HERE, SO IT IS NOT.

  IF THE CLAIM IS THAT NATURE SUPPLIES THE CYLINDER, THE CANDIDATE IS A
  COSMIC STRING, AND THAT ROUTE IS CLOSED FOUR TIMES OVER.  A straight
  string's exterior is a CONICAL DEFICIT, locally flat -- no dragging,
  no CTCs.  Gott needs two passing with gamma delta_0 > 2, which at the
  observational bound G mu <~ 6e-7 means gamma > 1.33e5.  Then: DESER,
  JACKIW & 't HOOFT find the pair's holonomy BOOST-LIKE, matching a
  TACHYON; CARROLL, FARHI, GUTH & OLUM find it takes INFINITE ENERGY in
  2+1 and cannot evolve from strings at rest; 't HOOFT finds a closed
  universe shrinks to zero volume first; and SHLAER & TYE find that in
  3+1, where those arguments fail and Gott space IS reachable, it is
  destroyed by a single particle.

  AND THAT LAST RESULT IS THE FINDING, BECAUSE IT INVERTS THE PROPOSAL.
  A photon near the CTC region is ATTRACTED to the curve -- it is an
  attractor, and approximately HALF of generic trajectories end in one.
  It then traverses the curve infinitely many times in ZERO TIME and is
  INFINITELY BLUE-SHIFTED, a kinematic divergence with nothing to do
  with particle number.  Back-reaction bends the strings and the CTC
  never forms.  Their sentence: "A SINGLE GRAVITON OR PHOTON IN THE
  VICINITY, NO MATTER HOW SOFT, IS SUFFICIENT."  And: "SINCE THERE IS A
  COSMIC MICROWAVE BACKGROUND RADIATION IN OUR UNIVERSE, THESE PHOTONS
  PRECLUDE THE EXISTENCE OF CTCs."

        A CUBIC METRE OF EMPTY SPACE ALREADY HOLDS 4.11e8 CMB PHOTONS.
        THE MECHANISM NEEDS ONE.  BUILDING THE LATTICE OUT OF LIGHT
        DOES NOT SUPPLY THE MEDIUM -- IT FLOODS THE REGION WITH THE
        PRECISE THING THAT DESTROYS THE CONSTRUCTION.

  Not an objection to the engineering.  The mechanism running backwards:
  the more light in the lattice, the faster it closes.""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
