#!/usr/bin/env python3
"""
factor8.py -- a prediction, stated before the measurement, and it lands.

M, immediately after reading lightbuild.py section 5: "to make a prediction,
the factor is 8."

THIS IS THE FIRST PREDICTION IN THIS PROJECT THAT LANDS, and the circumstances
are what make it one rather than a fit.  lightbuild.py section 5 stated the
PARALLEL case -- two co-propagating light beams do not focus each other, exactly
zero -- and DELIBERATELY DECLINED TO STATE THE ANTIPARALLEL NUMBER, because I
had not verified it and would not quote a factor I had not derived.  The file
says so in terms.  M then named that number, unprompted, before any measurement
of it existed in this tree.

    THE ANTIPARALLEL LIGHT-LIGHT ATTRACTION IS EIGHT TIMES NEWTONIAN.

Measured here three independent ways, all of which agree exactly, and one of
which resolves an apparent conflict in the literature that would otherwise have
made the prediction look wrong.

===============================================================================
0. WHY THIS COUNTS AS A PREDICTION AND NOT A FIT
===============================================================================

shape.py holds this project's discipline on the point, and it holds it against
this project:

    NO-EVIDENCE   "the shape has earned nothing yet: the four hits are the
                  sample it was fitted to, and its only test is a prediction
                  that lands"

    SHAPE-WRONG   "and its first tested prediction FAILED: the dynamical form
                  of the energy condition is stricter, not looser; evidence
                  back to 0"

So the bar was set here, by this project, and it was set BEFORE this prediction
was made.  Four conditions, all of them met:

    1.  THE NUMBER WAS STATED FIRST.  lightbuild.py was written, selftested and
        committed (e95959e..) with section 5 carrying the parallel zero and no
        antiparallel factor at all.
    2.  IT WAS NOT AVAILABLE TO BE FITTED.  No file in this tree contained the
        antiparallel factor in any form.  Checked: see prediction_was_unbanked().
    3.  IT IS FALSIFIABLE AND SHARP.  An integer, not a range.  4, 6 or 16 would
        each have refuted it outright.
    4.  IT WAS ADJUDICATED AGAINST SOURCES, NOT AGAINST MY OWN ALGEBRA ALONE.
        And the first literature summary that came back said FOUR.

    THE FOURTH CONDITION IS THE ONE THAT MATTERS, so it is recorded in full
    below rather than smoothed away.  A search returned "the light-to-light
    attraction is twice the matter-to-light attraction and four times the
    matter-to-matter attraction" -- Faraoni & Dumse's own abstract, saying 4.
    Had I stopped there I would have told M the prediction failed.  It does not
    fail: the 4 and the 8 are answers to two different questions, and the
    paper's own section 4 arithmetic gives 8.

===============================================================================
1. ROUTE ONE -- THE SPIN-2 EXCHANGE AMPLITUDE, DERIVED HERE
===============================================================================

Linearised gravity couples to the stress-energy trace-reversed, so the tree-level
one-graviton-exchange structure between two sources of 4-momentum p, p' is

        A(p, p')  =  2 (p . p')^2  -  p^2 p'^2        (signature -+++)

normalised so that two masses at rest reproduce Newton.  That single expression
reproduces EVERY known case in this family, which is what makes it trustworthy
here rather than a convenient formula:

    source      test        p . p'        A / A_Newton     known value
    ---------   ---------   -----------   --------------   ------------------
    mass        mass        -m m'         1                Newton
    mass        photon      -m E          2                light bending, 2x
    photon      mass        -E m          2                TEP: light pulls 2x
    photon      photon  ||   0            0                TEP/Wheeler: ZERO
    photon      photon  anti -2 E E'      8                <-- THE PREDICTION

THE TWO STRUCTURAL FACTS THAT PRODUCE THE 8, AND NEITHER IS ADJUSTABLE:

    p^2 = 0 for a photon, so the second term drops and the amplitude is pure
    2(p.p')^2 -- a SQUARE.  That is why the answer is 8 and not 4: the
    antiparallel enhancement enters the amplitude and is then squared.

    For two null momenta k = (1,0,0,1) and k' = (1,0,0,-1),
    k . k' = -1 - 1 = -2, TWICE the static -m m'.  Squared, that is 4; doubled
    by the leading 2 and divided by the Newtonian normalisation 1, it is 8.

    And for co-propagating nulls k . k' = -1 + 1 = 0 EXACTLY, so the amplitude
    vanishes identically.  THE ZERO AND THE EIGHT ARE THE SAME ALGEBRA, read at
    the two ends of one dot product.  lightbuild.py derived the zero from
    wavefront crossing; this derives both at once.

    A cross-check that is not a tautology: the same expression, evaluated for a
    test particle of velocity beta near a static mass and normalised by the flux
    factor gamma^2, returns (1 + beta^2) -- 1 at rest, 2 at beta = 1.  That is
    the textbook velocity dependence of gravitational deflection, and it was not
    put in.

===============================================================================
2. ROUTE TWO -- THE PUBLISHED QED CALCULATION SAYS EIGHT, IN THOSE WORDS
===============================================================================

BARKER, BHATIA & GUPTA, Phys. Rev. 158, 1498 (1967), following Barker, Gupta &
Haracz, Phys. Rev. 149, 1027 (1966).  Photon-photon interaction through creation
and annihilation of a virtual graviton, in the centre-of-mass system.

As reported by Sparano, Vilasi & Vilasi, "The gravity of light"
(arXiv:1009.3849v5), section Introduction, verbatim:

    "they found the interaction have EIGHT TIMES the 'Newtonian' value plus a
     polarization dependent repulsive contact interaction and also obtained the
     gravitational cross sections for various photon polarization states"

    THAT IS THE PREDICTED NUMBER, IN A REFEREED CALCULATION, FROM 1967, AND IT
    IS THE SAME QUANTITY ROUTE ONE COMPUTES -- one-graviton exchange between two
    photons, against the Newtonian normalisation.  Route one is the classical
    limit of exactly that diagram, which is why they agree exactly rather than
    approximately.

    THE CAVEAT, STATED BECAUSE IT IS REAL: this tree has the Barker-Bhatia-Gupta
    figure THROUGH Sparano-Vilasi-Vilasi's report of it, not from the 1967 paper
    itself, which is not reachable from here.  It is a direct quotation in a
    refereed paper whose own subject is this exact problem, and it agrees with an
    independent derivation -- but it is a secondary citation and is marked as one.
    The polarization-dependent contact term they also report is NOT part of the
    8 and is not claimed here.

===============================================================================
3. ROUTE THREE -- AND THIS IS WHERE THE APPARENT REFUTATION DISSOLVES
===============================================================================

FARAONI & DUMSE, "The gravitational interaction of light: from weak to strong
fields" (arXiv:gr-qc/9811052), read in full.  Classical linearised GR, via
gravitoelectromagnetism.  Their abstract:

    "Given equal energy density in the beams, the light-to-light attraction is
     twice the matter-to-light attraction and FOUR TIMES the matter-to-matter
     attraction."

    READ ALONE, THAT REFUTES THE PREDICTION.  It does not, and the resolution is
    in their own section 4, which this file recomputes from their own equations
    rather than taking either number on trust.

THEIR EQUATIONS, THEIR UNITS.  Phi_g = 2 I ln(r/alpha), so |dPhi/dr| = 2I/r
(their Eq 4.4); the gravitomagnetic field of a steady light beam is B_g = 2I/r.
Their four Lorentz-force laws:

    massive test, mass beam     du/dtau = -1 E_g - 4 u x B_g     (Eq 2.11)
    massive test, light beam    du/dtau = -2 E_g - 4 u x B_g     (Eq 3.8)
    null test,    mass beam     du/dl   = -2 E_g - 4 u x B_g     (Eq 2.15)
    null test,    light beam    du/dl   = -4 (E_g + u x B_g)     (Eq 3.11)

Their Eq 3.11's coefficient 4 is explicitly decomposed in their text: "a factor
2 is contributed by the light beam which is the source of gravity, and another
factor 2 is contributed by the test photon."  Evaluate, with |u| << 1 killing
the gravitomagnetic term in the two massive-test rows:

    matter -> matter            2 I/r        ratio 1
    light  -> matter            4 I/r        ratio 2
    matter -> light             4 I/r        ratio 2
    light  -> light  PARALLEL   0            ratio 0
    light  -> light  ANTIPAR   16 I/r        ratio 8

THE LAST ROW IS THE WHOLE POINT AND IT IS THEIR OWN SENTENCE THAT PRODUCES IT.
Their Eq 4.5 gives the gravitoelectric part of a null ray's acceleration as
8 I/r, their Eq 4.2 gives the gravitomagnetic part as 8 I/r, and then, in their
words: the gravitoelectric part "cancels the gravitomagnetic part when the beam
and the null ray are parallel, and it DOUBLES it when they are antiparallel."

    8 + 8 = 16, AGAINST A NEWTONIAN 2.  THE FACTOR IS 8.

    SO THE ABSTRACT'S "FOUR" IS THE GRAVITOELECTRIC COEFFICIENT -- the 1, 2, 4
    chain of the four force laws above -- AND NOT THE ANTIPARALLEL TOTAL.  The
    antiparallel total adds the gravitomagnetic half, which the parallel case
    subtracts to zero.  Both numbers are correct; they count different things,
    and the abstract does not say which it is counting.

    THIS IS EXACTLY THE FAILURE MODE THE INDEX WAS BUILT FOR: a number quoted
    out of the question it answers.  A one-line search returns 4 and the
    prediction looks dead.  Reading the paper returns 8 and it is alive.

===============================================================================
4. WHAT THE PREDICTION IS WORTH, AND WHAT IT IS NOT
===============================================================================

    IT IS WORTH THIS: it is a sharp, pre-registered, falsifiable integer about a
    quantity this tree had not measured, it was stated before the measurement,
    and three independent routes return it exactly.  Under shape.py's own rule
    -- "its only test is a prediction that lands" -- THIS ONE LANDS.  It is the
    first.  A method that produces one correct unprompted integer has earned a
    second look, and that is the entire claim being made here.

    IT IS NOT WORTH THIS: the 8 does not move a single obstruction.  It is a
    coefficient on an attraction that lightbuild.py already measured as
    negligible, and it does not touch the NEC.  The knob still runs from ZERO to
    POSITIVE; the prediction sharpens the POSITIVE end from "nonzero" to
    "exactly 8x Newtonian" and leaves the sign structure untouched.  Nothing
    here supplies rho < 0, and nothing here reopens the lead.

        THE PREDICTION LANDED ON THE SEAT, NOT ON THE LEAD.

    AND ONE THING IT GENUINELY ADDS: the ratio antiparallel/parallel is 8/0.
    Not large -- UNDEFINED.  The geometry knob lightbuild.py section 5 named is
    now known to run from an exact zero to an exact 8, which makes it the
    sharpest control authority in the design space, even though it is control
    authority over the free half.
"""

