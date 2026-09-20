#!/usr/bin/env python3
"""
coefficients.py -- M, after the certification and the reversal audit:

    "The clues lay in the undefined/underived coefficients.  Coefficients need
     to be derived into theorem or law, law being better of course.  Knowing
     what a coefficient IS allows us to know the inputs, what is
     interchangeable.  I predict that coefficients are what changes in a
     transition state.  And the difference between two locations in spacetime
     is the difference in the coefficients of each endpoint of the corridor."

Four claims, and they are not equally testable, so they are separated before
they are tested.

    C1  the clue is in the coefficients whose value nothing here fixes
    C2  a coefficient should be derived up to theorem, better to law
    C3  knowing a coefficient tells you its inputs and what is interchangeable
    C4  a transition state is a change of coefficients
    C5  the difference between two locations IS the difference of the
        coefficients at the two endpoints of the corridor

C5 IS FALSE AS STATED AND EXACTLY HALF TRUE, AND THE HALF THAT FAILS IS THE
HALF THIS PROJECT NEEDS.  That is the finding, it is measured below, and it
explains -- for the first time in this tree -- WHY THERE IS A LAMBDA AT ALL.

C1 LANDS, and lands harder than I expected: the census finds exactly TWO
coefficients in the whole framework that nothing here fixes, and BOTH of them
sit in L4, the only link of overturn.py's chain that touches the bill.

===============================================================================
1. THE CENSUS -- provenance.py for numbers rather than claims
===============================================================================

provenance.py sorted the project's CLAIMS by how they were come by.  It never
sorted the NUMBERS, and a number is where an unearned assumption hides best,
because a number does not look like an assertion.  Twenty-six coefficients
carry the framework -- twenty-five, and the one DOCKET 41 found hiding as a 1.  Sorted by status:

    LAW           fixed by a symmetry or a limit; it could not be otherwise
    GEOMETRIC     a dimension or solid-angle factor
    THEOREM       derived, here or cited, from stated premises
    IDENTITY      an exact relation between other coefficients
    MEASURED      a number this tree solved for
    EMPIRICAL     a measured constant of nature
    MODEL-PARAM   a FREE INPUT of the chosen ansatz
    ASSERTED      a structure taken on four confirming cases, not derived
    UNDEFINED     named by the framework; nothing here gives it a value

M asks for LAW and settles for THEOREM.  The census says how far that got:

    LAW            1     8 pi, fixed by the Newtonian limit
    GEOMETRIC      1     4 pi, the solid angle in dm/dr = 4 pi r^2 rho
    THEOREM        9     8, 4, 120 degrees, 1/2, Ford-Roman, Casimir, sqrt(L),
                         and DOCKET 41's two: the 2 in A, and the 1 it hid
    IDENTITY       3     2/Lambda, Lambda/2, E_Planck/Lambda
    MEASURED       2     the two sub-Planckian crossovers
    EMPIRICAL      3     G, c, hbar
    MODEL-PARAM    4     a, R_s, b, m -- the ansatz's free inputs
    MODEL          1     LAMBDA ITSELF, and the exchange rate inherits it
    ASSERTED       0     DOCKET 41 settled the one that was here
    UNDEFINED      2     xi and l_UV

    -- AND THE TWO UNDEFINED ONES ARE BOTH IN L4.

    xi, the non-minimal coupling: the framework needs xi > 0 and fixes no
    value.  Fewster-Osterbrink says no state-independent QEI exists for xi > 0,
    which is candidate D's entire hope, and the hope is attached to a number
    nothing here determines.

    l_UV, the effective-theory cutoff: Fliss et al. give |rho| ~ hbar c /
    (l_UV^2 delta^2), the one bound whose exponent matches the requirement, and
    the shortfall is then the pure number (l_UV/l_P)^2 / Lambda.  It closes at
    l_UV = sqrt(Lambda) l_P = 3.159514 l_P and nothing here says whether that
    is the true cutoff.

    C1 IS CORRECT.  The two coefficients nothing defines are the two the
    reversal runs through.  That is not a coincidence and it is not mystical
    either: an undefined coefficient is a free parameter, and a free parameter
    is exactly where a no-go can fail to bind.

===============================================================================
2. C3 -- WHAT THE INPUTS ARE, AND WHAT IS INTERCHANGEABLE
===============================================================================

Lambda = 2[ln(2 R_s / sqrt(b^2 + a^2)) - 1] takes THREE inputs and uses them
through ONE combination:

        X = 2 R_s / sqrt(b^2 + a^2)          X = 399.920024 as seated

So the three-parameter family (a, R_s, b) collapses to a one-parameter family
in X, and ANY change preserving X leaves Lambda bit-for-bit identical.  Scaling
all three together is the obvious such change, and it is exact:

        k = 1        Lambda = 9.982529174194637
        k = 7        Lambda = 9.982529174194637
        k = 1000     Lambda = 9.982529174194637

    -- all fifteen digits, because Lambda is SCALE-FREE in the geometry.  That
    is the answer to "what is interchangeable": the whole two-dimensional
    surface X = const.  Shrink the shell and the ray together and you have
    changed nothing.

AND THE PART OF C3 THAT BITES.  Knowing the input tells you the LEVERAGE, and
the leverage is logarithmic, which is to say there is none:

        Lambda x 2    needs X x 1.4712e+02
        Lambda x 10   needs X x 3.2293e+19
        Lambda x 100  needs X x 3.9828e+214

    LAMBDA IS LOGARITHMICALLY STIFF.  A factor of ten in the exchange rate
    costs a factor of 3e19 in the geometry.  There is no geometric
    engineering out of this: the coefficient that sets the bill is the one
    input that cannot be moved.

===============================================================================
3. C5 -- MEASURED, AND IT IS EXACTLY HALF TRUE
===============================================================================

C5 says the difference between two locations is the difference of the
coefficients at the two endpoints.  A static spacetime has two independent
metric coefficients, and C5 is TRUE of one and FALSE of the other.

    ds^2 = -e^{2 Phi(r)} dt^2 + dr^2/(1 - 2 m(r)/r) + r^2 dOmega^2

TIME -- C5 HOLDS, EXACTLY.  The redshift between two static observers is

        1 + z = sqrt( g_tt(r2) / g_tt(r1) ) = e^{Phi(r2) - Phi(r1)}

which is a DIFFERENCE OF THE POTENTIAL AT THE TWO ENDPOINTS and depends on
nothing in between.  Two corridors whose Phi agrees at the ends and disagrees
wildly in the middle have the SAME redshift.  Measured below: identical to
machine precision.  C5 is right about time, and right for the reason M gives
-- g_tt enters the observable as an ENDPOINT RATIO.

SPACE -- C5 FAILS.  Proper distance is

        Delta d = int_r1^r2 [ 1 - 1/sqrt(1 - 2 m(r)/r) ] dr

a LINE INTEGRAL, and the map (endpoint coefficients) -> Delta d is not even
well defined.  Two mass profiles agreeing at BOTH endpoints:

        m_A(r) = m0                                       (constant)
        m_B(r) = m0 + eps sin^2(pi (r-r1)/(r2-r1))        (bumped between)

with m0 = -1, eps = -1, r1 = 1, r2 = 200.  Every metric coefficient at every
endpoint is IDENTICAL -- m_A(r1) = m_B(r1) = -1, m_A(r2) = m_B(r2) = -1, and
Phi is held equal.  And:

        Delta d_A = 4.414026389
        Delta d_B = 5.540580582          ratio 1.255221, a 25.5% difference

    SAME ENDPOINT COEFFICIENTS.  DIFFERENT DISTANCE.  C5 IS FALSE FOR SPACE.

===============================================================================
4. AND THAT IS WHY THERE IS A LAMBDA
===============================================================================

This is the part worth having, because it explains a coefficient rather than
merely classifying it.

A quantity that IS an endpoint difference has no coefficient of its own: it is
read off the ends and there is nothing to integrate.  A quantity that is a LINE
INTEGRAL must carry one -- the number that says how much the path contributed.

    LAMBDA IS THAT NUMBER.  It is not a fudge factor and it is not a fitted
    constant.  It is the value of the integral along the corridor, and its
    functional form is a LOGARITHM because the integrand goes as 1/r and the
    integral of dr/r is a log.  Lambda exists precisely BECAUSE C5 fails.

Three things follow and all three were already in the tree without the reason:

    (a) Lambda is MODEL and not THEOREM.  An integral along a path needs the
        whole path specified, so it needs a Phi -- and provenance.py's verdict
        on the headline was never about carelessness.  IT WAS STRUCTURAL.
        A path integral cannot be ansatz-free the way an endpoint ratio can.

    (b) The certification's ansatz-free theorem is about a BALL integral and
        overturn.py's door is that a ball integral is not a line integral.
        Both are integrals.  NOTHING IN THE OBSTRUCTION IS AN ENDPOINT
        QUANTITY, which is exactly why no endpoint bookkeeping escapes it.

    (c) overturn.py's L3 result -- the logarithm is the BEST case and the
        strong field returns strictly less -- is the saturation of that same
        integral.  A difference cannot saturate.  An integral with a bounded
        integrand must.

===============================================================================
5. C4, AND THE SCOPE OF ALL OF IT
===============================================================================

C4 -- "a transition state is a change of coefficients" -- is TRUE AND NEARLY
TAUTOLOGICAL in general relativity, where a change of the gravitational state
IS a change of the metric coefficients and there is nothing else it could be.
It earns content only in the sharpened form the two measurements above give it:

    A TRANSITION CHANGES BOTH COEFFICIENTS, AND THEY BUY DIFFERENT THINGS.
    Changing g_tt buys TIME and is paid at the endpoints.
    Changing g_rr buys DISTANCE and is paid along the whole corridor.

That asymmetry is not the seat/lead split -- certify.py killed that one -- and
it must not be read as reviving it.  It is the older and more basic split
between a potential and a length.

SCOPE, TIGHTLY:

    The census is of THIS framework's coefficients and claims no completeness
    beyond it.  The C5 measurement is static and spherically symmetric, which
    is certify.py's scope and not one inch more.  Holding Phi fixed while m
    varies is a statement about METRICS, not a claim that both profiles solve
    the field equations with a sensible matter model -- they need not, and
    certify.py showed the seated one does not.  NOTHING HERE IS REPAIRED.
    C5 is recorded as half-refuted, not corrected.
"""

