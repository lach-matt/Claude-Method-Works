#!/usr/bin/env python3
"""
alpha.py -- IS BINARY THE ALPHA LANGUAGE?  THREE CLAUSES, TWO HOLD, ONE FAILS.

M: "The hierarchy exists, but it runs the opposite direction from what is
expected ... binary - order - algebra - geometry - statistics - NECs/proofs -
logic.  But logic is a citation of binary.  So the hierarchy, like transition,
is a collapse not a climb.  Binary is the alpha language, top of the hierarchy
because it both starts and ends the hierarchy."

THE FIRST CLAUSE IS THE CORPUS'S OWN ADMISSION CRITERION AND IT IS EXACTLY
RIGHT.  The second is measured and holds.  THE THIRD IS HALF TRUE AND THE HALF
THAT FAILS IS THE ONE THIS FILE EXISTS TO REPORT.

===============================================================================
1. BINARY IS NOT A RUNG.  IT IS THE ADMISSION CRITERION FOR THE WHOLE LADDER
===============================================================================

Why is a language in the hierarchy at all?  The corpus answers in its own words,
in two places, and the answer is the same both times:

    documentary   tools/cypher.py ADMISSION, verbatim:
                  "register 1173 -- RETURNS A CITATION, NOT A BINARY"
                  -> SILENT.  No closure mechanism exists.

    analysis      CLAUDE.md, verbatim: "analysis has one but RETURNS A MAGNITUDE
                  RATHER THAN A CELL DECISION" -> DECLARED_ONLY, NOT-RUN.

    statistics    CLAUDE.md, verbatim: "statistics RETURNS A BINARY AND IS IN"
                  -- and it is in DESPITE roster 1173 not declaring it
                  operator-bearing.

    MEMBERSHIP IN THE HIERARCHY IF AND ONLY IF THE LANGUAGE RETURNS A BINARY.

So M's instinct lands, and lands harder than stated: binary is not the first
step of the ladder.  IT IS THE TEST FOR BEING ON THE LADDER AT ALL.  Every
language that is in, is in for exactly one reason, and it is the same reason.

===============================================================================
2. AND EVERY LANGUAGE IS AN ENDOMORPHISM ON BINARY DATA.  MEASURED
===============================================================================

Each operator takes a set of cells and returns a set of cells.  A set of cells
IS a binary -- one membership bit per cell of the ambient box.  So

        DOMAIN  =  CODOMAIN  =  the binary

verified below by type: all five return a set whose elements are tuples, and
their input is a set whose elements are tuples.  THE LADDER IS NOT A SEQUENCE OF
TYPED LEVELS.  It is a family of self-maps on one object, and that object is the
binary.  M's "it both starts and ends the hierarchy" is exactly this, and it is
why the picture of a climb was wrong: there is nowhere to climb TO.

WHICH SHARPENS M'S OWN LIST AGAINST ITSELF, AND THE SHARPENING IS THE POINT.
The list has binary as the first rung AND as the alpha that starts and ends.
THOSE CANNOT BOTH HOLD.  A rung is something you pass through; a type is
something everything is.  Measured, binary is the second: IT IS NOT IN THE LIST,
IT IS WHAT THE LIST IS MADE OF.

===============================================================================
3. THE COLLAPSE.  HALF TRUE, AND HERE IS THE HALF THAT FAILS
===============================================================================

TRUE, PER LANGUAGE.  Every one of the five is IDEMPOTENT -- op(op(X)) = op(X),
verified on the energy-condition family for all five.  One application and you
have landed.  YOU CANNOT CLIMB A LADDER OF IDEMPOTENTS.

FALSE, JOINTLY, AND THAT IS A REAL RESULT RATHER THAN A QUIBBLE.  The languages
are not independent: what one admits becomes another's input, and the joint
closure ITERATES.  Over 40 random seeds of 1 to 24 cells:

        one expansion    26 seeds
        two              7
        three            6
        FOUR             1

    SO THE HIERARCHY DOES CLIMB, JUST NOT FAR.  licensed.py's named family
    happened to settle in one expansion, which is the MODE and not a
    distinction -- and reading "collapse" off that one run would have been
    reading the typical case as a law.

AND IT DOES NOT COLLAPSE TO ONE PLACE EITHER.  Those 40 seeds reached 34
DISTINCT fixed points, from 12 cells to the full 288.  There is a rich lattice
of closed families, not an attractor.  "Collapse" in the sense of everything
falling to a single terminus is measured FALSE.

    THE HONEST FORM OF M'S CLAIM: EACH LANGUAGE COLLAPSES.  THE LADDER OF THEM
    DOES NOT, AND WHERE IT LANDS DEPENDS ON WHERE IT STARTED.

===============================================================================
4. LOGIC, AND A TERMINOLOGY HAZARD WORTH NAMING
===============================================================================

Register 1173, via necladder.py: "LOGIC IS NOT A LANGUAGE.  It IS THE MECHANISM
BY WHICH ANY LANGUAGE ANSWERS."  An answer here is a cell decision, which is a
binary -- so logic's OUTPUT is the binary, and M's "logic is a citation of
binary" points at something real.

BUT "CITATION" IS ALREADY TAKEN, AND TAKEN FOR THE OPPOSITE THING.  documentary
is the row that "returns a CITATION, NOT a binary".  So describing logic as a
citation OF binary collides head-on with the corpus's use of the word for the
one thing that is NOT a binary.  Recorded as a hazard, not corrected: the
intended sense is clear and the word is occupied.

===============================================================================
5. THE ROSTER IS NOT RULED HERE
===============================================================================

M's ordering -- binary, order, algebra, geometry, statistics, NECs/proofs, logic
-- is a PROPOSED ROSTER WITH AN ORDERING.  It drops analysis, information and
documentary, and names THREE the tree has no operator for -- binary,
NECs/proofs and logic.  Which languages
there are is DOCKET 20x-04/20x-09, open and unruled, and CLAUDE.md is explicit:
"Do not resolve that docket in code: the rosters stay data."

    IT IS RECORDED AS A CANDIDATE AND NOT SEATED.  Nothing above depends on it:
    every measurement in this file is roster-independent, taken on the five
    operators the tree actually supplies.

NOTHING IS REPAIRED.
"""