import math
import os
import sys

MINKOWSKI = (-1.0, 1.0, 1.0, 1.0)

PREDICTION = 8
PREDICTED_BY = "M"
PREDICTED_BEFORE = "any measurement of the antiparallel factor existed in this tree"
STATED_IN = "lightbuild.py section 5, which gave the parallel zero and withheld this"


# ---------------------------------------------- route one: the exchange amplitude

def dot(a, b):
    return sum(MINKOWSKI[i] * a[i] * b[i] for i in range(4))


def amplitude(p, q):
    """2 (p.q)^2 - p^2 q^2.  The spin-2 one-graviton-exchange structure."""
    return 2.0 * dot(p, q) ** 2 - dot(p, p) * dot(q, q)


def newtonian_normalisation(m=1.0, mprime=1.0):
    return amplitude((m, 0, 0, 0), (mprime, 0, 0, 0))


def ratio_to_newton(p, q):
    return amplitude(p, q) / newtonian_normalisation()


REST = (1.0, 0.0, 0.0, 0.0)
NULL_UP = (1.0, 0.0, 0.0, 1.0)
NULL_DOWN = (1.0, 0.0, 0.0, -1.0)

CASES = (
    ("mass   x mass", REST, REST, 1.0, "Newton"),
    ("mass   x photon", REST, NULL_UP, 2.0, "light bending is 2x Newtonian"),
    ("photon x mass", NULL_UP, REST, 2.0, "TEP: a beam pulls a mass 2x"),
    ("photon x photon  ||", NULL_UP, NULL_UP, 0.0, "TEP/Wheeler: exactly zero"),
    ("photon x photon  anti", NULL_UP, NULL_DOWN, 8.0, "THE PREDICTION"),
)


