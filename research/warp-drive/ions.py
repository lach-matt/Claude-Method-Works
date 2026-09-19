#!/usr/bin/env python3
r"""
ions.py -- THE IONISATION LADDER: an index over IONS, and the first source to
reach a channel the element address cannot.

M: "build these three as well please" -- the fourth master index, over a member
set the first three do not touch.

    python3 ions.py             the reading
    python3 ions.py --selftest  fixtures

===============================================================================
0. THE WARNING FIRST, BECAUSE EVERYTHING HERE RESTS ON IT
===============================================================================

**THIS INDEX IS BUILT ON A RECONSTRUCTION AND THE CORPUS SAYS SO.**
`tools/populate.ionisation_cells` carries the status RECONSTRUCTED in its own
docstring, and states why:

    "Chapter 7 makes a Lambda_8 cell a TRANSITION -- a source configuration, a
    target configuration and the electron count moved between them -- so an
    element is not a cell and a mapping has to be chosen. The one chosen here
    is the element's own ionisation ladder... Nothing else in the store fixes
    this mapping, so it is marked RECONSTRUCTED and a later ruling can move it."

So every channel below is a fact about THAT MAPPING as much as about ions.  A
different mapping from elements to Lambda_8 cells -- and chapter 7 does not
forbid one -- could give a different index and a different channel.  The status
is not flattened anywhere in this file, and the headline in section 4 inherits
it in full.

===============================================================================
1. THE CONSTRUCTION
===============================================================================

A Lambda_8 cell is a TRANSITION, not an element:

    (sn, sl, k, q, tn, tl, g, 2S)

        sn, sl   the SOURCE subshell the electrons leave
        k        the parent's occupancy of that subshell
        q        how many electrons leave it
        tn, tl   the TARGET subshell
        g        how many arrive there
        2S       the ion's ground multiplicity

    **THE EIGHTH SLOT IS ALWAYS None AND IS DROPPED.**  2S is known only where
    the ion's term is known; over all 5,778 stage rows the corpus banks it NOT
    ONCE.  A coordinate with one value carries no information and would make
    every closure trivially wider, so the index is charted on the seven that are
    determined.  The drop is recorded, not silent: `RAW_ARITY` is 8 and
    `ARITY` is 7, and the selftest pins that the dropped slot really is
    constant rather than merely sparse.

**5,778 STAGE ROWS COLLAPSE TO 98 CELLS, AND THE COLLAPSE IS STRUCTURAL.**
Walking every element Z <= 108 and every charge stage gives 5,778 rows.  But
`ionisation_cells` builds each cell from `LW1.expand(Ne)` and `LW1.expand(Ne+1)`
alone -- the ELECTRON COUNT, never Z -- so the cell is a function of Ne and
nothing else.  Every element's ladder is a suffix of one universal ladder.

    107 electron counts produce 98 distinct cells, so nine collide.  The index
    is the 98, and reporting 5,778 would be counting the same transition once
    per element that passes through it.

===============================================================================
2. IT CLOSES NOTHING
===============================================================================

    98 cells, arity 7, box 43,904        K0 -- no language closes it
    cell on the admissible chart         (0, 18, 16)

That is the same channel as four of the nine master-index members and as every
element chart carrying two shell coordinates.  K0 is not a failure; it is the
statement that every one of the five operators generates cells this index does
not hold.

===============================================================================
3. THE SUB-CHART CENSUS
===============================================================================

Over all 120 sub-charts of arity 2 to 7:

        channels reached by ANY sub-chart     K0, K2, K3, K4, K7
        channels reached INJECTIVELY          K0 only
        never reached                         K1, K5, K6

    **INJECTIVELY, ONLY K0.**  Thirty-two sub-charts keep all 98 cells distinct
    and every one of them closes nothing.  So as a FAITHFUL index the ionisation
    ladder is a K0 object, flatly, with no alternative chart available.

===============================================================================
4. AND IT REACHES K4, WHICH THE ELEMENT ADDRESS CANNOT
===============================================================================

`charts3.py` censused 372 charts built from the differentiating electron's
address (n, l, k) and proved K1, K4 and K5 are **never reached, by any chart in
that pool**.  Here:

        (sl, tl)     7 cells     K4 = {information, statistics}

    **THE SOURCE SUBSHELL'S l AGAINST THE TARGET SUBSHELL'S l.**  One chart, of
    the hundred and twenty, and it is the only one.  It is the first object in
    this tree to sit in K4.

    THIS IS WHAT "A NEW SOURCE, NOT A NEW ARRANGEMENT" MEANT, and it is now
    demonstrated rather than predicted: changing the member set from elements to
    transitions reaches a channel that no rearrangement of the element address
    could.  charts3.py's negative result stands unaltered -- it was a statement
    about that pool and this is a different pool.

    THE PRICE, AND IT IS THE SAME PRICE AS K6's.  (sl, tl) holds 7 cells against
    98: it is a heavy COARSENING, and ninety-one cells lose their identity.  Like
    the K6 chart of DOCKET 10, K4 here is reachable and not faithful.  DOCKET 11
    records the pattern rather than ruling on it.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

    THAT THE LADDER IS SEATED.  It is built and measured; seating it in the
    master index is a ruling, and the RECONSTRUCTED status of the mapping is
    exactly the kind of thing a ruling should weigh first.

    THAT 5,778 IS THE SIZE OF ANYTHING.  It is the number of (element, stage)
    pairs, and the same 98 transitions seen repeatedly.  Quoting it as a cell
    count would be counting elements while claiming to count transitions.

    THAT 2S IS ABSENT BECAUSE IT IS ZERO.  It is absent because the corpus banks
    no ion term for any of these stages.  None is the honest value and it is
    not a measurement of anything.
"""

