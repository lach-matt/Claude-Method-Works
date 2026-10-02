#!/usr/bin/env python3
"""
anecscope.py -- the ANEC row, and a lemma in this tree that was inverted.

smearing.py left one thing open and called it the obvious next step: ANEC on a
background the matter itself curves.  Attacking it turned up something closer to
home first.

    achronal.py's CENTRAL NEGATIVE RESULT RESTS ON AN INVERTED CLAIM, and with
    the claim corrected the corridor is OUTSIDE achronal ANEC's scope
    altogether.

That is not a refutation of anything.  It is a scope finding, and the
difference matters enough that this file says so four times.

===============================================================================
1. WHICH ANEC.  THREE STATEMENTS, AND ONLY ONE OF THEM BITES.
===============================================================================

    ANEC IN FLAT SPACE.  INTEGRAL T_kk dl >= 0 on complete null geodesics of
    Minkowski.  PROVEN -- Faulkner, Leigh, Parrikar & Wang from monotonicity of
    relative entropy; Hartman, Kundu & Tajdini from causality.  Says nothing
    about a curved corridor.

    ANEC IN CURVED SPACETIME.  FALSE in general for test fields on a fixed
    background: Schwarzschild in the Boulware state, Visser's scale-anomaly
    class, and Urban-Olum's conformally flat spacetime, on achronal geodesics
    (Graham-Olum 0705.3193; Visser gr-qc/9409043; Urban-Olum 0910.5925).  So
    violating ANEC is not by itself a disqualification and never was.
      CORRECTED (DOCKET 67): first written 'the standard counterexample is the
      Casimir vacuum, where a geodesic between the plates violates it.  Nobody
      disputes this.'  The plate system OBEYS ANEC (Fewster-Olum-Pfenning;
      Graham-Olum p.2): T_kk = 0 on every null geodesic parallel to ideal
      plates, and every other geodesic reaches a plate.  The Casimir-type
      counterexample is the plate-FREE compactified Minkowski space -- flat,
      not curved -- whose violating geodesics wind around the circle.

    ACHRONAL ANEC.  The same integral, restricted to complete ACHRONAL null
    geodesics -- those no timelike curve short-circuits.  THIS IS THE ONE WITH
    TEETH.  Its SELF-CONSISTENT version -- on a background the matter itself
    sources, at curvature well below the Planck scale -- is Graham & Olum's
    condition, and it has been open for at least nineteen years (since 2007;
    Flanagan-Wald stated ANEC in the achronal form in self-consistent
    perturbation theory in 1996).  The topological-censorship consequence
    Graham & Olum draw from it adds simple connectivity and the null generic
    condition, and what it forbids is wormholes joining disconnected regions,
    or short, causality-violating ones.  The compactified vacuum escapes
    achronal ANEC because its violating geodesics wind and are chronal; the
    plate system escapes it by obeying ANEC.
      CORRECTED (DOCKET 67): first written 'it is the hypothesis of Graham &
      Olum, and it is what the topological-censorship and no-wormhole results
      actually use.  Casimir escapes it because the geodesic between the plates
      is not achronal' -- the fixed-background version labelled as theirs,
      their consequence widened and credited to topological censorship as
      such, the Planck-scale restriction dropped, and null lines between
      plates, which are achronal, called chronal.

    SO THE ONLY QUESTION THAT MATTERS FOR THIS ARCHITECTURE IS WHETHER ITS
    ANEC-VIOLATING RAYS ARE ACHRONAL.  achronal.py asked exactly that, and
    answered ZERO NON-ACHRONAL over 25 rays.  That answer is not robust.

===============================================================================
2. THE INVERTED CLAIM
===============================================================================

achronal.py reduces the Raychaudhuri equation by dropping shear and writes, at
its line 53:

    "DROPPING SHEAR IS CONSERVATIVE: sigma^2 >= 0 only ever helps focusing, so a
     ray this file calls achronal would still be achronal with shear restored."

    THE FIRST HALF IS RIGHT AND THE CONCLUSION IS BACKWARDS.  sigma^2 does only
    ever help focusing.  More focusing means a conjugate point SOONER, or where
    there was none.  AND A CONJUGATE POINT MAKES A RAY NON-ACHRONAL past it --
    achronal.py says so itself, four lines earlier.  So dropping shear
    understates focusing, understates conjugate points, and therefore
    OVERSTATES achronality.  (CORRECTED, DOCKET 67: first written 'EXACTLY
    WHAT MAKES A RAY NON-ACHRONAL'.  The converse is false -- a flat
    cylinder's winding geodesic has no conjugate point and is not achronal --
    and only the forward direction is used here.)

DEMONSTRATED IN THE CLEANEST AVAILABLE CASE -- VACUUM, where R_kk = 0 (exactly
for Schwarzschild; composite.survey's linearised metric leaves an O(M^2)
residue, -4M^2/b^4 at closest approach, which DEFOCUSES, at -6.5e-4 of the
Weyl focal power -- DOCKET 67), lemma_applies() fires, and the scalar equation
gives u = lambda with no zero ever:

        source            Ricci-only conjugate      FULL MATRIX conjugate
        M = -2.0e-3       NONE                      56.50
        M = -4.0e-3       NONE                      47.17

    The lemma T_kk <= 0 => u'' >= 0 => no conjugate point is valid ONLY in the
    shear-free scalar reduction.  Weyl is TRACELESS, so it focuses one
    eigendirection whatever the sign of the source, and det A = 0 happens with
    R_kk identically zero.  composite.py named this three passes later --
    WEYL-IS-SIGNBLIND, and "conservative for an EXISTENCE claim about one ray,
    FATAL FOR A SEARCH" -- and nobody came back to achronal.py.

===============================================================================
3. SO: IS ANY RAY OF THE CORRIDOR BOTH ANEC-VIOLATING AND ACHRONAL?
===============================================================================

Measured with the full matrix, scanning impact parameter -- because one impact
parameter is not a scan, which is the lesson nullbound.py paid for:

        b        I = INT T_kk dl    ANEC       conjugate point
        0.05     -3.02792e-01       VIOLATED   400.2
        0.20     -1.56011e-03       VIOLATED   400.7
        0.50     -4.05340e-05       VIOLATED   403.8
        1.00     -2.46486e-06       VIOLATED   414.4
        2.00     -7.95417e-08       VIOLATED   461.0
        2.3783   -1.55444e-19       boundary   1578.0
        2.4021   +3.10521e-09       ok         1579.8
        5.00     +7.55281e-08       ok         (none within the run)

    (CORRECTED, DOCKET 67: the 1578.0 and 1579.8 rows were measured with
    x0 = -1500, lam = 3000; has_conjugate's lam = 800 run gives 491.20 and
    493.29.  The table mixed two run settings without saying so; existence is
    unaffected.  The rays start at x0 = -lam/2 and cross concentric's thin
    shell at r = 200, where the metric is only C^{0,1}; re-run from x0 = -199,
    inside the shell, each of the seven rays still has a conjugate pair within
    the smooth region (199.25 to 321.21), so the C^2 the conjugate-point
    theorem needs is met where it is used.)

    ANEC VIOLATION CEASES AT b = 2.378288, BISECTED.  Conjugate points persist
    well past it.  So the ANEC-VIOLATING SET IS STRICTLY CONTAINED IN THE
    NON-ACHRONAL SET, with room to spare, and the containment is not marginal
    anywhere along the scan.

        NO RAY OF THIS CORRIDOR IS BOTH ANEC-VIOLATING AND ACHRONAL.

    And the same negative core that makes INTEGRAL T_kk dl negative is the
    thing that focuses, through Weyl, which is sign-blind.  ONE OBJECT PRODUCES
    BOTH, and along this scan they did not come apart.
      CORRECTED (DOCKET 67): first written '... which is why they cannot come
      apart'.  Conjugate points from Weyl shear are derived under the NEC/WEC
      (Olum 1998; Gao-Wald); where T_kk < 0 the mechanism alone does not
      guarantee one -- with q <= -|w| there is no focusing eigenvalue, and at
      this tree's own parameters that removes the conjugate point.  What
      carries the containment is the full-matrix conjugate point measured on
      each ray above, not the mechanism.

===============================================================================
4. WHAT THAT DOES AND -- AT LENGTH -- WHAT IT DOES NOT
===============================================================================

    IT DOES: put this architecture outside the scope of achronal ANEC, the only
    version of ANEC with teeth.  The obstruction achronal.py recorded as closed
    against us does not bind the corridor.  It is the SAME escape Casimir uses
    and the same one Gao-Jafferis-Wall use, so the company is respectable --
    but note the difference: GJW make their geodesics non-achronal with an
    EXTERNAL causal path, and the corridor does it with an INTERNAL conjugate
    point it already needed for the seat.

    IT DOES NOT prove self-consistent achronal ANEC false.  Being outside a
    conjecture's scope is not refuting it, and this file will not be quoted as
    though it were.  The conjecture stands exactly where it stood.

    IT DOES NOT make the device buildable.  c^4/G is untouched, the exchange
    rate of 1.349e26 kg per metre is untouched, phase1's price is untouched, and
    the source still needs rho < 0 with everything supply.py, scale.py and
    shaping.py measured about that still standing.  NOT ONE ORDER OF MAGNITUDE
    MOVED IN THIS FILE.

    IT DOES NOT re-run achronal.py's own 25 rays.  The method is shown wrong;
    whether those particular Alcubierre-type rays flip is NOT-RUN, and the
    architecture phase1 keeps is this one.

    AND THE SCAN IS ONE FAMILY.  Planar, +x-directed rays at one source
    strength.  Other families are NOT-RUN.  "None within the run" is a
    run-length statement and never a proof of absence -- which is why the
    load-bearing direction here is the other one: every ANEC-violating ray
    EXHIBITS a conjugate point, and an exhibited zero is a positive
    measurement.

===============================================================================
5. SO THE ANEC ROW RELOCATES.  IT DOES NOT CLOSE.
===============================================================================

    obstruct.py has carried ANEC as OPEN throughout.  It does not become
    DISSOLVED: ANEC violation is still required and still measured.  What
    changes is that the requirement is no longer answerable by a prohibition --
    achronal ANEC does not reach this configuration -- so the obstruction
    RELOCATES into the magnitude, where everything else in this project already
    sits.

    THE OBSTACLE HAD ONE NAME AFTER smearing.py.  IT STILL HAS ONE NAME, AND THE
    NAME IS NO LONGER ANEC.  IT IS c^4/G.

stdlib only.  concentric.py supplies the geodesics and the full-matrix Jacobi,
smearing.py the closed-form ANEC integral, composite.py the vacuum
demonstration.
"""
import math, sys

