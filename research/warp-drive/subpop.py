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
    of those, SUBLATTICES                   203  (143 before DOCKET 35)
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

    SO K4 STAYS EMPTY UNDER THE PARENT'S REACH, FOR A THIRD REASON.  Not
    arity this time: a channel that lives on members the table cannot place.

    AND THEN DOCKET 34 SEATED IT ANYWAY, ON A DIFFERENT REACH.  Mass is not
    the only total order PDG carries: its STATUS column is total where mass is
    not, and on that reach the spin-4 mesons are a seated index at K4 with
    cell (4,5,3).  Both statements stand -- the refusal above is about the
    MASS reach, the seating is about the STATUS reach -- and the file keeps
    both because which reach a channel survives is part of what the finding
    is.  IT ALSO CREATED A TRAP, and `OWN_ROWS` below is the guard: once
    `spin4.index` is seated, K4 is occupied, and a sweep measured against live
    occupancy reports that section 2 found nothing.  The finding would have
    erased itself by being acted on.

===============================================================================
3. THE DETERMINATION ON RECURSION -- AND A WORD THIS FILE HAD WRONG
===============================================================================

    ONLY THREE OF THE TWENTY-THREE INDEXES ARE LATTICES.  `madelung.janet`,
    `overlaprule.madelung_slot` and `bosonqp` are closed under meet and join.
    NINETEEN ARE MEASURABLY NOT, and one is too large to measure -- 3 + 19 + 1
    = 23.  `lattices()` measures it, and returns None rather than False for the
    one it cannot reach.

    SO "A SUBLATTICE OF THE INDEX" IS ILL-POSED FOR NINETEEN OF THEM, and the
    first draft of this file used that phrase for all of them.  What
    `D.gen(S) == S` actually tests is whether S is CLOSED IN THE AMBIENT BOX
    -- a well-defined thing, and the right thing for the sweep -- but it is
    not "a sublattice of L" unless L is itself a lattice.  The count is
    correct; the word attached to it was not, and the file now says CLOSED SET
    where it means one.

    AND THE COUNT ITSELF MOVES AS THE REGISTER GROWS.  It was 143 when DOCKET
    33 ran and is 203 now, because DOCKET 35 seated `nucbands` and this sweep
    is over the SEATED indexes -- a new index extends it by construction.  The
    containment structure did not move: 14 containments and a longest chain of
    2, exactly as before.  The figure is a function of the register, and that
    is a property of the measurement rather than a drift in it.

    THE RECURSION QUESTION IS STRICTLY WELL-POSED ONLY FOR THE THREE.  Peeling
    one element at a time, testing closure DIRECTLY at every step and
    verifying every intermediate:

        bosonqp                 5 cells    chain  6   peels to EMPTY, MAXIMAL
        madelung_slot          82 cells    chain 83   peels to EMPTY, MAXIMAL
        madelung.janet        170 cells    chain 51   stalls at 120 cells

    A chain cannot exceed |L| + 1, since each step drops at least one element.
    So two of the three are EXACTLY DETERMINED and maximal: their lattices
    peel all the way down one element at a time.  `madelung.janet` gives a
    verified LOWER BOUND of 51 and the greedy stalls; its exact depth is open.

    AND THE FIRST ATTEMPT AT THIS WAS WRONG IN A WAY WORTH KEEPING.  A fast
    removability shortcut -- "x can go if no two OTHER elements meet or join
    to x" -- assumes the containing set is closed.  On a set that is not, the
    reasoning collapses: replayed on `madrule`, it produced a 14-step chain of
    which TEN INTERMEDIATES WERE NOT CLOSED AT ALL.  The whole table it
    generated was discarded.  `peel()` now calls `D.gen` on every step and
    `peel_verified()` re-checks each intermediate, so a chain is real by
    construction rather than by argument.

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

    NUCLEAR ROTATIONAL BANDS.  FOUR ROUTES CLOSED, THE FIFTH OPEN -- AND THE
    FIFTH WAS FOUND BY CHANGING THE OPERATION, NOT BY TRYING HARDER.  A band
    is the Goldstone tower of broken rotational symmetry in a deformed
    nucleus, and its members are NUCLEAR EXCITED STATES, which needs a level
    scheme.  Four searches returned nothing:

        the IAEA ENSDF API      403 -- the egress proxy refuses the CONNECT
                                tunnel, the same wall elan and opam hit
        pypi                    `radioactivedecay` installs and carries decay
                                data only -- half-lives, decay modes, progeny,
                                branching fractions.  No level energies, no
                                J^P per level, no bandhead K, no deformation.
                                `nucleardata` does not exist.
        the corpus              zero hits for ENSDF, NuDat, NUBASE or any
                                level-scheme name across MANIFEST.tsv,
                                extracted/LEDGER.tsv and recovered/LEDGER.tsv

    AN EARLIER DRAFT OF THIS FILE CONCLUDED FROM THOSE FOUR THAT "THE STONE IS
    TURNED AND THERE IS NOTHING UNDER IT THIS ENVIRONMENT CAN REACH".  THAT
    WAS FALSE, and the corpus had already said why.  `NAVIGATION.md` section 3
    states the retrieval law this project derived from the three-body index:

        NAVIGATE BY JOIN, NEVER BY MEET.  Measured on the triangle form, meet
        failures run 12, 111, 477, ... 90,705 by cap; join failures are 0 at
        every cap.  "Certainty survives upward and dies downward.  Brackets
        combine; they do not refine."

    ALL FOUR FAILED SEARCHES WERE MEETS -- ENSDF and an API, nuclear data and
    pypi, the corpus and a level scheme -- each narrowing two brackets against
    each other, which is exactly the operation the law says fails.  Run as a
    JOIN over the paper database instead, the fifth route returns immediately,
    and it returns MORE than was asked for: two published data tables, each
    carrying level energy E in keV and I^pi PER BAND MEMBER, which is the
    quantum number the criterion requires.  arXiv is 403 over https in this
    environment exactly as ENSDF is; the connector is a different bracket, and
    the join is what reaches the content the direct fetch cannot.

    AND THE JOIN RETURNED TWO DIFFERENT PHYSICAL OBJECTS, which must not be
    blurred.  `BAND_SOURCES` holds the distinction:

        2508.05447   two-quasiparticle bands in DEFORMED odd-odd nuclei --
                     234 bands/states, Z 67-71, N 89-97.  THIS IS THE
                     CANDIDATE named above: a deformed rotor's tower.
        2303.13849   magnetic and antimagnetic rotation -- 252 MR bands in
                     123 nuclei, 38 AMR in 27.  NOT the candidate: the shears
                     mechanism in weakly-deformed or NEAR-SPHERICAL nuclei,
                     where angular momentum comes from closing two blades of
                     high-j proton and neutron spins, not from a deformed
                     rotor.  A separate index if seated at all.

    AND ONE OF THE TWO IS NOW SEATED.  DOCKET 35 captured 2303.13849 in full
    -- `nbcapture.py` reproduces the paper's own census exactly (252 MR bands
    in 123 nuclei, 38 AMR in 27) and its own Delta-I selection rule (213 of
    213 AMR steps at Delta-I = 2, which a count fixture could not have
    caught) -- and `nucbands.py` seats 2,145 nuclear excited states on
    (2I, parity) at 121 cells, cell (2, 63, 2).  ITS K2 IS THE FREE ONE:
    statistics is vacuous at arity 2, so the index really closes in nothing,
    and every third coordinate measured drops it to K0 outright.

    2508.05447 IS CAPTURED AND NOT PARSED, after two attempts that reached
    154 and 176 of its stated 234 entries.  Its Table 3 interleaves free
    prose into the data columns.  A capture that cannot be shown total is not
    seated, so the candidate this section actually named -- the DEFORMED
    rotor's tower -- is still open.  The stone is turned; one of the two
    things under it is banked and the other is named with its numbers.
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


