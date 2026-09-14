#!/usr/bin/env python3
r"""
spectra.py -- THE CHANNEL INDEX: the corpus's largest banked measurement set,
and a data fault in its most authoritative rows.

M: "any other available index that can be and has not yet been identified and
built in the same fashion and criterion as the rest."

    python3 spectra.py             the reading
    python3 spectra.py --selftest  fixtures

===============================================================================
0. THE SOURCE NOBODY HAD INDEXED
===============================================================================

`COORDINATES-2.13`, reached through `populate.Spectra`, holds **104,832 rows** --
more banked measurement than every other source in this tree combined.  Each row
is a spectroscopic channel: an element, a charge stage, an angular momentum, a
Pauli bound, a multiplicity, a quantum defect, and two provenance columns.

    IT IS FIRST-ORDER.  Its members are channels, not elements, not transitions,
    and not functions of the seated inventory.  So it is not a re-charting of
    anything charts3.py censused, and it earns a place by the same argument
    ions.py did: a new member set, not a new arrangement.

===============================================================================
1. THE INDEX: 209 CHANNEL SHAPES
===============================================================================

A row names a channel of a particular element.  What the corpus's own channel
equation (register 1205) turns on is the channel's SHAPE:

        (l, B, mult)      angular momentum, the Pauli bound of register 1141,
                          and the multiplicity

    **209 DISTINCT SHAPES over 104,807 usable rows**, between 3 and 3,124 rows
    apiece.  The index is the 209.  Reporting 104,832 would be counting
    observations and calling them channels -- the same error ions.py refuses
    over its 5,778 stage rows.

        209 cells, K0 -- closes NOTHING, cell (0, 16, 24)

===============================================================================
2. TWENTY-FIVE ROWS CARRY A DECIMAL WHERE AN INTEGER BELONGS
===============================================================================

`B` is `min(p, n0-l-1)`, a Pauli bound, and an integer in 104,807 rows.  In
**twenty-five** it holds a decimal -- `0.19569`, `0.10803`, `0.00449` and so on.

    **AND ALL TWENTY-FIVE ARE `measured` AND `witnessed`.**  They are not stray
    rows at the edge of the table; they are among the 358 most authoritative
    rows it has, and 25 of 358 is seven per cent of them.  A representative row:

        B 0.19569   delta 0.53527   Z 5   charge 1   l 1   mult 2
        grade measured   witness witnessed
        source "NIST ASD fetched 2026-08-14 ... BI 2P* n=2-9, 11 members"

    Both `B` and `delta` are decimals of the same magnitude, which is what a
    column slip looks like.  **RECORDED, NOT REPAIRED** -- the chat-67 hold
    governs a data fault exactly as it governs a section read, and this file
    drops the twenty-five from the index and says so rather than guessing what
    the true B was.

===============================================================================
3. TWO COLUMNS CARRYING ONE DISTINCTION
===============================================================================

        grade      computed 103,545   exact 929   measured 358
        witness    unwitnessed 104,474            witnessed 358

    **THE WITNESSED ROWS ARE EXACTLY THE MEASURED ROWS** -- not the same count,
    the same SET, verified row by row.  So `witness` is a function of `grade`:
    computed and exact are unwitnessed, measured is witnessed.

    AND THAT FUNCTION IS MONOTONE, which makes this a live test of the chart
    criterion on a source the criterion was never fitted to:

        (l, grade)        21 cells   K3
        (l, grade, wit)   21 cells   K3      -- unchanged, as DOCKET 3 requires

    The criterion predicted the channel would not move and it does not.  That is
    the first confirmation of it outside the element address.

===============================================================================
4. THE PROVENANCE SUB-CHART REACHES K3
===============================================================================

The channel shape closes nothing.  Chart the same rows by how well they are
KNOWN instead -- `(l, grade, witness)` -- and 21 cells close in
{geometry, statistics}, K3, at cell (3, 9, 3).

    SO THE SAME SOURCE SITS IN TWO CHANNELS depending on whether you chart what
    a channel IS or how well it is known.  Neither chart is the truer one; they
    are answers to different questions, which is section 2 of refusal.py's
    finding arriving from a fourth direction.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

    TO REPAIR THE TWENTY-FIVE.  Their B is wrong and this file does not guess
    what it should be.  They are dropped from the index, counted, and described.

    TO CALL 104,832 THE SIZE OF ANYTHING.  It is the row count.  The index is
    209 shapes.

    TO TREAT `delta` AS A COORDINATE.  The quantum defect is the quantity the
    channel equation PREDICTS; putting it on an axis of the index that is meant
    to test the equation would be assuming the answer.

    TO CALL THIS THE SPECTRA INDEX.  It is an index of channel SHAPES drawn from
    the spectra table.  A different chart of the same rows is a different index
    and section 4 builds one.
"""

