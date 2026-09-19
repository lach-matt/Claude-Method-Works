#!/usr/bin/env python3
r"""nucbands.py -- NUCLEAR EXCITED STATES IN ROTATIONAL BANDS.  DOCKET 35.

    python3 nucbands.py             the reading
    python3 nucbands.py --selftest  fixtures
    python3 nucbands.py --sweep     every coordinate subset, measured (slow)

M: "Expand your web search using navigation and retrieval methods outlined in
the corpus."  Then: "Seat and push everything to the repo."

===============================================================================
0. THE CANDIDATE DOCKET 33 DECLARED UNREACHABLE
===============================================================================

`subpop.py` section 4 named nuclear rotational bands as a candidate index and
then closed it: four searches for a level scheme returned nothing, and the file
concluded "THE STONE IS TURNED AND THERE IS NOTHING UNDER IT THIS ENVIRONMENT
CAN REACH."

THAT WAS FALSE, AND THE CORPUS HAD ALREADY SAID WHY.  `NAVIGATION.md` section 3
is a retrieval law derived from the three-body index, not a search heuristic:

    NAVIGATE BY JOIN, NEVER BY MEET.  Meet failures 12, 111, 477 ... 90,705 by
    cap; join failures 0 at every cap.  "Certainty survives upward and dies
    downward.  Brackets combine; they do not refine."

All four searches were MEETS -- ENSDF and an API, nuclear data and pypi, the
corpus and a level scheme.  Run as a join over the paper database the route
opens at once.  `nbcapture.py` is the capture that followed and carries the
totality argument; this file is the index.

===============================================================================
1. THE MEMBERS ARE LEVELS, NOT BANDS, AND THAT IS A CHOICE WITH A REASON
===============================================================================

A band is a FAMILY of levels -- the Goldstone tower itself.  A level is the
quantum object: a nuclear excited state carrying I and pi exactly as a particle
carries J and P.  The tree already indexes particles and not multiplets, and
seating both the tower and its rungs would be two vertices for one subject,
which is the over-representation the whole register exists to prevent.

    SO THE BANDS ARE MEASURED HERE AND NOT SEATED.  `band_chart()` reports
    them -- 67 cells, the same channel -- as a SUB-POPULATION of this index,
    which is exactly the object `subpop.py`'s machinery is for.

===============================================================================
2. WHAT THE INDEX REFUSES, AND ON THE CRITERION RATHER THAN FOR CONVENIENCE
===============================================================================

    27 BANDS CARRY NO I-pi COLUMN AT ALL.  The source prints their energies
    relative to an unknown bandhead (`200-Pb 1 X`, then 100.6+X, 223.9+X).
    They carry NO quantum number, so they are not members.  Refused on the
    criterion, counted, and named -- the same shape as the spin-4 mesons PDG
    could not place in a mass reach.

    93 LEVELS CARRY A SPIN BUT NO PARITY.  The source prints the spin and
    leaves the parity column empty.  An earlier draft said these sit "mostly in
    the A ~ 60 region" and that was WRONG: measured, they run 19 at A ~ 50, 11
    at 100, 12 at 110, 13 at 120, 9 at 130, 20 at 190 and 9 at 200 -- the
    largest single group is A ~ 190, not A ~ 60.  A member must carry BOTH
    coordinates, so they are refused -- and refused SEPARATELY, because "no
    parity printed" and "no spin printed" are different facts about the source
    and flattening them would lose one.

    AND SIX LEVEL ROWS CARRY NO I-pi AT ALL INSIDE A BAND THAT DOES.  A third
    refusal, and it was found by audit because these six were vanishing with NO
    COUNTER -- unlike the other two groups, which are captured and reported.
    103-Ag band 4, 132-Ba band 2, 194-Bi band 1 (twice), 197-Bi band 1 and
    144-Dy AMR band 1.  Each is the terminal row of its band and each CLOSES
    ITS OWN GAMMA ARITHMETIC against a level below it, so each is a real level
    whose spin the paper left unassigned rather than a parse artefact.
    `nbcapture.unplaced()` measures them and captures/NUCBANDS-unplaced.tsv
    carries them.

2,245 levels are captured; 2,152 carry both and are the members.

===============================================================================
3. THE CHANNEL IS K2 AND THE K2 IS THE FREE ONE.  SAY SO.
===============================================================================

On (2I, pi) the index closes in {statistics} -- channel K2.  IT WOULD BE A LIE
TO BANK THAT AS A CLOSURE.  `kdet` opens with `if k >= d: return True`, so at
arity 2 statistics closes for nothing, and this tree has measured that 105 of
105 arity-2 charts close it.  The honest reading:

    THE NUCLEAR BAND INDEX CLOSES IN NOTHING.  Its K2 is the free pass and its
    real content is K0, which is where `mesons` and `baryons` also sit.  A K0
    index is still an index -- it is a chart of quantum objects on quantum
    numbers -- but it predicts nothing, and this file does not pretend it does.

AND NO WIDER READING RESCUES IT.  MEASURED, over the supersets of (2I, pi) in
the five coordinates the capture carries:

    K2    121 cells   (2, 63, 2)    2I, pi
    K0    194 cells   (0, 64, 4)    2I, pi, dI
    K0    997 cells   (0, 85, 34)   2I, pi, Z
    K0  1,247 cells   (0, 83, 42)   2I, pi, N
    K0  1,054 cells   (0, 85, 42)   2I, pi, dI, Z
    K0  1,307 cells   (0, 80, 55)   2I, pi, dI, N
    K0  1,672 cells   (0, 61, 74)   2I, pi, Z, N

    K0  1,715 cells   (0, 59, 81)   2I, pi, dI, Z, N

Every extra coordinate moves the channel DOWN, not up: it buys cells and loses
the free pass.  ALL SEVEN SUPERSETS ARE MEASURED and every one is K0, so the
claim has no hole in it.  The last row had to wait: it timed out at 40 minutes
and was carried as UNMEASURED -- named rather than filled in from the six K0
rows above -- until a 90-minute run returned it.  `ARITY3` holds the figures
and `--sweep` re-derives them; the selftest re-measures the dI row rather than
trusting the table.

===============================================================================
4. THE TWO PAPERS ARE TWO OBJECTS, AND ONLY ONE IS CAPTURED HERE
===============================================================================

The join returned two data tables and they are NOT the same physics:

    arXiv:2303.13849   magnetic and antimagnetic rotation -- the SHEARS
                       mechanism in weakly-deformed or near-spherical nuclei,
                       where angular momentum comes from closing two blades of
                       high-j proton and neutron spins.  THIS FILE.
    arXiv:2508.05447   two-quasiparticle bands in DEFORMED odd-odd nuclei --
                       a deformed rotor's tower, which is what `subpop.py`
                       actually named.  CAPTURED AS TEXT, NOT PARSED.

The second is seated in `captures/` and is NOT indexed here.  Its Table 3
interleaves free prose into the data columns, so a parse of it would need its
own totality argument and would not share this one.  Named, not smuggled in.
"""