import itertools
import sys

import hlaw
import mi

sys.path.insert(0, "/home/user/Claude-Method-Works/tools")
import populate as _pop          # noqa: E402  -- the seated member, imported

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    "COMPUTED from the Madelung construction through charts3.py; the reach Z <= 108 is LW1-ground.py's table.",
    (),
)


RAW_ARITY = 8
ARITY = 7
NAMES = ("sn", "sl", "k", "q", "tn", "tl", "g")
DROPPED = "2S"
REACH_Z = 108                    # LW1-ground.py's own table


# ---------------------------------------------------------------------------

_ROWS, _IDX, _SUB = {}, {}, {}


def stage_rows(reach=REACH_Z):
    """[(Z, charge, Ne, raw 8-tuple)] -- every element, every charge stage.

    MEMOISED: 108 calls into LW1.expand per run, asked for by every function
    below and by the census 120 times over.
    """
    if reach not in _ROWS:
        _ROWS[reach] = [(Z, r["charge"], r["Ne"], r["cell"])
                        for Z in range(1, reach + 1)
                        for r in _pop.ionisation_cells(Z)]
    return _ROWS[reach]


def dropped_slot_is_constant(reach=REACH_Z):
    """(the distinct values the 2S slot takes, whether it is constant).

    A one-valued coordinate carries no information and widens every closure for
    free.  Dropping it is only legitimate if it really is constant, so that is
    measured rather than assumed.
    """
    vals = {r[3][RAW_ARITY - 1] for r in stage_rows(reach)}
    return sorted(vals, key=str), len(vals) == 1


def index(reach=REACH_Z):
    """The 98 distinct Lambda_8 transitions, on the seven determined slots."""
    if reach not in _IDX:
        _IDX[reach] = frozenset(r[3][:ARITY] for r in stage_rows(reach))
    return _IDX[reach]


def is_function_of_Ne(reach=REACH_Z):
    """True iff each electron count determines its cell -- the collapse's cause."""
    byNe = {}
    for _Z, _c, Ne, cell in stage_rows(reach):
        byNe.setdefault(Ne, set()).add(cell[:ARITY])
    return all(len(v) == 1 for v in byNe.values()), len(byNe)


