#!/usr/bin/env python3
r"""
obstruction.py -- THE OBSTRUCTION INDEX and its two sub-indexes: the currency
index and the exotic-matter index.  Fifty-three members, first-order, and the
first candidate this tree has for the cells only a first-order index can fill.

M: "I also suspect a information currency index, an exotic matter index (which
likely has a spectra, gravity, and other indexes associated)."

    python3 obstruction.py             the reading
    python3 obstruction.py --selftest  fixtures

===============================================================================
0. BOTH NAMES WERE ALREADY IN THE LEDGER, WHICH IS WHY THIS IS NOT AN INVENTION
===============================================================================

`obstruct.LEDGER` carries fifty-three rows, each a claim about why a warp drive
cannot be built, with a status and the instrument that settled it.  Two of those
rows are named almost exactly as M named them:

    INFORMATION-CURRENCY   "the bill can be paid in information rather than
                            mass-energy"                    CLOSED-NEGATIVE
    EXOTIC-MATTER          "warp transport needs negative energy"
                                                            DISSOLVED

So the objects exist and are banked.  What did not exist is an INDEX over them --
the ledger is a list, and nothing had asked what shape it has.

===============================================================================
1. THE MEMBERS, AND THE THREE SETS
===============================================================================

    the obstruction index   all 53 rows
    the currency index      the rows that price the bill in some denomination
    the exotic-matter index the rows about negative energy and what supplies it

    THE TWO SUB-SETS ARE RECONSTRUCTED AND THE STATUS IS NOT FLATTENED.  The
    ledger does not tag a row as a currency row or an exotic-matter row; the
    groupings below are read off the claims by hand and are named in
    `CURRENCY_ROWS` and `EXOTIC_ROWS` so they can be argued with.  Every figure
    that depends on them inherits `SUBSETS_ARE_RECONSTRUCTED = True`.  The full
    fifty-three inherit nothing: that set is the ledger.

    AND THE SUB-INDEXES ARE SUB-INDEXES, which is the shape M predicted.  The
    currency index and the exotic-matter index are restrictions of the same
    index to subsets of its members -- same coordinates, same operators, same
    laws -- so "an exotic matter index with other indexes associated" is a
    statement about member sets, and it is literally true here.

===============================================================================
2. THE THREE COORDINATES
===============================================================================

        status    where the row stands.  GIVEN -- the ledger states it per row.
        checked   1 if `obstruct.py` carries a `check_<row>` function that
                  re-derives the verdict, 0 if the row rests on prose.  READ by
                  introspection, not by a list kept here.
        load      how many of the fifty-three the settling instrument settles.
                  A row closed by a file that closed four is differently
                  supported from one closed by a file that closed only it.

    THE STATUS ORDER IS RECONSTRUCTED AND SAYS SO.  `STATUS_ORDER` puts
    DISSOLVED below RELOCATED below CONDITIONAL below CLOSED-NEGATIVE below OPEN
    -- increasing in how much of the obstruction survives.  Nothing in the
    corpus orders them, `axes.py` had the same problem with its provenance words
    and solved it the same way, and `STATUS_ORDER_IS_RECONSTRUCTED = True` is
    carried here for the same reason.

===============================================================================
3. WHAT THIS FILE REFUSES
===============================================================================

To read `checked` as a quality score.  A row with no `check_` function may rest
on a calculation in another instrument entirely; the coordinate measures what
`obstruct.py` itself re-derives, and nothing more.

To treat the sub-sets as the corpus's own.  They are this file's reading, and a
different reading gives a different index.  The full fifty-three are not a
reading of anything.

To claim any of the three fills a demanded cell.  `occupy.py` measured that eight
of the ten cells the figure is missing can only be first-order; this is the first
first-order candidate built since.  Where it lands is reported in section 6
whichever way it goes, and the two indexes built before it both missed.
"""

import collections
import sys

import hlaw
import mi
import obstruct

SUBSETS_ARE_RECONSTRUCTED = True
STATUS_ORDER_IS_RECONSTRUCTED = True

STATUS_ORDER = ("DISSOLVED", "RELOCATED", "CONDITIONAL", "CLOSED-NEGATIVE",
                "OPEN", "UNTESTED")

# Read off the claims by hand.  See section 1: RECONSTRUCTED, and arguable.
CURRENCY_ROWS = ("ENERGY", "ER-BRIDGE", "BALANCE-EVADES-PMT",
                 "INFORMATION-CURRENCY", "SPECTRAL-CURRENCY",
                 "LIGHT-AS-THE-SOURCE", "CHARGE-STATE",
                 "COLLECTION-IN-TRANSIT", "CHEAPER-CURRENCY",
                 "LIGHT-AS-THE-SUPPLY", "COMPRESSION-IS-DENSITY")

EXOTIC_ROWS = ("EXOTIC-MATTER", "ANEC", "ACHRONALITY", "TYPE-IV",
               "TYPEIV-SOURCES", "BARE-NEGATIVE-MASS", "DEVICE-SHELL",
               "ENTANGLEMENT-ROUTE", "GRAHAM-OLUM-ESCAPE", "SNEC-LOOPHOLE",
               "CORE-TYPE-IV", "MODIFIED-GRAVITY-DOOR", "STATIC-BOUND")


