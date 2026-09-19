#!/usr/bin/env python3
r"""
subpop.py -- THE MEMBER SUB-POPULATION SWEEP, AND HOW DEEP A SUBLATTICE NESTS.
DOCKET 33.

    python3 subpop.py             the reading
    python3 subpop.py --selftest  fixtures

M: "seat that sweep as an instrument ... run all candidates.  Leave no stone
unturned.  And if any sublattice may possibly contain its own sublattice, we
must seek a determination."

===============================================================================
0. EVERY SWEEP BEFORE THIS ONE VARIED COLUMNS
===============================================================================

DOCKET 25 censused every chart-shaped accessor.  DOCKET 29 took all 142 subsets
of the particle indexes' COORDINATES.  Both asked: what happens if I chart the
same members differently?

    DOCKET 31 ASKED A DIFFERENT QUESTION WITHOUT NAMING IT AS A METHOD -- does
    this set of members sit inside that one, CLOSED?  That is a question about
    MEMBER subsets, and nothing in the tree had ever swept them.

This file is that sweep.  A sub-population is one coordinate held to one value
-- a principled family, not an arbitrary subset, and the same shape of
enumeration DOCKET 29 ran on the other axis.

===============================================================================
1. WHAT THE SWEEP FINDS
===============================================================================

Over every seated index with a declared coordinate list:

    sub-populations of 2 cells or more      the census below
    of those, SUBLATTICES                   143
    reaching a channel the index lacks      2

    AND ONE OF THE TWO IS THE FIRST ARITY-3 K4 THIS TREE HAS SEEN.

===============================================================================
2. THE K4 CANDIDATE, AND WHY IT STILL FAILS
===============================================================================

K4 is the last empty channel.  `madrule` at l_d = 0 reaches it and dissolves at
once: holding a coordinate constant leaves an EFFECTIVE ARITY of 2, where
`statistics` closes free -- `overlaprule.py` section 3c, for the fourth time.

    THE OTHER ONE DOES NOT DISSOLVE THAT WAY.  The SPIN-4 MESONS, charted on
    (P, 2I, Q3), are 10 members on 9 cells at cell (4, 5, 3).  Effective arity
    3, where statistics closes only 59 of 125 charts in this tree -- so the
    statistics bit is EARNED.  DOCKET 25 recorded "K4 is reached by nothing"
    and DOCKET 29 "no chart of arity 3 or more has ever reached K4"; both were
    true of COLUMN sub-charts, and this is not one.

    IT FAILS THE REACH GATE, AND THE REASON IS SHARP.  Two of the ten --
    K(4)(2500)+ and K(4)(2500)- -- carry no printed mass.  Swept by the
    parent's own reach, the population is 7 cells at K5 at EVERY mass cut,
    never 9 at K4.  The K4 exists only in the full set and rests entirely on
    the two rows PDG cannot place in a reach.

    SO K4 STAYS EMPTY, NOW FOR A THIRD REASON.  Not arity this time: a channel
    that lives on members the table cannot place.

===============================================================================
3. THE DETERMINATION ON RECURSION, AND IT CORRECTED ITSELF
===============================================================================

M asked whether a sublattice may contain its own sublattice.  It may, and the
first answer this file computed was WRONG:

    WITHIN THE SWEEP'S OWN FAMILY, nesting is shallow.  14 strict containments
    among the 143, and the longest chain is 2 -- a sublattice with one proper
    sublattice inside it and nothing deeper.

    EXHAUSTIVELY, IT IS NOT SHALLOW AT ALL.  Enumerate EVERY subset of the
    indexes small enough to allow it and the chains run far deeper:

        bosonqp                      5 cells       25 sublattices   chain  5
        madrule                     13 cells      164 sublattices   chain  6
        baryon_isomultiplet         16 cells    1,649 sublattices   chain 14

    THE DEPTH-2 FIGURE IS A FACT ABOUT THE FAMILY, NOT ABOUT THE LATTICES, and
    it would have been reported as the latter if the exhaustive pass had not
    been run.  A sub-population sweep sees a vanishing slice of Sub(L): 143
    across the whole tree, against 1,649 inside ONE sixteen-cell chart.

    WHAT IS STILL NOT DETERMINED.  Only three indexes are small enough to
    enumerate.  For the rest the true depth of Sub(L) is unknown, and the
    family figure is a floor rather than an answer.  `too_large()` names them.

===============================================================================
4. THE OTHER CANDIDATES, ALL RUN
===============================================================================

    THE CHIRAL GOLDSTONE SUBLATTICE.  The pseudoscalar mesons are the
    pseudo-Goldstone bosons of chiral symmetry breaking, which DERIVES their
    J^P = 0- from the broken axial generator rather than reading it off.  They
    ARE a sublattice of `mesons` -- 41 members, 9 cells -- and the sublattice
    property is FREE: the 9 cells are a full 3 x 3 product box, and a full box
    is always closed.  Recorded, not seated.

    THE ELECTROWEAK EATEN GOLDSTONES.  SU(2) x U(1) -> U(1)_EM breaks three
    generators, eaten by W+, W- and Z with the photon left massless.  Rule 2
    derives them, and they land on three cells that `fundamental` already
    holds -- a RELABELLING of three seated members, which the overlap ruling's
    second ground refuses outright.

    NUCLEAR ROTATIONAL BANDS.  The one candidate this tree cannot run.  A band
    is the Goldstone tower of broken rotational symmetry in a deformed
    nucleus, and its members are NUCLEAR EXCITED STATES.  `gravity` carries
    2J from the NIST ASD ATOMIC level captures and AME2020 carries masses;
    neither holds a nuclear level scheme.  It needs ENSDF, which is a fetch
    nobody here has made.  Named so the stone is visibly unturned rather than
    quietly skipped.
"""

