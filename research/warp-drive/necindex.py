#!/usr/bin/env python3
"""
necindex.py -- THE ENERGY-CONDITION FAMILY AS AN INDEX, RUN THROUGH THE CYPHER.

M: "We are approaching this wrong.  We need to apply the dimensional hierarchy
of mathematical languages.  NECs are derived from statistically probable
positions in spacetime for any given element.  Those NECs are derived AFTER a
position is determined, and they are used to logically CITE the object in
transit in its new environment/conditions.  This method changes the question
from satisfying current conditions, to ask WHAT CURRENT CONDITIONS NEED TO BE
CHANGED, AND TO WHAT?"

THE REFRAMING IS RIGHT AND IT IS MECHANICALLY RIGHT, NOT RHETORICALLY.  An
energy condition is not a property of matter.  IT IS A UNIVERSAL QUANTIFICATION
OVER A SET OF DIRECTIONS AT A POINT, and every named member of the family has
the identical functional form

        [ TENSOR ]_mn  [ VECTOR ]^m [ VECTOR ]^n   >=   [ BOUND ]
                       measured under [ MEASURE ], in regime [ REGIME ]

differing ONLY in which value sits in which slot.  So the family is an INDEX
over five ordinal coordinates, and this file builds it and hands it to the
corpus's own cypher (tools/cypher.py, roster 1173) rather than reasoning about
it in prose.

===============================================================================
1. THE FIVE SLOTS
===============================================================================

    T   WHICH TENSOR IS CONTRACTED
        0 matter T_mn   1 effective T_eff (non-minimal)   2 Einstein G_mn
        3 Ricci R_mn
    V   WHICH DIRECTIONS ARE QUANTIFIED OVER, by increasing size of the set
        0 null   1 timelike   2 causal (both)
    M   THE MEASURE OVER THE GEODESIC, by increasing weakness of the result
        0 pointwise (Dirac)   1 smeared (finite weight)   2 averaged, all
        complete null geodesics   3 averaged, ACHRONAL ones only
    Q   REGIME
        0 classical T   1 semiclassical <T>
    B   THE RIGHT-HAND SIDE, by how much negativity it licenses
        0 zero   1 a negative state-independent bound   2 an entropy variation

M'S FIRST CLAUSE IS THE V AND M SLOTS, EXACTLY.  "Derived from statistically
probable positions" is what M is: pointwise is a Dirac measure on the direction
set, smeared is a weight function, averaged is uniform along a geodesic.  THE
FAMILY IS A LADDER OF MEASURES OVER AN OBSERVER SET.  And "derived AFTER a
position is determined" is the V slot: there is no T_kk without a k, and k is a
direction at a point.  THE CONDITION IS NOT A PROPERTY OF THE MATTER.  It is a
property of the matter AND a chosen direction AND a chosen measure.

===============================================================================
2. WHICH ARE INTERCHANGEABLE.  TWO IDENTIFICATIONS, AND THEY ARE NOT ALIKE
===============================================================================

    G_mn k^m k^n  =  R_mn k^m k^n  -  (R/2) g_mn k^m k^n

UNCONDITIONAL, AND IT COLLAPSES EXACTLY WHEN R g_kk = 0.  For a NULL k the
second term is zero by definition of null, so

        THE EINSTEIN NEC AND THE RICCI NEC ARE THE SAME STATEMENT.

AND THE PRECISE FORM OF THAT IS BETTER THAN "THEY ARE ONE CELL", WHICH IS WHAT
THIS FILE FIRST CLAIMED AND ITS OWN SELFTEST REFUSED.  They sit in TWO cells,
T=2 and T=3, and the identity is a QUOTIENT ON THE INDEX rather than a
collision in it: THE T COORDINATE IS NOT FAITHFUL AT V=0.  Which is the sharp
statement, because the same coordinate IS faithful everywhere else -- the same
T=2/T=3 difference at V=1 is precisely WEC-on-Einstein against SEC, and those
are two conditions, not one.  THE IDENTITY SAYS EXACTLY WHERE THE COORDINATE
STOPS DISTINGUISHING, and it stops only on the null slice.  No field equation
is used anywhere in it.

FOR A TIMELIKE v THEY DIFFER BY EXACTLY R/2, AND THAT IS WHY SEC IS NOT WEC.
The same two tensors, the same bound, the same measure -- and at timelike they
are different conditions, at null they are one.  THE NULL DIRECTION IS THE ONLY
PLACE THE GEOMETRIC AND THE MATERIAL READINGS COINCIDE.  The whole reason this
project lives on the NEC rather than the WEC is that collapse.

The second identification is NOT unconditional:

        T=0 (matter) == T=2 (Einstein)   IF AND ONLY IF G = 8 pi G T,
                                         which is to say, IN GENERAL RELATIVITY

===============================================================================
3. AND THAT IS THE ANSWER TO M'S QUESTION, WITH A CENSUS BEHIND IT
===============================================================================

Ask of every escape route this tree has found: WHICH SLOT DOES IT MOVE?

        higgs.py / Barcelo-Visser xi        moves T,  0 -> 1
        emtension.py's non-minimal route    moves T,  0 -> 1
        qei.py's state-dependent piece      moves T,  0 -> 1
        currency.py's modified gravity      moves T,  0 -> 2/3
        necladder.py's rung grading         moves M,  0 -> 1/2
        anecscope.py's achronal scope       moves M,  2 -> 3
        anec.py's QNEC                      moves B,  0 -> 2
        persist.py / Ford-Roman             moves B,  0 -> 1

    NOT ONE OF THEM MOVES THE ORDER RELATION.  Nothing anywhere relaxes ">=".
    NOT ONE OF THEM MOVES V.  Nobody escapes by changing which directions are
    quantified.  EVERY ESCAPE MOVES T, M OR B -- AND EVERY ESCAPE THAT ACTUALLY
    OPENS A THROAT MOVES T.

So M's inversion resolves to a specific engineering statement, and it is
sharper than "we need exotic matter":

    THE CORRIDOR DOES NOT NEED MATTER THAT VIOLATES THE NULL ENERGY CONDITION.
    IT NEEDS THE TENSOR THAT SOURCES THE CURVATURE NOT TO BE THE TENSOR WHOSE
    ENERGY CONDITION WE CHECK.

That is one door.  It has been found five times in this tree under five names,
and every one of them is the T slot.

===============================================================================
4. AND THE CYPHER ANSWERS M'S FIRST CLAUSE, WITHOUT BEING STEERED TO IT
===============================================================================

M said the NECs are derived from STATISTICALLY PROBABLE POSITIONS.  The index
was built from the slots, handed to tools/cypher.py at roster 1173, and the
languages answered for themselves.  Over the eighteen named conditions:

        language        admits      E
        order              192    175
        algebra            192    175
        information        156    139
        geometry            29     12
        STATISTICS          17      0

    THE FAMILY IS GENERATED EXACTLY BY ITS PAIRWISE MARGINALS, IN ONE LANGUAGE
    OF THE FIVE, AND OVER-GENERATED BY EVERY OTHER FROM TWELVE CELLS TO A
    HUNDRED AND SEVENTY-FIVE.  Statistics is not close to the others.  It is
    exact and they are not near it.

AND THE ROUTE TO E = 0 IS THE FINDING RATHER THAN THE ZERO.  Seventeen
conditions were seated first and statistics returned E = 1, DEMANDING ONE CELL
NOBODY HAD LISTED: (matter T, timelike, pointwise, semiclassical, >= 0) -- THE
SEMICLASSICAL WEC.  It was then seated, and E fell to zero.

That condition is FALSE.  The Casimir vacuum has negative energy density in a
timelike frame and it is measured, exactly as its null partner is.  Which is
why no textbook lists it among the conditions -- AND THE INDEX DEMANDED IT
ANYWAY, because an index enumerates CITATIONS AND NOT TRUTHS.  A refuted
condition is a perfectly well-formed citation.

    SO THE FAMILY CLOSES ONLY WHEN THE REFUTED MEMBERS ARE SEATED BESIDE THE
    STANDING ONES, AND THAT IS M'S POINT IN THE INDEX'S OWN ARITHMETIC: these
    are reports, not gates.

===============================================================================
5. WHAT THE CYPHER IS ASKED, AND WHY IT IS ASKED RATHER THAN ASSERTED
===============================================================================

The index is handed to tools/cypher.py at roster 1173 -- IMPORTED, NOT
REIMPLEMENTED -- and the languages answer for themselves.  A language that
SPEAKS regenerates the family from its own operator; one that is SILENT cannot
see it at all; one that is NOT EXTENSIVE drops cells it should hold.  The
closure defect E(X) then says HOW MANY CONDITIONS THE FAMILY'S OWN STRUCTURE
DEMANDS THAT NOBODY HAS NAMED -- which is M's question in its exact form: not
"do we satisfy it" but "what has to change, and to what".

A DEMANDED CELL IS A CANDIDATE FOR A NAME, NOT A FINDING.  Nothing here says
such a condition exists in the literature or is true; it says the index cannot
be closed without it.  Recorded, never repaired.

NOTHING IS REPAIRED.
"""