def rows():
    """[(name, claim, status, reason, instrument)] -- the ledger, unaltered."""
    return list(obstruct.LEDGER)


def checked_names():
    """The row names obstruct.py re-derives, by introspection not by a list.

    A `check_<slug>` function is matched to a row by lowercasing the row name
    and replacing '-' with '_'; the match is partial in both directions because
    the file's naming is not perfectly regular, and `check_coverage()` reports
    how many functions went unmatched so the looseness is visible.
    """
    fns = [n[6:] for n in dir(obstruct) if n.startswith("check_")]
    out, used = set(), set()
    for name, *_rest in obstruct.LEDGER:
        slug = name.lower().replace("-", "_")
        for f in fns:
            if f == slug or f.startswith(slug) or slug.startswith(f):
                out.add(name)
                used.add(f)
    return out, sorted(set(fns) - used)


def check_coverage():
    """(rows matched, check_ functions, functions matched to no row)."""
    got, unused = checked_names()
    fns = [n for n in dir(obstruct) if n.startswith("check_")]
    return len(got), len(fns), unused


def load():
    """{instrument: how many of the 53 it settles}."""
    return dict(collections.Counter(r[4] for r in obstruct.LEDGER))


def coords(row):
    """(status, checked, load) for one ledger row."""
    name, _claim, status, _reason, inst = row
    got, _u = checked_names()
    return (STATUS_ORDER.index(status), 1 if name in got else 0,
            load()[inst])


def index(names=None):
    """The obstruction index, or its restriction to `names`."""
    rs = rows() if names is None else [r for r in rows() if r[0] in set(names)]
    return frozenset(coords(r) for r in rs)


def currency_index():
    return index(CURRENCY_ROWS)


def exotic_index():
    return index(EXOTIC_ROWS)


def members(names=None):
    """How many ledger rows the index is built from (not its cell count)."""
    return len(rows() if names is None else
               [r for r in rows() if r[0] in set(names)])


def named_rows_exist():
    """[(name, present)] -- every name in the two subsets is a real ledger row.

    A typo in CURRENCY_ROWS would silently shrink the index, so this is a
    fixture rather than a comment.
    """
    have = {r[0] for r in rows()}
    return [(n, n in have) for n in CURRENCY_ROWS + EXOTIC_ROWS]


def criterion(names=None):
    """{coordinate: moves under a monotone redundant append}.  DOCKET 3."""
    X = index(names)
    lifted = frozenset(t + (t[0],) for t in X)
    return {"K": 0 if mi.K(X) == mi.K(lifted) else 1,
            "height": 0 if mi.height(X) == mi.height(lifted) else 1,
            "width": 0 if mi.width(X) == mi.width(lifted) else 1}


def closers(names=None):
    X = index(names)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell(names=None):
    return mi.cell(index(names))


def faithful(names=None):
    """(members, distinct cells) -- how much the three coordinates forget."""
    return members(names), len(index(names))


def status_spread(names=None):
    """{status: count} over the chosen member set."""
    rs = rows() if names is None else [r for r in rows() if r[0] in set(names)]
    return dict(collections.Counter(r[2] for r in rs))


def sub_index_law():
    """[(name, members, cell, is a subset of the full index?)].

    A restriction to a subset of members must give a SUBSET of the cells.  That
    is not deep, but it is the thing that makes "sub-index" mean something, so
    it is checked.
    """
    full = index()
    out = []
    for nm, ns in (("currency", CURRENCY_ROWS), ("exotic matter", EXOTIC_ROWS)):
        X = index(ns)
        out.append((nm, members(ns), mi.cell(X), X <= full))
    return out