import math
import sys

# ---------------------------------------------------------------------------
# Statuses.  Ordered worst-to-best is deliberate: the census is read from the
# bottom, where the free parameters are.
# ---------------------------------------------------------------------------

LAW = "LAW"
GEOMETRIC = "GEOMETRIC"
THEOREM = "THEOREM"
IDENTITY = "IDENTITY"
MEASURED = "MEASURED"
EMPIRICAL = "EMPIRICAL"
MODEL_PARAM = "MODEL-PARAM"
MODEL = "MODEL"
ASSERTED = "ASSERTED"
UNDEFINED = "UNDEFINED"

# (symbol, value-as-text, status, where, what fixes it -- or what does not)
COEFFICIENTS = [
    ("8 pi", "25.132741", LAW, "G_mn = 8 pi T_mn",
     "the Newtonian limit; no freedom at all"),
    ("4 pi", "12.566371", GEOMETRIC, "dm/dr = 4 pi r^2 rho",
     "the solid angle of a sphere"),

    ("8", "8", THEOREM, "factor8.py",
     "2(1-cos th)^2 at th = pi; the antiparallel extreme of the spin-2 "
     "amplitude, pre-registered before it was computed"),
    ("4", "4", THEOREM, "bisector.py",
     "gravitoelectric half = gravitomagnetic half; a BISECTOR, and not a "
     "value the curve takes"),
    ("120 deg", "120", THEOREM, "bisector.py",
     "2 s^2 (3 - 2 s) = 0 at s = 3/2, exact in Fraction arithmetic"),
    ("1/2", "0.5", THEOREM, "teardown.py",
     "the CTC window tau/loop = R/(2D) <= 1/2"),
    ("3/(32 pi^2)", "0.0094989", THEOREM, "candidates.py",
     "Ford-Roman, cited: |rho| <= 3 hbar c/(32 pi^2 L^4)"),
    ("pi^2/720", "0.013708", THEOREM, "candidates.py",
     "Casimir, cited: pi^2 hbar c/(720 d^4)"),
    ("sqrt(Lambda)", "3.159514", THEOREM, "overturn.py",
     "where candidate D's shortfall closes, in units of l_P"),

    ("2/Lambda", "0.200350028", IDENTITY, "lightbuild.py",
     "E_transition/E_kugelblitz, exact at every d over 31 decades"),
    ("Lambda/2", "4.9912645871", IDENTITY, "lightbuild.py",
     "the margin, the same identity inverted"),
    ("E_P/Lambda", "1.959505e8 J", IDENTITY, "planckcell.py",
     "the Planck cell, 195.95 MJ -- an identity wearing joules"),

    ("crossover FR", "0.307933 l_P", MEASURED, "candidates.py",
     "solved here, sub-Planckian"),
    ("crossover Cas", "0.369917 l_P", MEASURED, "candidates.py",
     "solved here, sub-Planckian"),

    ("G", "6.67430e-11", EMPIRICAL, "phase1.py", "measured"),
    ("c", "2.99792458e8", EMPIRICAL, "phase1.py", "defined exactly"),
    ("hbar", "1.054572e-34", EMPIRICAL, "candidates.py", "measured"),

    ("a  (A_CORE)", "0.02", MODEL_PARAM, "phase1.py",
     "FREE INPUT of the chosen Phi; enters Lambda only through X"),
    ("R_s (R_SHELL)", "200.0", MODEL_PARAM, "phase1.py",
     "FREE INPUT; enters Lambda only through X"),
    ("b  (B_RAY)", "1.0", MODEL_PARAM, "phase1.py",
     "FREE INPUT; enters Lambda only through X"),
    ("m  (core)", "2.0e-2", MODEL_PARAM, "phase1.py",
     "FREE INPUT; sets Phi(0) = m/a = 0.9999 and does not enter Lambda"),

    ("Lambda", "9.982529174194637", MODEL, "phase1.py",
     "THE COEFFICIENT THAT SETS THE BILL.  2[ln X - 1], the value of the "
     "integral along the corridor for the CHOSEN Phi.  c^4/(G Lambda) "
     "inherits this and so does every joule in the tree"),

    # DOCKET 41 SETTLED THIS ROW AND SHOWED THE CENSUS HAD FLAGGED THE WRONG
    # DIGIT.  propagator.py contracts the de Donder graviton propagator against
    # two point sources: the leading 2 is the number of index pairings of a
    # symmetric rank-2 source, the same in every dimension, and (alpha, beta)
    # = (2, -1) is UNIQUE given that ratio and the Newtonian normalisation.
    # The contingent digit is the SILENT 1 on p^2 p'^2 -- it is 2/(D-2), and
    # equals 1 only at D = 4 -- so a second row is added for it rather than
    # leaving it uncounted.  A coefficient written as a 1 is not written.
    ("2 in A", "2", THEOREM, "propagator.py",
     "the two index pairings of a symmetric rank-2 source against the "
     "symmetric graviton propagator; dimension-independent, and z3 finds no "
     "counterexample to the identity over the reals"),

    ("1 on p^2 p'^2", "2/(D-2) = 1 at D=4", THEOREM, "propagator.py",
     "the graviton propagator's trace term.  NOT dimension-free: light "
     "bending is (D-2)/(D-3) and the antiparallel prediction 4(D-2)/(D-3), so "
     "the 2 and the 8 this tree quotes are statements about FOUR dimensions "
     "and the co-propagating zero is the only one that is not"),

    ("xi", "UNDEFINED", UNDEFINED, "candidates.py / L4",
     "non-minimal coupling.  The framework needs xi > 0 -- Fewster-"
     "Osterbrink (arXiv:0708.2450) gives no state-independent QEI there -- "
     "and NOTHING HERE FIXES A VALUE"),
    ("l_UV", "UNDEFINED", UNDEFINED, "candidates.py / L4",
     "the EFT cutoff in Fliss et al. (arXiv:2309.10848), the one bound whose "
     "exponent matches.  Closes at sqrt(Lambda) l_P and NOTHING HERE SAYS "
     "WHETHER THAT IS THE CUTOFF"),
]

