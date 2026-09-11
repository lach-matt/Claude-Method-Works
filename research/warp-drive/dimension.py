#!/usr/bin/env python3
"""
dimension.py -- M: "The dimension claim is important.  Because I assert directly
that warp travel is exactly dimensional travel.  A superhighway through
dimensions to reach a corresponding position in another connected system in the
same dimension as origination."

The assertion is testable and it splits into three claims that have different
answers, so they are separated before they are answered.

    M1  the mechanism is dimensional -- dimension matters to how this works
    M2  the TRAVEL is dimensional -- going somewhere means leaving D = 4
    M3  the destination is "another connected system in the same dimension
        as origination", reached by a superhighway

M1 IS RIGHT, AND MORE SHARPLY THAN EXPECTED.  Lambda is a LOGARITHM ONLY IN
FOUR DIMENSIONS, and its scale-freedom -- the fifteen-digit invariance
coefficients.py measured -- IS A D = 4 PROPERTY THAT EXISTS IN NO OTHER
DIMENSION.

M2 IS WRONG, AND THE MEASUREMENT SAYS SO IN THE DIRECTION THAT HURTS: the
obstruction is DIMENSION-INDEPENDENT -- contraction still requires negative
enclosed mass in every D, exactly -- and higher dimensions make the RATE
STRICTLY WORSE, by 5.32x at D = 5 and 116x at D = 26.

M3 IS RIGHT ABOUT THE OBJECT AND WRONG BY ONE WORD.  "Another connected system
in the same dimension as origination" is an excellent description of a
WORMHOLE, and a wormhole is TOPOLOGY, NOT DIMENSION -- a handle on a
four-manifold, not a road out of one.  "Same dimension as origination" is
exactly right for a handle and exactly wrong for an extra dimension.  The
correction is one word and it points at instruments this tree already holds.

AND THE PASS SETTLES ONE BRANCH OF L2 WITHOUT NEEDING M'S SCOPE DECISION,
because the answer is the same under both scopes and only its STATUS differs.

===============================================================================
1. LAMBDA IS A LOGARITHM ONLY IN FOUR DIMENSIONS
===============================================================================

The Schwarzschild-Tangherlini solution in D spacetime dimensions has

        f(r) = 1 - mu / r^(D-3)

and the proper-length deficit this project buys is int (1 - 1/sqrt(f)) dr,
whose weak field is (|mu|/2) int r^-(D-3) dr.  THAT INTEGRAL CHANGES CHARACTER
AT EVERY DIMENSION AND D = 4 IS THE SINGULAR ONE:

    D = 3   f = 1 - mu, WITH NO r IN IT AT ALL.  A constant g_rr is a conical
            deficit, not a gradient: no Newtonian attraction, no tidal force,
            nothing localised to contract.  This is the known fact that 2+1
            gravity has no Newtonian limit, and solve.py already met it from
            the other side -- the static exchange amplitude VANISHES at D = 3.

    D = 4   int dr/r = LOGARITHM.  Divergent at BOTH ends, which is why the
            construction needs two cutoffs, which is where a and R_s come
            from, which is where X = 2 R_s/sqrt(b^2+a^2) comes from, WHICH IS
            WHERE LAMBDA COMES FROM.  Lambda exists because a logarithm needs
            two cutoffs and a power law does not.

    D >= 5  int r^-(D-3) dr = a CONVERGENT power law.  The total available
            contraction is FINITE and set by the INNER cutoff alone; the outer
            one stops mattering.  There is no Lambda-shaped object at all.

AND THE PROPERTY coefficients.py MEASURED IS THE D = 4 SIGNATURE.  It found
Lambda invariant to fifteen digits under scaling all three geometric inputs
together.  A logarithm of a RATIO is scale-free; a power law is not:

        D = 4   scale by k = 1 -> 2.649158683e-04
                scale by k = 10 -> 2.649158683e-04      IDENTICAL
        D = 5   k = 1 -> 4.975000000e-05
                k = 10 -> 4.975000000e-06               falls as 1/k
        D = 6   k = 1 -> 2.499937500e-05
                k = 10 -> 2.499937500e-07               falls as 1/k^2

    SCALE-FREEDOM IS NOT A PROPERTY OF THIS ARCHITECTURE.  IT IS A PROPERTY OF
    FOUR DIMENSIONS, and this architecture inherited it.  M1 LANDS.

===============================================================================
2. TWO INDEPENDENT D = 4 FACTS, AND AN HONEST CAUTION ABOUT COUNTING THEM
===============================================================================

    (a) THE AMPLITUDE RATIO.  solve.py derived A = 2(p.p')^2 - (2/(D-2))p^2p'^2
        from the de Donder propagator and found the ratio to Newton runs
        8, 6, 24/5, 32/7, 9/2, 96/23 and is undefined at D = 3.  EIGHT OCCURS
        IN D = 4 ALONE.  The bisector is half of it, 2(D-2)/(D-3), which is 4
        in D = 4 and 3 in D = 5 -- SO THE BISECTOR IS D = 4 ONLY TOO.

    (b) LAMBDA'S LOGARITHM, section 1.

    THESE ARE TWO FACTS, NOT THREE.  The 8 and the 4 are one calculation seen
    twice -- a bisector is half an extreme -- and counting them separately
    would inflate the pattern.  (a) and (b) are genuinely independent: one is
    a propagator contraction, the other is a radial integral.

    AND THE CAUTION, WHICH MATTERS MORE THAN THE PATTERN.  A theory written in
    four dimensions will be full of fours, and finding them is not evidence
    that four is metaphysically special.  WHAT IS ACTUALLY MEASURED HERE IS
    NARROWER AND SURVIVES THE CAUTION: in both places the D = 4 value is
    QUALITATIVELY DIFFERENT FROM ITS NEIGHBOURS, not merely numerically
    different -- a logarithm against power laws, a defined ratio against an
    undefined one below and a decreasing sequence above.  That is a structural
    observation.  IT IS NOT A NUMEROLOGICAL ONE AND IS NOT OFFERED AS ONE.

===============================================================================
3. THE OBSTRUCTION IS DIMENSION-INDEPENDENT, AND HIGHER D IS WORSE
===============================================================================

This is M2, and it is the claim that fails.

certify.py's theorem generalises without effort.  In D dimensions the static
spherically symmetric metric in areal radius has f(r) = 1 - 2m(r)/r^(D-3) with
dm/dr proportional to r^(D-2) rho -- still the VOLUME INTEGRAL of rho -- and
proper length dl = dr/sqrt(f).  Contraction is f > 1, and since r^(D-3) > 0,

        f - 1 = -2 m(r) / r^(D-3)  >  0   <=>   m(r) < 0

    EXACTLY, IN EVERY DIMENSION.  Tested in exact rational arithmetic at
    D = 4, 5, 6, 8, 11, 26 over masses and radii spanning seven orders:
    NO COUNTEREXAMPLES.

    SO LEAVING FOUR DIMENSIONS DOES NOT REMOVE THE REQUIREMENT FOR NEGATIVE
    ENCLOSED ENERGY.  It is not a loophole, it is the same theorem.

AND THE RATE GETS WORSE, WHICH IS THE PART THAT DECIDES IT.  Return per unit
|mu| over r1 = 1 to r2 = 200:

        D = 4    2.649159        the logarithm
        D = 5    0.497500        worse by 5.3249x
        D = 6    0.249994        worse by 10.5969x
        D = 8    0.125000        worse by 21.1933x
        D = 11   0.071429        worse by 37.0882x
        D = 26   0.022727        worse by 116.5630x

    MORE DIMENSIONS COST MORE, MONOTONICALLY, and the reason is the same
    saturation overturn.py found: a convergent integral has a ceiling and a
    divergent one does not.  FOUR DIMENSIONS IS THE CHEAPEST PLACE TO DO THIS,
    and it is where we already are.

===============================================================================
4. M3 -- RIGHT ABOUT THE OBJECT, WRONG BY ONE WORD
===============================================================================

"A superhighway ... to reach a corresponding position in another connected
system IN THE SAME DIMENSION AS ORIGINATION."

That is not a description of extra dimensions.  IT IS A DESCRIPTION OF A
WORMHOLE, and precisely so:

    "another connected system"          another asymptotic region
    "in the same dimension as
     origination"                       the SAME four-manifold
    "a superhighway"                    a throat that is shorter than the
                                        ambient route between the mouths

A wormhole is a HANDLE ON A FOUR-MANIFOLD.  The manifold stays four
dimensional and stops being simply connected.  THAT IS TOPOLOGY, NOT DIMENSION,
and the distinction is not pedantry because the two have different physics and
different tests:

    EXTRA DIMENSIONS    the manifold has dimension > 4.  Gravity's force law
                        changes to r^-(D-2) and Newton's law is violated at
                        short range -- which is measured, and constrains it.
                        Section 3 says this does not help us anyway.

    TOPOLOGY            the manifold stays 4D and gains a handle.  The force
                        law is untouched.  The price is that the throat must
                        violate the energy conditions to stay open
                        (Morris-Thorne), and chronology becomes a question.

    M IS DESCRIBING THE SECOND AND CALLING IT THE FIRST.  The correction is one
    word, and it points at instruments this tree already has: wormhole.py and
    gjw.py (Gao-Jafferis-Wall), which were built for exactly this object.

    AND THE PRICE IS THE SAME PRICE.  A traversable throat needs the energy
    conditions violated, which is certify.py's requirement in different
    clothing.  The superhighway is a real object in the literature; it is not
    a way around the bill.

===============================================================================
5. THIS SETTLES ONE BRANCH OF L2 WITHOUT M'S SCOPE DECISION
===============================================================================

wormhole.py has carried SCOPE_CHOSEN_HERE = None for the whole project, and it
asserts that None in its own selftest so that nobody can quietly decide it.
L2 asks whether modified gravity could supply a negative effective mass where
the matter term is not negative, via G = 8 pi T_matter + T_effective.

EXTRA DIMENSIONS ARE ONE OF THAT FAMILY -- Kaluza-Klein, Einstein-Gauss-Bonnet,
braneworld -- AND SECTION 3 CLOSES THAT BRANCH:

    the contraction <=> negative-enclosed-mass theorem holds in EVERY D,
    and the rate is WORSE in every D above four.

    SO THE BRANCH IS CLOSED AND THE SCOPE DECISION DID NOT HAVE TO BE MADE TO
    CLOSE IT.  The FINDING is the same whether or not higher-dimensional
    gravity "counts as proven" for M's purposes; only the STATUS of the finding
    depends on that.  THE FLAG IS NOT TOUCHED HERE and remains None.

    WHAT L2 STILL HAS OPEN is the part section 3 does not reach: f(R) and
    scalar-tensor theories in FOUR dimensions, where the effective term comes
    from higher powers of curvature rather than from extra directions.  That is
    still M's decision and this file does not make it.

===============================================================================
6. A PRECISION ARTEFACT, RECORDED
===============================================================================

The biconditional in section 3 was first tested in floating point as f > 1,
and reported FIVE COUNTEREXAMPLES at D = 11 and D = 26.  They were not
counterexamples.  At D = 26, m = -1e-6, r = 100 the true f - 1 is 2.000e-52,
and 1.0 + 2e-52 == 1.0 in double precision, SO THE TEST DESTROYED THE QUANTITY
IT WAS TESTING.  Rerun in exact rational arithmetic on the sign of f - 1 alone,
there are none.

    A HIGH-DIMENSIONAL TEST IS A PRECISION TEST WHETHER OR NOT YOU MEANT IT
    TO BE, because r^(D-3) at D = 26 is r^23.  Recorded beside SIMPSON-ODD,
    QUAD-CAUGHT and DIFFERENCE-CAUGHT: the fourth quadrature-or-precision
    fault this tree has caught in its own work.

SCOPE.  Sections 1 and 3 are weak-field and exact-arithmetic statements about
Schwarzschild-Tangherlini and the D-dimensional Misner-Sharp form; they are
not claims about any solution of any field equation with a matter model, and
certify.py's verdict on the seated ansatz is unchanged.  Section 4 classifies
M's description against two standard objects and RESOLVES NOTHING about whether
either is achievable.  NOTHING IS REPAIRED.
"""

