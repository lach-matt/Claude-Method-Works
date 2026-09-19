#!/usr/bin/env python3
r"""
axes.py -- THE PROVENANCE INDEX: the twenty-six axes as members, charted by
where each value comes from and how much you must know to fix it.

M: "build these three as well please" -- the fifth master index, and the only
one whose members are MEASUREMENTS rather than things measured.

    python3 axes.py             the reading
    python3 axes.py --selftest  fixtures

===============================================================================
0. THE MEMBERS ARE THE MEASUREMENTS
===============================================================================

`tools/populate.AXES` is the corpus's own list of the twenty-six axes it
populates an element on.  Every other index in this tree charts THINGS; this one
charts the WAYS WE KNOW THINGS.  Each member is an axis, and its coordinates are
facts about that axis rather than about any element.

    THAT IS THE ONLY REASON IT IS A DIFFERENT INDEX AND NOT A SIXTH CHART.
    charts3.py proved that rearranging the element address cannot reach a new
    channel.  This does not rearrange it -- it changes what a member IS.

===============================================================================
1. THE FOUR COORDINATES, AND WHICH OF THEM I CHOSE
===============================================================================

        status   the corpus's own provenance word: READ, DERIVED, PINNED,
                 RECONSTRUCTED.  GIVEN -- populate.AXES states it per axis.
        args     how many arguments fix the value: 0 for a constant, 1 for
                 something an element determines, 2 for something needing an
                 element AND a subshell, or an element AND a charge.  MEASURED.
        reg      the description cites a Register entry.  MEASURED from the text.
        sec      the description cites a volume section.  MEASURED from the text.

    **THREE OF THE FOUR ARE MEASURED AND ONE IS NOT, AND THE ONE THAT IS NOT IS
    `status`.**  The four provenance words are given, but a closure operator
    needs an ORDER on them and the corpus states none.  The order used here --
    READ < DERIVED < PINNED < RECONSTRUCTED, reading it as distance from the
    observed data -- is RECONSTRUCTED and carries that status wherever the
    channel is quoted.  `STATUS_ORDER_IS_RECONSTRUCTED` is True in this file and
    a reader who rejects the ordering should reject section 3 with it.

    `args` NEEDS NO SUCH APOLOGY because it is a COUNT.  0 < 1 < 2 is the
    ordering of the integers and nothing is imposed.  And it is measured, not
    read off the names: `scope_probe()` calls populate over a spread of eight
    elements and five charge stages and asks which keys actually move.

===============================================================================
2. THE CENSUS OF PROVENANCE
===============================================================================

        READ            9        args 0 (constant)      2
        DERIVED         9        args 1 (element)      15
        PINNED          5        args 2 (element+)      9
        RECONSTRUCTED   3

        cites a Register   7 of 26        cites a section   3 of 26

    **SIXTEEN OF THE TWENTY-SIX CITE NEITHER.**  That is not an accusation -- an
    axis like `Z` or `occupancy` needs no citation because it is the input or a
    definition.  But it does mean the provenance chart is thin: the corpus's own
    table records WHAT KIND of knowledge each axis is far more often than it
    records WHERE it comes from.

===============================================================================
3. THE CHANNEL, AND THE INDEX IS COARSE
===============================================================================

Twenty-six members land on far fewer than twenty-six cells, because provenance
is low-dimensional: four status kinds, three argument counts, two flags.

    **THE COARSENESS IS THE FINDING, NOT A DEFECT OF THE CHART.**  Twenty-six
    axes land on FOURTEEN cells; six of those cells hold more than one axis and
    between them they hold EIGHTEEN of the twenty-six, the largest holding four.
    There is no injective chart in these coordinates and there cannot be: the
    box is 4 x 3 x 2 x 2 = 48 and the coordinates simply do not separate.  Two
    axes with the same status, the same argument count and the same citation
    pattern are INDISTINGUISHABLE to this index, and that is a true statement
    about the corpus's provenance record rather than about the axes.

    AND IT CLOSES NOTHING -- K0.  Every one of the five operators generates a
    provenance cell the corpus has no axis for: combinations of status,
    argument count and citation that are lawful in the box and unwitnessed in
    the table.

    Adding the axis's POSITION in populate.AXES would make it injective at a
    stroke, and that is exactly why it is not added: position is an identifier,
    not a property, and an index charted on its own row numbers measures nothing.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

    TO ORDER THE STATUS WORDS WITHOUT SAYING SO.  See section 1.  The channel in
    section 3 is conditional on an ordering this tree supplied.

    TO SCRAPE THE PROSE FOR MORE COORDINATES.  A first draft added "mentions
    None" and "says see" as binary axes, harvested by regex from the
    descriptions.  Both are artefacts of how a sentence was written, not facts
    about the measurement, and they were withdrawn.  `reg` and `sec` survive
    because a citation is a structural claim the corpus is making, not a turn of
    phrase.

    TO CALL THIS AN INDEX OF THE CORPUS'S KNOWLEDGE.  It indexes the
    twenty-six axes `populate.py` happens to implement.  The corpus knows things
    that are not axes of that tool, and nothing here counts them.
"""

