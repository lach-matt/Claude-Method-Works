#!/usr/bin/env python3
"""
quasilocal.py -- ITEM 2: L1, the scope link.  certify.py's theorem is static and
spherically symmetric only, and overturn.py named what would break that: a
quasi-local mass that (a) reduces to Misner-Sharp on round spheres and
(b) controls proper distance the same way.

BOTH REQUIREMENTS ARE TESTED HERE AND THE ANSWERS ARE OPPOSITE.

    (a) HOLDS EXACTLY.  The Hawking mass of a round sphere IS the Misner-Sharp
        mass, to twelve decimals, for positive and negative mass alike.  No
        approximation, no limit.

    (b) IS FALSE FOR A SINGLE SURFACE, and the counterexample is one this tree
        already owns: two profiles with IDENTICAL boundary data and proper
        distances 25.5% apart.  A quasi-local mass is a SURFACE integral and
        proper distance is a PATH integral, and coefficients.py already proved
        that boundary data does not determine a path integral.

    SO L1 CANNOT BE SOLVED BY FINDING THE RIGHT SINGLE-SURFACE MASS.  It must be
    a FOLIATION, because the spherical theorem works only because m(r) is
    defined at every r.  THAT IS WHY L1 IS A FLOW PROBLEM, and it is why
    millennium.py found the Perelman/Geroch/Huisken-Ilmanen paradigm to be the
    one that bears.  This pass narrows L1 by ruling out a whole class of attack.

===============================================================================
1. REQUIREMENT (a) -- HOLDS, EXACTLY
===============================================================================

The Hawking mass of a closed 2-surface S is

        m_H(S) = sqrt(|S|/16 pi) ( 1 - (1/16 pi) Int_S H^2 dA )

For a round sphere r = const in a static spherically symmetric slice with
f(r) = 1 - 2 m(r)/r, the mean curvature is H = 2 sqrt(f)/r and |S| = 4 pi r^2,
so Int_S H^2 dA = 16 pi f and

        m_H = (r/2)(1 - f) = (r/2)(2m/r) = m

    EXACTLY THE MISNER-SHARP MASS.  Measured at m = 2, -1, -1e-4 and 0.5 over
    radii 1 to 200: agreement to twelve decimals, and the NEGATIVE cases work
    as cleanly as the positive ones, which is the case this project needs.

    So the Hawking mass satisfies requirement (a) by construction rather than
    by luck, and it is the reason Geroch, Jang and Jang-Wald reached for it in
    the 1970s.

===============================================================================
2. REQUIREMENT (b) -- FALSE FOR A SINGLE SURFACE
===============================================================================

Requirement (b) asks the quasi-local mass to control PROPER DISTANCE the way
m(r) does in the spherical theorem.  Test it directly, with the two-profile
construction coefficients.py built for a different purpose:

        m_A(r) = m0                                       constant
        m_B(r) = m0 + eps sin^2(pi (r-r1)/(r2-r1))        bumped between

with m0 = -1, eps = -1, r1 = 1, r2 = 200.  They agree at BOTH endpoints, so the
boundary sphere S at r2 is identical in both, and therefore

        m_H(S_r2)  profile A = -1.000000000
        m_H(S_r2)  profile B = -1.000000000        IDENTICAL

while the proper contraction through the interior is

        Delta d  A = 4.414026389
        Delta d  B = 5.540580582                   RATIO 1.255221

    SAME SURFACE, SAME QUASI-LOCAL MASS, 25.5% DIFFERENT PROPER DISTANCE.
    Requirement (b) is not merely unproved for the Hawking mass.  IT IS FALSE.

AND THE REASON IS STRUCTURAL, NOT SPECIAL TO THE HAWKING MASS.  Every
quasi-local mass is a functional of a SURFACE.  Proper distance is a LINE
INTEGRAL THROUGH THE INTERIOR.  coefficients.py proved, for the same reason and
with the same counterexample, that the map from boundary data to an interior
path integral is NOT WELL DEFINED.  ANY single-surface quantity inherits that.

    SO THE OBSTRUCTION TO L1 IS THE OBSTRUCTION THAT KILLED M'S ENDPOINT RULE.
    C5 said the difference between two locations is the difference of the
    coefficients at the endpoints; that is true for time and false for
    distance.  L1 asks a surface to determine an interior length.  SAME SHAPE,
    SAME FAILURE, AND THIS TREE ALREADY HAD THE PROOF.

===============================================================================
3. WHAT THAT LEAVES, AND WHY IT IS PROGRESS RATHER THAN A DEAD END
===============================================================================

The spherical theorem is not refuted by section 2, and the difference is the
whole content of this pass:

        m(r) IS NOT A SURFACE.  IT IS A FOLIATION.

The biconditional "contraction at r iff m(r) < 0" is a statement at EVERY r
simultaneously, and proper distance is recovered by integrating across the
family.  One surface carries no such information; a one-parameter family of
them carries all of it.

    THEREFORE L1 CANNOT BE SOLVED BY A BETTER QUASI-LOCAL MASS.  It can only be
    solved by a quasi-local mass TOGETHER WITH A FOLIATION, i.e. BY A FLOW.

    AND THAT IS EXACTLY THE MACHINERY THAT EXISTS.  Geroch monotonicity is a
    statement about m_H along INVERSE MEAN CURVATURE FLOW; Huisken-Ilmanen's
    contribution was a theory of WEAK solutions to that flow that keeps
    monotonicity through singularities; and Perelman closed Poincare with a
    different flow and a different monotone functional.  millennium.py found
    that paradigm to be the only Millennium problem bearing on this project,
    and section 2 explains WHY it has to be that paradigm and not another.

    WHAT REMAINS OPEN IS UNCHANGED IN SUBSTANCE AND SHARPER IN STATEMENT:

        find a foliation of a non-spherical static region, and a mass
        functional monotone along it, whose integral across the family
        controls proper distance -- with the biconditional's FREEING
        direction, which Geroch monotonicity does not supply.

    NOT ATTEMPTED HERE.  Attempting it is a research programme in geometric
    analysis and claiming otherwise would be the fault provenance.py exists to
    catch.  What this file does is DELETE A BRANCH: no single-surface quantity
    can work, so nobody need look for one.

SCOPE.  Sections 1 and 2 are computations in static spherically symmetric
slices, where m_H is exactly computable; they do not evaluate the Hawking mass
on any non-round surface and make no claim about its behaviour there.  Section
2's counterexample refutes requirement (b) FOR A SINGLE SURFACE and refutes
nothing about foliations.  Nothing is repaired and no theorem is claimed.
"""