# Which link of overturn.py's chain each UNDEFINED coefficient sits in.
UNDEFINED_LINKS = {"xi": "L4", "l_UV": "L4"}

# M's five claims, and this file's verdict on each.
CLAIMS = [
    ("C1", "the clue is in the undefined coefficients", "LANDS",
     "exactly two are undefined and both are in L4, the only link that "
     "touches the bill"),
    ("C2", "derive coefficients up to theorem, better to law", "PARTIAL",
     "one LAW, one GEOMETRIC, seven THEOREM, three IDENTITY -- and the one "
     "that sets the bill is still MODEL"),
    ("C3", "knowing a coefficient tells you what is interchangeable", "LANDS",
     "(a, R_s, b) enter Lambda only through X = 2 R_s/sqrt(b^2+a^2), so the "
     "surface X = const is exactly interchangeable -- and the leverage is "
     "logarithmic, so it is also inert"),
    ("C4", "a transition state is a change of coefficients", "TRUE-BUT-THIN",
     "near-tautological in GR; earns content only as the time/space split"),
    ("C5", "location difference = endpoint coefficient difference", "HALF",
     "TRUE for time, an endpoint ratio of g_tt; FALSE for distance, a line "
     "integral of g_rr -- and distance is the half this project buys"),
]

# ---------------------------------------------------------------------------
# C3.  The one combination.
# ---------------------------------------------------------------------------