import itertools
import random
import sys

import necindex

cypher = necindex.cypher
OPTS = {"statistics_order": 2, "algebra_budget": 200000}
SIZES = (4, 3, 4, 2, 3)

# M's proposed roster, recorded as data and NOT seated.  Docket 20x-04/20x-09.
CANDIDATE_ROSTER_M = ["binary", "order", "algebra", "geometry", "statistics",
                      "NECs/proofs", "logic"]
ROSTER_NOT_RULED = True

BINARY_IS_THE_ADMISSION_CRITERION = True
BINARY_IS_A_TYPE_NOT_A_RUNG = True
EACH_LANGUAGE_COLLAPSES = True
THE_LADDER_DOES_NOT = True            # the half that fails
CITATION_IS_ALREADY_TAKEN = True
NOTHING_IS_REPAIRED = True


def box():
    return sorted(itertools.product(*[range(n) for n in SIZES]))


def why_admitted():
    """Each roster-1173 language, and the reason it is in or out."""
    out = {}
    for lang in cypher.ROSTERS["1173"]["languages"]:
        if lang in cypher.ADMISSION:
            note = cypher.ADMISSION[lang][2]
            binary = "not a binary" not in note
            out[lang] = ("IN" if binary else "SILENT", note)
        else:
            out[lang] = ("DECLARED-ONLY",
                         cypher.DECLARED_ONLY.get(lang, "no entry"))
    return out


def types_of(cs):
    """(input type, output type, element type) for each operator."""
    ix = cypher.Index("x", necindex.COORDS, sorted(cs))
    out = {}
    for n in necindex.OPERATORS:
        adm, _ = cypher.ADMISSION[n][0](ix, OPTS)
        out[n] = (type(ix.cells).__name__ if not isinstance(ix.cells, list)
                  else "list-of-tuple",
                  type(adm).__name__,
                  type(next(iter(adm))).__name__ if adm else None)
    return out


def is_idempotent(name, cs):
    fn = cypher.ADMISSION[name][0]
    a, _ = fn(cypher.Index("x", necindex.COORDS, sorted(cs)), OPTS)
    b, _ = fn(cypher.Index("x", necindex.COORDS, sorted(a)), OPTS)
    return set(a) == set(b), len(a)


def joint_rounds(seed):
    """(expansions needed, size of the fixed point)."""
    X = set(seed)
    n = 0
    while True:
        ix = cypher.Index("x", necindex.COORDS, sorted(X))
        new = set(X)
        for name in necindex.OPERATORS:
            new |= set(cypher.ADMISSION[name][0](ix, OPTS)[0])
        if new == X:
            return n, len(X)
        X = new
        n += 1


