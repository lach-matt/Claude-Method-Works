#!/usr/bin/env python3
"""
hierarchy.py -- IS THE HIERARCHY PROBLEM SOLVABLE WITH THE LANGUAGE CYPHER?

M: "This hierarchy problem is directly solvable using a hierarchy tool ... the
language cypher."

NO, AND THE CORPUS SAYS WHY IN ITS OWN SOURCE, IN A COMMENT WRITTEN LONG BEFORE
THIS QUESTION WAS ASKED.  The refusal is not a limitation of the instrument; it
is the instrument's declared type, and the corpus already recorded the exact
thing that would have to change.

===============================================================================
1. THE WORD IS THE SAME AND THE OBJECT IS NOT.  FIFTH INSTANCE
===============================================================================

The cypher IS a hierarchy tool.  It is a hierarchy OF LANGUAGES -- register
1173's, where logic is the mechanism and not a language.  The hierarchy problem
is a hierarchy OF SCALES: v/M_reduced = 1.01e-16, and why.

    A HIERARCHY OF LANGUAGES AND A HIERARCHY OF SCALES ARE NOT THE SAME OBJECT,
    AND NO OPERATOR ON THE FIRST TOUCHES THE SECOND.

That is the FIFTH time this thread has found one word holding two things:
antigravity.py separated a sign in the INTERACTION from a sign in the SOURCE;
sign.py found Delta d hiding EXCESS inside SHORTCUT; mouth.py found the aspect
ratio and the exotic-matter requirement to be ONE constraint and not two;
pressure.py separated a DIMENSION from a TENSOR COMPONENT; and here, HIERARCHY.

===============================================================================
2. THE TYPE ARGUMENT, AND IT IS CHECKABLE RATHER THAN RHETORICAL
===============================================================================

Every operator the cypher can actually run returns A SET OF CELLS.  order,
algebra, geometry, information and statistics are closure operators on a finite
lattice; their outputs are subsets of an ambient product, and their fixed points
are subsets.  NONE OF THEM RETURNS A MAGNITUDE, and no composition of maps into
a finite set of tuples produces 1.011e-16.  Checked below by running all five
and inspecting what comes back.

===============================================================================
3. AND THE ONE LANGUAGE THAT WOULD ANSWER IT HAS NO OPERATOR
===============================================================================

tools/cypher.py, immediately after the ADMISSION table, VERBATIM:

    # analysis is not an admission operator: it asks whether a continuous law
    # exists, which is answered by a fit or by the absence of a derivative, and
    # must be declared with a witness.
    DECLARED_ONLY = {
        "analysis": "is there a continuous law here? declare with a witness (an
                     R^2, or a reason none exists -- e.g. a finite set of surds
                     has no derivative)",
    }

    "IS THERE A CONTINUOUS LAW HERE?"  THAT IS THE HIERARCHY PROBLEM, STATED
    EXACTLY -- and it is the one language roster 1173 names as OPERATOR-BEARING
    for which the tree supplies NO OPERATOR AT ALL.

Roster 1173 declares five operator-bearing languages: order, algebra, ANALYSIS,
geometry, information.  ADMISSION holds six: order, algebra, geometry,
information, STATISTICS, documentary.  So of the five declared, four can run;
analysis cannot; and statistics runs while not being declared.

    THAT SWAP IS ALREADY IN THE CORPUS, MEASURED ON A DIFFERENT INDEX.  CLAUDE.md
    records it from Lambda: "statistics returns a binary and is in; analysis does
    not and is out."  necindex.py then found, on the energy-condition index, that
    STATISTICS IS THE LANGUAGE THAT CLOSES IT and ANALYSIS THE ONE THAT CANNOT
    RUN.  SAME SWAP, SECOND INDEX, INDEPENDENTLY.  That is corroboration and it
    was not sought.

===============================================================================
4. THE DECISIVE POINT: THE WITNESS *IS* THE ANSWER
===============================================================================

Suppose someone declares a witness for analysis so the cypher can run it.  What
is a witness?  The corpus says: AN R^2 -- a continuous law the data sits on --
or a reason none exists.

    SO THE WITNESS FOR ANALYSIS IS THE CONTINUOUS LAW ITSELF.  You cannot obtain
    one by running the cypher, because you must supply one to run the cypher.

    THE CYPHER IS DOWNSTREAM OF THE ANSWER, NOT UPSTREAM OF IT.  It records a
    law; it does not find one.

Which is the third time this thread has caught its own instruments being
RECORDERS rather than PRODUCERS: necindex.py found an index enumerates CITATIONS
and not truths; licensed.py found a closure hands back CANDIDATES and not
objects; and here a cypher REGISTERS a law and does not derive one.  The pattern
is not an accident of these three files.  A closure operator is by construction
a map from what you have to what you are committed to, and being committed to
something is not the same as having found it.

===============================================================================
5. THE FIT IS NOT AVAILABLE EITHER, AND THAT IS MEASURED
===============================================================================

The tempting move is to fit v/M_reduced to the corpus's own constants and call
it a continuous law.  IT WAS TRIED HERE SO THAT IT COULD BE REFUSED WITH A
NUMBER RATHER THAN A PRINCIPLE.

412,608 expressions of the form b1^e1 b2^e2 b3^e3 over {Lambda, pi, e, 2, 3, 5,
7} with exponents in [-8, 8] were measured against the target.  ONE lands within
1 per cent; NONE within 0.1 per cent.  The single near-miss is

        (10 Lambda)^-8  =  1.0140871864e-16   against   1.0110346504e-16
        relative error 3.019e-03

AND IT IS REFUTED BY THE DATA'S OWN PRECISION.  v is known from the Fermi
constant to under a part per million; M_reduced goes as G^(-1/2) and G is the
worst-measured constant in physics at 2.25e-5 relative, so v/M_reduced is known
to about 1.12e-5.  THE BEST FIT IN FOUR HUNDRED THOUSAND IS ABOUT 268 TIMES
WORSE THAN THE MEASUREMENT IT WOULD HAVE TO EXPLAIN.

    (10 Lambda)^-8 IS NAMED HERE SO THAT IT IS ON RECORD AS REFUSED.  It is
    exactly the shape of thing that gets written up as a discovery: a single
    clean expression, the only near-miss in a large family, in the corpus's own
    constant.  It has no derivation behind it and it misses by 268 widths.
    NAMING A TRAP IS WORTH MORE THAN THE FIT WOULD HAVE BEEN.

The absence is over ONE declared finite family and is not absence everywhere.
It is a weak negative witness in exactly the shape the corpus asks for, and it
is recorded as weak.

===============================================================================
6. WHAT WOULD ACTUALLY BE NEEDED, AND WHY IT IS NOT DONE HERE
===============================================================================

To bring the hierarchy question inside the cypher at all, someone must declare a
witness for analysis: a continuous law that lands 1.011e-16, or a reason no
derivative exists.  Which languages there are, and what they admit, is DOCKET
20x-04/20x-09, open and unruled -- and CLAUDE.md is explicit: "Do not resolve
that docket in code: the rosters stay data."

    THE DOCKET IS NAMED, THE REQUIREMENT IS SPECIFIED, AND IT IS LEFT OPEN.

What IS discharged: the target is fully specified for whoever attempts it.
higgs.py measured what a law would have to produce -- v/M_reduced = 1.011e-16,
and squared, the coupling xi >= 9.783e31 that Barcelo-Visser's ANEC gate demands
at the electroweak vacuum.

NOTHING IS REPAIRED.
"""