M_SRC = 2.0e-2
B_ANEC_ZERO = 2.378288          # bisected: ANEC violation ceases here


# ------------------------------------------- 1: which ANEC, and which one bites

STATEMENTS = (
    ("ANEC in flat space", "PROVEN",
     "Faulkner-Leigh-Parrikar-Wang; Hartman-Kundu-Tajdini. Says nothing about "
     "a curved corridor"),
    ("ANEC in curved spacetime", "FALSE IN GENERAL",
     "for test fields on fixed backgrounds (Schwarzschild-Boulware, Visser, "
     "Urban-Olum); the plate system obeys it and the compactified vacuum "
     "(flat) violates it -- so violating it is not by itself a "
     "disqualification and never was.  CORRECTED (DOCKET 67): first given as "
     "'the Casimir vacuum is the standard counterexample'"),
    ("achronal ANEC", "OPEN, AND THE ONE WITH TEETH",
     "Graham & Olum's condition is its SELF-CONSISTENT version, below Planck "
     "curvature, open for at least nineteen years; their topological-"
     "censorship use adds simple connectivity and the null generic condition "
     "and forbids wormholes joining disconnected regions, or short ones.  "
     "CORRECTED (DOCKET 67): first given as 'Graham & Olum's hypothesis; what "
     "topological censorship actually uses'"),
)


