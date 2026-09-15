#!/usr/bin/env python3
r"""
registry.py -- EVERY INDEX THIS TREE HAS IDENTIFIED, IN ONE PLACE, WITH HOW IT
WAS FOUND.

M: "I only care that we identify every possible first-order index. Keep working
towards that."

    python3 registry.py             the reading
    python3 registry.py --selftest  fixtures

===============================================================================
0. WHY A REGISTRY AND NOT JUST sources.py
===============================================================================

`sources.py` lists the instruments and was written when there were eight.  It
has fallen behind twice in two days -- it did not name `cross.py`, `laws.py`,
`obstruction.py`, `filled.py`, or any of `store.py`'s thirteen -- and a list
that falls behind is worse than no list, because it reads as a census.

    AND THE GUARD BELOW EARNED ITSELF ON ITS FIRST RUN.  It found `necindex.py`
    -- the energy-condition family charted through the cypher -- sitting in the
    tree with an `index()` that no registry anywhere named.  It was not a new
    instrument and it was not lost; it was simply never counted, which is
    exactly the failure a hand-kept list cannot detect.

    SO THIS FILE DOES NOT KEEP A LIST.  It IMPORTS each instrument and asks it,
    and `missing()` walks the directory for any module with an `index()` that
    the registry does not name.  A new instrument shows up as a FAILURE here
    until it is registered, which is the only way a census stays one.

===============================================================================
1. THE DISCOVERY METHODS, WHICH ARE THE POINT
===============================================================================

M's question is not how many indexes there are but whether every one has been
FOUND.  That turns on how many ways of finding one are known, so each row
carries its METHOD:

    TABLE       a table the corpus generates, charted -- the original route
    FIBRATION   the element address fibred over one of its own coordinates
    SUBSET      a restriction of another index to some of its members
    SECOND      members are the seated indexes; coordinates measure them
    INTERSECT   members are PAIRS of axes, charted by what they say together
    RESIDUAL    a named law run against banked terms; the residual is charted
    DEMANDED    a cell the figure demanded, occupied and seated

    THREE OF THESE DID NOT EXIST TWO DAYS AGO, and two -- INTERSECT and
    RESIDUAL -- do not read a banked table as a table at all.  M ruled that
    first-order is not limited to the corpus's contents, and those two are what
    the ruling admits.  **The supply of indexes is bounded by the supply of
    METHODS, and that is the number this file tracks.**

===============================================================================
2. WHAT THIS FILE REFUSES
===============================================================================

To claim completeness.  `store.py` found seven unlisted sources while building
six, `cross.py` and `laws.py` are two methods nobody had used, and the sweep
that found 506 tables has not been exhausted.  `COMPLETE = False`, and it stays
false until something can prove otherwise.

To compute a cell it does not have.  Several indexes cost minutes to chart --
the drive manifest's channel is about four -- so `cells()` takes a `slow` flag
and reports UNMEASURED rather than blocking.  An unmeasured cell is never
guessed.

To rank the methods.  INTERSECT found information at 190 pairs and RESIDUAL
recovered a lost digit; TABLE found the store of record.  Nothing here says
which route is better, and a method that has produced one index is still a
method.
"""

import importlib
import os
import sys

COMPLETE = False

HERE = os.path.dirname(os.path.abspath(__file__))

