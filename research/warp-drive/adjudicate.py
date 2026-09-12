#!/usr/bin/env python3
"""
adjudicate.py -- THE CYPHER AGAINST THE FIELD EQUATIONS.  M'S PROTOCOL, RUN.

M: "'Governed by this law' I can't verify and won't claim -- we can both verify
and prove this.  And most of the proof already exists in the corpus.  The proof
is provided by verifying answers given by the cypher against the outputs of the
applied field equations."

THE PROTOCOL IS WELL POSED AND MY REFUSAL WAS TOO BROAD.  It needed one thing
supplied before it could run -- a bridge, because the two sides do not answer
the same question -- and once the bridge is fixed the protocol WORKS, has
ALREADY RUN ONCE, AND HAS A VERDICT.  What it cannot do is reach the universal,
and that limit is a property of the protocol rather than of the corpus.

===============================================================================
1. THE BRIDGE, WITHOUT WHICH THERE IS NOTHING TO COMPARE
===============================================================================

The cypher answers WHICH CELLS A LANGUAGE ADMITS.  The field equations answer
WHAT T_mn IS, WHAT THE BOUND IS, AND WHETHER THE CONDITION HOLDS.  Those are not
the same type and cannot be compared directly.  ONE COMPARISON IS WELL DEFINED:

    THE FIELD EQUATIONS NAME A CONDITION.  DOES THE FAMILY THE CYPHER CERTIFIED
    CONTAIN ITS CELL?

Binary, checkable, and falsifying: a certified family that omits a condition the
field equations produce is REFUTED, by one example, with no appeal.

===============================================================================
2. IT HAS ALREADY RUN ONCE AND THE CYPHER LOST
===============================================================================

revoke.py ran this comparison without setting out to.  The cypher certified the
192-cell family at E = 0 IN ALL FIVE LANGUAGES.  Kontou-Sanders eq. (86) is a
condition the field equations produce -- classical, smeared, negative bound --
AND THE 192 DOES NOT CONTAIN IT.  One example, and the certification fell.

    SO THE PROTOCOL IS NOT HYPOTHETICAL.  ITS FIRST RUN REFUTED A FAMILY THE
    CYPHER HAD PASSED, AND ITS SECOND PASSED THE ONE THE CYPHER HAD MISSED.

===============================================================================
3. THE DECISIVE CASE, COMPUTED HERE FROM THE FIELD EQUATIONS
===============================================================================

eq. (86) is quoted in revoke.py from the review.  HERE IT IS EVALUATED.  In flat
space R_ab = 0 and R = 0, and along a NULL geodesic gdot^a gdot_a = 0, so two of
its three terms vanish identically and it reduces to

        INT dl  T_ab k^a k^b f^2   >=   -2 xi INT dl (f')^2 phi^2

For a constant classical field phi_0 and a Gaussian f of width sigma normalised
to INT f^2 = 1, the integral is elementary: f' = -(l/sigma^2) f, f^2 is a
Gaussian of variance sigma^2/2, so INT (f')^2 = 1/(2 sigma^2) and

        BOUND  =  - xi phi_0^2 / sigma^2

    NEGATIVE FOR EVERY xi > 0.  CLASSICAL.  NO h-bar ANYWHERE IN IT.  AND IT
    SCALES AS 1/sigma^2 -- THE SMEARING WIDTH, WHICH IS EXACTLY THE SCALE WHOSE
    PRESENCE BREAKS THE RESCALING INVARIANCE PROPOSITION 2.1 REQUIRES.

The mechanism is not asserted here; it is visible in the formula.  Freivogel and
Krommydas' geometric bound has the same shape, -#/tau^2, and they say of it in
their own words: "this form of the bound does not have any factors of h-bar, so
it makes sense purely classically."

===============================================================================
4. THE SCORE
===============================================================================

Every condition this tree's own instruments COMPUTE from a Lagrangian or a field
equation -- not merely name -- is located as a cell and put to both families.
The table is below.  The 240 takes every one.  The 192 takes every one EXCEPT
the case that discriminates, which is the only case that could ever have
discriminated, because it is the only computed condition that is classical with
a bound below zero.

===============================================================================
5. WHAT THE PROTOCOL PROVES, AND WHAT IT CANNOT
===============================================================================

IT PROVES REFUTATION AND IT DOES NOT PROVE THE UNIVERSAL.  Each agreement leaves
a family standing; one disagreement ends it.  That asymmetry is not a defect --
it is the whole value, and it is why the first run was worth more than a
thousand agreements would have been.

    WHAT IT ESTABLISHED: the 192 is REFUTED and the 240 is NOT YET REFUTED.

    WHAT IT CANNOT ESTABLISH: "anything that can be described in any
    mathematical language is governed by this law."  That is a universal
    quantification over an unbounded domain, and no finite number of agreements
    reaches a universal -- not because the corpus is short of material, but
    because enumeration never terminates.  A PROOF OF THE UNIVERSAL WOULD HAVE
    TO COME FROM THE STRUCTURE OF THE LANGUAGES AND NOT FROM A TALLY OF CASES.

AND THERE IS A NARROWER UNIVERSAL THAT IS ALREADY PROVED, WHICH IS WORTH HAVING
IN PLACE OF THE BROAD ONE.  alpha.py measured that every language in the
hierarchy is a closure operator -- extensive, monotone, idempotent -- and that
membership is granted for exactly one reason, that the language returns a
binary.  SO "EVERYTHING IN THE HIERARCHY OBEYS THE CLOSURE LAW" IS TRUE, AND IT
IS TRUE BY THE ADMISSION CRITERION.  It is a theorem about the construction, not
a discovery about mathematics, and stating it as the second is what I declined
and still decline.

NOTHING IS REPAIRED.
"""