A_CORE, R_SHELL, B_RAY = 0.02, 200.0, 1.0


def X(a=A_CORE, Rs=R_SHELL, b=B_RAY):
    """The single combination the three geometric inputs enter through."""
    return 2.0 * Rs / math.sqrt(b * b + a * a)


def lam_from_X(x):
    """Lambda = 2[ln X - 1]."""
    return 2.0 * (math.log(x) - 1.0)


def lam(a=A_CORE, Rs=R_SHELL, b=B_RAY):
    return lam_from_X(X(a, Rs, b))


LAMBDA = lam()


def X_for_lambda(target):
    """Invert: what X gives this Lambda.  The leverage question."""
    return math.exp(target / 2.0 + 1.0)


def geometric_cost_of(factor):
    """How much X must move to move Lambda by `factor`."""
    return X_for_lambda(factor * LAMBDA) / X()


# ---------------------------------------------------------------------------
# C5.  Two measurements, one for each metric coefficient.
#
#   KINEMATIC.  These are statements about METRICS.  Holding Phi fixed while m
#   varies does not assert that either profile solves the field equations with
#   a sensible matter model -- certify.py showed the seated one does not.
# ---------------------------------------------------------------------------

R1, R2 = 1.0, 200.0


def redshift(phi, r1=R1, r2=R2):
    """1 + z = e^{Phi(r2) - Phi(r1)}.  An ENDPOINT quantity, by construction."""
    return math.exp(phi(r2) - phi(r1))