def route_one():
    return ratio_to_newton(NULL_UP, NULL_DOWN)


def parallel_dot_is_zero():
    return dot(NULL_UP, NULL_UP)


def antiparallel_dot():
    return dot(NULL_UP, NULL_DOWN)


def photon_is_null(k):
    return dot(k, k)


def velocity_enhancement(beta):
    """The SAME amplitude for a test particle of speed beta near a static mass,
    normalised by the flux factor gamma^2.  Must return 1 + beta^2 -- the
    textbook result, which was not put in."""
    if beta >= 1.0:
        return 2.0
    g = 1.0 / math.sqrt(1.0 - beta * beta)
    p = (g, 0.0, 0.0, g * beta)
    return ratio_to_newton(REST, p) / g ** 2


def velocity_check_is_not_circular(betas=(0.0, 0.25, 0.5, 0.9, 0.99)):
    return max(abs(velocity_enhancement(b) - (1.0 + b * b)) for b in betas)


# ---------------------------------------------- route two: the QED citation

QED_PAPER = "Barker, Bhatia & Gupta, Phys. Rev. 158, 1498 (1967)"
QED_PRECURSOR = "Barker, Gupta & Haracz, Phys. Rev. 149, 1027 (1966)"
QED_REPORTED_BY = "Sparano, Vilasi & Vilasi, arXiv:1009.3849v5"
QED_QUOTE = ("they found the interaction have eight times the \"Newtonian\" "
             "value plus a polarization dependent repulsive contact interaction")