def against_demand():
    """[(name, cell, verdict)] -- where each of the three lands on the figure."""
    import demand
    import hexad
    D = set(demand.demand(hexad.figure()))
    J, _r = demand.closure(hexad.figure())
    out = []
    for nm, ns in (("obstruction index", None), ("currency index", CURRENCY_ROWS),
                   ("exotic-matter index", EXOTIC_ROWS)):
        c = cell(ns)
        if c in D:
            v = "DEMANDED -- seating it drops E by one"
        elif c in J:
            v = "already a cell of the closure"
        elif demand.neutral(c, hexad.figure()):
            v = "neutral -- costs nothing, closes nothing"
        else:
            v = "disruptive -- raises E by %d" % (
                demand.E(hexad.figure() | {c}) - demand.E(hexad.figure()))
        out.append((nm, c, v))
    return out


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("THE OBSTRUCTION INDEX, AND THE TWO SUB-INDEXES M NAMED")
    print("=" * 74)
    print()
    print("1. BOTH NAMES WERE ALREADY IN THE LEDGER.")
    for n in ("INFORMATION-CURRENCY", "EXOTIC-MATTER"):
        r = next(x for x in rows() if x[0] == n)
        print("   %-22s %-16s %s" % (r[0], r[2], r[1]))
    print("   So the objects are banked. What did not exist is an INDEX over")
    print("   them -- the ledger is a list, and nothing had asked its shape.")
    print()

    print("2. THE MEMBER SETS.")
    for nm, ns in (("obstruction", None), ("currency", CURRENCY_ROWS),
                   ("exotic matter", EXOTIC_ROWS)):
        m, k = faithful(ns)
        print("   %-16s %2d rows -> %2d distinct cells   %s"
              % (nm, m, k, status_spread(ns)))
    print("   The two sub-sets are RECONSTRUCTED -- read off the claims by hand,")
    print("   named in the source so they can be argued with.")
    print()

    print("3. THE COORDINATES.")
    got, fns, unused = check_coverage()
    print("   status    GIVEN by the ledger; the ORDER is RECONSTRUCTED")
    print("   checked   %d of 53 rows have a check_ function (%d functions, %d"
          % (got, fns, len(unused)))
    print("             matched no row)")
    print("   load      %d distinct instruments; the busiest settles %d rows"
          % (len(load()), max(load().values())))
    print()

    print("4. A SUB-INDEX IS A SUBSET OF CELLS, CHECKED.")
    for nm, m, c, sub in sub_index_law():
        print("   %-16s %2d members  cell %-12s subset of the full: %s"
              % (nm, m, str(c), sub))
    print()

    print("5. THE CHART CRITERION (DOCKET 3).")
    bad = False
    for nm, ns in (("obstruction", None), ("currency", CURRENCY_ROWS),
                   ("exotic matter", EXOTIC_ROWS)):
        crit = criterion(ns)
        bad |= any(crit.values())
        print("   %-16s K %d  height %d  width %d   %s"
              % (nm, crit["K"], crit["height"], crit["width"],
                 "all admissible" if not any(crit.values()) else "A COORDINATE MOVED"))
    if bad:
        print("   The reading below is void.")
        return 1
    print()

    print("6. WHERE THEY LAND -- reported whichever way it goes.")
    print("   %-22s %-12s %s" % ("index", "cell", "verdict"))
    for nm, c, v in against_demand():
        print("   %-22s %-12s %s" % (nm, str(c), v))
    for nm, ns in (("obstruction", None), ("currency", CURRENCY_ROWS),
                   ("exotic matter", EXOTIC_ROWS)):
        print("   %-16s closes %s" % (nm, ", ".join(closers(ns)) or "nothing"))
    print()

    print("7. REFUSED: to read `checked` as a quality score -- it measures what")
    print("   obstruct.py itself re-derives, not whether a row is well founded.")
    print("   To treat the two sub-sets as the corpus's own. To claim any of the")
    print("   three fills a demanded cell: the two indexes built before these")
    print("   both missed, and that is the control.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("the ledger is fifty-three rows", len(rows()), 53)
    chk("every subset name is a real ledger row",
        [n for n, p in named_rows_exist() if not p], [])
    chk("INFORMATION-CURRENCY is banked",
        any(r[0] == "INFORMATION-CURRENCY" for r in rows()), True)
    chk("and it is CLOSED-NEGATIVE",
        next(r[2] for r in rows() if r[0] == "INFORMATION-CURRENCY"),
        "CLOSED-NEGATIVE")
    chk("EXOTIC-MATTER is banked and DISSOLVED",
        next(r[2] for r in rows() if r[0] == "EXOTIC-MATTER"), "DISSOLVED")
    chk("every ledger status is in STATUS_ORDER",
        sorted({r[2] for r in rows()} - set(STATUS_ORDER)), [])
    chk("the status order is flagged RECONSTRUCTED",
        STATUS_ORDER_IS_RECONSTRUCTED, True)
    chk("the subsets are flagged RECONSTRUCTED", SUBSETS_ARE_RECONSTRUCTED, True)
    chk("currency members", members(CURRENCY_ROWS), len(CURRENCY_ROWS))
    chk("exotic members", members(EXOTIC_ROWS), len(EXOTIC_ROWS))
    chk("the sub-sets do not exhaust the ledger",
        members(CURRENCY_ROWS) + members(EXOTIC_ROWS) < 53, True)
    for nm, _m, _c, sub in sub_index_law():
        chk("the %s index is a subset of the full one" % nm, sub, True)
    got, fns, _u = check_coverage()
    chk("some rows are machine-checked", got > 0, True)
    chk("not all of them are", got < 53, True)
    chk("there are check_ functions to match", fns >= 20, True)
    chk("the load sums to the ledger", sum(load().values()), 53)
    for nm, ns in (("obstruction", None), ("currency", CURRENCY_ROWS),
                   ("exotic matter", EXOTIC_ROWS)):
        crit = criterion(ns)
        chk("%s: K admissible" % nm, crit["K"], 0)
        chk("%s: height admissible" % nm, crit["height"], 0)
        chk("%s: width admissible" % nm, crit["width"], 0)
        c = cell(ns)
        chk("%s: the cell is a 3-tuple" % nm, len(c), 3)
        chk("%s: height and width bound the size" % nm,
            max(c[1], c[2]) <= len(index(ns)) <= c[1] * c[2], True)
    chk("the three verdicts are all reported", len(against_demand()), 3)
    print("obstruction selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