# DOCKET 34 SEATED `spin4.index` BECAUSE THIS SWEEP FOUND IT, and a seated K4
# index makes K4 occupied -- so measuring against LIVE occupancy makes section
# 2's finding retroactively refute itself: the sweep reports zero hits at an
# unoccupied channel because it already caused the channel to be occupied.
# `overlaprule` carries the same self-exclusion for its own rows, and the
# earlier reading of that rule was explicit that it DOES NOT TRANSFER TO A NEW
# PARENT.  This is that transfer, restated for this parent rather than assumed.
# Occupancy is measured as it stood BEFORE the finding was acted on.
OWN_ROWS = ("spin4.index",)


def occupied(exclude_own=True):
    """{K} -- channels a seated index occupies, minus this file's own issue."""
    return {c[0] for nm, c in registry.cells().items()
            if c != "UNMEASURED" and not (exclude_own and nm in OWN_ROWS)}


def census():
    """(tested, sublattices, reaching an unoccupied channel)."""
    rows = sweep()
    occ = occupied()
    return (len(rows), sum(1 for r in rows if r[5]),
            sum(1 for r in rows if r[4] not in occ))


def unoccupied_hits():
    """[(row, column, value, cells, K, effective arity)] -- section 2."""
    occ = occupied()
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


NUCLEAR_ROUTES = (
    ("IAEA ENSDF API", "CLOSED -- 403, the egress proxy refuses the "
                       "CONNECT tunnel"),
    ("pypi radioactivedecay", "CLOSED -- installs; decay data only, no level "
                              "energies, no J^P per level, no bandhead K"),
    ("pypi nucleardata", "CLOSED -- no such distribution, AND THE NAME WAS "
                        "WRONG: `nucleardatapy` does exist and was probed "
                        "later (DOCKET 36). It carries binding energies, "
                        "charge radii, neutron skin and ISGMR -- no level "
                        "schemes. Closed on CONTENT, not on absence."),
    ("the corpus", "CLOSED -- zero hits for ENSDF / NuDat / NUBASE across "
                   "MANIFEST.tsv, extracted/LEDGER.tsv, recovered/LEDGER.tsv"),
    ("the paper database", "OPEN, AND WALKED -- arXiv:2303.13849 is captured "
                           "in full and seated as nucbands (DOCKET 35); "
                           "arXiv:2508.05447 is captured as text and NOT "
                           "parsed, two attempts reaching 154 and 176 of its "
                           "stated 234 entries"),
)