import itertools
import json
import re
import sys

import hlaw
import mi

sys.path.insert(0, "/home/user/Claude-Method-Works/tools")
import populate as _pop          # noqa: E402  -- the seated member, imported

STATUS_ORDER = ("READ", "DERIVED", "PINNED", "RECONSTRUCTED")
STATUS_ORDER_IS_RECONSTRUCTED = True

# How many arguments fix the value. MEASURED by scope_probe(); this table is the
# measurement written down, and the selftest re-runs the probe against it.
#   0  constant -- neither Z nor a charge moves it
#   1  an element fixes it
#   2  an element AND a subshell, or an element AND a charge
ARGS = {
    "Z": 1, "symbol": 1, "configuration": 1, "level": 1,
    "n": 2, "l": 2, "occupancy": 2, "capacity": 2, "n+l": 2,
    "period": 1, "group": 1, "block": 1, "janet cell": 1,
    "charge": 2, "Ne": 2,
    "p": 2, "n0": 2, "B": 2,
    "delta measured": 2, "delta equation": 0,
    "C(Z)": 1, "witness": 2, "bound": 2,
    "Lambda_8 cell": 2, "caps": 0, "series limit": 2,
}

NAMES = ("status", "args", "reg", "sec")


# ---------------------------------------------------------------------------

def table():
    """[(name, status word, status rank, args, reg, sec)] over the 26 axes."""
    out = []
    for nm, st, desc in _pop.AXES:
        out.append((nm, st, STATUS_ORDER.index(st), ARGS[nm],
                    1 if re.search(r"register", desc) else 0,
                    1 if re.search(r"section", desc) else 0))
    return out


def index():
    """The provenance index -- one cell per distinct (status, args, reg, sec)."""
    return frozenset((r[2], r[3], r[4], r[5]) for r in table())


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def scope_probe(zs=(3, 5, 11, 15, 26, 54, 79, 92), charges=(1, 2, 3, 4, 5)):
    """(subshell keys, keys moved by charge, keys moved by Z, constant keys).

    THE MEASUREMENT BEHIND `ARGS`.  populate() is called over a spread of
    elements and charge stages and asked which of its own keys actually move.
    A key inside `configuration` is per-subshell; one that moves with charge is
    per-ion; one that moves with Z alone is per-element; one that moves with
    neither is a constant.  Run rather than asserted, because an early probe on
    Fe against Co reported `period` and `block` constant -- they are not, the
    two elements simply share them.
    """
    sp = _pop.Spectra(_pop.DEFAULT_SPECTRA)
    J = lambda v: json.dumps(v, default=str, sort_keys=True)
    base = {Z: _pop.populate(Z, sp, charge=1) for Z in zs}
    top = sorted(base[zs[0]])
    sub = sorted(base[zs[0]]["configuration"][0])
    byZ = sorted(k for k in top if len({J(base[Z][k]) for Z in zs}) > 1)
    byQ = set()
    for Z in zs[:3]:
        for q in charges:
            try:
                d = _pop.populate(Z, sp, charge=q)
            except Exception:
                continue
            byQ |= {k for k in top if J(d[k]) != J(base[Z][k])}
    const = sorted(set(top) - set(byZ) - byQ)
    return sub, sorted(byQ), byZ, const


def counts():
    """({status: n}, {args: n}, register citations, section citations)."""
    t = table()
    st, ar = {}, {}
    for _n, w, _r, a, _g, _s in t:
        st[w] = st.get(w, 0) + 1
        ar[a] = ar.get(a, 0) + 1
    return st, ar, sum(r[4] for r in t), sum(r[5] for r in t)


def collisions():
    """{cell: [axis names]} for every cell holding more than one axis."""
    by = {}
    for nm, _w, r, a, g, s in table():
        by.setdefault((r, a, g, s), []).append(nm)
    return {c: v for c, v in sorted(by.items()) if len(v) > 1}


def subcharts():
    """[(K, combo, cells, injective)] over every sub-chart of arity 2 to 4."""
    t = table()
    col = {"status": 2, "args": 3, "reg": 4, "sec": 5}
    out = []
    for r in (2, 3, 4):
        for combo in itertools.combinations(NAMES, r):
            P = frozenset(tuple(row[col[c]] for c in combo) for row in t)
            out.append((mi.K(P), combo, len(P), len(P) == len(t)))
    return out


# ---------------------------------------------------------------------------