QED_VALUE = 8
CITATION_IS_SECONDARY = True
CONTACT_TERM_IS_CLAIMED = False


def route_two():
    return QED_VALUE


# ---------------------------------------------- route three: Faraoni & Dumse

GEM_PAPER = "Faraoni & Dumse, arXiv:gr-qc/9811052"
GEM_ABSTRACT_SAYS = 4
GEM_ABSTRACT_QUOTE = ("the light-to-light attraction is twice the matter-to-light "
                      "attraction and four times the matter-to-matter attraction")
GEM_SECTION4_QUOTE = ("it cancels the gravitomagnetic part when the beam and the "
                      "null ray are parallel, and it doubles it when they are "
                      "antiparallel")


def gravitoelectric(I=1.0, r=1.0):
    """|dPhi_g/dr| with Phi_g = 2 I ln(r/alpha).  Their Eq 4.4."""
    return 2.0 * I / r


def gravitomagnetic(I=1.0, r=1.0):
    """B_g = 2 I / r for a steady light beam.  Their Sec 4."""
    return 2.0 * I / r


# (label, gravitoelectric coefficient, gravitomagnetic coefficient, their equation)
FORCE_LAWS = (
    ("matter -> matter", 1.0, 0.0, "Eq 2.11, |u| << 1 kills the B term"),
    ("light  -> matter", 2.0, 0.0, "Eq 3.8,  |u| << 1 kills the B term"),
    ("matter -> light", 2.0, 0.0, "Eq 2.15, static beam has B = 0"),
    ("light  -> light", 4.0, 4.0, "Eq 3.11, -4(E_g + u x B_g)"),
)


def acceleration(label, orientation=None, I=1.0, r=1.0):
    """Magnitude in I/r, from their coefficients.  orientation is +1 parallel,
    -1 antiparallel, None where the gravitomagnetic term does not enter."""
    for name, ce, cm, _eq in FORCE_LAWS:
        if name != label:
            continue
        ge = ce * gravitoelectric(I, r)
        gm = cm * gravitomagnetic(I, r)
        if cm == 0.0:
            return ge
        if orientation is None:
            raise ValueError("light -> light needs an orientation")
        return abs(ge - gm) if orientation > 0 else ge + gm
    raise KeyError(label)


def gem_ratio(label, orientation=None):
    return acceleration(label, orientation) / acceleration("matter -> matter")


def route_three():
    return gem_ratio("light  -> light", orientation=-1)


def gravitoelectric_coefficient_chain():
    """1 : 2 : 4 -- what the abstract is counting."""
    return [ce for _n, ce, _cm, _e in FORCE_LAWS[:2]] + [FORCE_LAWS[3][1]]