import math
import sys
from fractions import Fraction as F

# ---------------------------------------------------------------------------

DIMENSIONS = (3, 4, 5, 6, 8, 11, 26)
R1, R2 = 1.0, 200.0


# -- 1.  The radial integral, and where it changes character -----------------

def integral_character(D):
    """What int r^-(D-3) dr is, as a kind rather than a value."""
    if D == 3:
        return "NO-r-DEPENDENCE"      # f = 1 - mu, a conical deficit
    if D == 4:
        return "LOGARITHM"            # divergent both ends -> needs 2 cutoffs
    return "CONVERGENT-POWER"         # finite, set by the inner cutoff alone


def deficit_closed(mu, r1, r2, D):
    """Weak-field (|mu|/2) int_r1^r2 r^-(D-3) dr, in closed form."""
    a = abs(mu) / 2.0
    if D == 3:
        return 0.0                    # no gradient, nothing localised
    if D == 4:
        return a * math.log(r2 / r1)
    k = D - 4
    return a * (r1 ** -k - r2 ** -k) / k


def deficit_numeric(mu, r1, r2, D, n=50001):
    """int (1 - 1/sqrt(1 - mu/r^(D-3))) dr, to validate the closed form."""
    if n % 2 == 0:
        n += 1
    h = (r2 - r1) / (n - 1)
    s = 0.0
    for i in range(n):
        r = r1 + i * h
        w = 1.0 if (i == 0 or i == n - 1) else (4.0 if i % 2 else 2.0)
        s += w * (1.0 - 1.0 / math.sqrt(1.0 - mu / r ** (D - 3)))
    return s * h / 3.0