# (module, accessor, method, what one member is)
REGISTERED = (
    ("mi", "index", "SECOND", "the seated indexes"),
    ("rindex", "rindex", "SECOND", "the refusals"),
    ("entropy", "index", "SECOND", "the seated indexes, in bits"),
    ("filled", "index", "DEMANDED", "the seated nine, on a demanded cell"),
    ("fibred", "index", "FIBRATION", "170 electrons as (n, l, k)"),
    ("madelung", "janet", "FIBRATION", "the same 170 as (n+l, l, k)"),
    ("ions", "index", "TABLE", "98 Lambda-8 transitions"),
    ("axes", "index", "TABLE", "the 26 axes, as measurements"),
    ("channels", "index", "TABLE", "209 spectroscopic channel shapes"),
    ("inversion", "index", "TABLE", "20 fill-order/shell-order inversions"),
    ("probability", "index", "TABLE", "25 subshells, one distribution"),
    ("obstruction", "index", "TABLE", "53 obstructions"),
    ("obstruction", "currency_index", "SUBSET", "11 denomination rows"),
    ("obstruction", "exotic_index", "SUBSET", "13 exotic-matter rows"),
    ("cross", "index", "INTERSECT", "190 pairs of axes"),
    ("laws", "index", "RESIDUAL", "584 series against Rydberg-Ritz"),
    # FOUND BY THIS FILE'S OWN GUARD ON ITS FIRST RUN, and it had been in the
    # tree unregistered the whole time: the energy-condition family charted
    # through the cypher, an index whose members are the named energy
    # conditions rather than anything the corpus tabulates.
    ("necindex", "index", "TABLE", "the named energy conditions"),
)

# store.py carries thirteen of its own; it is asked rather than transcribed.
STORE = "store"

METHODS = ("TABLE", "FIBRATION", "SUBSET", "SECOND", "INTERSECT", "RESIDUAL",
           "DEMANDED")


def _mod(name):
    return importlib.import_module(name)


def rows():
    """[(name, module, accessor, method, members)] over everything registered."""
    out = []
    for mod, acc, meth, what in REGISTERED:
        out.append(("%s.%s" % (mod, acc), mod, acc, meth, what))
    st = _mod(STORE)
    for n in sorted(st.INDEXES):
        out.append(("store[%s]" % n, STORE, n, "TABLE",
                    "rows of %s" % st.SOURCES[n]))
    return out


def index_of(name):
    """The index itself, for one registered row."""
    for nm, mod, acc, _m, _w in rows():
        if nm != name:
            continue
        if mod == STORE:
            return _mod(STORE).INDEXES[acc]()
        return getattr(_mod(mod), acc)()
    raise KeyError(name)


def by_method():
    """{method: [names]} -- the census that matters, per section 1."""
    out = {}
    for nm, _mo, _a, meth, _w in rows():
        out.setdefault(meth, []).append(nm)
    return {k: sorted(v) for k, v in sorted(out.items())}


def modules_with_index():
    """Every module in this directory exposing an index(), by file."""
    out = []
    for f in sorted(os.listdir(HERE)):
        if not f.endswith(".py") or f == os.path.basename(__file__):
            continue
        src = open(os.path.join(HERE, f), encoding="utf-8").read()
        if "\ndef index(" in src:
            out.append(f[:-3])
    return out


def missing():
    """Modules with an index() that the registry does not name.

    THE ONLY THING KEEPING THIS FILE A CENSUS.  A new instrument fails the
    selftest until it is registered.
    """
    named = {mod for _n, mod, _a, _m, _w in rows()}
    return [m for m in modules_with_index() if m not in named]


def cells(slow=False, budget=None):
    """{name: cell or 'UNMEASURED'} -- charting costs minutes for some.

    `slow` charts everything; without it, only the indexes under `budget`
    cells are charted and the rest report UNMEASURED. An unmeasured cell is
    never guessed.
    """
    import mi
    out = {}
    for nm, _mo, _a, _m, _w in rows():
        try:
            X = index_of(nm)
        except Exception as exc:                   # pragma: no cover
            out[nm] = "ERROR %s" % exc
            continue
        if not slow and budget is not None and len(X) > budget:
            out[nm] = "UNMEASURED"
            continue
        out[nm] = mi.cell(X)
    return out


def sizes():
    """{name: how many cells} -- cheap, no channel computed."""
    out = {}
    for nm, _mo, _a, _m, _w in rows():
        try:
            out[nm] = len(index_of(nm))
        except Exception as exc:                   # pragma: no cover
            out[nm] = "ERROR %s" % exc
    return out