def proper_contraction(mfun, r1=R1, r2=R2, n=100001):
    """int (1 - 1/sqrt(1-2m(r)/r)) dr.  A LINE INTEGRAL, by construction."""
    if n % 2 == 0:
        n += 1
    h = (r2 - r1) / (n - 1)
    s = 0.0
    for i in range(n):
        r = r1 + i * h
        w = 1.0 if (i == 0 or i == n - 1) else (4.0 if i % 2 else 2.0)
        s += w * (1.0 - 1.0 / math.sqrt(1.0 - 2.0 * mfun(r) / r))
    return s * h / 3.0


def bump(base, eps, r1=R1, r2=R2):
    """A profile equal to `base` at BOTH endpoints and different between."""
    def f(r):
        return base + eps * math.sin(math.pi * (r - r1) / (r2 - r1)) ** 2
    return f


def c5_time(eps_list=(0.0, 3.0, -7.0)):
    """Same endpoint Phi, wildly different between.  Redshift must not move."""
    base = -0.1
    return [redshift(bump(base, e)) for e in eps_list]


def c5_space(m0=-1.0, eps=-1.0, n=100001):
    """Same endpoint m, different between.  Delta d must move -- and does."""
    flat = lambda r: m0                                     # noqa: E731
    return proper_contraction(flat, n=n), proper_contraction(bump(m0, eps), n=n)


# ---------------------------------------------------------------------------