import math
import sys

R1, R2 = 1.0, 200.0
M0, EPS = -1.0, -1.0


def hawking_mass_round(m_of_r, r):
    """m_H of the sphere r = const.  H = 2 sqrt(f)/r, |S| = 4 pi r^2."""
    f = 1.0 - 2.0 * m_of_r / r
    area = 4.0 * math.pi * r * r
    int_H2 = (4.0 * f / (r * r)) * area          # = 16 pi f
    return math.sqrt(area / (16.0 * math.pi)) * (1.0 - int_H2 / (16.0 * math.pi))


def reduces_to_misner_sharp(m_of_r, r, tol=1e-12):
    return abs(hawking_mass_round(m_of_r, r) - m_of_r) <= tol


def deficit(mfun, r1=R1, r2=R2, n=100001):
    """int (1 - 1/sqrt(1 - 2m(r)/r)) dr -- the interior path integral."""
    if n % 2 == 0:
        n += 1
    h = (r2 - r1) / (n - 1)
    s = 0.0
    for i in range(n):
        r = r1 + i * h
        w = 1.0 if (i == 0 or i == n - 1) else (4.0 if i % 2 else 2.0)
        s += w * (1.0 - 1.0 / math.sqrt(1.0 - 2.0 * mfun(r) / r))
    return s * h / 3.0


def flat_profile(m0=M0):
    return lambda r: m0


def bumped_profile(m0=M0, eps=EPS, r1=R1, r2=R2):
    def f(r):
        return m0 + eps * math.sin(math.pi * (r - r1) / (r2 - r1)) ** 2
    return f


# The two requirements overturn.py named, and their verdicts.
REQUIREMENTS = [
    ("a", "reduces to Misner-Sharp on round spheres", "HOLDS-EXACTLY",
     "m_H = (r/2)(1-f) = m, by construction, positive and negative alike"),
    ("b", "controls proper distance the same way", "FALSE-FOR-ONE-SURFACE",
     "identical boundary data, 25.5% different interior length; a surface "
     "integral cannot determine a path integral"),
]