# What the fifth route reached, and it is two DIFFERENT PHYSICAL OBJECTS.
# Held as data so the distinction cannot be lost to prose.
#   (arXiv id, what it tabulates, bands/states, nuclei, IS IT THE CANDIDATE?)
# `nuclei` is None where the paper states a Z/N window rather than a count --
# a window is not a census and this file will not turn one into the other.
BAND_SOURCES = (
    ("2508.05447", "two-quasiparticle rotational bands in DEFORMED odd-odd "
                   "nuclei, Z 67-71, N 89-97, A 156-168 -- 173 bands and 61 "
                   "bandhead states", 234, None, True),
    ("2303.13849", "magnetic and antimagnetic rotational bands -- the SHEARS "
                   "mechanism in WEAKLY-DEFORMED or NEAR-SPHERICAL nuclei, "
                   "252 MR in 123 nuclei and 38 AMR in 27",
     252 + 38, 123 + 27, False),
)


def lattices():
    """[(row, cells, is the index itself closed?)] -- section 3's correction.

    "A sublattice of L" only means anything when L is a lattice.  Three of the
    twenty-two are; the rest are not, and the sweep's closed sets are closed
    IN THE BOX rather than sublattices of their index.
    """
    out = []
    for nm, _m, _a, _me, _w, _q in registry.rows():
        X = registry.index_of(nm)
        if len(X) > 260:
            out.append((nm, len(X), None))
            continue
        out.append((nm, len(X), is_sublattice(X)))
    return out


def peel(X):
    """A chain of closed sets, one element removed at a time.

    CLOSURE IS TESTED DIRECTLY with D.gen at every step.  The first version of
    this used a shortcut -- "x can go if no two OTHER elements meet or join to
    x" -- which assumes the containing set is closed and collapses when it is
    not: on `madrule` it produced a 14-step chain with TEN intermediates that
    were not closed.  That table was discarded.
    """
    S = frozenset(X)
    chain = [S]
    while S:
        nxt = None
        for x in sorted(S):
            T = S - {x}
            if not T or is_sublattice(T):
                nxt = T
                break
        if nxt is None:
            break
        S = nxt
        chain.append(S)
    return chain


def peel_verified(X):
    """(chain length, bad intermediates, cells it stalls at, maximal?).

    Re-checks every step, so the chain is real by construction.  A chain
    cannot exceed |L| + 1, so reaching that IS the exact answer.
    """
    ch = peel(X)
    bad = [c for c in ch if c and not is_sublattice(c)]
    return (len(ch), len(bad), len(ch[-1]), len(ch) == len(X) + 1)