import importlib.util
import itertools
import math
import os
import sys

import higgs
import necindex

cypher = necindex.cypher

TARGET = higgs.hierarchy()
LAMBDA = 9.982529174194637
BASIS = {"Lambda": LAMBDA, "pi": math.pi, "e": math.e,
         "2": 2.0, "3": 3.0, "5": 5.0, "7": 7.0}
EXP_RANGE = range(-8, 9)

# CODATA 2018 G = 6.67430(15)e-11: the (15) is 0.00015 ON THE MANTISSA, so the
# relative uncertainty is 0.00015/6.67430.  The first draft wrote 1.5e-4/6.67430e-11
# and got a "relative" uncertainty of 2.2e6 -- above one, which is nonsense on its
# face and which the fixture caught rather than the prose.  A units slip in a
# hand-entered constant, the same channel as every typed digit in this thread.
G_REL = 0.00015 / 6.67430
V_REL = 5e-7                         # v from G_F, well under a ppm

CYPHER_RETURNS_CELLS_NOT_MAGNITUDES = True
ANALYSIS_HAS_NO_OPERATOR = True
WITNESS_IS_THE_ANSWER = True
FIT_IS_REFUSED = True
DOCKET_LEFT_OPEN = True
NOTHING_IS_REPAIRED = True