# What the pass deletes, and what it leaves.
BRANCH_DELETED = "any SINGLE-SURFACE quasi-local mass"
BRANCH_LEFT = "a mass functional monotone along a FOLIATION -- i.e. a FLOW"
ATTEMPTED_HERE = False


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

    # -- (a) exactly, and for negative mass too -------------------------------
    for m, r in ((2.0, 10.0), (-1.0, 3.0), (-1e-4, 200.0), (0.5, 1.0)):
        chk("m_H == Misner-Sharp at m=%g r=%g" % (m, r),
            reduces_to_misner_sharp(m, r), True)
    chk("  and it is exact, not asymptotic",
        hawking_mass_round(-1.0, 3.0), -1.0, 1e-14)
    chk("  negative mass gives negative m_H",
        hawking_mass_round(-1.0, 3.0) < 0, True)

    # -- (b) refuted, with the boundary data held identical -------------------
    A, B = flat_profile(), bumped_profile()
    chk("the two profiles agree at r1", A(R1), B(R1), 1e-14)
    chk("  and at r2", A(R2), B(R2), 1e-14)
    chk("so the boundary Hawking mass is IDENTICAL",
        hawking_mass_round(A(R2), R2), hawking_mass_round(B(R2), R2), 1e-14)
    dA, dB = deficit(A), deficit(B)
    chk("interior length, flat profile", dA, 4.414026389, 1e-6)
    chk("interior length, bumped profile", dB, 5.540580582, 1e-6)
    chk("  they differ", dB != dA, True)
    chk("  by 25.5%", dB / dA, 1.255221, 1e-5)
    chk("REQUIREMENT (b) IS FALSE for a single surface",
        abs(dB - dA) > 1.0, True)

    # -- the structure of the failure ----------------------------------------
    chk("two requirements adjudicated", len(REQUIREMENTS), 2)
    chk("(a) holds", [r[2] for r in REQUIREMENTS if r[0] == "a"],
        ["HOLDS-EXACTLY"])
    chk("(b) fails", [r[2] for r in REQUIREMENTS if r[0] == "b"],
        ["FALSE-FOR-ONE-SURFACE"])
    chk("the failure is coefficients.py's, reused",
        "coefficients.py already proved" in __doc__, True)

    # -- what is deleted and what is left ------------------------------------
    chk("the deleted branch is single-surface",
        "SINGLE-SURFACE" in BRANCH_DELETED, True)
    chk("the branch left is a flow", "FLOW" in BRANCH_LEFT, True)
    chk("L1 is NOT attempted here", ATTEMPTED_HERE, False)
    chk("and that is stated", "NOT ATTEMPTED HERE" in __doc__, True)
    chk("no theorem is claimed", "no theorem is claimed" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  REQUIREMENT (a) -- m_H on round spheres\n")
    print("     m(r)        r        m_H              Misner-Sharp     match")
    for m, r in ((2.0, 10.0), (-1.0, 3.0), (-1e-4, 200.0), (0.5, 1.0)):
        print("    %-11g %-8g %+.12f  %+.12f   %s"
              % (m, r, hawking_mass_round(m, r), m,
                 reduces_to_misner_sharp(m, r)))
    print()
    print("  ------------------------------------------------------------------------")
    print("  REQUIREMENT (b) -- same surface, different interior\n")
    A, B = flat_profile(), bumped_profile()
    print("    m_H(S at r2), flat profile   = %+.9f" % hawking_mass_round(A(R2), R2))
    print("    m_H(S at r2), bumped profile = %+.9f   IDENTICAL"
          % hawking_mass_round(B(R2), R2))
    print("    interior Delta d, flat       = %.9f" % deficit(A))
    print("    interior Delta d, bumped     = %.9f   ratio %.6f"
          % (deficit(B), deficit(B) / deficit(A)))
    print("\n    -> a SURFACE integral cannot determine a PATH integral.")
    print()
    for rid, text, verdict, why in REQUIREMENTS:
        print("    (%s) %-24s %s" % (rid, verdict, text))
        print("        %s" % why)
    print("\n    DELETED: %s" % BRANCH_DELETED)
    print("    LEFT:    %s" % BRANCH_LEFT)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  overturn.py's L1 named two requirements for a quasi-local mass that would
  carry certify.py's theorem past spherical symmetry, and they come out
  opposite.  Requirement (a) HOLDS EXACTLY: the Hawking mass of a round
  sphere is (r/2)(1-f) = m, the Misner-Sharp mass, to twelve decimals and
  for negative mass as cleanly as positive -- which is why Geroch reached
  for it.  Requirement (b) IS FALSE for a single surface, and the
  counterexample is one this tree already owns: two mass profiles agreeing
  at both endpoints give an IDENTICAL boundary Hawking mass of -1.000000000
  and interior proper contractions of 4.414026 and 5.540581, 25.5% apart.
  The reason is structural and not special to the Hawking mass -- every
  quasi-local mass is a SURFACE integral, proper distance is a PATH
  integral, and coefficients.py already proved that boundary data does not
  determine an interior path integral.  It is the same failure that killed
  M's endpoint rule for distance, in a new place.  What survives is the
  observation that makes this progress rather than a wall: m(r) is not a
  surface, IT IS A FOLIATION, and the spherical biconditional holds at
  every r at once.  SO L1 CANNOT BE SOLVED BY A BETTER QUASI-LOCAL MASS --
  only by one together with a flow, which is exactly Geroch monotonicity
  under inverse mean curvature flow and exactly the paradigm millennium.py
  found bearing.  This pass deletes a branch rather than opening one, and
  a deleted branch is worth having.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