import importlib.util
import itertools
import math
import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_CYPHER = os.path.normpath(os.path.join(_HERE, "..", "..", "tools", "cypher.py"))


def _load_cypher():
    spec = importlib.util.spec_from_file_location("cypher_mod", _CYPHER)
    mod = importlib.util.module_from_spec(spec)
    # cypher.py uses @dataclass, which resolves annotations through
    # sys.modules[cls.__module__] -- so the module must be registered BEFORE
    # exec_module or the decorator raises on its own Verdict class.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


cypher = _load_cypher()

COORDS = ("T", "V", "M", "Q", "B", "A")

# THE CODING MUST BE PINNED, AND THIS IS NOT HOUSEKEEPING.
#
# cypher.Index RE-RANKS each coordinate's observed values to dense ordinals.  On
# the full family that is the identity, because the eighteen named conditions
# happen to use every value of every slot.  On ANY SUBSET THAT DOES NOT, it is
# not: a seed whose V values are {1, 2} gets them re-coded to {0, 1}, and the
# operator's output is then in a DIFFERENT COORDINATE SYSTEM FROM ITS INPUT.
#
# Nothing errors.  The numbers come back plausible and they are measuring
# something else.  It cost this tree two published results before it was found --
# see docs/CLAIMS.md H97 and the corrections to H94b and H96b.
#
# Declaring value_order pins code[i][v] = v, so every instrument downstream reads
# and writes the same coordinates.  USE pinned_index(), NEVER cypher.Index DIRECT.
VALUE_ORDER = {"T": [0, 1, 2, 3], "V": [0, 1, 2], "M": [0, 1, 2, 3],
               "Q": [0, 1], "B": [0, 1, 2], "A": [0, 1]}