import sys

import hlaw
import mi

sys.path.insert(0, "/home/user/Claude-Method-Works/tools")
import populate as _pop          # noqa: E402  -- the seated member, imported

GRADE = ("computed", "exact", "measured")
WITNESS = ("unwitnessed", "witnessed")
SHAPE = ("l", "B", "mult")

_SP = None
_ROWS = {}


def _spectra():
    global _SP
    if _SP is None:
        _SP = _pop.Spectra(_pop.DEFAULT_SPECTRA)
    return _SP


def _int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return None


def rows():
    """Every row of COORDINATES-2.13, as the corpus banks it."""
    return _spectra().rows


def malformed():
    """The rows whose B is not an integer -- a Pauli bound cannot be a decimal."""
    return [r for r in rows() if _int(r["B"]) is None]


def usable():
    """Rows with an integer B.  The twenty-five are dropped, not repaired."""
    if "u" not in _ROWS:
        _ROWS["u"] = [r for r in rows() if _int(r["B"]) is not None]
    return _ROWS["u"]


def index():
    """The 209 distinct channel shapes (l, B, mult)."""
    return frozenset((_int(r["l"]), _int(r["B"]), _int(r["mult"]))
                     for r in usable())


def provenance_chart():
    """(l, grade, witness) -- the same rows charted by how well they are known."""
    return frozenset((_int(r["l"]), GRADE.index(r["grade"]),
                      WITNESS.index(r["witness"])) for r in usable())


def grade_only_chart():
    """(l, grade) -- the provenance chart with its redundant coordinate dropped."""
    return frozenset((_int(r["l"]), GRADE.index(r["grade"]))
                     for r in usable())


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def counts():
    """({grade: n}, {witness: n}) over every row, malformed included."""
    g, w = {}, {}
    for r in rows():
        g[r["grade"]] = g.get(r["grade"], 0) + 1
        w[r["witness"]] = w.get(r["witness"], 0) + 1
    return g, w


def witnessed_is_measured():
    """(are the two sets identical, how many rows) -- not merely equal counts."""
    wit = {i for i, r in enumerate(rows()) if r["witness"] == "witnessed"}
    mea = {i for i, r in enumerate(rows()) if r["grade"] == "measured"}
    return wit == mea, len(wit)


def witness_is_monotone_in_grade():
    """The (grade, witness) pairs that occur, and whether witness is monotone."""
    pairs = sorted({(GRADE.index(r["grade"]), WITNESS.index(r["witness"]))
                    for r in usable()})
    by = dict(pairs)
    mono = all(by[a] <= by[b] for a in by for b in by if a <= b)
    return pairs, len(by) == len(set(g for g, _w in pairs)) and mono


def rows_per_shape():
    """(fewest, most) rows behind a single channel shape."""
    c = {}
    for r in usable():
        k = (_int(r["l"]), _int(r["B"]), _int(r["mult"]))
        c[k] = c.get(k, 0) + 1
    return min(c.values()), max(c.values())


# ---------------------------------------------------------------------------