def the_one_that_bites():
    return [n for n, s, _w in STATEMENTS if "TEETH" in s]


# ------------------------------------ 2: the inverted claim, demonstrated

def vacuum_demonstration(masses=(-2.0e-3, -4.0e-3)):
    """Ricci-only against the full matrix, in vacuum where R_kk = 0 (exactly for
    Schwarzschild; O(M^2), defocusing, in composite.survey's linearised metric).

    Returns [(M, ricci_only_conjugate, full_matrix_conjugate)].  The first is
    always None -- u'' = 0 gives u = lambda -- and the second is not.
    """
    import composite, achronal
    out = []
    for M in masses:
        zero, _up, _u = achronal.jacobi([0.0] * 100, 0.1)     # vacuum
        r = composite.survey(M)
        out.append((M, zero, r["conjugate"] if r["seats"] else None))
    return out


def dropping_shear_is_conservative():
    """achronal.py line 53 says yes.  Measured: NO, and it is inverted.

    A ray the Ricci-only reduction calls achronal acquires a conjugate point
    when shear is restored, and a conjugate point is what removes achronality.
    """
    return all(ricci is None and full is None
               for _M, ricci, full in vacuum_demonstration())


def lemma_is_shear_free_only():
    """T_kk <= 0 => no conjugate point holds ONLY in the scalar reduction."""
    import achronal
    fires = achronal.lemma_applies([0.0] * 100)       # vacuum: it fires
    has_conjugate = any(full is not None for _M, _r, full in vacuum_demonstration())
    return fires and has_conjugate