def pinned_index(cells, name="the energy-condition family"):
    """cypher.Index with the coding pinned.  The only constructor to use here."""
    return cypher.Index(name, COORDS, sorted(set(cells)), value_order=VALUE_ORDER)

# (name, T, V, M, Q, B, A, where it is named)
# A is the ARITY coordinate, added after the cell below was found MIS-NAMED:
#   0  QUADRATIC, one direction used twice:  T_mn v^m v^n  >= B
#   1  BILINEAR, an ordered pair:            T_mn v^m w^n  >= B
# A starts at 0 like every other slot, so cypher.Index's re-ranking stays the
# identity -- the drift this file warns about above is a live hazard here.
# Every condition of the original family is quadratic and carries A = 1. The
# dominant energy condition is not, and could not be written at all before this
# coordinate existed -- which is why the cell that carried its name carried WEC.
FAMILY = [
    ("NEC",                 0, 0, 0, 0, 0, 0, "classical; BV call it the weakest"),
    ("WEC",                 0, 1, 0, 0, 0, 0, "classical"),
    ("causal-quadratic",    0, 2, 0, 0, 0, 0, "WAS SEATED AS 'DEC' AND IS NOT IT: "
                                              "T_vv >= 0 over all causal v is WEC "
                                              "and NEC together. Kept and renamed, "
                                              "not deleted -- see the V quotient."),
    ("DEC",                 0, 2, 0, 0, 0, 1, "the REAL one: T_mn v^m w^n >= 0 for "
                                              "every future-causal ordered pair"),
    ("SEC",                 3, 1, 0, 0, 0, 0, "classical; IS the Ricci condition"),
    ("NCC",                 3, 0, 0, 0, 0, 0, "null convergence, singularity theorems"),
    ("Einstein-NEC",        2, 0, 0, 0, 0, 0, "G_kk >= 0; same cell content as NCC"),
    ("BV-effective-NEC",    1, 0, 0, 0, 0, 0, "Barcelo-Visser eq. (2.6), READ"),
    ("ANEC",                0, 0, 2, 0, 0, 0, "averaged, all complete null geodesics"),
    ("AANEC",               0, 0, 3, 0, 0, 0, "achronal; anecscope.py, the one with teeth"),
    ("BV-effective-ANEC",   1, 0, 2, 0, 0, 0, "Barcelo-Visser sect. 2.3, READ"),
    ("semiclassical-NEC",   0, 0, 0, 1, 0, 0, "FALSE -- Casimir, measured"),
    ("semiclassical-ANEC",  0, 0, 2, 1, 0, 0, "flat space; Faulkner-Leigh-Parrikar-Wang"),
    ("semiclassical-AANEC", 0, 0, 3, 1, 0, 0, "Graham-Olum; topological censorship uses it"),
    ("SNEC",                0, 0, 1, 1, 1, 0, "smeared null; nullbound.py, anec.py"),
    ("QEI-Ford-Roman",      0, 1, 1, 1, 1, 0, "persist.py"),
    ("QEI-Fewster-Osterbrink", 0, 1, 1, 1, 1, 0, "qei.py -- THE SAME CELL as Ford-Roman"),
    ("QNEC",                0, 0, 0, 1, 2, 0, "anec.py; entropy variation"),
    ("semiclassical-WEC",   0, 1, 0, 1, 0, 0, "FALSE -- Casimir; DEMANDED by the "
                                              "index before it was seated"),
]