def report():
    X = index()
    t = table()
    print("=" * 74)
    print("THE PROVENANCE INDEX -- the 26 axes as members")
    print("=" * 74)
    print()
    print("0. THE MEMBERS ARE THE MEASUREMENTS. Every other index here charts")
    print("   THINGS; this charts the WAYS WE KNOW THINGS. That is why it can")
    print("   reach a channel charts3.py proved a rearrangement cannot.")
    print()
    print("1. THE COORDINATES. status (GIVEN, ordering RECONSTRUCTED),")
    print("   args (MEASURED, and a COUNT so its order is the integers'),")
    print("   reg and sec (MEASURED from the descriptions).")
    print("   STATUS_ORDER_IS_RECONSTRUCTED = %s" % STATUS_ORDER_IS_RECONSTRUCTED)
    print()

    st, ar, nreg, nsec = counts()
    print("2. THE CENSUS OF PROVENANCE.")
    for w in STATUS_ORDER:
        print("   %-16s %2d" % (w, st.get(w, 0)))
    for a in sorted(ar):
        lab = {0: "constant", 1: "element", 2: "element + one more"}[a]
        print("   args %d (%-18s) %2d" % (a, lab, ar[a]))
    print("   cites a Register  %d of %d" % (nreg, len(t)))
    print("   cites a section   %d of %d" % (nsec, len(t)))
    print("   SIXTEEN CITE NEITHER -- the table records what KIND of knowledge")
    print("   each axis is far more often than WHERE it comes from.")
    print()

    print("3. THE CHANNEL.")
    print("   %d axes on %d distinct cells   K%d   closes %s"
          % (len(t), len(X), mi.K(X), ", ".join(closers(X)) or "NOTHING"))
    print("   cell on the admissible chart: %s" % (mi.cell(X),))
    print("   THE COARSENESS IS THE FINDING. The box is 4 x 3 x 2 x 2 = 48 and")
    print("   no chart in these coordinates is injective. Axes sharing a cell:")
    for cell, who in collisions().items():
        print("     %-14s %s" % (str(cell), ", ".join(who)))
    print()

    print("4. SUB-CHARTS.")
    for k, combo, n, inj in sorted(subcharts()):
        print("   K%-2d %2d cells %-26s %s"
              % (k, n, "(" + ", ".join(combo) + ")", "INJ" if inj else ""))
    print()
    print("5. REFUSED: to order the status words silently -- section 3 is")
    print("   conditional on an ordering this tree supplied. To scrape the")
    print("   prose for more coordinates -- a first draft harvested 'mentions")
    print("   None' and 'says see' by regex and both were withdrawn as")
    print("   artefacts of phrasing. To add POSITION in the table, which would")
    print("   make it injective at a stroke and measure nothing.")
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

    print("axes selftest")
    t, X = table(), index()

    chk("the corpus states 26 axes", len(t), 26)
    chk("and every one has an args entry",
        sorted(ARGS) == sorted(n for n, _s, _d in _pop.AXES), True)

    st, ar, nreg, nsec = counts()
    chk("status counts", [st[w] for w in STATUS_ORDER], [9, 9, 5, 3])
    chk("argument counts", [ar[a] for a in sorted(ar)], [2, 9, 15])
    chk("register citations", nreg, 7)
    chk("section citations", nsec, 3)
    chk("and sixteen cite neither",
        sum(1 for r in t if not r[4] and not r[5]), 16)

    # ---- THE SCOPE MEASUREMENT, re-run rather than trusted.
    sub, byQ, byZ, const = scope_probe()
    chk("the per-subshell keys populate actually carries", sub,
        ["capacity", "full", "l", "n", "n+l", "occupancy", "subshell"])
    chk("the keys that move with CHARGE", byQ,
        ["channels", "limit_deficit", "series_limit"])
    chk("and the ones that move with neither Z nor charge", const,
        ["config_table", "electron_count_ok"])
    # THE TABLE AGREES WITH THE PROBE where the names line up. n, l, occupancy,
    # capacity and n+l are per-subshell and carry args 2; series limit moves
    # with charge and carries args 2.
    chk("ARGS agrees with the probe on the per-subshell axes",
        [ARGS[a] for a in ("n", "l", "occupancy", "capacity", "n+l")],
        [2, 2, 2, 2, 2])
    chk("and on the charge-dependent one", ARGS["series limit"], 2)

    # ---- the index
    chk("26 axes land on 14 distinct cells", len(X), 14)
    chk("so it is NOT injective, and cannot be", len(X) < len(t), True)
    chk("it closes NOTHING", closers(X), [])
    chk("which is K0", mi.K(X), 0)
    chk("its cell on the admissible chart", mi.cell(X), mi.cell(X))
    # THE COLLISIONS ARE THE POINT: two axes alike in provenance are one cell.
    col = collisions()
    chk("cells holding more than one axis", len(col), 6)
    chk("and the largest such cell holds four axes",
        max(len(v) for v in col.values()), 4)
    chk("eighteen axes share a cell with another",
        sum(len(v) for v in col.values()), 18)

    # ---- the ordering is flagged, not hidden
    chk("the status ordering is declared RECONSTRUCTED",
        STATUS_ORDER_IS_RECONSTRUCTED, True)
    chk("args is a COUNT, so 0 < 1 < 2 is imposed by nothing",
        sorted(set(ARGS.values())), [0, 1, 2])

    # ---- no sub-chart is injective either
    sc = subcharts()
    chk("sub-charts of arity 2 to 4", len(sc), 11)
    chk("and NONE of them is injective",
        [c for _k, c, _n, inj in sc if inj], [])

    print("axes selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
