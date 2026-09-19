#!/usr/bin/env python3
r"""predict.py -- WHAT DOES THE REGISTER PREDICT?  DOCKET 38.

    python3 predict.py             the reading
    python3 predict.py --selftest  fixtures

M: "What other scientific data can be derived from the index?"

THE ANSWER THE MACHINERY ALREADY CONTAINS.  Section 25.6 says the number of
predictions an index can make is E(X), and `demand.py` computes E for the
FIGURE.  It had never been computed for the SEATED INDEXES themselves.  This
file does that, and then does the harder half: says what an E cell is actually
worth.

===============================================================================
1. E PER SEATED INDEX -- SIXTEEN PREDICT, SIX DO NOT
===============================================================================

E(X) = |J(X) \ X|: the cells the index's own join-closure DEMANDS and no member
occupies.  Measured over every seated index small enough to close (gravity, at
914 cells, is not):

    baryons 1012   readrezayi 678   channels 367   ions 296   laws 254
    fibred 140     probability 112  terms 98       fqh 71     observed 56
    fundamental 46 inversion 24     madrule 18     mesons 15  nucshell 14
    nucbands 5

    janet 0   gravity_bound 0   madelung_slot 0   baryon_isomultiplet 0
    bosonqp 0   spin4 0

THE PARTITION IS EXACT AND IT IS NOT A DISCOVERY.  Every index that closes
under INFORMATION has E = 0; every index that does not has E > 0; no
exceptions.  That is close to definitional -- E is the join-closure deficit and
the information closer IS the join closer -- and it is stated here so nobody
mistakes it for a result.  THE RESULT IS THE NUMBERS, and the numbers say the
register is overwhelmingly INCOMPLETE: sixteen of twenty-two measurable indexes
demand cells they do not hold.

===============================================================================
2. AND AN E CELL IS NOT A PREDICTION UNTIL IT IS ADJUDICATED
===============================================================================

THE CORPUS ALREADY KNOWS THIS AND THE WEBSITE ALREADY DRAWS IT.  The element
layout has E = 36, and `docs/WEB-INDEX.md` records that all thirty-six were
adjudicated rather than announced: 25 FORBIDDEN by the hydrogenic bound
l <= n-1 -- orbitals that cannot exist -- and 11 DEFERRED, real but filled
elsewhere.  Register 448 rules the split.  An unadjudicated E is a count of
QUESTIONS, not of objects.

THE PARTICLE LAYER NEEDS A THIRD BIN, AND THIS FILE IS WHERE IT IS NAMED.
Checking the smallest prediction set -- mesons, fifteen cells -- the very first
cell examined was neither forbidden nor deferred:

    CELL (2J, P, 2I, Q3) = (2, -1, 0, 3) is J^P = 1-, I = 0, Q = +1.
    That combination is physical: 78 of the 242 members carry 2I = 0, and
    (2I=0, Q3=3) is the D_s and B_c family.  So the cell is not forbidden.
    D_s*(2112)+ IS such a particle AND IT EXISTS.  It is absent from the index
    because the capture carries it with J = None and P = "?" -- PDG assigns it
    no spin-parity here -- so `mesons.py` cannot place it.

    THE CELL IS EMPTY BECAUSE OF THE SOURCE, NOT BECAUSE OF NATURE.

So an E cell is one of THREE things, and only the third is a prediction:

    FORBIDDEN   a bound rules the combination out.  25 of the element 36.
    UNPLACED    the object exists and the SOURCE does not give it the
                coordinates.  D_s*(2112)+ is one.  This tree has met the same
                thing three times already and refused on it each time -- the
                spin-4 mesons PDG cannot place in a mass reach, the 27 bands
                with no I^pi column, the 93 levels with no parity.
    OPEN        physical, coordinates assignable, and nothing there.  THIS is
                a prediction in the sense section 25.6 means.

E IS THEREFORE AN UPPER BOUND ON PREDICTIONS AND THIS FILE REPORTS IT AS ONE.
Nothing here claims 1,012 unobserved baryons.  It claims 1,012 cells whose
closure demands them, of which an unknown number are forbidden, an unknown
number are unplaced, and the remainder -- only the remainder -- are open.

===============================================================================
3. WHAT WOULD ACTUALLY DERIVE THE SCIENCE
===============================================================================

    A BOUND PER INDEX, the way l <= n-1 served the elements.  For the mesons
    and baryons the candidates are the quark-model constraints: P = (-1)^(L+1)
    and C = (-1)^(L+S) for a q-qbar state, which forbid J^PC = 0--, 0+-, 1-+,
    2+- and so on -- the famous "exotic" quantum numbers.  A cell in that set
    is FORBIDDEN in the quark model and its emptiness is a theorem, not a gap.

    A SOURCE-COMPLETENESS PASS, separating UNPLACED from OPEN.  That one is
    mechanical: for each demanded cell, ask whether the raw capture holds a row
    that would land there if the source assigned it coordinates.  The D_s* case
    above was found exactly that way and took one query.

Neither is done here.  This file measures E, names the three bins, and proves
by one worked case that the bins are not empty of each other.
"""