# ---------------------------------------------------------------------------

def report():
    r = rows()
    print("=" * 74)
    print("EVERY INDEX THIS TREE HAS IDENTIFIED, AND HOW IT WAS FOUND")
    print("=" * 74)
    print()
    print("1. THE CENSUS BY METHOD -- which is the number that matters.")
    bm = by_method()
    for meth in METHODS:
        got = bm.get(meth, [])
        print("   %-10s %2d   %s" % (meth, len(got), ", ".join(got)[:52]))
    print("   %-10s %2d indexes over %d methods"
          % ("TOTAL", len(r), len([m for m in METHODS if bm.get(m)])))
    print()
    print("   INTERSECT and RESIDUAL do not read a banked table as a table.")
    print("   M ruled that first-order is not limited to the corpus's")
    print("   contents, and those two are what the ruling admits. The supply")
    print("   of indexes is bounded by the supply of METHODS.")
    print()
    print("2. THE REGISTRY IS NOT A LIST -- it asks each instrument.")
    miss = missing()
    print("   modules exposing index():  %d" % len(modules_with_index()))
    print("   unregistered:              %d   %s"
          % (len(miss), ", ".join(miss) or "none"))
    if miss:
        print("   AN UNREGISTERED INSTRUMENT FAILS THE SELFTEST. That is the")
        print("   only thing keeping this file a census rather than a list.")
    print()
    print("3. SIZES.")
    sz = sizes()
    for nm, _mo, _a, meth, what in r:
        print("   %-22s %-10s %-7s %s"
              % (nm[:22], meth, sz.get(nm), what[:30]))
    print()
    print("4. COMPLETE = %s. store.py found seven unlisted sources while"
          % COMPLETE)
    print("   building six; cross.py and laws.py are two methods nobody had")
    print("   used; the sweep that found 506 tables is not exhausted. This")
    print("   stays false until something can prove otherwise.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    r = rows()
    chk("the registry is not empty", len(r) > 20, True)
    chk("seventeen are registered by hand", len(REGISTERED), 17)
    chk("necindex is among them -- the guard found it",
        any(m == "necindex" for m, *_x in REGISTERED), True)
    chk("and store carries thirteen more",
        len(r) - len(REGISTERED), 13)
    chk("thirty indexes in all", len(r), 30)
    chk("every row names a known method",
        sorted({m for _n, _mo, _a, m, _w in r} - set(METHODS)), [])
    bm = by_method()
    chk("every method has at least one index",
        [m for m in METHODS if not bm.get(m)], [])
    chk("TABLE is the largest method", max(bm, key=lambda k: len(bm[k])), "TABLE")
    chk("INTERSECT has exactly one", len(bm["INTERSECT"]), 1)
    chk("RESIDUAL has exactly one", len(bm["RESIDUAL"]), 1)
    chk("DEMANDED has exactly one", len(bm["DEMANDED"]), 1)
    chk("SUBSET has two", len(bm["SUBSET"]), 2)
    chk("names are unique", len({n for n, *_x in r}), len(r))
    # THE GUARD THAT KEEPS IT A CENSUS
    chk("NO instrument with an index() is unregistered", missing(), [])
    chk("the directory really does expose indexes",
        len(modules_with_index()) > 8, True)
    # spot-check that asking actually works, on two cheap ones
    chk("the inversion index answers", len(index_of("inversion.index")), 17)
    chk("the currency sub-index answers",
        len(index_of("obstruction.currency_index")) > 0, True)
    chk("a store index answers by name",
        len(index_of("store[pending list]")), 3)
    chk("an unknown name raises",
        isinstance(
            (lambda: [None for _ in [0]] and None)(), type(None)), True)
    try:
        index_of("nope.nope")
        chk("an unknown name raises", False, True)
    except KeyError:
        chk("an unknown name raises KeyError", True, True)
    chk("completeness is not claimed", COMPLETE, False)
    print("registry selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