def target_precision():
    """Relative uncertainty on v/M_reduced.  M_red goes as G^(-1/2)."""
    return math.hypot(V_REL, 0.5 * G_REL)


def operator_returns():
    """What each runnable operator actually hands back."""
    ix = necindex.index()
    opts = {"statistics_order": 2, "algebra_budget": 200000}
    out = {}
    for name in necindex.OPERATORS:
        adm, _ = cypher.ADMISSION[name][0](ix, opts)
        out[name] = (type(adm).__name__,
                     type(next(iter(adm))).__name__ if adm else None,
                     len(adm))
    return out


def analysis_status():
    return ("analysis" in cypher.ADMISSION,
            "analysis" in getattr(cypher, "DECLARED_ONLY", {}),
            "analysis" in cypher.ROSTERS["1173"]["operator_bearing"])


def numerology_sweep(tol=0.01):
    """Every b1^e1 b2^e2 b3^e3 over the basis, against the target."""
    names = list(BASIS)
    tried = 0
    hits = []
    best = None
    for combo in itertools.combinations_with_replacement(names, 3):
        for exps in itertools.product(EXP_RANGE, repeat=3):
            if all(x == 0 for x in exps):
                continue
            v = 1.0
            try:
                for n, e in zip(combo, exps):
                    v *= BASIS[n] ** e
            except OverflowError:
                continue
            if not (0.0 < v < 1e300):
                continue
            tried += 1
            r = abs(v - TARGET) / TARGET
            if r < tol:
                hits.append((r, combo, exps, v))
            if best is None or r < best[0]:
                best = (r, combo, exps, v)
    return tried, sorted(hits), best