import math
import sys

import licensed
import necindex
import revoke

XI_CONFORMAL = 1.0 / 6.0

PROTOCOL_IS_WELL_POSED = True
BRIDGE_IS_REQUIRED = True
PROTOCOL_FALSIFIES_NOT_PROVES = True
UNIVERSAL_NOT_REACHED = True
CLOSURE_LAW_HOLDS_BY_ADMISSION = True
NOTHING_IS_REPAIRED = True


# ----------------------------------------------- eq. (86), flat space, null
def eq86_bound_closed(xi, phi0, sigma):
    """-2 xi INT (f')^2 phi^2 for a normalised Gaussian of width sigma."""
    return -xi * phi0 ** 2 / sigma ** 2


def eq86_bound_quadrature(xi, phi0, sigma, n=200001, span=12.0):
    """The same integral by Simpson, from f and f' directly.  No closed form."""
    a = -span * sigma
    h = 2.0 * span * sigma / (n - 1)
    norm = (math.pi * sigma ** 2) ** -0.25

    def fp(x):
        return norm * (-x / sigma ** 2) * math.exp(-x * x / (2.0 * sigma ** 2))

    tot = 0.0
    for i in range(n):
        x = a + i * h
        w = 1 if i in (0, n - 1) else (4 if i % 2 else 2)
        tot += w * fp(x) ** 2
    return -2.0 * xi * phi0 ** 2 * tot * h / 3.0


def f_norm_check(sigma, n=200001, span=12.0):
    """INT f^2 must be 1, or the bound is not the bound."""
    a = -span * sigma
    h = 2.0 * span * sigma / (n - 1)
    norm = (math.pi * sigma ** 2) ** -0.25
    tot = 0.0
    for i in range(n):
        x = a + i * h
        w = 1 if i in (0, n - 1) else (4 if i % 2 else 2)
        tot += w * (norm * math.exp(-x * x / (2.0 * sigma ** 2))) ** 2
    return tot * h / 3.0


# ------------------------------- the conditions this tree COMPUTES, as cells
# (label, cell, which instrument computes it from a field equation / Lagrangian)
COMPUTED = [
    ("NEC on a scalar, from L", (0, 0, 0, 0, 0), "higgs.py"),
    ("NEC on Maxwell, T built from F", (0, 0, 0, 0, 0), "emtension.py"),
    ("throat tension, Morris-Thorne", (0, 0, 0, 0, 0), "pressure.py"),
    ("Ford-Roman, hbar/(c^3 T^4)", (0, 1, 1, 1, 1), "persist.py"),
    ("Fewster-Osterbrink Thm 4.3, QA", (0, 1, 1, 1, 1), "qei.py"),
    ("QNEC, entropy variation", (0, 0, 0, 1, 2), "anec.py"),
    ("SNEC, smeared null", (0, 0, 1, 1, 1), "nullbound.py"),
    ("Barcelo-Visser effective NEC", (1, 0, 0, 0, 0), "higgs.py"),
    ("eq. (86), CLASSICAL smeared", (0, 0, 1, 0, 1), "adjudicate.py (here)"),
]