import sys

import demand
import mi
import registry

# Measured by `python3 predict.py --measure`; recorded so the default report
# runs in seconds rather than re-closing twenty-two indexes.  The selftest
# RE-MEASURES a sample rather than trusting the table.
E_BY_INDEX = {
    "baryons.index": 1012, "readrezayi.index": 678, "channels.index": 367,
    "ions.index": 296, "laws.index": 254, "fibred.index": 140,
    "probability.index": 112, "terms.index": 98, "fqh.index": 71,
    "observed.index": 56, "fundamental.index": 46, "inversion.index": 24,
    "madrule.index": 18, "mesons.index": 15, "nucshell.index": 14,
    "nucbands.index": 5,
    "madelung.janet": 0, "overlaprule.gravity_bound": 0,
    "overlaprule.madelung_slot": 0, "overlaprule.baryon_isomultiplet": 0,
    "bosonqp.index": 0, "spin4.index": 0,
}

# gravity is 914 cells and its closure is not computed here.  Named, not
# silently omitted.
TOO_LARGE = ("gravity.index",)

# The element layer's own adjudication, from docs/WEB-INDEX.md and register 448.
# The precedent this file generalises.
ELEMENT_GHOSTS = {"E": 36, "forbidden": 25, "deferred": 11}

# The worked case that forced the third bin.
UNPLACED_CASE = (
    "mesons.index", (2, -1, 0, 3),
    "J^P = 1-, I = 0, Q = +1 -- the D_s / B_c slot.  D_s*(2112)+ EXISTS; the "
    "capture carries it with J = None and P = '?', so mesons.py cannot place "
    "it.  The cell is empty because of the SOURCE, not because of nature.")

BINS = (
    ("FORBIDDEN", "a bound rules the combination out; emptiness is a theorem"),
    ("UNPLACED", "the object exists and the source gives it no coordinates"),
    ("OPEN", "physical, placeable, and nothing there -- a real prediction"),
)


def measure():
    """{index: E} re-derived.  Slow; the table above is its record."""
    out = {}
    for nm, _mod, _a, _me, _w, _q in registry.rows():
        X = registry.index_of(nm)
        if len(X) > 400:
            continue
        out[nm] = demand.E(frozenset(X))
    return out


def closes_information(nm):
    return "information" in mi.channels()[mi.K(registry.index_of(nm))]


def partition():
    """(E=0 and closing information, E>0 and not) -- the exact split."""
    zero = sorted(n for n, e in E_BY_INDEX.items() if e == 0)
    pos = sorted(n for n, e in E_BY_INDEX.items() if e > 0)
    return (all(closes_information(n) for n in zero),
            all(not closes_information(n) for n in pos),
            len(zero), len(pos))