def is_scale_free(D, k=10.0, mu=-1e-4):
    """Scale r1 and r2 together.  Only a log of a ratio survives."""
    a = deficit_closed(mu, R1, R2, D)
    b = deficit_closed(mu, R1 * k, R2 * k, D)
    return abs(b - a) <= 1e-15 * max(1.0, abs(a))


# -- 2.  The amplitude ratio and its bisector, from solve.py's propagator ----

def ratio_to_newton(D):
    """8 / (2 - 2/(D-2)).  None where the normalisation vanishes."""
    norm = 2 - F(2, D - 2)
    return None if norm == 0 else F(8) / norm


def bisector(D):
    """Half the extreme: 2(D-2)/(D-3)."""
    r = ratio_to_newton(D)
    return None if r is None else r / 2


# -- 3.  The D-dimensional Misner-Sharp biconditional, EXACT ----------------
#
#   f - 1 = -2 m(r)/r^(D-3), and r^(D-3) > 0, so sign(f-1) = sign(-m).
#   Tested on the sign of f - 1 alone: adding it to 1.0 in float destroys it.

def f_minus_one(m, r, D):
    return F(-2) * m / r ** (D - 3)


def contracts(m, r, D):
    return f_minus_one(m, r, D) > 0


def biconditional_counterexamples(dims=DIMENSIONS):
    bad = []
    for D in dims:
        if D == 3:
            continue                  # no r-dependence; the form does not apply
        for m in (F(-3), F(-1, 10 ** 6), F(1, 10 ** 6), F(3)):
            for r in (F(1, 2), F(1), F(7), F(100)):
                if contracts(m, r, D) != (m < 0):
                    bad.append((D, m, r))
    return bad