import collections
import csv
import os
import sys

import mi

HERE = os.path.dirname(os.path.abspath(__file__))
BANDS_TSV = os.path.join(HERE, "captures", "NUCBANDS-bands.tsv")
LEVELS_TSV = os.path.join(HERE, "captures", "NUCBANDS-levels.tsv")
UNPLACED_TSV = os.path.join(HERE, "captures", "NUCBANDS-unplaced.tsv")

SOURCE = (
    "Read from captures/NUCBANDS-levels.tsv, written by nbcapture.py from "
    "captures/arxiv-2303.13849.txt -- Teng & Ma, 'Magnetic and antimagnetic "
    "rotational bands data tables', submitted to Atomic Data and Nuclear Data "
    "Tables.  The capture reproduces the paper's own census exactly (252 MR "
    "bands in 123 nuclei, 38 AMR in 27) and its own Delta-I selection rule "
    "(213/213 AMR steps at Delta-I = 2).  Nothing is written down by hand.",
    ("research/warp-drive/captures/NUCBANDS-levels.tsv",
     "research/warp-drive/captures/NUCBANDS-bands.tsv",
     "research/warp-drive/captures/arxiv-2303.13849.txt"),
)

# The second paper: reached by the same join, a DIFFERENT physical object, and
# deliberately not indexed here.  Held as data so the distinction survives.
NOT_INDEXED = (
    ("arxiv-2508.05447.txt",
     "two-quasiparticle rotational bands in DEFORMED odd-odd nuclei, "
     "Z 67-71, N 89-97 -- 234 bands/states, of which the paper says 173 are "
     "bands and 61 are bandhead states",
     "CAPTURED IN FULL, NOT SEATED, AND THE REASON CHANGED TWICE UNDER "
     "AUDIT.  deformed.py once claimed a proof that NO parse could recover "
     "this table's entry boundaries; that conclusion is RETRACTED.  What "
     "stands is narrower and stronger: the delimiter the paper itself defines "
     "-- a blank row between entries -- is absent from this extraction, ZERO "
     "of its 71 blank lines being separators (50 page boundaries, 21 "
     "nuclide-header internals).  A sequence-with-reset rule on the band "
     "number recovers the entries anyway, and it now recovers ALL 234: the "
     "one it missed is a band-number line printed `6. `, with a trailing full "
     "stop the regex refused, and exactly one line in the table has that "
     "shape.  The capture is total against three of the paper's own numbers "
     "-- 234 entries, 173 bands, 61 bandhead states, all exact -- in 24 "
     "blocks matching the 24 nuclide sections, every block contiguous.  "
     "NOTHING IS SEATED, and the reason is no longer the capture: a capture "
     "is not an index, and seating is a ruling.  On (2I, parity) these levels "
     "give 96 cells at K2, cell (2, 49, 2) -- a cell no seated index holds, "
     "from a member set this one does not cover."),
)