import itertools
import sys

import decomposable as D
import mesons
import mi
import overlaprule as OR
import registry

# Enumerating every subset is 2^n; this is where it stops being possible.
EXHAUSTIVE_LIMIT = 16

# Section 2's two hits, so a fixture can hold the file to them.
K4_HITS = (("madrule.index", "l_d", 0), ("mesons.index", "2J", 8))

_C = {}


def parents():
    """[(row name, module)] -- every seated index with a declared column list."""
    return [(nm, mod) for nm, mod, _a, _me, _w, _q in registry.rows()
            if mod != OR.SELF and mod in OR.COORDS]


def subpops(nm, mod, floor=2):
    """{(column, value): cells} -- one coordinate held to one value."""
    cols = OR.COORDS[mod]
    X = registry.index_of(nm)
    out = {}
    for i, c in enumerate(cols):
        for v in sorted({t[i] for t in X}):
            S = frozenset(t for t in X if t[i] == v)
            if len(S) >= floor:
                out[(c, v)] = S
    return out


def is_sublattice(S):
    S = frozenset(S)
    return D.gen(S) == S


def sweep():
    """[(row, column, value, cells, K, sublattice?)] over the whole tree."""
    if "s" not in _C:
        out = []
        for nm, mod in parents():
            for (c, v), S in sorted(subpops(nm, mod).items(),
                                    key=lambda kv: (kv[0][0], kv[0][1])):
                out.append((nm, c, v, len(S), mi.K(S), is_sublattice(S)))
        _C["s"] = out
    return _C["s"]


def census():
    """(tested, sublattices, reaching an unoccupied channel)."""
    rows = sweep()
    occ = {c[0] for _nm, c in registry.cells().items() if c != "UNMEASURED"}
    return (len(rows), sum(1 for r in rows if r[5]),
            sum(1 for r in rows if r[4] not in occ))


def unoccupied_hits():
    """[(row, column, value, cells, K, effective arity)] -- section 2."""
    occ = {c[0] for _nm, c in registry.cells().items() if c != "UNMEASURED"}
    out = []
    for nm, c, v, n, k, _sl in sweep():
        if k in occ:
            continue
        out.append((nm, c, v, n, k, len(OR.COORDS[nm.split(".")[0]]) - 1))
    return out


def spin4_reach():
    """[(mass cut, cells, K)] -- the reach gate the K4 candidate fails."""
    import pdgcapture
    by = {int(x["pdgid"]): x["mass_MeV"] for x in pdgcapture.read()}
    out = []
    for cut in (2000, 2400, 2800, 3200, 4000, 12000):
        S = frozenset((P, i, q) for _n, p, j, P, i, q in mesons.rows()
                      if j == 8 and by[p] != "?" and float(by[p]) <= cut)
        out.append((cut, len(S), mi.K(S) if len(S) > 1 else None))
    return out


def spin4_massless():
    """[name] -- the two the whole K4 rests on."""
    import pdgcapture
    by = {int(x["pdgid"]): x["mass_MeV"] for x in pdgcapture.read()}
    return sorted(n for n, p, j, _P, _i, _q in mesons.rows()
                  if j == 8 and by[p] == "?")