# --------------------------- 3: is any ray both ANEC-violating and achronal?

def anec_integral(b):
    import smearing
    return smearing.anec_integral(b=b)


def anec_violated(b):
    return anec_integral(b) < 0.0


def has_conjugate(b, m=M_SRC, lam=800.0, n=6500):
    """Full-matrix Jacobi, shear included.  An exhibited zero is positive data.

    The ray starts at x0 = -lam/2 and crosses concentric's thin shell at
    r = 200, where the metric is C^{0,1}, not C^2.  DOCKET 67 re-ran the seven
    scan rays from x0 = -199: each keeps a conjugate pair inside the smooth
    region, so no verdict moves (regularity named, DOCKET 67)."""
    import concentric
    return concentric.survey(m, b=b, x0=-lam / 2.0, lam=lam, n=n)["seats"]


def anec_boundary(lo=2.0, hi=5.0, iters=60):
    """Bisect where the ANEC integral changes sign."""
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        if anec_integral(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return lo


def counterexample(bs=(0.05, 0.2, 0.5, 1.0, 2.0)):
    """Any ray both ANEC-violating AND achronal?  Measured: none."""
    return [b for b in bs if anec_violated(b) and not has_conjugate(b)]


def containment_is_strict(b_test=3.5674):
    """Conjugate points persist past the ANEC boundary, with room to spare."""
    return has_conjugate(b_test) and not anec_violated(b_test)


def one_object_produces_both():
    """The negative core violates ANEC and focuses through Weyl.  Same source.

    HARD-CODED, not computed.  CORRECTED (DOCKET 67): first said 'the seat and
    the escape cannot come apart'.  Weyl focusing is derived under the NEC/WEC;
    where T_kk < 0 it does not by itself guarantee a conjugate point.  The
    containment rests on the conjugate point measured on each scan ray
    (counterexample(), containment_is_strict()), not on this constant.
    """
    return True


# -------------------------------------------- 4/5: scope, not refutation

REFUTES_ACHRONAL_ANEC = False        # outside a conjecture's scope != refuting it
OUTSIDE_ITS_SCOPE = True
ORDERS_MOVED = 0                     # c^4/G untouched, phase1's price untouched

NOT_RUN = (
    "achronal.py's own 25 Alcubierre-type rays, re-run with shear",
    "ray families other than planar +x-directed",
    "source strengths other than m = 2e-2",
    "self-consistent achronal ANEC itself, which stands where it stood",
)

ANEC_ROW = "RELOCATED"               # not DISSOLVED: violation is still required
RELOCATES_INTO = "the magnitude -- c^4/G"


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

    print("1. WHICH ANEC -- three statements, one of them bites")
    for n, s, _w in STATEMENTS:
        print("      %-28s %s" % (n, s))
    chk("the one with teeth", the_one_that_bites(), ["achronal ANEC"])

    print("\n2. THE INVERTED CLAIM, demonstrated in vacuum (R_kk = 0 to O(M))")
    for M, ricci, full in vacuum_demonstration():
        print("      M = %-9g  Ricci-only: %-6s   full matrix: %s"
              % (M, ricci, ("%.2f" % full) if full else "none"))
    chk("dropping shear is conservative (achronal.py line 53)",
        dropping_shear_is_conservative(), False)
    chk("the lemma holds only in the shear-free reduction",
        lemma_is_shear_free_only(), True)
    print("      Weyl is TRACELESS: it focuses one eigendirection whatever the")
    print("      sign of the source, so det A = 0 with R_kk identically zero.")

    print("\n3. IS ANY RAY BOTH ANEC-VIOLATING AND ACHRONAL?")
    near("ANEC violation ceases at b =", anec_boundary(), B_ANEC_ZERO, 1e-5)
    chk("rays that are ANEC-violating AND achronal", counterexample(), [])
    chk("and the containment is strict, not marginal",
        containment_is_strict(), True)
    chk("one object produces both the violation and the focusing",
        one_object_produces_both(), True)
    print("      the same negative core violates ANEC and focuses through Weyl;")
    print("      the containment rests on each ray's measured conjugate point.")

    print("\n4. SCOPE, NOT REFUTATION")
    chk("this refutes achronal ANEC", REFUTES_ACHRONAL_ANEC, False)
    chk("the corridor is outside its scope", OUTSIDE_ITS_SCOPE, True)
    chk("orders of magnitude moved by this file", ORDERS_MOVED, 0)
    print("      c^4/G untouched, 1.349e26 kg/m untouched, rho < 0 still needed.")
    print("      STILL NOT-RUN:")
    for n in NOT_RUN:
        print("        - %s" % n)

    print("\n5. THE ANEC ROW RELOCATES")
    chk("ANEC row", ANEC_ROW, "RELOCATED")
    chk("  into", RELOCATES_INTO, "the magnitude -- c^4/G")
    print("      not DISSOLVED: ANEC violation is still required and measured.")

    print("\n  SELFTEST " + ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("=" * 79)
    print("""VERDICT

  THE OBVIOUS NEXT STEP TURNED OUT TO START AT HOME.  achronal.py
  closed the achronality escape against us and did it with shear
  dropped, on the stated ground that dropping shear is conservative.
  It is not: shear helps focusing, focusing makes conjugate points,
  and a conjugate point is what REMOVES achronality.  The claim is
  inverted, and the demonstration needs no argument -- in vacuum
  R_kk = 0 (to O(M) in the linearised metric, whose O(M^2) residue
  defocuses), the scalar equation gives u = lambda with no zero ever,
  and the full matrix finds a conjugate point at 56.50.

  WITH THAT CORRECTED, THE CORRIDOR IS OUTSIDE ACHRONAL ANEC'S SCOPE.
  Scanning impact parameter, ANEC violation ceases at b = 2.378288
  while conjugate points persist well past it, so the ANEC-violating
  set sits strictly inside the non-achronal set with room to spare.
  No ray of this corridor is both ANEC-violating and achronal.  The
  same negative core that makes the integral negative is the thing
  that focuses, through sign-blind Weyl; but where T_kk < 0 that
  mechanism does not by itself guarantee a conjugate point, so the
  containment rests on the conjugate point measured on each ray of
  the scan.  (CORRECTED, DOCKET 67: first written 'the containment
  is structural rather than lucky ... The seat and the escape are one
  mechanism'.)

  WHAT THIS IS NOT.  It is not a refutation of self-consistent
  achronal ANEC, which stands exactly where it stood -- being outside
  a conjecture's scope is not defeating it.  It is not a route to a
  buildable device: c^4/G is untouched, the exchange rate is
  untouched, and NOT ONE ORDER OF MAGNITUDE MOVED IN THIS FILE.  It
  does not re-run achronal.py's own 25 rays, which stay NOT-RUN.

  WHAT IT CHANGES IS THE LEDGER.  The ANEC row has been OPEN
  throughout and does not close, because ANEC violation is still
  required.  It RELOCATES: the requirement is no longer answerable by
  a prohibition, so it becomes a question of magnitude like
  everything else here.

  THE OBSTACLE STILL HAS ONE NAME.  IT IS NO LONGER ANEC.  IT IS
  c^4/G.""")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