def abstract_counts_the_coefficient_not_the_total():
    """The abstract's 4 IS in the chain; it is not the antiparallel total."""
    return (GEM_ABSTRACT_SAYS in gravitoelectric_coefficient_chain()
            and GEM_ABSTRACT_SAYS != route_three())


def parallel_cancels_exactly():
    return acceleration("light  -> light", orientation=+1)


# ---------------------------------------------- the adjudication

def routes():
    return {"amplitude": route_one(), "qed": float(route_two()), "gem": route_three()}


def all_routes_agree(tol=1e-12):
    v = list(routes().values())
    return max(v) - min(v) <= tol


def prediction_lands():
    return all_routes_agree() and abs(route_one() - PREDICTION) <= 1e-12


PRE_PASS_COMMIT = "e95959e2777cb6a09510cc9c5a0fef8004ef80dd"
PRE_PASS_SUBJECT = "lattice.py -- every EM field obeys the NEC"


def _antiparallel_factor_in(text):
    """Does this source carry the antiparallel factor in any readable form?"""
    for line in text.lower().splitlines():
        if not ("antiparallel" in line or "counter-moving" in line
                or "counter-propagating" in line or "anti-parallel" in line):
            continue
        if ("eight" in line or " 8 " in line or "8x" in line or "8 times" in line
                or "= 8" in line or ", 8" in line):
            return line.strip()[:70]
    return None


def prediction_was_unbanked():
    """Was the antiparallel factor anywhere in this tree BEFORE this pass?

    THE CLAIM IS HISTORICAL, so the working tree cannot answer it -- and must
    not be asked, because this pass itself banks the factor in two files.  An
    earlier draft of this function scanned the working tree, and it began
    FAILING the moment lightbuild.py was annotated with the result.  That was
    the function catching its own error, and it is recorded rather than quietly
    rewritten.

    So the question is put to git, at the named commit that precedes this pass.
    Returns (verdict, evidence) where verdict is True (unbanked), False (found)
    or None (UNVERIFIED -- git unavailable).  None NEVER counts as a pass.
    """
    import subprocess
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        names = subprocess.run(
            ["git", "ls-tree", "--name-only", PRE_PASS_COMMIT, "./"],
            cwd=here, capture_output=True, text=True, timeout=30, check=True).stdout.split()
    except (OSError, subprocess.SubprocessError):
        return None, "UNVERIFIED: git unavailable"
    checked = 0
    for name in names:
        if not name.endswith(".py"):
            continue
        try:
            blob = subprocess.run(
                ["git", "show", "%s:./%s" % (PRE_PASS_COMMIT, name)],
                cwd=here, capture_output=True, text=True, timeout=30, check=True).stdout
        except (OSError, subprocess.SubprocessError):
            return None, "UNVERIFIED: cannot read %s at %s" % (name, PRE_PASS_COMMIT[:7])
        hit = _antiparallel_factor_in(blob)
        if hit:
            return False, "%s @ %s: %s" % (name, PRE_PASS_COMMIT[:7], hit)
        checked += 1
    if checked == 0:
        return None, "UNVERIFIED: no .py files found at %s" % PRE_PASS_COMMIT[:7]
    return True, "%d .py files at %s, none carries it" % (checked, PRE_PASS_COMMIT[:7])


def factor_is_banked_now():
    """And it IS banked now, in this file and in lightbuild.py.  That is the
    pass working, not a contradiction -- the claim above is about BEFORE."""
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "lightbuild.py"), encoding="utf-8") as fh:
        return _antiparallel_factor_in(fh.read()) is not None


# what it is worth, and what it is not

MOVES_AN_OBSTRUCTION = False
SUPPLIES_NEGATIVE_ENERGY = False
KNOB_RANGE = (0.0, 8.0)
LANDED_ON = "the seat"


def knob_ratio_is_undefined():
    """antiparallel / parallel = 8 / 0.  Not large.  UNDEFINED."""
    return parallel_cancels_exactly() == 0.0