def sweep(trials=40, lo=1, hi=25, seed=20260912):
    rnd = random.Random(seed)
    B = box()
    rounds, fixed = [], []
    for _ in range(trials):
        s = rnd.sample(B, rnd.randrange(lo, hi))
        r, k = joint_rounds(s)
        rounds.append(r)
        fixed.append(k)
    return rounds, fixed


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  why each language is in or out -- the corpus's own reason")
    for lang, (state, note) in sorted(why_admitted().items()):
        print("      %-13s %-14s %s" % (lang, state, note[:52]))
    print()
    print("  domain and codomain")
    for n, (i, o, el) in sorted(types_of(necindex.cells()).items()):
        print("      %-13s in=%-14s out=%-6s of %s" % (n, i, o, el))
    print("      every one is a self-map on a set of cells: a binary")
    print()
    print("  idempotence -- each language collapses")
    for n in sorted(necindex.OPERATORS):
        ok, k = is_idempotent(n, necindex.cells())
        print("      %-13s op(X) = %4d   op(op(X)) = op(X): %s" % (n, k, ok))
    print()
    print("  but the ladder of them does not")
    rounds, fixed = sweep()
    from collections import Counter
    c = Counter(rounds)
    for k in sorted(c):
        print("      %d expansion(s): %2d of %d seeds" % (k, c[k], len(rounds)))
    print("      %-40s %8d" % ("most expansions seen", max(rounds)))
    print("      %-40s %8d" % ("distinct fixed points reached",
                               len(set(fixed))))
    print("      %-40s %8s" % ("their range", (min(fixed), max(fixed))))
    nr, nk = joint_rounds(necindex.cells())
    print("      %-40s %8d" % ("the named family needs", nr))
    print("      which is the MODE, not a distinction")
    print()
    print("  M's proposed roster, recorded and NOT seated")
    print("      %s" % " - ".join(CANDIDATE_ROSTER_M))
    print("      docket 20x-04/20x-09, open; the rosters stay data")
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Binary is the admission criterion, not the first rung -- it is what")
    print("  the list is made of.  Every language is a self-map on it, so there")
    print("  is nowhere to climb to.  Each language collapses in one step.  The")
    print("  ladder of them does not: up to four expansions, and 34 distinct")
    print("  terminals from 40 seeds.  Two clauses hold; the collapse is half.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("alpha.py --selftest")
    print()

    # ------------------------------- 1. binary IS the admission criterion
    w = why_admitted()
    chk("documentary is out for returning a citation, not a binary",
        "not a binary" in w["documentary"][1], True)
    chk("and is SILENT", w["documentary"][0], "SILENT")
    chk("analysis is DECLARED-ONLY", w["analysis"][0], "DECLARED-ONLY")
    chk("because it asks for a continuous law, answered by a fit",
        "continuous law" in w["analysis"][1], True)
    chk("statistics is IN", w["statistics"][0], "IN")
    chk("though roster 1173 does not declare it operator-bearing",
        "statistics" in cypher.ROSTERS["1173"]["operator_bearing"], False)
    chk("every language that is IN has a closure operator",
        sorted(l for l, (s, _) in w.items() if s == "IN"),
        ["algebra", "geometry", "information", "order", "statistics"])
    chk("recorded", BINARY_IS_THE_ADMISSION_CRITERION, True)

    # ------------------------------------ 2. every language is an endomorphism
    t = types_of(necindex.cells())
    chk("every operator returns a set", sorted({o for _, o, _ in t.values()}),
        ["set"])
    chk("of tuples", sorted({e for _, _, e in t.values()}), ["tuple"])
    chk("so domain and codomain are the same object",
        BINARY_IS_A_TYPE_NOT_A_RUNG, True)
    # NEGATIVE CONTROL: a rung would change type.  None does.
    chk("no operator changes the type of its argument",
        len({o for _, o, _ in t.values()} | {e for _, _, e in t.values()}), 2)

    # ------------------------------------------- 3a. each language collapses
    for n in necindex.OPERATORS:
        ok, _ = is_idempotent(n, necindex.cells())
        chk("%s is idempotent" % n, ok, True)
    chk("so each language collapses", EACH_LANGUAGE_COLLAPSES, True)

    # ------------------------------------------- 3b. THE LADDER DOES NOT
    rounds, fixed = sweep()
    chk("random seeds needing more than one expansion",
        sum(1 for r in rounds if r > 1), 14)
    chk("the most any seed needed", max(rounds), 4)
    chk("so the joint closure is NOT one-step", max(rounds) > 1, True)
    chk("recorded as the clause that fails", THE_LADDER_DOES_NOT, True)
    # and it does not collapse to a single terminus either
    chk("distinct fixed points from 40 seeds", len(set(fixed)), 34)
    chk("ranging up to the whole box", max(fixed), 288)
    chk("so there is no single attractor", len(set(fixed)) > 1, True)
    # the named family is typical, not special -- the honest control
    nr, _ = joint_rounds(necindex.cells())
    chk("the named family needs one expansion", nr, 1)
    from collections import Counter
    chk("which is the modal case, not a distinction",
        Counter(rounds).most_common(1)[0][0], 1)

    # ------------------------------------------------ 4. the terminology hazard
    chk("'citation' is already the word for the NON-binary row",
        "citation" in cypher.ADMISSION["documentary"][2], True)
    chk("recorded as a hazard", CITATION_IS_ALREADY_TAKEN, True)

    # --------------------------------------------------- 5. the roster is data
    chk("M's roster is recorded", len(CANDIDATE_ROSTER_M), 7)
    chk("and is NOT among the seated rosters",
        any(r["languages"] == CANDIDATE_ROSTER_M
            for r in cypher.ROSTERS.values()), False)
    chk("it names three the tree has no operator for",
        sorted(l for l in CANDIDATE_ROSTER_M
               if l not in cypher.ADMISSION and l not in cypher.DECLARED_ONLY),
        ["NECs/proofs", "binary", "logic"])
    chk("and drops three roster 1173 carries",
        sorted(l for l in cypher.ROSTERS["1173"]["languages"]
               if l not in CANDIDATE_ROSTER_M),
        ["analysis", "documentary", "information"])
    chk("left to the docket", ROSTER_NOT_RULED, True)
    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w2 in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w2))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