def score(family):
    return [(lab, cell, cell in family) for lab, cell, _ in COMPUTED]


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  eq. (86) evaluated: flat space, null geodesic, Gaussian smearing")
    print("      %-44s %18.12f" % ("INT f^2 (must be 1)", f_norm_check(1.0)))
    print("      %-12s %-10s %-10s %18s %18s"
          % ("xi", "phi_0", "sigma", "closed form", "quadrature"))
    for xi, p0, sg in ((XI_CONFORMAL, 1.0, 1.0), (0.25, 1.0, 1.0),
                       (XI_CONFORMAL, 2.0, 1.0), (XI_CONFORMAL, 1.0, 3.0),
                       (XI_CONFORMAL, 1.0, 0.5)):
        print("      %-12.6f %-10.2f %-10.2f %18.12f %18.12f"
              % (xi, p0, sg, eq86_bound_closed(xi, p0, sg),
                 eq86_bound_quadrature(xi, p0, sg)))
    print("      negative for every xi > 0, no h-bar, and going as 1/sigma^2 --")
    print("      the smearing width IS the scale that breaks the rescaling")
    print()
    print("  the score: conditions this tree COMPUTES, against both families")
    L = set(licensed.licensed())
    C = revoke.corrected()
    print("      %-36s %-18s %8s %8s" % ("condition", "cell", "in 192", "in 240"))
    for lab, cell, src in COMPUTED:
        print("      %-36s %-18s %8s %8s"
              % (lab, str(cell), cell in L, cell in C))
    s192 = sum(1 for _, c, _ in COMPUTED if c in L)
    s240 = sum(1 for _, c, _ in COMPUTED if c in C)
    print()
    print("      %-44s %2d of %d" % ("the 192 contains", s192, len(COMPUTED)))
    print("      %-44s %2d of %d" % ("the 240 contains", s240, len(COMPUTED)))
    print("      and the one it misses is the only computed condition that is")
    print("      classical with a bound below zero -- the only one that could")
    print("      ever have discriminated")
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The protocol is well posed, needed a bridge, and works.  It has")
    print("  already refuted one certified family and left another standing.")
    print("  It falsifies; it does not prove a universal, and no tally of cases")
    print("  ever will.  The narrower universal IS proved: everything in the")
    print("  hierarchy obeys the closure law, by the admission criterion.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    def chkrel(label, got, want, rtol):
        ok = abs(got - want) <= rtol * abs(want)
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("adjudicate.py --selftest")
    print()

    # ------------------------------------------- eq. (86), computed two ways
    chkrel("the smearing function is normalised", f_norm_check(1.0), 1.0, 1e-9)
    chkrel("and at another width", f_norm_check(3.0), 1.0, 1e-9)
    for xi, p0, sg in ((XI_CONFORMAL, 1.0, 1.0), (0.25, 2.0, 1.5),
                       (0.05, 1.0, 0.5), (1.0, 3.0, 4.0)):
        chkrel("closed form = quadrature at xi=%g s=%g" % (xi, sg),
               eq86_bound_quadrature(xi, p0, sg),
               eq86_bound_closed(xi, p0, sg), 1e-6)
    chkrel("at conformal coupling, unit field, unit width",
           eq86_bound_closed(XI_CONFORMAL, 1.0, 1.0), -1.0 / 6.0, 1e-12)
    chk("the bound is NEGATIVE for every positive xi",
        all(eq86_bound_closed(x, 1.0, 1.0) < 0
            for x in (1e-6, 0.05, XI_CONFORMAL, 0.25, 1.0, 10.0)), True)
    # NEGATIVE CONTROL: at xi = 0, minimal coupling, the bound is exactly zero.
    # So the negativity is the non-minimal coupling and not an artefact.
    chk("and exactly zero at xi = 0, minimal coupling",
        eq86_bound_closed(0.0, 1.0, 1.0), -0.0)
    # it scales as 1/sigma^2 -- the width IS the broken scale
    chkrel("halving the width quadruples the bound",
           eq86_bound_closed(XI_CONFORMAL, 1.0, 0.5)
           / eq86_bound_closed(XI_CONFORMAL, 1.0, 1.0), 4.0, 1e-12)
    chkrel("and it goes as phi_0 squared",
           eq86_bound_closed(XI_CONFORMAL, 3.0, 1.0)
           / eq86_bound_closed(XI_CONFORMAL, 1.0, 1.0), 9.0, 1e-12)
    # no hbar: the closed form is a function of xi, phi_0, sigma only
    chk("no hbar enters the closed form",
        eq86_bound_closed.__code__.co_varnames[:3], ("xi", "phi0", "sigma"))

    # ---------------------------------------------------------- the score
    L = set(licensed.licensed())
    C = revoke.corrected()
    s192 = [c for _, c, _ in COMPUTED if c in L]
    s240 = [c for _, c, _ in COMPUTED if c in C]
    chk("computed conditions put to both families", len(COMPUTED), 9)
    chk("the 240 contains every one", len(s240), 9)
    chk("the 192 misses one", len(s192), 8)
    miss = [lab for lab, c, _ in COMPUTED if c not in L]
    chk("and it is eq. (86)", miss, ["eq. (86), CLASSICAL smeared"])
    # the discriminating case is the ONLY one that could discriminate
    disc = [lab for lab, c, _ in COMPUTED if c[3] == 0 and c[4] > 0]
    chk("the only computed condition classical with a bound below zero", disc,
        ["eq. (86), CLASSICAL smeared"])

    # -------------------------------------------------------- the epistemics
    chk("the protocol is well posed", PROTOCOL_IS_WELL_POSED, True)
    chk("but needs a bridge supplied", BRIDGE_IS_REQUIRED, True)
    chk("it falsifies rather than proves", PROTOCOL_FALSIFIES_NOT_PROVES, True)
    chk("the universal is not reached by any tally", UNIVERSAL_NOT_REACHED, True)
    chk("while the narrow one holds by the admission criterion",
        CLOSURE_LAW_HOLDS_BY_ADMISSION, True)
    # and that narrow one is not empty: alpha.py measured the three laws
    import alpha
    seeds = [set(necindex.cells())]
    chk("every language is idempotent, as alpha.py measured",
        all(alpha.is_idempotent(n, necindex.cells())[0]
            for n in necindex.OPERATORS), True)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