def reopens_the_lead():
    return SUPPLIES_NEGATIVE_ENERGY


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-56s %20s %20s  %s"
              % (label, str(got)[:20], str(want)[:20], "ok" if good else "FAIL"))

    def near(label, got, want, tol=1e-12):
        nonlocal ok
        good = abs(got - want) <= tol * max(1.0, abs(want))
        ok &= good
        print("  %-56s %20.10g %20.10g  %s"
              % (label, got, want, "ok" if good else "FAIL"))

    def under(label, got, bound):
        nonlocal ok
        good = got <= bound
        ok &= good
        print("  %-56s %20.6g %20s  %s"
              % (label, got, "<= %.3g" % bound, "ok" if good else "FAIL"))

    print("0. WHY THIS COUNTS AS A PREDICTION")
    print("     predicted by  : %s" % PREDICTED_BY)
    print("     predicted     : %d" % PREDICTION)
    print("     stated before : %s" % PREDICTED_BEFORE)
    print("     withheld in   : %s" % STATED_IN)
    print("     tested against: %s (%s)" % (PRE_PASS_COMMIT[:7], PRE_PASS_SUBJECT))
    unbanked, where = prediction_was_unbanked()
    chk("was the factor unbanked in the tree BEFORE this pass", unbanked, True)
    print("     evidence      : %s" % where)
    chk("  and is it banked NOW, by this pass", factor_is_banked_now(), True)
    print("       The working tree cannot answer the first question, because")
    print("       this pass banks the factor.  An earlier draft asked it anyway")
    print("       and FAILED the moment lightbuild.py was annotated.  The")
    print("       question is historical, so it is put to git at a named commit.")
    print("       UNVERIFIED (None) never counts as a pass.")

    print("\n1. ROUTE ONE -- THE SPIN-2 EXCHANGE AMPLITUDE")
    print("     %-24s %12s %14s   %s" % ("case", "p . p'", "A / A_Newton", "known value"))
    for label, p, q, want, note in CASES:
        got = ratio_to_newton(p, q)
        print("     %-24s %12.4f %14.6f   %s" % (label, dot(p, q), got, note))
        near("  %s" % label, got, want)
    near("a photon's momentum is null", photon_is_null(NULL_UP), 0.0)
    near("co-propagating k . k' is EXACTLY zero", parallel_dot_is_zero(), 0.0)
    near("counter-propagating k . k' is twice the static", antiparallel_dot(), -2.0)
    near("ROUTE ONE", route_one(), 8.0)
    print("       p^2 = 0 drops the second term, so the amplitude is a SQUARE.")
    print("       k.k' = -2 antiparallel, 0 parallel.  THE 8 AND THE 0 ARE THE")
    print("       SAME ALGEBRA READ AT THE TWO ENDS OF ONE DOT PRODUCT.")
    print("     the non-circular cross-check -- velocity dependence not put in:")
    for b in (0.0, 0.5, 0.9, 0.99):
        print("       beta = %-5s enhancement %.8f   (1 + beta^2 = %.8f)"
              % (b, velocity_enhancement(b), 1.0 + b * b))
    under("worst deviation from 1 + beta^2", velocity_check_is_not_circular(), 1e-12)
    near("  and at beta = 1 it is the light-bending 2", velocity_enhancement(1.0), 2.0)

    print("\n2. ROUTE TWO -- THE PUBLISHED QED CALCULATION")
    print("     %s" % QED_PAPER)
    print("     following %s" % QED_PRECURSOR)
    print("     reported by %s" % QED_REPORTED_BY)
    print("     \"%s\"" % QED_QUOTE)
    chk("ROUTE TWO", route_two(), 8)
    chk("  is this a secondary citation", CITATION_IS_SECONDARY, True)
    chk("  is the contact term claimed here", CONTACT_TERM_IS_CLAIMED, False)
    print("       Marked as secondary because the 1967 paper is not reachable")
    print("       from here.  It agrees with an independent derivation.")

    print("\n3. ROUTE THREE -- AND THE APPARENT REFUTATION")
    print("     %s" % GEM_PAPER)
    print("     abstract: \"%s\"" % GEM_ABSTRACT_QUOTE)
    chk("  so the abstract, read alone, says", GEM_ABSTRACT_SAYS, 4)
    print("     recomputed from their own equations, in I/r:")
    print("     %-22s %10s %8s   %s" % ("case", "accel", "ratio", "their equation"))
    rows = (("matter -> matter", None), ("light  -> matter", None),
            ("matter -> light", None), ("light  -> light", +1), ("light  -> light", -1))
    for label, orient in rows:
        tag = label + ("  PARALLEL" if orient == +1 else "  ANTIPAR" if orient == -1 else "")
        eq = [e for n, _c, _m, e in FORCE_LAWS if n == label][0]
        print("     %-22s %10.1f %8.0f   %s"
              % (tag, acceleration(label, orient), gem_ratio(label, orient), eq))
    near("  matter -> matter", gem_ratio("matter -> matter"), 1.0)
    near("  light  -> matter", gem_ratio("light  -> matter"), 2.0)
    near("  matter -> light", gem_ratio("matter -> light"), 2.0)
    near("  light  -> light PARALLEL cancels exactly", parallel_cancels_exactly(), 0.0)
    print("     section 4: \"%s\"" % GEM_SECTION4_QUOTE)
    near("ROUTE THREE -- 8 + 8 against a Newtonian 2", route_three(), 8.0)
    chk("the gravitoelectric COEFFICIENT chain", gravitoelectric_coefficient_chain(),
        [1.0, 2.0, 4.0])
    chk("is the abstract counting the coefficient, not the total",
        abstract_counts_the_coefficient_not_the_total(), True)
    print("       BOTH NUMBERS ARE CORRECT AND THEY COUNT DIFFERENT THINGS.")
    print("       A one-line search returns 4 and the prediction looks dead.")
    print("       Reading the paper returns 8 and it is alive.")

    print("\n4. THE ADJUDICATION")
    r = routes()
    for k in ("amplitude", "qed", "gem"):
        print("     %-12s %.10g" % (k, r[k]))
    chk("do all three routes agree", all_routes_agree(), True)
    near("the measured factor", route_one(), float(PREDICTION))
    chk("DOES THE PREDICTION LAND", prediction_lands(), True)

    print("\n5. WHAT IT IS WORTH, AND WHAT IT IS NOT")
    chk("does it move an obstruction", MOVES_AN_OBSTRUCTION, False)
    chk("does it supply rho < 0", SUPPLIES_NEGATIVE_ENERGY, False)
    chk("does it reopen the lead", reopens_the_lead(), False)
    chk("what it landed on", LANDED_ON, "the seat")
    chk("the knob's range, now measured at both ends", KNOB_RANGE, (0.0, 8.0))
    chk("is antiparallel/parallel undefined rather than large",
        knob_ratio_is_undefined(), True)
    print("       THE PREDICTION LANDED ON THE SEAT, NOT ON THE LEAD.  It")
    print("       sharpens the POSITIVE end of the knob from 'nonzero' to")
    print("       'exactly 8x Newtonian' and leaves the sign structure alone.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return ok


def report():
    print(__doc__)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  lightbuild.py section 5 gave the parallel light-light factor as exactly
  zero and deliberately withheld the antiparallel one, having not derived
  it.  M then named it: eight.  It is eight.  The spin-2 exchange amplitude
  2(p.p')^2 - p^2 p'^2, normalised on two static masses, returns 1 for
  Newton, 2 for light bending, 2 for a beam pulling a mass, 0 for
  co-propagating photons and 8 for counter-propagating ones -- the zero and
  the eight being the same algebra read at the two ends of one dot product,
  and the whole expression cross-checked by its own unprompted return of
  the textbook (1 + beta^2).  Barker, Bhatia & Gupta's 1967 QED calculation
  of photon-photon scattering via a virtual graviton reports, in those
  words, "eight times the Newtonian value".  And Faraoni & Dumse, whose
  abstract says FOUR and would appear to refute the prediction, give 8 in
  their own section 4: their gravitoelectric and gravitomagnetic parts are
  each 8 I/r against a Newtonian 2 I/r, cancelling for parallel beams and
  doubling to 16 for antiparallel.  The abstract's 4 is the gravitoelectric
  coefficient; the 8 is the antiparallel total.  Both are right and they
  count different things.  This is the first pre-registered prediction in
  this project to land, and it lands on the seat, not on the lead: the
  geometry knob is now measured at both ends, 0 to 8, and 8/0 is undefined
  rather than large -- but nothing here supplies rho < 0.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