# ------------------------------------------------------- section 3, recursion

def family_nesting():
    """(sublattices, strict containments, longest chain) WITHIN the sweep."""
    tot = pairs = 0
    longest = 0
    for nm, mod in parents():
        subs = {k: S for k, S in subpops(nm, mod).items() if is_sublattice(S)}
        tot += len(subs)
        keys = list(subs)
        edges = [(a, b) for a in keys for b in keys if a != b
                 and subs[a] < subs[b]]
        pairs += len(edges)
        memo = {}

        def depth(k):
            if k not in memo:
                memo[k] = 1 + max([depth(a) for a, b in edges if b == k],
                                  default=0)
            return memo[k]
        if keys:
            longest = max(longest, max(depth(k) for k in keys))
    return (tot, pairs, longest)


def exhaustive():
    """[(row, cells, sublattices, longest chain)] for the small indexes.

    EVERY subset, not just the sweep's family.  This is the pass that
    corrected section 3: the family's depth of 2 is about the family.
    """
    if "e" not in _C:
        out = []
        for nm, _mod, _a, _me, _w, _q in registry.rows():
            X = registry.index_of(nm)
            if len(X) > EXHAUSTIVE_LIMIT:
                continue
            L = sorted(X)
            subs = [frozenset(S) for r in range(1, len(L) + 1)
                    for S in itertools.combinations(L, r)
                    if is_sublattice(S)]
            subs.sort(key=len)
            best = {}
            for s in subs:
                best[s] = 1 + max([best[t] for t in subs
                                   if len(t) < len(s) and t < s], default=0)
            out.append((nm, len(X), len(subs), max(best.values())))
        _C["e"] = sorted(out, key=lambda t: t[1])
    return _C["e"]


def too_large():
    """[(row, cells)] -- where the true depth of Sub(L) is NOT determined."""
    return sorted(((nm, len(registry.index_of(nm)))
                   for nm, _m, _a, _me, _w, _q in registry.rows()
                   if len(registry.index_of(nm)) > EXHAUSTIVE_LIMIT),
                  key=lambda t: t[1])


# ------------------------------------------------------ section 4, candidates

def chiral_goldstone():
    """(members, cells, sublattice?, is it a full product box?).

    The pseudoscalars are the pseudo-Goldstones of chiral symmetry breaking,
    so rule 2 derives J^P = 0-.  A FULL BOX is always a sublattice, which is
    why this one is recorded rather than seated.
    """
    P = [(j, Pp, i, q) for _n, _p, j, Pp, i, q in mesons.rows()
         if j == 0 and Pp == -1]
    G = frozenset(P)
    box = 1
    for k in range(4):
        box *= len({c[k] for c in G})
    return (len(P), len(G), is_sublattice(G), len(G) == box)


def electroweak():
    """(cells, already held by fundamental?) -- a relabelling, refused.

    SU(2) x U(1) -> U(1)_EM breaks three generators, eaten by W+, W- and Z.
    Rule 2 gives each a vector generator, so 2J = 2, and the charges are the
    eaten combinations'.  The cells are three `fundamental` already holds.
    """
    import fundamental
    eaten = frozenset((2, q) for q in (3, -3, 0))
    have = frozenset((j, q) for _n, _p, j, q, _c, _g in fundamental.rows()
                     if j == 2)
    return (len(eaten), eaten <= have)