# MEASURED by --sweep over the seated member set.  Every superset of (2I, pi)
# LOSES the channel: the third coordinate buys cells and costs the free pass.
ARITY3 = (
    (("2I", "par"), 2, 121, (2, 63, 2)),
    (("2I", "par", "dI"), 0, 194, (0, 64, 4)),
    (("2I", "par", "Z"), 0, 997, (0, 85, 34)),
    (("2I", "par", "N"), 0, 1247, (0, 83, 42)),
    (("2I", "par", "dI", "Z"), 0, 1054, (0, 85, 42)),
    (("2I", "par", "dI", "N"), 0, 1307, (0, 80, 55)),
    (("2I", "par", "Z", "N"), 0, 1672, (0, 61, 74)),
    (("2I", "par", "dI", "Z", "N"), 0, 1715, (0, 59, 81)),
)

# NOTHING IS UNMEASURED HERE ANY MORE, and the way that resolved is worth
# keeping.  The five-coordinate row timed out at 40 minutes and this file
# carried it as UNMEASURED rather than filling it in from the six K0 rows
# above -- with a fixture asserting it was NAMED rather than assumed.  Re-run
# on a 90-minute budget it returned K0, 1,715 cells, (0, 59, 81).  THE GUESS
# WOULD HAVE BEEN RIGHT AND WITHHOLDING IT WAS STILL CORRECT: a pattern in six
# is not a measurement of the seventh, and the only way to know which it was
# is to spend the CPU.
UNMEASURED = ()

_C = {}


def _read(path):
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader((l for l in f if not l.startswith("#")),
                                   delimiter="\t"))


def levels():
    """Every captured level, including the ones this index refuses."""
    if "l" not in _C:
        _C["l"] = _read(LEVELS_TSV)
    return _C["l"]


def bandrows():
    if "b" not in _C:
        _C["b"] = _read(BANDS_TSV)
    return _C["b"]


def members():
    """The levels that carry BOTH quantum numbers.  A member carries both."""
    return [r for r in levels() if r["2I"] and r["par"]]


def refusals():
    """(bands with no I^pi, levels with no parity, level rows with no I^pi).

    THREE groups, counted apart.  The third was found by audit: it was being
    dropped silently while the other two were reported, which is exactly the
    asymmetry this function now refuses to keep.
    """
    return (sum(1 for r in bandrows() if r["status"] == "NO-SPIN"),
            sum(1 for r in levels() if r["2I"] and not r["par"]),
            len(unplaced_rows()))


def unplaced_rows():
    """The third refusal, read from the capture rather than recomputed."""
    if "u" not in _C:
        _C["u"] = _read(UNPLACED_TSV)
    return _C["u"]


def index():
    """{(2I, parity)} -- the seated chart."""
    return frozenset((int(r["2I"]), int(r["par"])) for r in members())


def cell():
    return mi.cell(index())


def band_chart():
    """The BAND sub-population: {(bandhead 2I, parity)}, measured not seated."""
    return frozenset((int(r["head_2I"]), int(r["head_par"]))
                     for r in bandrows() if r["head_2I"] and r["head_par"])


def statistics_is_free():
    """(arity, does kdet close for nothing at this arity?).

    `kdet` opens `if k >= d: return True`, so at arity 2 the statistics closer
    is vacuous.  The channel is measured honestly and then SAID to be free.
    """
    import decomposable as D
    X = index()
    box = [sorted({t[i] for t in X}) for i in range(2)]
    return (2, D.kdet(X, box, 2))


def resolution():
    """[(axis, distinct, cells, ratio)] -- >= 0.9 would make it a row label."""
    X = index()
    return [(nm, len({t[i] for t in X}), len(X), len({t[i] for t in X}) / len(X))
            for i, nm in enumerate(("2I", "par"))]