def float_artefact(D=26, m=-1e-6, r=100.0):
    """The test that destroyed its own quantity.  Kept as a fixture."""
    x = -2.0 * m / r ** (D - 3)
    return x, (1.0 + x == 1.0), (x > 0)


# -- 4.  The classification ---------------------------------------------------

CLAIM = ("warp travel is exactly dimensional travel -- a superhighway through "
         "dimensions to reach a corresponding position in another connected "
         "system in the same dimension as origination")

VERDICTS = [
    ("M1", "the MECHANISM is dimensional", "LANDS",
     "Lambda is a logarithm only in D=4, and its scale-freedom is a D=4 "
     "property this architecture inherited rather than one it has"),
    ("M2", "the TRAVEL is dimensional", "FAILS",
     "contraction <=> m(r) < 0 holds exactly in every D, and the rate is "
     "worse in every D above four -- 5.32x at D=5, 116x at D=26"),
    ("M3", "another connected system, same dimension as origination", "OBJECT-"
     "RIGHT-WORD-WRONG",
     "that is a WORMHOLE: a handle on a four-manifold.  Topology, not "
     "dimension -- and the price is the same energy-condition price"),
]

# The one-word correction, and where it points.
CORRECTION = "topology, not dimension"
POINTS_AT = ("wormhole.py", "gjw.py")