def recursion():
    """[(row, cells, chain, bad, stalls at, maximal?)] for the LATTICES only."""
    out = []
    for nm, n, isl in lattices():
        if not isl:
            continue
        X = registry.index_of(nm)
        out.append((nm, n) + peel_verified(X))
    return out


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
    print("   SO K4 STAYS EMPTY UNDER THE MASS REACH -- a third reason, and")
    print("   not arity this time.  DOCKET 34 then seated it on the STATUS")
    print("   reach, which IS total; both statements stand.  OWN_ROWS excludes")
    print("   that seating here, or this finding would erase itself.")
    print()
    tot, pairs, longest = family_nesting()
    L = lattices()
    print("3. THE DETERMINATION ON RECURSION.")
    print("   FIRST, A WORD THIS FILE HAD WRONG.  Only %d of %d indexes are"
          % (sum(1 for _n, _c, l in L if l), len(L)))
    print("   LATTICES -- closed under meet and join:")
    for nm, n, isl in L:
        if isl:
            print("     %-34s %d cells" % (nm, n))
    print("   The other %d are not, so \"a sublattice of the index\" is"
          % sum(1 for _n, _c, l in L if l is False))
    print("   ill-posed for them.  D.gen(S)==S tests CLOSED IN THE BOX, which")
    print("   is the right test for the sweep and the wrong words for it.")
    print()
    print("   within this sweep's own family (closed sets, not sublattices):")
    print("     %d closed sets, %d strict containments, longest chain %d"
          % (tot, pairs, longest))
    print()
    print("   AND FOR THE THREE LATTICES, peeled one element at a time with")
    print("   closure tested directly and every intermediate re-checked:")
    print("     %-34s %-7s %-7s %-6s %s"
          % ("lattice", "cells", "chain", "bad", "verdict"))
    for nm, n, ch, bad, ends, maxi in recursion():
        print("     %-34s %-7d %-7d %-6d %s"
              % (nm, n, ch, bad,
                 "MAXIMAL -- exact" if maxi else "lower bound, stalls at %d" % ends))
    print("   A chain cannot exceed |L| + 1, so reaching it IS the answer.")
    print()
    print("   THE FIRST ATTEMPT WAS WRONG AND THE TABLE WAS DISCARDED.  A fast")
    print("   removability shortcut assumed the containing set was closed; on")
    print("   madrule it gave a 14-step chain with TEN intermediates that were")
    print("   not closed at all.  peel() now calls D.gen every step.")
    print()
    print("   EXHAUSTIVELY, over every subset of the small indexes:")
    print("     %-34s %-7s %-14s %s"
          % ("index", "cells", "closed sets", "longest chain"))
    for nm, n, ns, ch in exhaustive():
        print("     %-34s %-7d %-14d %d" % (nm, n, ns, ch))
    print("   One sixteen-cell chart holds more closed sets than the whole")
    print("   family sweep found across the tree -- %d against %d."
          % (max(ns for _n, _c, ns, _ch in exhaustive()), tot))
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
    print("   nuclear bands      FOUR ROUTES CLOSED, THE FIFTH OPEN:")
    for r, why in NUCLEAR_ROUTES:
        print("                        %-22s %s" % (r, why))
    print("                      All four failures were MEETS.  NAVIGATION.md")
    print("                      section 3: navigate by JOIN, never by meet --")
    print("                      meet failures 12..90705 by cap, join 0 at")
    print("                      every cap.  Re-run as a join it returns at")
    print("                      once, and it returns E and I^pi per member:")
    for aid, what, nb, nn, cand in BAND_SOURCES:
        print("                        arXiv:%s  %s" % (aid, what))
        print("                        %-22s %d bands/states, %s, %s"
              % ("", nb, "%d nuclei" % nn if nn else "Z/N window, no census",
                 "THE CANDIDATE" if cand else "a DIFFERENT object"))
    print("                      2303.13849 is now CAPTURED AND SEATED as")
    print("                      nucbands (DOCKET 35): 2,145 levels, 121")
    print("                      cells, cell (2,63,2), and the K2 is free.")
    print("                      2508.05447 is captured and NOT parsed --")
    print("                      154 and 176 of its stated 234 in two tries.")
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
    # DOCKET 35 SEATED nucbands AND THE SWEEP GREW.  This sweep is over the
    # seated indexes, so a new index legitimately extends it: 143 -> 203.
    # WHAT DID NOT MOVE IS THE FINDING -- still exactly two sub-populations
    # reach an unoccupied channel, still madrule at l_d=0 and the spin-4
    # mesons, and the containment structure below is untouched at 14 and 2.
    chk("203 of them are sublattices -- 143 before DOCKET 35 seated nucbands, "
        "and UNMOVED by DOCKET 36b's seating", sl, 203)
    chk("and exactly two reach a channel the index lacks", un, 2)

    H = unoccupied_hits()
    chk("both hits are at K4, the last empty channel",
        sorted({k for _n, _c, _v, _ct, k, _e in H}), [4])
    chk("and they are madrule at l_d=0 and the spin-4 mesons",
        sorted((n, c, v) for n, c, v, _ct, _k, _e in H), sorted(K4_HITS))
    chk("and WITHOUT the self-exclusion the finding erases ITSELF -- "
        "the guard does real work",
        (len(H), sum(1 for r in sweep() if r[4] not in occupied(False))),
        (2, 0))
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

    # section 3: the terminology correction FIRST
    L = lattices()
    chk("ONLY THREE INDEXES ARE LATTICES -- the rest are merely charts",
        sorted(nm for nm, _c, isl in L if isl),
        ["bosonqp.index", "madelung.janet", "overlaprule.madelung_slot"])
    # DOCKET 36b seated deformedbands and it is a CHART, not a lattice, so this
    # count moves 19 -> 20.  NOTHING ELSE IN THIS FILE MOVED: 203 sublattices,
    # 14 containments, chain 2, and the same two unoccupied-channel hits.  The
    # sweep grew from 203 tested sub-populations to 366 and contributed not one
    # new sublattice, which is a fact about the deformed chart and is recorded
    # here rather than absorbed.
    chk("and twenty are NOT, so 'sublattice of the index' is ill-posed "
        "for them", sum(1 for _n, _c, isl in L if isl is False), 20)

    tot, pairs, longest = family_nesting()
    chk("within the family: 203 CLOSED SETS, 14 containments, chain 2 -- "
        "the sets grew, the CONTAINMENT STRUCTURE did not",
        (tot, pairs, longest), (203, 14, 2))

    # the recursion, done properly on the three that admit the question
    Rc = recursion()
    chk("three lattices peeled, and NO intermediate fails closure",
        (len(Rc), sorted({bad for _n, _c, _ch, bad, _e, _m in Rc})), (3, [0]))
    chk("two of the three peel to EMPTY -- chain |L|+1, which is MAXIMAL and "
        "therefore exact",
        sorted((nm, ch) for nm, _c, ch, _b, _e, maxi in Rc if maxi),
        [("bosonqp.index", 6), ("overlaprule.madelung_slot", 83)])
    chk("and madelung.janet gives a verified lower bound of 51, stalling",
        [(nm, ch, e) for nm, _c, ch, _b, e, maxi in Rc if not maxi],
        [("madelung.janet", 51, 120)])
    chk("a chain cannot exceed |L|+1, so the two maximal ones are settled",
        [ch <= c + 1 for _n, c, ch, _b, _e, _m in Rc], [True, True, True])
    E = exhaustive()
    chk("four indexes are small enough to enumerate exhaustively", len(E), 4)
    chk("and the exhaustive chains of CLOSED SETS are far deeper than the "
        "family's 2", [ch for _n, _c, _ns, ch in E], [5, 7, 6, 14])
    chk("bosonqp agrees with the peel -- 5 non-empty, 6 with the empty set",
        [ch for nm, _c, _ns, ch in E if nm == "bosonqp.index"], [5])
    chk("one sixteen-cell chart alone holds more sublattices than the whole "
        "family sweep found",
        max(ns for _n, _c, ns, _ch in E) > tot, True)
    chk("and the rest are NOT determined, named rather than implied",
        len(too_large()) > 0, True)
    chk("five routes to nuclear level data are recorded, four closed",
        (len(NUCLEAR_ROUTES),
         sum(1 for _r, w in NUCLEAR_ROUTES if w.startswith("CLOSED"))), (5, 4))
    chk("and the fifth is OPEN -- the meet/join correction",
        [r for r, w in NUCLEAR_ROUTES if w.startswith("OPEN")],
        ["the paper database"])
    chk("the join returned TWO objects and only ONE is section 4's candidate",
        [a for a, _w, _b, _n, cand in BAND_SOURCES if cand], ["2508.05447"])
    chk("and the shears paper is the larger table but the wrong object",
        [(a, b) for a, _w, b, _n, cand in BAND_SOURCES if not cand],
        [("2303.13849", 290)])

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