def report():
    X = index()
    print("=" * 74)
    print("THE CHANNEL INDEX -- 209 shapes out of the corpus's largest table")
    print("=" * 74)
    print()
    g, w = counts()
    lo, hi = rows_per_shape()
    print("0. THE SOURCE. COORDINATES-2.13 via populate.Spectra.")
    print("   rows banked           %d" % len(rows()))
    print("   rows with integer B   %d" % len(usable()))
    print("   channel shapes        %d   (between %d and %d rows apiece)"
          % (len(X), lo, hi))
    print("   FIRST-ORDER: its members are channels, so it is not a re-charting")
    print("   of anything charts3.py censused.")
    print()

    print("1. THE INDEX.")
    print("   %d cells   K%d   closes %s   cell %s"
          % (len(X), mi.K(X), ", ".join(closers(X)) or "NOTHING", mi.cell(X)))
    print("   height %d  width %d  Dilworth %s"
          % (mi.height(X), mi.width(X), len(X) <= mi.height(X) * mi.width(X)))
    print()

    bad = malformed()
    print("2. TWENTY-FIVE ROWS CARRY A DECIMAL WHERE AN INTEGER BELONGS.")
    print("   B is min(p, n0-l-1), a Pauli bound. In %d rows it is a decimal."
          % len(bad))
    print("   AND ALL %d ARE measured AND witnessed -- %d of the %d most"
          % (len(bad), len(bad), g.get("measured", 0)))
    print("   authoritative rows the table has, which is %d per cent of them."
          % round(100 * len(bad) / max(1, g.get("measured", 1))))
    r0 = bad[0]
    print("     B %s  delta %s  Z %s  charge %s  l %s  mult %s  %s/%s"
          % (r0["B"], r0["delta"], r0["Z"], r0["charge"], r0["l"],
             r0["mult"], r0["grade"], r0["witness"]))
    print("   Both B and delta are decimals of the same magnitude, which is")
    print("   what a column slip looks like. RECORDED, NOT REPAIRED.")
    print()

    same, n = witnessed_is_measured()
    pairs, mono = witness_is_monotone_in_grade()
    A, B = grade_only_chart(), provenance_chart()
    print("3. TWO COLUMNS CARRYING ONE DISTINCTION.")
    print("   grade   %s" % g)
    print("   witness %s" % w)
    print("   the witnessed rows are EXACTLY the measured rows: %s (%d rows)"
          % (same, n))
    print("   so witness is a function of grade, and monotone: %s  %s"
          % (pairs, mono))
    print("   (l, grade)       %2d cells  K%d" % (len(A), mi.K(A)))
    print("   (l, grade, wit)  %2d cells  K%d   -- UNCHANGED, as DOCKET 3 requires"
          % (len(B), mi.K(B)))
    print("   THE FIRST CONFIRMATION OF THE CHART CRITERION OUTSIDE THE")
    print("   ELEMENT ADDRESS, on a source it was never fitted to.")
    print()

    print("4. THE PROVENANCE SUB-CHART REACHES K3.")
    print("   (l, grade, witness)  %d cells  K%d  closes %s  cell %s"
          % (len(B), mi.K(B), ", ".join(closers(B)), mi.cell(B)))
    print("   So the same source sits in TWO channels depending on whether you")
    print("   chart what a channel IS or how well it is KNOWN. Neither is the")
    print("   truer one; they answer different questions.")
    print()
    print("5. REFUSED: to repair the twenty-five. To call 104,832 the size of")
    print("   anything. To treat delta as a coordinate -- it is what the channel")
    print("   equation PREDICTS, and charting it would assume the answer. To")
    print("   call this THE spectra index: it is one chart of those rows.")
    return 0


# ---------------------------------------------------------------------------

def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("spectra selftest")
    X = index()

    # ---- the source
    chk("rows banked in COORDINATES-2.13", len(rows()), 104832)
    chk("rows with an integer B", len(usable()), 104807)
    chk("channel shapes -- THE INDEX", len(X), 209)
    chk("rows behind a shape, fewest and most", rows_per_shape(), (3, 3124))

    # ---- the index
    chk("it closes NOTHING", closers(X), [])
    chk("which is K0", mi.K(X), 0)
    chk("its cell on the admissible chart", mi.cell(X), (0, 16, 24))
    chk("Dilworth holds", len(X) <= mi.height(X) * mi.width(X), True)

    # ---- THE DATA FAULT, and it is in the best rows
    bad = malformed()
    chk("rows whose B is not an integer", len(bad), 25)
    chk("and EVERY ONE of them is measured and witnessed",
        sorted({(r["grade"], r["witness"]) for r in bad}),
        [("measured", "witnessed")])
    g, _w = counts()
    chk("which is 25 of the 358 most authoritative rows",
        (len(bad), g["measured"]), (25, 358))
    chk("their B values are decimals, not integers",
        all("." in r["B"] for r in bad), True)

    # ---- two columns, one distinction
    chk("grade counts", [g[k] for k in GRADE], [103545, 929, 358])
    _g, w = counts()
    chk("witness counts", [w[k] for k in WITNESS], [104474, 358])
    same, n = witnessed_is_measured()
    # NOT MERELY EQUAL COUNTS -- the same rows, checked one by one.
    chk("the witnessed rows are EXACTLY the measured rows", (same, n),
        (True, 358))
    pairs, mono = witness_is_monotone_in_grade()
    chk("so witness is a function of grade", pairs, [(0, 0), (1, 0), (2, 1)])
    chk("and that function is MONOTONE", mono, True)

    # ---- THE LIVE TEST OF THE CHART CRITERION, on a new source
    A, B = grade_only_chart(), provenance_chart()
    chk("(l, grade) and (l, grade, wit) have the same cell count",
        (len(A), len(B)), (21, 21))
    chk("AND THE SAME CHANNEL, as DOCKET 3 requires", (mi.K(A), mi.K(B)),
        (3, 3))
    chk("which is K3 -- geometry and statistics", closers(B),
        ["geometry", "statistics"])
    chk("the provenance chart's cell", mi.cell(B), (3, 9, 3))

    # ---- the same source in two channels
    chk("the shape chart and the provenance chart differ in channel",
        (mi.K(X), mi.K(B)), (0, 3))

    print("spectra selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