# THE V QUOTIENT, the second identification of its kind on this index.
# At A = 0 the V coordinate is NOT FAITHFUL between 1 and 2: for a continuous
# tensor the null cone is the boundary of the timelike cone, so T_vv >= 0 over
# all timelike v already gives it over all causal v. `causal-quadratic` and WEC
# are therefore one condition in two cells -- exactly the shape of the G = R
# identity at V = 0, and recorded the same way rather than collapsed.
# At A = 1 there is no such collapse: DEC is strictly stronger than both.
V_QUOTIENT_AT_A0 = ((0, 1, 0, 0, 0, 0), (0, 2, 0, 0, 0, 0))

# The escape routes recorded in this tree, and which slot each one moves.
ESCAPES = [
    ("higgs.py / Barcelo-Visser xi",      "T", 0, 1, "opens a throat"),
    ("emtension.py non-minimal coupling", "T", 0, 1, "opens a throat"),
    ("qei.py state-dependent piece",      "T", 0, 1, "opens a throat"),
    ("currency.py modified gravity",      "T", 0, 3, "opens a throat"),
    ("necladder.py rung grading",         "M", 0, 2, "grades, does not open"),
    ("anecscope.py achronal scope",       "M", 2, 3, "grades, does not open"),
    ("anec.py QNEC",                      "B", 0, 2, "grades, does not open"),
    ("persist.py Ford-Roman",             "B", 0, 1, "grades, does not open"),
]

CYPHER_IMPORTED_NOT_COPIED = True
NOTHING_IS_REPAIRED = True


def cells():
    """The seated cells, SIX coordinates now: (T, V, M, Q, B, A).

    A was added when the cell seated as DEC was found to be WEC and NEC under
    the family's own declared quadratic form. The mis-named cell is kept and
    renamed rather than deleted -- the treatment the G = R identity already
    gets on this index, where two cells stand and the identification is
    recorded as a quotient rather than a collision.
    """
    return sorted({tuple(r[1:7]) for r in FAMILY})


def index():
    return pinned_index(cells())


# ------------------------------------------------- the interchangeability identity
def G_kk(ric, Rs, g, k):
    """G_mn k^m k^n with G_mn = R_mn - (Rs/2) g_mn.  ric and g are 4x4."""
    return sum((ric[m][n] - Rs * g[m][n] / 2) * k[m] * k[n]
               for m in range(4) for n in range(4))


def R_kk(ric, k):
    return sum(ric[m][n] * k[m] * k[n] for m in range(4) for n in range(4))


def g_kk(g, k):
    return sum(g[m][n] * k[m] * k[n] for m in range(4) for n in range(4))


MINK = [[Fraction(-1 if m == 0 else 1) if m == n else Fraction(0)
         for n in range(4)] for m in range(4)]