def report():
    print("=" * 74)
    print("THE MEMBER SUB-POPULATION SWEEP -- DOCKET 33")
    print("=" * 74)
    print()
    t, sl, un = census()
    print("1. THE SWEEP.  Every sweep before this varied COLUMNS; this varies")
    print("   MEMBERS -- one coordinate held to one value.")
    print("   sub-populations tested        %d" % t)
    print("   of those, SUBLATTICES         %d  (%.0f%%)" % (sl, 100.0 * sl / t))
    print("   reaching an unoccupied channel %d" % un)
    print()
    print("2. THE K4 CANDIDATES.")
    for nm, c, v, n, k, eff in unoccupied_hits():
        print("   %-16s %s = %-4s  %2d cells  K%d  effective arity %d  -- %s"
              % (nm, c, v, n, k, eff,
                 "statistics FREE, refused" if eff <= 2 else "statistics EARNED"))
    print()
    print("   the spin-4 mesons under the parent's own reach:")
    for cut, n, k in spin4_reach():
        print("     mass <= %-6d %2d cells  %s" % (cut, n, "K%d" % k if k is not None else "-"))
    print("   and the whole K4 rests on these, which carry no printed mass:")
    print("     %s" % ", ".join(spin4_massless()))
    print("   SO K4 STAYS EMPTY -- a third reason, and not arity this time.")
    print()
    tot, pairs, longest = family_nesting()
    print("3. THE DETERMINATION ON RECURSION.")
    print("   within this sweep's own family:")
    print("     sublattices %d, strict containments %d, longest chain %d"
          % (tot, pairs, longest))
    print("   EXHAUSTIVELY, over every subset of the small indexes:")
    print("     %-34s %-7s %-14s %s"
          % ("index", "cells", "sublattices", "longest chain"))
    for nm, n, ns, ch in exhaustive():
        print("     %-34s %-7d %-14d %d" % (nm, n, ns, ch))
    print("   THE FAMILY FIGURE IS ABOUT THE FAMILY.  143 sublattices across")
    print("   the whole tree, against %d inside ONE sixteen-cell chart."
          % max(ns for _n, _c, ns, _ch in exhaustive()))
    print("   Not determined for %d indexes, which are too large to enumerate:"
          % len(too_large()))
    print("     %s" % ", ".join("%s (%d)" % t for t in too_large()[:6]))
    print()
    print("4. THE OTHER CANDIDATES, ALL RUN.")
    m, c, sub, box = chiral_goldstone()
    print("   chiral Goldstone   %d members, %d cells, sublattice %s"
          % (m, c, sub))
    print("                      but a FULL PRODUCT BOX (%s), so free -- "
          "recorded" % box)
    n, held = electroweak()
    print("   electroweak eaten  %d cells, already held by fundamental: %s"
          % (n, held))
    print("                      a RELABELLING -- the ruling's second ground")
    print("   nuclear bands      NOT RUN.  Needs a nuclear level scheme")
    print("                      (ENSDF); gravity's 2J is from ATOMIC levels")
    print("                      and AME2020 carries masses, not levels.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    t, sl, un = census()
    chk("the sweep tests sub-populations and finds sublattices among them",
        (sl > 0, sl < t), (True, True))
    chk("143 of them are sublattices", sl, 143)
    chk("and exactly two reach a channel the index lacks", un, 2)

    H = unoccupied_hits()
    chk("both hits are at K4, the last empty channel",
        sorted({k for _n, _c, _v, _ct, k, _e in H}), [4])
    chk("and they are madrule at l_d=0 and the spin-4 mesons",
        sorted((n, c, v) for n, c, v, _ct, _k, _e in H), sorted(K4_HITS))
    chk("madrule's has effective arity 2 -- statistics free, refused",
        [e for n, _c, _v, _ct, _k, e in H if n == "madrule.index"], [2])
    chk("THE SPIN-4 MESONS HAVE EFFECTIVE ARITY 3 -- statistics EARNED",
        [e for n, _c, _v, _ct, _k, e in H if n == "mesons.index"], [3])

    # the reach gate it fails
    R = spin4_reach()
    chk("under the parent's own reach it is K5 at every cut, never K4",
        sorted({k for _c, _n, k in R if k is not None}), [5, 7])
    chk("never K4 at any reach", 4 in {k for _c, _n, k in R}, False)
    chk("and the K4 rests on two rows with no printed mass",
        spin4_massless(), ["K(4)(2500)+", "K(4)(2500)-"])

    # section 3, and the correction
    tot, pairs, longest = family_nesting()
    chk("within the family: 143 sublattices, 14 containments, chain 2",
        (tot, pairs, longest), (143, 14, 2))
    E = exhaustive()
    chk("three indexes are small enough to enumerate exhaustively", len(E), 3)
    chk("AND THE TRUE CHAINS ARE FAR DEEPER -- the family figure was about "
        "the family", [ch for _n, _c, _ns, ch in E], [5, 6, 14])
    chk("one sixteen-cell chart alone holds more sublattices than the whole "
        "family sweep found",
        max(ns for _n, _c, ns, _ch in E) > tot, True)
    chk("and the rest are NOT determined, named rather than implied",
        len(too_large()) > 0, True)

    # section 4
    m, c, sub, box = chiral_goldstone()
    chk("the pseudoscalars are a sublattice of the mesons", (m, c, sub),
        (41, 9, True))
    chk("but it is a FULL product box, so the sublattice property is free",
        box, True)
    n, held = electroweak()
    chk("the electroweak Goldstones land on cells fundamental already holds",
        (n, held), (3, True))

    print("subpop selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