def closers(X):
    X = frozenset(X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def subchart(combo, reach=REACH_Z):
    """The index projected onto a named subset of the seven coordinates."""
    key = (tuple(combo), reach)
    if key not in _SUB:
        idx = [NAMES.index(c) for c in combo]
        _SUB[key] = frozenset(tuple(c[i] for i in idx) for c in index(reach))
    return _SUB[key]


_CEN = {}


def census(reach=REACH_Z):
    """({K: charts}, {K: injective charts}, [(K, combo, cells, injective)])."""
    if reach in _CEN:
        return _CEN[reach]
    X = index(reach)
    allk, injk, rows = {}, {}, []
    for r in range(2, ARITY + 1):
        for combo in itertools.combinations(NAMES, r):
            P = subchart(combo, reach)
            k = mi.K(P)
            inj = len(P) == len(X)
            allk[k] = allk.get(k, 0) + 1
            if inj:
                injk[k] = injk.get(k, 0) + 1
            rows.append((k, combo, len(P), inj))
    _CEN[reach] = (allk, injk, rows)
    return _CEN[reach]


def new_channels(reach=REACH_Z):
    """Channels this source reaches that the element address provably cannot.

    charts3.py censuses 372 charts over the differentiating electron's address
    and finds K1, K4 and K5 unreachable there.  This asks which of those three
    the ladder reaches, and by which chart.
    """
    import charts3
    elem = set(charts3.census()["all"])
    allk, _i, rows = census(reach)
    return {k: [(c, n) for kk, c, n, _j in rows if kk == k]
            for k in sorted(set(allk) - elem)}


# ---------------------------------------------------------------------------

def report():
    X = index()
    rows = stage_rows()
    print("=" * 74)
    print("THE IONISATION LADDER -- an index over transitions, not elements")
    print("=" * 74)
    print()
    print("0. STATUS FIRST. populate.ionisation_cells is RECONSTRUCTED by its")
    print("   own docstring: chapter 7 makes a Lambda_8 cell a TRANSITION, so a")
    print("   mapping from elements had to be CHOSEN and nothing in the store")
    print("   fixes it. Every channel below is a fact about that mapping as")
    print("   much as about ions.")
    print()

    vals, const = dropped_slot_is_constant()
    fn, nNe = is_function_of_Ne()
    print("1. THE CONSTRUCTION.")
    print("   stage rows (element x charge)   %d" % len(rows))
    print("   distinct cells                  %d" % len(X))
    print("   the cell is a function of Ne    %s   (%d electron counts)"
          % (fn, nNe))
    print("   so every ladder is a suffix of ONE universal ladder, and 5,778")
    print("   is the number of (element, stage) pairs, not of transitions.")
    print("   the %s slot takes values %s -- constant: %s. DROPPED."
          % (DROPPED, vals, const))
    print("   arity %d raw, %d charted" % (RAW_ARITY, ARITY))
    print()

    print("2. IT CLOSES NOTHING.")
    cl, box = hlaw.closures(X)
    import math
    print("   %d cells, arity %d, box %d" % (len(X), ARITY,
                                             math.prod(len(b) for b in box)))
    print("   K%d -- closes %s" % (mi.K(X), ", ".join(closers(X)) or "NOTHING"))
    print("   cell on the admissible chart: %s" % (mi.cell(X),))
    print()

    allk, injk, rws = census()
    print("3. THE SUB-CHART CENSUS, over %d sub-charts of arity 2 to %d."
          % (len(rws), ARITY))
    print("   reached by ANY sub-chart   %s"
          % ", ".join("K%d" % k for k in sorted(allk)))
    print("   reached INJECTIVELY        %s"
          % ", ".join("K%d" % k for k in sorted(injk)))
    print("   never reached              %s"
          % ", ".join("K%d" % k for k in range(8) if k not in allk))
    print("   INJECTIVELY ONLY K0: %d faithful sub-charts, every one closing"
          % sum(injk.values()))
    print("   nothing. As a FAITHFUL index the ladder is flatly K0.")
    print()

    print("4. AND IT REACHES A CHANNEL THE ELEMENT ADDRESS CANNOT.")
    nc = new_channels()
    for k, charts in nc.items():
        for combo, n in charts:
            print("   K%d  (%s)  %d cells  closes %s"
                  % (k, ", ".join(combo), n,
                     ", ".join(closers(subchart(combo)))))
    print("   charts3.py proved K1, K4 and K5 unreachable from the element")
    print("   address over 372 charts. This source reaches K%s."
          % ", K".join(str(k) for k in nc))
    print("   THAT IS 'A NEW SOURCE, NOT A NEW ARRANGEMENT', DEMONSTRATED.")
    print("   charts3.py's negative result is unaltered -- it was about that")
    print("   pool, and this is a different pool.")
    print()
    print("   THE PRICE IS THE SAME AS K6's: the chart holds 7 cells against")
    print("   98, so ninety-one lose their identity. Reachable, not faithful.")
    print()

    print("5. REFUSED: that the ladder is SEATED -- it is built and measured,")
    print("   and seating is a ruling that must weigh the RECONSTRUCTED status")
    print("   first. That 5,778 is the size of anything. That 2S is absent")
    print("   because it is zero -- it is absent because nothing is banked.")
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

    print("ions selftest")
    rows, X = stage_rows(), index()

    # ---- the construction
    chk("stage rows over Z <= 108", len(rows), 5778)
    chk("distinct transitions", len(X), 98)
    # THE COLLAPSE IS STRUCTURAL, not a coincidence of this reach.
    fn, nNe = is_function_of_Ne()
    chk("the cell is a function of the ELECTRON COUNT alone", fn, True)
    chk("107 electron counts onto 98 cells -- nine collide", (nNe, len(X)),
        (107, 98))
    # THE DROPPED SLOT. Legitimate only because it really is constant.
    vals, const = dropped_slot_is_constant()
    chk("the 2S slot is None at every one of the 5,778 rows", (vals, const),
        ([None], True))
    chk("so the chart is 7 of the 8 raw coordinates", (RAW_ARITY, ARITY), (8, 7))
    chk("and every charted coordinate varies",
        all(len({c[i] for c in X}) > 1 for i in range(ARITY)), True)

    # ---- the index
    chk("it closes NOTHING", closers(X), [])
    chk("which is K0", mi.K(X), 0)
    chk("its cell on the admissible chart", mi.cell(X), (0, 18, 16))

    # ---- the census
    allk, injk, rws = census()
    chk("sub-charts of arity 2 to 7", len(rws), 120)
    chk("channels reached by ANY sub-chart", sorted(allk), [0, 2, 3, 4, 7])
    # THE FAITHFUL VERDICT IS FLAT.
    chk("reached INJECTIVELY: K0 and nothing else", sorted(injk), [0])
    chk("and 32 sub-charts are faithful", injk[0], 32)
    chk("never reached", [k for k in range(8) if k not in allk], [1, 5, 6])

    # ---- THE HEADLINE, and it is checked against charts3's negative result
    nc = new_channels()
    chk("the ladder reaches exactly one channel the element address cannot",
        sorted(nc), [4])
    chk("by exactly one chart, and it is (sl, tl)",
        [c for c, _n in nc[4]], [("sl", "tl")])
    chk("7 cells, closing information and statistics",
        (len(subchart(("sl", "tl"))), closers(subchart(("sl", "tl")))),
        (7, ["information", "statistics"]))
    # AND THE PRICE, PINNED SO IT CANNOT BE QUOTED WITHOUT IT.
    chk("BUT IT IS A COARSENING -- 91 of the 98 lose their identity",
        len(X) - len(subchart(("sl", "tl"))), 91)
    # THE NEGATIVE RESULT IT LEANS ON IS RE-READ, NOT REMEMBERED.
    import charts3
    chk("charts3 still says K1, K4, K5 are unreachable from the address",
        [k for k in range(8) if k not in charts3.census()["all"]], [1, 4, 5])
    chk("so K4 is genuinely new and K1 and K5 are still unreached anywhere",
        (4 in allk, 1 in allk, 5 in allk), (True, False, False))

    # ---- provenance is not flattened
    chk("the mapping's own status is RECONSTRUCTED",
        "RECONSTRUCTED" in _pop.ionisation_cells.__doc__, True)

    print("ions selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