def by_table():
    """{MR/AMR: (levels, cells, K)} -- the two mechanisms charted apart."""
    out = {}
    for tag in ("MR", "AMR"):
        S = frozenset((int(r["2I"]), int(r["par"]))
                      for r in members() if r["table"] == tag)
        out[tag] = (sum(1 for r in members() if r["table"] == tag),
                    len(S), mi.K(S))
    return out


def alternatives():
    """[(K, cells, cell, coords)] over every subset of the five coordinates."""
    import itertools
    COLS = {
        "2I":  lambda r: int(r["2I"]),
        "par": lambda r: int(r["par"]),
        "dI":  lambda r: 1 if r["table"] == "MR" else 2,
        "Z":   lambda r: int(r["Z"]),
        "N":   lambda r: int(r["A"]) - int(r["Z"]),
    }
    M = members()
    out = []
    for k in range(2, len(COLS) + 1):
        for c in itertools.combinations(COLS, k):
            X = frozenset(tuple(COLS[n](r) for n in c) for r in M)
            out.append((mi.K(X), len(X), mi.cell(X), c))
    return sorted(out, key=lambda t: (-t[0], t[1]))


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("2,245 levels captured, 2,152 carrying BOTH quantum numbers",
        (len(levels()), len(members())), (2245, 2152))
    chk("and the refusals are THREE different facts, counted apart",
        refusals(), (27, 93, 6))
    chk("the no-parity levels are NOT mostly A ~ 60 -- that claim was wrong",
        sorted(collections.Counter(
            int(r["A"]) // 10 * 10 for r in levels()
            if r["2I"] and not r["par"]).items()),
        [(50, 19), (100, 11), (110, 12), (120, 13), (130, 9), (190, 20), (200, 9)])
    chk("290 bands captured -- the paper's 252 MR plus its 38 AMR",
        (len(bandrows()),
         sum(1 for r in bandrows() if r["table"] == "MR"),
         sum(1 for r in bandrows() if r["table"] == "AMR")),
        (290, 252, 38))

    X = index()
    chk("the index is 121 cells on (2I, parity)", len(X), 121)
    chk("and its cell is (2, 63, 2) -- channel K2", cell(), (2, 63, 2))

    chk("BUT THE K2 IS THE FREE ONE: statistics is vacuous at arity 2",
        statistics_is_free(), (2, True))

    r = resolution()
    chk("no axis resolves the rows -- neither is a label",
        [round(x[3], 3) for x in r], [0.521, 0.017])
    chk("and the widest axis is well under the 0.9 label threshold",
        max(x[3] for x in r) < 0.9, True)

    b = band_chart()
    chk("the BAND sub-population is 67 cells and NOT seated", len(b), 67)
    chk("it sits in the same channel, which is why seating it too would "
        "double-count", mi.K(b), 2)

    t = by_table()
    chk("MR and AMR charted apart stay in the same channel",
        (t["MR"][2], t["AMR"][2]), (2, 2))
    # 1,907 + 238 = 2,145.  The AMR count is NOT the 213 that nbcapture
    # reports: that is the number of consecutive STEPS between levels, which
    # is levels minus one per band.  Two different quantities, and this
    # fixture had the wrong one first.
    chk("and AMR is much the smaller of the two",
        (t["MR"][0], t["AMR"][0], t["MR"][0] + t["AMR"][0]),
        (1914, 238, 2152))

    chk("the second paper is named as NOT indexed, not quietly dropped",
        [n for n, _w, _y in NOT_INDEXED], ["arxiv-2508.05447.txt"])
    # The attempt record lives in deformed.py, which owns that docket; this
    # file asserts it is THERE rather than keeping a second copy that can
    # drift from it.
    import deformed
    chk("all four failed parse attempts are recorded, with their numbers",
        [n for _w, n, _y in deformed.ATTEMPTS], [154, 176, 160, 195])
    chk("and none of them reached the stated census",
        [n for _w, n, _y in deformed.ATTEMPTS if n == 234], [])
    chk("and the entry points at deformed.py, where the RETRACTION lives",
        [n for n, _w, why in NOT_INDEXED
         if "deformed.py" in why and "RETRACTED" in why],
        ["arxiv-2508.05447.txt"])
    # Re-run deformed.py's own measurement here, so this file cannot go on
    # citing a state of that docket which has stopped holding.
    import deformed
    absent, got, _why = deformed.verdict()
    chk("the blank-row delimiter is still absent, and all 234 entries are "
        "now recoverable", (absent, got), (True, 234))
    chk("and that docket's capture is total against the paper's own census",
        deformed.census2(), (234, 173, 61))

    # Re-MEASURE the cheapest arity-3 row rather than trusting the table.
    # The other two are 997 and 1,247 cells and belong in --sweep.
    import itertools
    M = members()
    X3 = frozenset((int(r["2I"]), int(r["par"]),
                    1 if r["table"] == "MR" else 2) for r in M)
    chk("adding dI LOSES the channel -- K2 falls to K0, as ARITY3 records",
        (mi.K(X3), len(X3), mi.cell(X3)), (0, 194, (0, 64, 4)))
    chk("and ARITY3 says the same", ARITY3[1][1:], (0, 194, (0, 64, 4)))
    chk("ALL SEVEN supersets measured, and every one loses the channel",
        (len(ARITY3) - 1, sorted({k for _c, k, _n, _cell in ARITY3[1:]})),
        (7, [0]))
    chk("and nothing is left unmeasured", list(UNMEASURED), [])
    chk("the five-coordinate row is the one that had to wait for CPU",
        ARITY3[-1], (("2I", "par", "dI", "Z", "N"), 0, 1715, (0, 59, 81)))

    for p in (BANDS_TSV, LEVELS_TSV):
        chk("%s is in the tree" % os.path.basename(p), os.path.exists(p), True)

    print("nucbands selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("NUCLEAR EXCITED STATES IN ROTATIONAL BANDS -- DOCKET 35")
    print("=" * 79)
    print()
    print("0. THE CANDIDATE subpop.py DECLARED UNREACHABLE, REACHED BY JOIN.")
    print("   Four searches failed and all four were MEETS.  NAVIGATION.md")
    print("   section 3: navigate by JOIN, never by meet -- meet failures run")
    print("   12 to 90,705 by cap, join failures are 0 at every cap.")
    print()
    print("1. THE MEMBERS ARE LEVELS.")
    nb, npar, nun = refusals()
    print("   levels captured                 %d" % len(levels()))
    print("   refused, no parity printed      %d" % npar)
    print("   refused, no I^pi on the row     %d  (the third refusal)" % nun)
    print("   MEMBERS (2I and parity both)    %d" % len(members()))
    print("   bands captured                  %d  (252 MR + 38 AMR)"
          % len(bandrows()))
    print("   refused, no I^pi column at all  %d bands" % nb)
    print("   Both refusals are on the CRITERION -- a member carries quantum")
    print("   numbers -- and they are counted apart because they are")
    print("   different facts about the source.")
    print()
    print("2. THE CHART.")
    print("   coordinates   (2I, parity)")
    print("   cells         %d" % len(index()))
    print("   cell          %s" % (cell(),))
    for nm, d, n, ratio in resolution():
        print("   resolution    %-4s %3d / %3d = %.3f   %s"
              % (nm, d, n, ratio, "LABEL" if ratio >= 0.9 else "measurement"))
    print()
    print("3. AND THE K2 IS THE FREE ONE.")
    ar, free = statistics_is_free()
    print("   arity %d, and kdet returns %s for nothing at that arity." % (ar, free))
    print("   THE INDEX CLOSES IN NOTHING.  Its real content is K0, where")
    print("   mesons and baryons also sit.  Recorded, not dressed up.")
    print()
    print("4. THE TWO MECHANISMS, CHARTED APART.")
    t = by_table()
    print("     %-5s %-9s %-7s %s" % ("", "levels", "cells", "channel"))
    for tag in ("MR", "AMR"):
        n, c, k = t[tag]
        print("     %-5s %-9d %-7d K%d" % (tag, n, c, k))
    print()
    print("5. THE BAND SUB-POPULATION -- MEASURED, NOT SEATED.")
    b = band_chart()
    print("   %d cells, channel K%d.  A band is a FAMILY of levels; seating"
          % (len(b), mi.K(b)))
    print("   both the tower and its rungs would be two vertices for one")
    print("   subject, which is the over-representation the register prevents.")
    print()
    print("6. EVERY THIRD COORDINATE LOSES THE CHANNEL.  MEASURED.")
    print("     %-4s %-8s %-14s %s" % ("K", "cells", "cell", "coordinates"))
    for cols, k, n, c in ARITY3:
        print("     K%-3d %-8d %-14s %s" % (k, n, str(c), ", ".join(cols)))
    print()
    print("7. THE OTHER PAPER, NAMED AND NOT SMUGGLED IN.")
    for n, what, why in NOT_INDEXED:
        print("   %s" % n)
        print("     %s" % what)
        print("     NOT PARSED: %s" % why)
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--sweep" in sys.argv:
        print("%-4s %-7s %-14s %s" % ("K", "cells", "cell", "coordinates"))
        for k, n, c, cols in alternatives():
            print("K%-3d %-7d %-14s %s" % (k, n, str(c), ", ".join(cols)))
        sys.exit(0)
    sys.exit(report())