def total():
    return sum(E_BY_INDEX.values())


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("twenty-two indexes measured, one too large to close",
        (len(E_BY_INDEX), len(TOO_LARGE)), (22, 1))
    chk("and the one left out is named", list(TOO_LARGE), ["gravity.index"])

    info_zero, noinfo_pos, nzero, npos = partition()
    chk("every E = 0 index closes under INFORMATION", info_zero, True)
    chk("and every E > 0 index does not -- no exceptions", noinfo_pos, True)
    chk("sixteen predict, six are complete", (npos, nzero), (16, 6))

    # RE-MEASURE a sample rather than trusting the recorded table.
    for nm in ("mesons.index", "nucbands.index", "spin4.index"):
        X = frozenset(registry.index_of(nm))
        chk("re-measured E(%s)" % nm, demand.E(X), E_BY_INDEX[nm])

    # 3,206, not the 3,241 I first typed -- the sum is measured, not added up
    # by hand, and the fixture caught the hand arithmetic.
    chk("the register demands 3,206 cells it does not hold", total(), 3206)

    chk("the element layer's 36 ghosts were adjudicated 25 + 11, not announced",
        (ELEMENT_GHOSTS["forbidden"] + ELEMENT_GHOSTS["deferred"],
         ELEMENT_GHOSTS["E"]), (36, 36))

    # the worked case, re-derived: the cell IS demanded, and (2I=0, Q3=3) IS
    # occupied elsewhere, so the cell is not forbidden.
    X = frozenset(registry.index_of("mesons.index"))
    d = set(demand.demand(X))
    nm, cell, _why = UNPLACED_CASE
    chk("the worked cell is genuinely demanded by the closure", cell in d, True)
    chk("and (2I=0, Q3=3) is occupied by other members, so it is NOT forbidden",
        any(c[2] == 0 and c[3] == 3 for c in X), True)
    chk("three bins, and the third is the only one that is a prediction",
        [b for b, _w in BINS], ["FORBIDDEN", "UNPLACED", "OPEN"])

    print("predict selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 38 -- WHAT DOES THE REGISTER PREDICT?")
    print("=" * 79)
    print()
    print("Section 25.6: the number of predictions an index can make is E(X).")
    print("demand.py computed E for the FIGURE; it had never been computed for")
    print("the seated indexes themselves.")
    print()
    print("1. E PER SEATED INDEX")
    print("     %-34s %6s %6s" % ("index", "K", "E"))
    for nm, e in sorted(E_BY_INDEX.items(), key=lambda kv: -kv[1]):
        print("     %-34s %6s %6d"
              % (nm, "K%d" % mi.K(registry.index_of(nm)), e))
    for nm in TOO_LARGE:
        print("     %-34s %6s %6s" % (nm, "-", "not closed (914 cells)"))
    info_zero, noinfo_pos, nzero, npos = partition()
    print()
    print("   %d predict, %d are complete.  THE PARTITION IS EXACT: every E = 0"
          % (npos, nzero))
    print("   index closes under INFORMATION and every E > 0 index does not.")
    print("   That is near-definitional -- E is the join deficit and the")
    print("   information closer IS the join closer -- and is said so nobody")
    print("   mistakes it for a result.  The result is the numbers: the")
    print("   register demands %s cells it does not hold." % format(total(), ","))
    print()
    print("2. BUT AN E CELL IS NOT A PREDICTION UNTIL IT IS ADJUDICATED.")
    print("   The element layer already does this: E = %d ghosts, split %d"
          % (ELEMENT_GHOSTS["E"], ELEMENT_GHOSTS["forbidden"]))
    print("   FORBIDDEN by the hydrogenic bound and %d DEFERRED, per register"
          % ELEMENT_GHOSTS["deferred"])
    print("   448 -- adjudicated, not announced.")
    print()
    print("   THE PARTICLE LAYER NEEDS A THIRD BIN.  Checking the smallest")
    print("   prediction set -- mesons, 15 cells -- the FIRST cell examined:")
    nm, cell, why = UNPLACED_CASE
    print("     %s  cell %s" % (nm, cell))
    print("     %s" % why)
    print()
    for b, w in BINS:
        print("     %-11s %s" % (b, w))
    print()
    print("   E IS AN UPPER BOUND ON PREDICTIONS, NOT A COUNT OF THEM.  This")
    print("   file does NOT claim 1,012 unobserved baryons.  It claims 1,012")
    print("   cells whose closure demands them, of which an unknown number are")
    print("   forbidden, an unknown number unplaced, and only the remainder")
    print("   open.")
    print()
    print("3. WHAT WOULD ACTUALLY DERIVE THE SCIENCE")
    print("   A BOUND PER INDEX, as l <= n-1 served the elements.  For mesons")
    print("   and baryons: P = (-1)^(L+1) and C = (-1)^(L+S) for a q-qbar")
    print("   state, which forbid the exotic J^PC -- 0--, 0+-, 1-+, 2+-.  A")
    print("   cell in that set is empty by theorem, not by gap.")
    print("   A SOURCE-COMPLETENESS PASS separating UNPLACED from OPEN: for")
    print("   each demanded cell, ask whether the raw capture holds a row that")
    print("   would land there if the source assigned it coordinates.  The")
    print("   D_s* case was found that way and took one query.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--measure" in sys.argv:
        for k, v in sorted(measure().items(), key=lambda kv: -kv[1]):
            print("%-34s %6d" % (k, v))
        sys.exit(0)
    sys.exit(report())