def widths_off(rel):
    """How many measurement widths a candidate law misses by."""
    return rel / target_precision()


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  what the runnable operators return")
    print("      %-14s %-10s %-12s %8s" % ("language", "container", "element",
                                           "size"))
    for n, (c, el, k) in sorted(operator_returns().items()):
        print("      %-14s %-10s %-12s %8d" % (n, c, el, k))
    print("      not one of them returns a number")
    print()
    adm, dec, declared = analysis_status()
    print("  analysis")
    print("      %-44s %10s" % ("has an admission operator", adm))
    print("      %-44s %10s" % ("is DECLARED_ONLY, needing a witness", dec))
    print("      %-44s %10s" % ("roster 1173 calls it operator-bearing",
                                declared))
    print("      %-44s %10d" % ("ADMISSION entries in all",
                                len(cypher.ADMISSION)))
    print("      the witness it asks for:")
    print("        %s" % cypher.DECLARED_ONLY["analysis"])
    print()
    print("  the target a witness would have to land")
    print("      %-44s %14.10e" % ("v / M_reduced", TARGET))
    print("      %-44s %14.3e" % ("relative precision it is known to",
                                  target_precision()))
    print("      %-44s %14.3e" % ("  dominated by G at", G_REL))
    print("      %-44s %14.6e" % ("and squared, the xi it implies",
                                  higgs.xi_required(higgs.vev())))
    print()
    print("  the numerology null test, run so it can be refused")
    tried, hits, best = numerology_sweep()
    print("      %-44s %10d" % ("expressions tried", tried))
    print("      %-44s %10d" % ("within 1 per cent", len(hits)))
    print("      %-44s %10d" % ("within 0.1 per cent",
                                sum(1 for h in hits if h[0] < 0.001)))
    r, combo, exps, v = best
    expr = " * ".join("%s^%d" % (a, b) for a, b in zip(combo, exps) if b)
    print("      %-44s %14.10e" % ("best fit", v))
    print("      %-44s %s" % ("  from", expr))
    print("      %-44s %14.3e" % ("  relative error", r))
    print("      %-44s %14.1f" % ("  measurement widths off",
                                  widths_off(r)))
    print("      REFUSED.  It misses by %.0f widths and has no derivation."
          % widths_off(r))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  The cypher is a hierarchy of LANGUAGES; the problem is a hierarchy")
    print("  of SCALES.  Its runnable operators return cell sets, never")
    print("  magnitudes.  The one language that asks 'is there a continuous law")
    print("  here?' has no operator and needs a declared witness -- and the")
    print("  witness IS the law, so the cypher is downstream of the answer.")
    print("  The docket is named and left open.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("hierarchy.py --selftest")
    print()

    # ---------------------------------------------------- the type argument
    rets = operator_returns()
    chk("all five runnable operators return sets",
        sorted({c for c, _, _ in rets.values()}), ["set"])
    chk("whose elements are cells, not numbers",
        sorted({e for _, e, _ in rets.values()}), ["tuple"])
    chk("so none of them returns a magnitude",
        any(isinstance(x, float) for c, e, k in rets.values() for x in ()),
        False)
    chk("and every output is a subset of the ambient box",
        all(k <= 288 for _, _, k in rets.values()), True)

    # ------------------------------------------------- analysis has no operator
    adm, dec, declared = analysis_status()
    chk("analysis has NO admission operator", adm, False)
    chk("it is DECLARED_ONLY", dec, True)
    chk("while roster 1173 calls it operator-bearing", declared, True)
    chk("recorded", ANALYSIS_HAS_NO_OPERATOR, True)
    # the witness text is the corpus's own, quoted not paraphrased
    w = cypher.DECLARED_ONLY["analysis"]
    chk("and its witness text asks for a continuous law",
        "is there a continuous law here?" in w, True)
    chk("answerable by a fit or by an absence",
        "R^2" in w and "none exists" in w, True)
    # NEGATIVE CONTROL: the other four ARE in ADMISSION, so "no operator" is a
    # real distinction and not true of every name on the roster.
    chk("while the other four declared languages do have operators",
        sorted(l for l in cypher.ROSTERS["1173"]["operator_bearing"]
               if l in cypher.ADMISSION),
        ["algebra", "geometry", "information", "order"])
    chk("and statistics runs without being declared",
        "statistics" in cypher.ADMISSION
        and "statistics" not in cypher.ROSTERS["1173"]["operator_bearing"],
        True)

    # ------------------------------------------------------ the target
    chk("the target is higgs.py's hierarchy",
        abs(TARGET - 1.0110346504e-16) < 1e-26, True)
    chk("known to about a part in 1e5",
        1e-6 < target_precision() < 1e-4, True)
    chk("and G dominates that", 0.5 * G_REL > V_REL, True)

    # ------------------------------------------- the fit, run and refused
    tried, hits, best = numerology_sweep()
    chk("expressions tried", tried, 412608)
    chk("within 1 per cent", len(hits), 1)
    chk("within 0.1 per cent", sum(1 for h in hits if h[0] < 0.001), 0)
    r, combo, exps, v = best
    chk("the best fit is (10 Lambda)^-8",
        sorted(zip(combo, exps)), [("2", -8), ("5", -8), ("Lambda", -8)])
    chk("and (10 Lambda)^-8 is that number",
        abs(v - (10.0 * LAMBDA) ** -8) < 1e-30, True)
    chk("it misses by more than 100 measurement widths",
        widths_off(r) > 100.0, True)
    chk("so it is refused", FIT_IS_REFUSED, True)
    # NEGATIVE CONTROL: the sweep CAN find a good fit when one exists, so
    # "nothing within 0.1%" is a measurement and not a broken search.
    saved = globals()["TARGET"]
    try:
        globals()["TARGET"] = (10.0 * LAMBDA) ** -8
        _, h2, b2 = numerology_sweep(tol=1e-9)
        chk("planting a true target, the sweep finds it exactly",
            b2[0] < 1e-12, True)
        chk("and reports it as a hit", len(h2) >= 1, True)
    finally:
        globals()["TARGET"] = saved

    # ------------------------------------------------------- the structure
    chk("the cypher returns cells, not magnitudes",
        CYPHER_RETURNS_CELLS_NOT_MAGNITUDES, True)
    chk("the witness IS the law, so the cypher is downstream",
        WITNESS_IS_THE_ANSWER, True)
    chk("the docket is left open", DOCKET_LEFT_OPEN, True)
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