# This file does NOT decide M's scope question.
TOUCHES_SCOPE_FLAG = False
L2_BRANCH_CLOSED = "extra dimensions (Kaluza-Klein, Gauss-Bonnet, braneworld)"
L2_BRANCH_OPEN = "f(R) and scalar-tensor in FOUR dimensions"


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

    # -- 1: the integral changes character, and D=4 is the singular one ------
    chk("D=3 has no r-dependence at all",
        integral_character(3), "NO-r-DEPENDENCE")
    chk("D=4 is the LOGARITHM", integral_character(4), "LOGARITHM")
    chk("every D>=5 is a convergent power",
        sorted({integral_character(D) for D in DIMENSIONS if D >= 5}),
        ["CONVERGENT-POWER"])
    chk("the logarithm happens in EXACTLY one dimension",
        [D for D in DIMENSIONS if integral_character(D) == "LOGARITHM"], [4])

    # -- 1: closed forms validated against the numeric integral --------------
    for D in (4, 5, 6, 11):
        chk("closed form matches quadrature at D=%d" % D,
            deficit_numeric(-1e-4, R1, R2, D) /
            deficit_closed(-1e-4, R1, R2, D), 1.0, 1e-4)

    # -- 1: scale-freedom is D=4 ONLY -- the coefficients.py property --------
    chk("D=4 is scale-free", is_scale_free(4), True)
    chk("D=5 is NOT", is_scale_free(5), False)
    chk("D=6 is NOT", is_scale_free(6), False)
    chk("scale-freedom holds in exactly one dimension",
        [D for D in DIMENSIONS if D >= 4 and is_scale_free(D)], [4])
    chk("and D=5 falls as 1/k",
        deficit_closed(-1e-4, R1 * 10, R2 * 10, 5) /
        deficit_closed(-1e-4, R1, R2, 5), 0.1, 1e-9)

    # -- 2: the amplitude ratio and its bisector, both D=4 only --------------
    chk("ratio is 8 at D=4", ratio_to_newton(4), F(8))
    chk("bisector is 4 at D=4", bisector(4), F(4))
    chk("bisector is 3 at D=5", bisector(5), F(3))
    chk("8 occurs in D=4 alone",
        [D for D in DIMENSIONS if ratio_to_newton(D) == F(8)], [4])
    chk("4 occurs in D=4 alone",
        [D for D in DIMENSIONS if bisector(D) == F(4)], [4])
    chk("the 8 and the 4 are ONE fact, not two",
        bisector(11), ratio_to_newton(11) / 2)

    # -- 3: the obstruction is dimension-independent, EXACTLY ----------------
    chk("no counterexamples to contraction <=> m<0, any D",
        biconditional_counterexamples(), [])
    chk("tested in exact rational arithmetic",
        isinstance(f_minus_one(F(-3), F(7), 26), F), True)

    # -- 3: and higher D is strictly worse -----------------------------------
    rates = [(D, deficit_closed(-1.0, R1, R2, D)) for D in DIMENSIONS if D >= 4]
    chk("return falls monotonically with dimension",
        all(rates[i + 1][1] < rates[i][1] for i in range(len(rates) - 1)), True)
    chk("D=4 return", rates[0][1], 2.649159, 1e-6)
    chk("D=5 is worse by 5.3249x", rates[0][1] / rates[1][1], 5.3249, 1e-4)
    chk("D=26 is worse by 116.563x", rates[0][1] / rates[-1][1], 116.563, 1e-5)
    chk("four dimensions is the CHEAPEST place to do this",
        max(rates, key=lambda t: t[1])[0], 4)

    # -- 4: the classification -----------------------------------------------
    chk("three sub-claims adjudicated", len(VERDICTS), 3)
    chk("M1 lands", [v[2] for v in VERDICTS if v[0] == "M1"], ["LANDS"])
    chk("M2 fails", [v[2] for v in VERDICTS if v[0] == "M2"], ["FAILS"])
    chk("the correction is one word", CORRECTION, "topology, not dimension")
    chk("and it points at files this tree holds",
        POINTS_AT, ("wormhole.py", "gjw.py"))

    # -- 5: the scope flag is not touched ------------------------------------
    chk("this file does not decide L2", TOUCHES_SCOPE_FLAG, False)
    chk("the branch closed is extra dimensions",
        "Kaluza-Klein" in L2_BRANCH_CLOSED, True)
    chk("the branch still open is 4D modified gravity",
        "FOUR dimensions" in L2_BRANCH_OPEN, True)

    # -- 6: the precision artefact, kept as a fixture ------------------------
    x, killed, survives = float_artefact()
    chk("true f-1 at D=26 is 2e-52", x, 2.0e-52, 1e-3)
    chk("adding it to 1.0 destroys it", killed, True)
    chk("  but its sign alone survives", survives, True)
    chk("the artefact is recorded, not hidden",
        "PRECISION ARTEFACT, RECORDED" in __doc__, True)

    # -- scope ---------------------------------------------------------------
    chk("the numerological reading is refused",
        "IT IS NOT A NUMEROLOGICAL ONE" in __doc__, True)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE RADIAL INTEGRAL, BY DIMENSION   (r1=%g, r2=%g, |mu|=1)\n" % (R1, R2))
    print("    D    character            return      scale-free?   ratio 8?")
    for D in DIMENSIONS:
        v = deficit_closed(-1.0, R1, R2, D)
        r = ratio_to_newton(D)
        print("   %-4d  %-20s %-11.6f %-13s %s"
              % (D, integral_character(D), v,
                 is_scale_free(D) if D >= 4 else "--",
                 "UNDEFINED" if r is None else r))
    print("\n    D = 4 is the only logarithm, the only scale-free case,")
    print("    the only 8 -- and the cheapest.  We are already in it.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE OBSTRUCTION, IN EVERY DIMENSION\n")
    print("    f - 1 = -2 m(r)/r^(D-3),  r^(D-3) > 0,  so  f > 1  <=>  m(r) < 0")
    print("    exact-arithmetic counterexamples over D, m, r: %r"
          % biconditional_counterexamples())
    print("    -> leaving four dimensions does NOT remove the requirement.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE CLAIM\n")
    for cid, text, verdict, why in VERDICTS:
        print("    %-3s %-26s %s" % (cid, verdict, text))
        print("        %s" % why)
    print("\n    CORRECTION: %s   ->  %s" % (CORRECTION, ", ".join(POINTS_AT)))
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M asserts that warp travel is exactly dimensional travel.  Split three
  ways and measured: the MECHANISM is dimensional and more sharply than
  expected -- Lambda is a logarithm in FOUR DIMENSIONS ONLY, because
  int r^-(D-3) dr is a log at D=4, has no r in it at D=3, and is a
  convergent power everywhere above; and the scale-freedom coefficients.py
  measured to fifteen digits is a property of the logarithm, hence of D=4,
  not of this architecture.  The TRAVEL is not dimensional: the
  contraction <=> negative-enclosed-mass theorem holds EXACTLY in every
  dimension, tested in rational arithmetic with no counterexamples, and
  the return per unit mass falls monotonically -- D=5 is 5.32x worse, D=26
  is 116x worse -- so four dimensions is the cheapest place to do this and
  we are already in it.  The DESTINATION M describes, "another connected
  system in the same dimension as origination", is right about the object
  and wrong by one word: that is a WORMHOLE, a handle on a four-manifold,
  which is TOPOLOGY rather than DIMENSION -- exactly right that the
  dimension does not change, exactly wrong that dimensions are travelled
  -- and it points at wormhole.py and gjw.py, which this tree already
  holds, at the same energy-condition price.  The pass also closes one
  branch of L2 without M's scope decision, because extra dimensions are a
  modified-gravity family and section 3 refuses them under either scope;
  f(R) in four dimensions stays open and stays M's.  One caution kept
  loud: a theory written in four dimensions will be full of fours, and
  what is measured here is only that the D=4 value is QUALITATIVELY unlike
  its neighbours in both places -- a structural observation, offered as
  nothing more.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