def census_counts():
    out = {}
    for row in COEFFICIENTS:
        out[row[2]] = out.get(row[2], 0) + 1
    return out


def undefined_symbols():
    return sorted(r[0] for r in COEFFICIENTS if r[2] == UNDEFINED)


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

    # -- the census is well formed -------------------------------------------
    shape = [r for r in COEFFICIENTS if len(r) != 5]
    chk("every row is (symbol, value, status, where, what fixes it)", shape, [])
    chk("no duplicate symbols",
        len({r[0] for r in COEFFICIENTS}), len(COEFFICIENTS))
    chk("coefficients censused", len(COEFFICIENTS), 26)

    c = census_counts()
    chk("LAW", c.get(LAW, 0), 1)
    chk("GEOMETRIC", c.get(GEOMETRIC, 0), 1)
    chk("THEOREM", c.get(THEOREM, 0), 9)
    chk("IDENTITY", c.get(IDENTITY, 0), 3)
    chk("MEASURED", c.get(MEASURED, 0), 2)
    chk("EMPIRICAL", c.get(EMPIRICAL, 0), 3)
    chk("MODEL-PARAM", c.get(MODEL_PARAM, 0), 4)
    chk("MODEL", c.get(MODEL, 0), 1)
    # DOCKET 41: the one ASSERTED row became a THEOREM, and a second THEOREM
    # row was added for the digit the census had never counted.
    chk("ASSERTED", c.get(ASSERTED, 0), 0)
    chk("UNDEFINED", c.get(UNDEFINED, 0), 2)
    chk("the census is exhaustive", sum(c.values()), len(COEFFICIENTS))

    # -- C1: the two undefined ones, and where they sit ----------------------
    chk("the undefined coefficients", undefined_symbols(), ["l_UV", "xi"])
    chk("and BOTH are in L4", sorted(set(UNDEFINED_LINKS.values())), ["L4"])
    chk("every undefined symbol has a link",
        sorted(UNDEFINED_LINKS), undefined_symbols())

    # -- the headline is still MODEL, and that is the point -------------------
    chk("Lambda's status is MODEL",
        [r[2] for r in COEFFICIENTS if r[0] == "Lambda"], [MODEL])

    # -- C3: one combination, and it is exactly interchangeable --------------
    chk("X as seated", X(), 399.920024, 1e-8)
    chk("Lambda", LAMBDA, 9.982529174194637, 1e-15)
    for k in (7.0, 1000.0):
        chk("scale-free in the geometry at k=%g" % k,
            lam(A_CORE * k, R_SHELL * k, B_RAY * k), LAMBDA, 1e-15)
    chk("a and b enter only through b^2 + a^2",
        lam(a=B_RAY, b=A_CORE), LAMBDA, 1e-15)

    # -- C3: and the leverage is logarithmic, i.e. there is none -------------
    chk("Lambda x 2 costs X x 147", geometric_cost_of(2.0), 1.4712e2, 1e-3)
    chk("Lambda x 10 costs X x 3.23e19",
        geometric_cost_of(10.0), 3.2293e19, 1e-3)
    chk("the cost grows faster than the gain",
        geometric_cost_of(10.0) > geometric_cost_of(2.0) ** 5, True)

    # -- C5, time: the endpoint rule HOLDS -----------------------------------
    zs = c5_time()
    chk("three wildly different Phi profiles, same endpoints", len(zs), 3)
    chk("  redshift is identical (1 vs 2)", zs[1], zs[0], 1e-15)
    chk("  redshift is identical (1 vs 3)", zs[2], zs[0], 1e-15)
    chk("  and it is the endpoint ratio e^{dPhi}", zs[0], 1.0, 1e-15)

    # -- C5, space: the endpoint rule FAILS ----------------------------------
    da, db = c5_space()
    chk("flat profile Delta d", da, 4.414026389, 1e-6)
    chk("bumped profile Delta d", db, 5.540580582, 1e-6)
    chk("same endpoint m, DIFFERENT distance", db != da, True)
    chk("  by 25.5%", db / da, 1.255221, 1e-5)
    chk("  so (endpoint coefficients) -> Delta d is not well defined",
        abs(db - da) > 1.0, True)

    # -- the claim ledger ----------------------------------------------------
    chk("five claims adjudicated", len(CLAIMS), 5)
    chk("C5 is HALF, not TRUE and not FALSE",
        [c[2] for c in CLAIMS if c[0] == "C5"], ["HALF"])
    chk("C1 lands", [c[2] for c in CLAIMS if c[0] == "C1"], ["LANDS"])
    chk("nothing is claimed repaired",
        "NOTHING HERE IS REPAIRED" in __doc__, True)
    chk("the kinematic scope is stated",
        "a statement about METRICS" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE CENSUS\n")
    order = [LAW, GEOMETRIC, THEOREM, IDENTITY, MEASURED, EMPIRICAL,
             MODEL_PARAM, MODEL, ASSERTED, UNDEFINED]
    for st in order:
        rows = [r for r in COEFFICIENTS if r[2] == st]
        print("    %-12s (%d)" % (st, len(rows)))
        for sym, val, _, where, why in rows:
            print("      %-14s %-20s %-22s %s" % (sym, val, where, why[:60]))
    print()
    print("  ------------------------------------------------------------------------")
    print("  C3 -- LEVERAGE ON THE ONE COEFFICIENT THAT SETS THE BILL\n")
    print("    X = 2 R_s / sqrt(b^2 + a^2) = %.6f    Lambda = %.15f"
          % (X(), LAMBDA))
    for k in (1.0, 7.0, 1000.0):
        print("    scale all three by %-8g -> Lambda = %.15f"
              % (k, lam(A_CORE * k, R_SHELL * k, B_RAY * k)))
    for f in (2.0, 10.0, 100.0):
        print("    Lambda x %-5g needs X x %.4e" % (f, geometric_cost_of(f)))
    print()
    print("  ------------------------------------------------------------------------")
    print("  C5 -- MEASURED ON BOTH METRIC COEFFICIENTS\n")
    zs = c5_time()
    print("    TIME   three Phi profiles, same endpoints, different between:")
    for i, z in enumerate(zs):
        print("             1 + z  =  %.17g" % z)
    print("           -> C5 HOLDS.  g_tt enters as an ENDPOINT RATIO.\n")
    da, db = c5_space()
    print("    SPACE  two m profiles, same endpoints, different between:")
    print("             Delta d (flat)   = %.9f" % da)
    print("             Delta d (bumped) = %.9f     ratio %.6f" % (db, db / da))
    print("           -> C5 FAILS.  g_rr enters as a LINE INTEGRAL.")
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE LEDGER\n")
    for cid, text, verdict, why in CLAIMS:
        print("    %-3s %-12s %s" % (cid, verdict, text))
        print("        %s" % why)
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M predicted the clue was in the undefined coefficients, and it is: a
  census of the twenty-four numbers carrying this framework finds exactly
  TWO that nothing here fixes -- xi, the non-minimal coupling, and l_UV,
  the effective-theory cutoff -- and BOTH sit in L4, the only link of the
  reversal chain that touches the bill.  His rule for locations is exactly
  half true, and the measurement says which half: redshift is
  e^{Phi(r2)-Phi(r1)}, a difference of the coefficient at the two
  endpoints, and three wildly different corridors agreeing only at their
  ends give identical redshift to machine precision -- C5 holds for TIME.
  But two mass profiles agreeing at BOTH endpoints give proper
  contractions of 4.414026 and 5.540580, a 25.5% difference, so the map
  from endpoint coefficients to distance is not even well defined -- C5
  FAILS for SPACE, which is the half this project buys.  And that failure
  is why there is a Lambda at all: an endpoint difference needs no
  coefficient, a line integral must carry one, and Lambda is the value of
  that integral -- a logarithm because the integrand goes as 1/r.  Which
  makes provenance.py's verdict structural rather than careless: a path
  integral cannot be ansatz-free the way an endpoint ratio can.  On
  interchangeability M is right and it does not help: (a, R_s, b) enter
  only through X = 2 R_s/sqrt(b^2+a^2), so the surface X = const is
  exactly interchangeable -- and the leverage is logarithmic, a factor of
  ten in Lambda costing a factor of 3e19 in the geometry.  Nothing is
  repaired.  C5 is recorded half-refuted, not corrected.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