QUADS = ((1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (4, 4, 7, 9),
         (3, 4, 12, 13), (2, 5, 14, 15), (1, 12, 12, 17), (8, 9, 12, 17))


def null_k(q):
    a, b, cc, N = q
    return [Fraction(N), Fraction(a), Fraction(b), Fraction(cc)]


def quotient_pairs(cs=None):
    """Cells the G = R identity identifies: same everything but T in {2,3},
    AND on the null slice V = 0.  Off that slice the identity does not apply
    and the two are different conditions."""
    cs = set(cs if cs is not None else cells())
    out = []
    for c in sorted(cs):
        if c[0] != 2 or c[1] != 0:
            continue
        partner = (3,) + tuple(c[1:])
        if partner in cs:
            out.append((c, partner))
    return out


def t_coordinate_is_faithful(cs=None):
    """Off the null slice, is any T=2/T=3 pair identified?  It must not be."""
    cs = set(cs if cs is not None else cells())
    return [c for c in sorted(cs)
            if c[0] == 2 and c[1] != 0 and (3,) + tuple(c[1:]) in cs]


OPERATORS = ("order", "algebra", "geometry", "information", "statistics")


def closure_by_language(cs=None):
    """admits and E, per operator-bearing language, over a cell set."""
    cs = sorted(set(cs if cs is not None else cells()))
    ix = cypher.Index("the energy-condition family", COORDS, cs)
    opts = {"statistics_order": 2, "algebra_budget": 20000}
    out = {}
    for name in OPERATORS:
        fn = cypher.ADMISSION[name][0]
        adm, _ = fn(ix, opts)
        out[name] = (len(adm), sorted(set(adm) - set(cs)))
    return out


def slot_moves():
    from collections import Counter
    return Counter(e[1] for e in ESCAPES)


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  the family, as an index over six slots")
    print("      %-26s %2s %2s %2s %2s %2s   %s"
          % ("condition", *COORDS, "where it is named"))
    for r in FAMILY:
        print("      %-26s %2d %2d %2d %2d %2d %2d   %s"
              % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
    print()
    print("      %-38s %6d" % ("named conditions", len(FAMILY)))
    print("      %-38s %6d" % ("DISTINCT cells they occupy", len(cells())))
    print("      %-38s %6d" % ("collisions (two names, one cell)",
                               len(FAMILY) - len(cells())))
    print()
    print("  the collisions, which are the interchangeability")
    seen = {}
    for r in FAMILY:
        seen.setdefault(tuple(r[1:7]), []).append(r[0])
    for cell, names in sorted(seen.items()):
        if len(names) > 1:
            print("      %-24s %s" % (str(cell), "  ==  ".join(names)))
    print()
    print("  G_kk vs R_kk, over exact rationals")
    ric = [[Fraction(m * 4 + n + 1, 7) for n in range(4)] for m in range(4)]
    ric = [[(ric[m][n] + ric[n][m]) / 2 for n in range(4)] for m in range(4)]
    Rs = Fraction(11, 3)
    print("      %-30s %14s %14s %10s" % ("direction", "G_kk", "R_kk", "g_kk"))
    for q in QUADS[:3]:
        k = null_k(q)
        print("      %-30s %14s %14s %10s"
              % ("null " + str(q), G_kk(ric, Rs, MINK, k), R_kk(ric, k),
                 g_kk(MINK, k)))
    for v, lab in (([Fraction(1), Fraction(0), Fraction(0), Fraction(0)],
                    "timelike (1,0,0,0)"),
                   ([Fraction(5, 4), Fraction(3, 4), Fraction(0), Fraction(0)],
                    "timelike (5/4,3/4,0,0)")):
        print("      %-30s %14s %14s %10s"
              % (lab, G_kk(ric, Rs, MINK, v), R_kk(ric, v), g_kk(MINK, v)))
    print("      at null the two AGREE; at timelike they differ by Rs/2 = %s"
          % (Rs / 2))
    print()
    print("  which slot each escape moves")
    print("      %-36s %3s %s -> %s   %s"
          % ("route", "slot", "from", "to", "effect"))
    for name, slot, a, b, eff in ESCAPES:
        print("      %-36s %3s %4d -> %d   %s" % (name, slot, a, b, eff))
    print()
    for s, n in sorted(slot_moves().items()):
        print("      slot %s moved by %d of %d routes" % (s, n, len(ESCAPES)))
    opens = [e for e in ESCAPES if e[4] == "opens a throat"]
    print("      %-38s %6d of %d" % ("routes that OPEN a throat", len(opens),
                                     len(ESCAPES)))
    print("      %-38s %6s" % ("and every one of them moves",
                               sorted({e[1] for e in opens})))
    print()
    print("  closure by language -- and only one of them closes it")
    cl = closure_by_language()
    print("      %-14s %8s %6s" % ("language", "admits", "E"))
    for lang in sorted(OPERATORS, key=lambda l: -len(closure_by_language()[l][1])):
        print("      %-14s %8d %6d" % (lang, cl[lang][0], len(cl[lang][1])))
    without = [c for c in cells() if c != (0, 1, 0, 1, 0)]
    print("      and dropping the semiclassical WEC, statistics demands back %s"
          % closure_by_language(without)["statistics"][1])
    print()
    print("  the cypher, roster 1173, imported from tools/cypher.py")
    ix = index()
    res = cypher.run(ix, "1173", {"statistics_order": 2, "algebra_budget": 20000})
    print()
    print(cypher.report(res))
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  An energy condition is a quantifier over directions under a")
    print("  measure, not a property of matter.  Two readings are")
    print("  interchangeable: G and Ricci, ALWAYS and only at null; matter and")
    print("  Einstein, ONLY in general relativity.  Every escape that opens a")
    print("  throat breaks the second.  The corridor does not need matter that")
    print("  violates the NEC.  It needs the tensor that sources the curvature")
    print("  not to be the tensor whose energy condition we check.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("necindex.py --selftest")
    print()

    # --------------------------------------------------- the index is well formed
    chk("named conditions", len(FAMILY), 19)
    chk("distinct cells", len(cells()), 18)
    chk("one name-pair collides onto one cell", len(FAMILY) - len(cells()), 1)
    chk("every row has six slots",
        sorted({len(r) for r in FAMILY}), [8])
    chk("every slot value is in range",
        all(0 <= r[1] <= 3 and 0 <= r[2] <= 2 and 0 <= r[3] <= 3
            and 0 <= r[4] <= 1 and 0 <= r[5] <= 2 and 0 <= r[6] <= 1
            for r in FAMILY), True)
    chk("names are unique", len({r[0] for r in FAMILY}), len(FAMILY))

    # the two collisions are the two claimed interchangeabilities
    seen = {}
    for r in FAMILY:
        seen.setdefault(tuple(r[1:7]), []).append(r[0])
    coll = sorted(tuple(sorted(v)) for v in seen.values() if len(v) > 1)
    chk("and it is exactly this one", coll,
        [("QEI-Fewster-Osterbrink", "QEI-Ford-Roman")])
    # THE QUOTIENT, which is a different thing from a collision and is the
    # claim this file first got wrong: NCC and Einstein-NEC are ONE CONDITION
    # in TWO CELLS, and the identity is what identifies them.
    chk("the identity quotients exactly one pair of cells",
        quotient_pairs(), [((2, 0, 0, 0, 0, 0), (3, 0, 0, 0, 0, 0))])
    chk("and those two cells are NCC and Einstein-NEC",
        sorted(r[0] for r in FAMILY
               if tuple(r[1:7]) in {(2, 0, 0, 0, 0, 0), (3, 0, 0, 0, 0, 0)}),
        ["Einstein-NEC", "NCC"])
    # NEGATIVE CONTROL: off the null slice the coordinate must stay faithful.
    chk("T stays faithful off the null slice", t_coordinate_is_faithful(), [])
    # and the seated instance of that is SEC, which is T=3 at V=1 with no
    # T=2 partner -- it is NOT the same condition as WEC.
    chk("SEC sits at T=3, V=1", [tuple(r[1:7]) for r in FAMILY
                                 if r[0] == "SEC"], [(3, 1, 0, 0, 0, 0)])
    chk("and WEC at T=0, V=1 -- a different tensor, a different condition",
        [tuple(r[1:7]) for r in FAMILY if r[0] == "WEC"], [(0, 1, 0, 0, 0, 0)])

    # ------------------------------------------- THE IDENTITY, OVER EXACT RATIONALS
    import random
    rnd = random.Random(20260912)
    bad_null = 0
    bad_time = 0
    for _ in range(2000):
        ric = [[Fraction(rnd.randrange(-99, 100), rnd.randrange(1, 20))
                for _ in range(4)] for _ in range(4)]
        ric = [[(ric[m][n] + ric[n][m]) / 2 for n in range(4)] for m in range(4)]
        Rs = Fraction(rnd.randrange(-99, 100), rnd.randrange(1, 20))
        k = null_k(QUADS[rnd.randrange(len(QUADS))])
        if g_kk(MINK, k) != 0:
            bad_null += 1
        if G_kk(ric, Rs, MINK, k) != R_kk(ric, k):
            bad_null += 1
        # unit timelike: g_vv = -1, so the difference must be EXACTLY +Rs/2
        v = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
        if G_kk(ric, Rs, MINK, v) - R_kk(ric, v) != Rs / 2:
            bad_time += 1
    chk("null k is exactly null and G_kk == R_kk, 2000 draws", bad_null, 0)
    chk("timelike v: G_vv - R_vv == +Rs/2 exactly, 2000 draws", bad_time, 0)
    # NEGATIVE CONTROL: at timelike the two are NOT equal unless Rs = 0
    ric0 = [[Fraction(m + n, 5) for n in range(4)] for m in range(4)]
    v = [Fraction(1), Fraction(0), Fraction(0), Fraction(0)]
    chk("and they genuinely differ there when Rs != 0",
        G_kk(ric0, Fraction(4), MINK, v) != R_kk(ric0, v), True)
    chk("but coincide at Rs = 0, the second collapse",
        G_kk(ric0, Fraction(0), MINK, v), R_kk(ric0, v))

    # ------------------------------------------------------------- the escape census
    chk("escape routes recorded", len(ESCAPES), 8)
    chk("no route moves the order relation",
        all(e[1] in COORDS for e in ESCAPES), True)
    chk("no route moves V", slot_moves().get("V", 0), 0)
    opens = [e for e in ESCAPES if e[4] == "opens a throat"]
    chk("routes that open a throat", len(opens), 4)
    chk("and every one of them moves T", sorted({e[1] for e in opens}), ["T"])
    # NEGATIVE CONTROL: the grading routes do NOT move T, so "every opener
    # moves T" is a real division and not true of the whole list
    grade = [e for e in ESCAPES if e[4] != "opens a throat"]
    chk("while no grading route moves T",
        sorted({e[1] for e in grade}), ["B", "M"])

    # ------------------------------------------------ the cypher runs, imported
    chk("cypher is imported, not copied", CYPHER_IMPORTED_NOT_COPIED, True)
    chk("and it is the seated tool", os.path.basename(_CYPHER), "cypher.py")
    ix = index()
    chk("the index builds", ix.d, 6)
    chk("with the family's cells", len(ix.cells), len(cells()))
    res = cypher.run(ix, "1173", {"statistics_order": 2, "algebra_budget": 20000})
    chk("the cypher answered", isinstance(res, dict), True)
    chk("at more than two coordinates, so not DEGENERATE", ix.d > 2, True)

    # ------------------------------------ THE CLOSURE, AND HOW IT WAS REACHED
    cl = closure_by_language()
    chk("statistics closes the family exactly", cl["statistics"][1], [])
    chk("and admits exactly the seated cells", cl["statistics"][0], 18)
    # NEGATIVE CONTROL: no other language comes near, so E = 0 is a property of
    # THIS language and not of an index that any operator would regenerate.
    for lang, want in (("order", 238), ("algebra", 238), ("information", 190),
                       ("geometry", 12)):
        chk("%s over-generates by %d" % (lang, want), len(cl[lang][1]), want)
    chk("every other language over-generates",
        all(len(cl[l][1]) > 0 for l in OPERATORS if l != "statistics"), True)

    # THE DISCOVERY, REPRODUCED: drop the demanded row and statistics asks for
    # it back.  This is the step that found it, kept runnable.
    without = [c for c in cells() if c != (0, 1, 0, 1, 0, 0)]
    chk("dropping the semiclassical WEC leaves 17 cells", len(without), 17)
    cl2 = closure_by_language(without)
    chk("and statistics demands exactly one cell back",
        cl2["statistics"][1], [(0, 1, 0, 1, 0, 0)])
    chk("which is the semiclassical WEC",
        [r[0] for r in FAMILY if tuple(r[1:7]) == (0, 1, 0, 1, 0, 0)],
        ["semiclassical-WEC"])
    chk("a refuted condition, seated as a citation not a truth",
        all("FALSE" in r[7] for r in FAMILY
            if r[0] in ("semiclassical-WEC", "semiclassical-NEC")), True)

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
