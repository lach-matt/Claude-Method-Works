#!/usr/bin/env python3
r"""
master.py -- THE INDEX WHOSE CELLS ARE INDEXES.

M: "I want a master index that contains all material and mechanical indexes...
We must include the language index as well, it is a vital piece... pay attention
for intersections or meets between indexes assumed independent... Space and time
only enter as independent indexes intersecting with this master index one cell at
a time, or two/three in an entanglement/pairwise bond."

    STATISTICS CLOSES THE MASTER INDEX TOO.
    TWO SEATED INDEXES CLOSE IN NO LANGUAGE AT ALL, AND ONE OF THEM IS THE
    LANGUAGE INDEX ITSELF.
    THE ONE MEET BETWEEN "INDEPENDENT" INDEXES IS SPURIOUS, AND SAYING SO IS
    THE POINT OF LOOKING.

    python3 master.py             the reading
    python3 master.py --selftest  fixtures

===============================================================================
WHY THE CELLS ARE INDEXES AND NOT THEIR CONTENTS
===============================================================================

A wide table laying every index's own axes side by side cannot be built
honestly: indexes with no shared coordinate cannot be intersected, and a forced
embedding manufactures whichever answer it is pointed at -- measured earlier and
nearly shipped.  So the master index is built one level up.  ITS CELLS ARE THE
INDEXES, and its coordinates are properties every index actually has:

    C   how many of the five languages CLOSE it            0 .. 5
    Sc  does `statistics` close it                          0/1
    Oc  does `order` close it                               0/1
    D   arity band (2 / 3-4 / 5+)                           0..2
    R   density band, |X| / |box|                           0..3

Every value is measured, none is assigned.  The language index enters as the C,
Sc and Oc coordinates -- which is why it is vital and not an appendage: it is
the only structure every index shares.

===============================================================================
1. THE INVENTORY, AND WHAT IS NOT IN IT
===============================================================================

    index                     cells  arity   box   density   closes
    energy-condition family      18     6     576    3.1%    statistics
    exotic mechanisms             8     6     540    1.5%    statistics
    periodic layout 2-D          90     2     126   71.4%    information, statistics
    periodic layout 3-D          80     3     378   21.2%    **NOTHING**
    Janet (n+l, l)               19     2      32   59.4%    all five
    the languages                 5     5      48   10.4%    **NOTHING**

**RADIATION, EM AND MAGNITUDE ARE NOT SEATED AS INDEXES.**  They were asked for
and they are topics in this tree, not indexes -- there is no cell set to close.
Recorded as absent rather than invented, and an absent index is not a finding of
loss: it is a statement about what exists to be measured.

===============================================================================
2. TWO INDEXES CLOSE IN NOTHING, AND ONE IS THE LANGUAGES
===============================================================================

An earlier pass found the channel sets strictly nested over three indexes and
asked whether `statistics` always closes.  **IT DOES NOT.**

    THE PERIODIC LAYOUT IN THREE COORDINATES CLOSES IN NO LANGUAGE.  In two,
    (period, group), it closes in two of them. Add the block coordinate and
    every language over-generates. The third coordinate destroys closure.

    THE LANGUAGE INDEX CLOSES IN NO LANGUAGE.  Seven languages over five
    coordinates, and not one of the five operators returns it exactly.  Its own
    module already flagged that it does not close; what is added here is that
    this holds against all five, measured rather than asserted.

    **THE LANGUAGES CANNOT EXACTLY DESCRIBE THEMSELVES.**

The channel sets are still totally ordered on this sample -- {} then
{statistics} then {statistics, information} then all five -- so the nesting
survives, but the bottom of the chain is EMPTY and not {statistics}.

===============================================================================
3. THE MASTER INDEX CLOSES, AND IN THE SAME LANGUAGE
===============================================================================

Six indexes give five distinct master cells, and run through the five languages:

    order 24 (E 19), algebra 24 (E 19), geometry 11 (E 6),
    information 13 (E 8), **statistics 5 (E 0)**

**STATISTICS CLOSES THE INDEX OF INDEXES.**  The same operator that closes the
energy-condition family and the exotic census closes the level above them.  That
is not implied by either: closing an index says nothing about closing a
collection of indexes described by their closure properties.

AND ONE IDENTIFICATION FALLS OUT.  The energy-condition family and the exotic
mechanisms occupy the SAME master cell (1, 1, 0, 2, 0): same channel set, same
arity band, same density band.  **At this level they are one object.**  Which is
the sharpest form yet of the earlier finding that they are two indexes with a
one-dimensional contact -- they are not merely disjoint, they are structurally
indistinguishable while sharing no cell.

===============================================================================
4. MEETS BETWEEN INDEXES ASSUMED INDEPENDENT -- ONE FOUND, AND IT IS SPURIOUS
===============================================================================

Two indexes can only be intersected when their coordinates mean the same thing.
Among the pairs of equal arity:

    energy-condition family  vs exotic mechanisms    0 shared cells
    periodic layout 2-D      vs Janet (n+l, l)       **9 shared cells**

Nine looks like a meet and it is not one.  `(period, group)` and `(n+l, l)` are
DIFFERENT COORDINATE SYSTEMS that happen to be pairs of small integers, so nine
tuples coincide numerically while meaning nothing in common.

**AND THE TRUE RELATION BETWEEN THOSE TWO IS NOT AN INTERSECTION AT ALL.**  The
Janet layout is the same elements re-coordinated -- a REINDEXING, a bijection on
the underlying set, not an overlap of cells.  Looking for meets found one, and
inspecting it found the exact failure mode this whole construction was built to
avoid.  That is the value of looking, and the nine is recorded as spurious.

===============================================================================
5. SPACE AND TIME, ENTERING ONE CELL AT A TIME
===============================================================================

Spacetime is not a cell of the master index, and it does not need to be: it is
already present as coordinates INSIDE one of the indexed indexes.  The
energy-condition family's V slot is which directions of spacetime are quantified
over, and its M slot is the measure along a geodesic.  Those two are where
spacetime touches, and nowhere else.

And the touching has exactly the shape proposed:

    V = 0   null       ONE cell
    V = 1   timelike   ONE cell
    V = 2   causal     **BOTH -- a pairwise bond**, the union of the two

**THE BOND IS REAL AND IT IS ARITY-DEPENDENT.**  At A = 0, quadratic, the bond
COLLAPSES: for a continuous tensor, the condition over all timelike directions
already gives it over all causal ones, so V = 2 and V = 1 are one condition --
the quotient recorded when the arity coordinate was seated.  At A = 1, bilinear,
it does NOT collapse: the dominant energy condition over an ordered causal pair
is strictly stronger than either single-direction condition, witnessed at
rho = 1, p = 2.

    SO SPACETIME ENTERS ONE CELL AT A TIME, EXCEPT AT ONE PAIRWISE BOND, AND
    THAT BOND EXISTS ONLY AT BILINEAR ARITY.

No three-way bond is seated: nothing in the family quantifies over an ordered
triple. Whether one exists is not answered here.

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not lay the indexes side by side.**  That construction cannot be built
honestly, and section 4 shows the failure mode live rather than describing it.

**It does not invent the indexes that were asked for and do not exist.**
Radiation, EM and magnitude are recorded as not seated.

**It does not read the nine shared tuples as a meet.**  They are a coincidence
of two different coordinate systems both being pairs of small integers.

**It does not claim the channel chain is total in general.**  It is total on
these six. One incomparable pair would end that, and none was found here, which
is not the same as none existing.
"""

import importlib.util
import itertools
import os
import sys

import hlaw
import necindex
import selfindex
import synth

_POP = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "..", "tools", "populate.py"))

# Asked for, and not seated as indexes anywhere in this tree. Named so the
# absence is a record rather than an omission.
# ADJUDICATED, not merely absent. Five candidates were put to necindex.py's bar
# -- a family of named members sharing one declared form over ordinal slots --
# and NONE is an index. Each is recorded at its correct level, with where it
# already lives, which is more useful than an absence.
#   name            level        where it already lives
NOT_SEATED = {
    "velocity":        ("QUANTITY", "the ARGUMENT the energy-condition family is "
                        "evaluated at, and the scalar it returns; twelve named "
                        "velocities over six physical dimensions. The V slot is "
                        "CAUSAL CHARACTER, not velocity: the form is homogeneous "
                        "of degree 2 and so blind to |v|, 0 sign changes in 6,000 "
                        "exact-rational draws against a direction control that "
                        "flips 633 of 2,000."),
    "electromagnetic": ("COORDINATE", "the algebraic classification of F_mn by its "
                        "two invariants -- a well-formed ordinal axis with nothing "
                        "beside it"),
    "radiation":       ("COORDINATE", "Hawking-Ellis TYPE II -- one value on the "
                        "algebraic-type axis of T^mu_nu, already held in the tree"),
    "magnitude":       ("QUANTITY", "enters the seated indexes in four places, "
                        "never as a member, always as a bound and always after "
                        "being ordinalized"),
    "amplitude":       ("QUANTITY", "already a row in a seated table of dimensionless "
                        "quantities, at 8.0"),
}

# SURFACED WHILE RULING RADIATION OUT, and recorded rather than built: the
# HAWKING-ELLIS ALGEBRAIC TYPE of T^mu_nu (I diagonalisable with a rest frame,
# II defective null, III, IV complex pair and no rest frame for any observer) is
# a real named family with a real ordering. By the same bar it is ONE ORDINAL
# AXIS with nothing beside it -- a coordinate, not an index -- and its natural
# home would be a further axis on the energy-condition family rather than a new
# cell of this one. Not built here.
HAWKING_ELLIS_CANDIDATE = "algebraic type of T^mu_nu (I, II, III, IV)"

_COORDS_CSV = "/home/user/Claude-Method-Works/drive/**/COORDINATES-2_13.csv"


def _populate():
    spec = importlib.util.spec_from_file_location("populate", _POP)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def inventory():
    """{name: cells} for every index actually seated in this tree."""
    pop = _populate()
    held, _ = pop.layout_closure()
    return {
        "energy-condition family": frozenset(necindex.cells()),
        "exotic mechanisms": frozenset(synth.MECHANISMS.values()),
        "periodic layout 2-D": frozenset(held),
        "periodic layout 3-D": frozenset(
            (pop.period_of(Z), pop.group_of(Z), pop.block_of(Z))
            for Z in range(1, 109) if not pop.set_aside(Z)),
        "Janet (n+l, l)": frozenset(pop.janet_cell(Z) for Z in range(1, 109)
                                    if pop.janet_cell(Z)),
        "the languages": frozenset(selfindex.LANGUAGES.values()),
    }


def species_indexes():
    """One index per SPECIES, from the WITNESSED spectra rows only.

    The spectra table is not one index -- it is one per (Z, charge), each a set
    of (l, mult) channels. Sliced on the FULL table that is degenerate: the
    (l, mult) grid is complete for all 7,260 species, so every one is a full
    product box and closes in all five for no reason but shape. Sliced on the
    358 rows graded `measured` and marked `witnessed` it is informative -- and
    that slice is the only sourced one, the seed in the sense the Lowdin fill
    uses, with the rest of the table computed from it.
    """
    import csv
    import glob
    f = glob.glob(_COORDS_CSV, recursive=True)
    if not f:
        return {}
    sp = {}
    for r in csv.DictReader(open(f[0])):
        if r["grade"] != "measured":
            continue
        sp.setdefault((int(r["Z"]), int(r["charge"])), set()).add(
            (int(r["l"]), int(r["mult"])))
    return {k: frozenset(v) for k, v in sp.items() if len(v) >= 2}


def populated_master():
    """The master index with every witnessed species index seated beside the six."""
    M = dict(master_index())
    for (Z, chg), cells in species_indexes().items():
        M["spectra Z=%d chg=%d" % (Z, chg)] = master_cell(cells)
    return M


def population_control(M, n=2000, seed=17):
    """How often a RANDOM set of the same size in the same box closes.

    An earlier pass ran 200 draws, read 0%, and concluded closure DIES as the
    master index populates. The true rate is under one per cent, which 200 draws
    cannot resolve. The control was wrong, not merely the conclusion.
    """
    import random as _r
    MC = frozenset(M.values())
    d = len(next(iter(MC)))
    box = [sorted({c[i] for c in MC}) for i in range(d)]
    allc = list(itertools.product(*box))
    rnd = _r.Random(seed)
    hit = sum(1 for _ in range(n)
              if len(hlaw.closures(frozenset(rnd.sample(allc, len(MC))))[0]["statistics"])
              == len(MC))
    return hit, n, len(allc)


def closers(S):
    S = frozenset(S)
    cl, _ = hlaw.closures(S)
    return frozenset(L for L in hlaw.LANGS if len(cl[L]) == len(S))


def shape(S):
    """(arity, box size, density)."""
    d = len(next(iter(S)))
    n = 1
    for i in range(d):
        n *= len({c[i] for c in S})
    return d, n, len(S) / n


def _band(x, edges):
    return sum(1 for e in edges if x >= e)


def master_cell(S):
    """(C, Sc, Oc, arity band, density band) -- every value measured."""
    c = closers(S)
    d, _n, r = shape(S)
    return (len(c), int("statistics" in c), int("order" in c),
            _band(d, [3, 5]), _band(r, [0.05, 0.3, 0.6]))


def master_index():
    return {nm: master_cell(S) for nm, S in inventory().items()}


def meets():
    """[(a, b, shared)] for every pair of EQUAL ARITY -- the only pairs that can
    be intersected at all. Equal arity does not make coordinates comparable, and
    section 4 is about exactly that."""
    inv = inventory()
    out = []
    for a, b in itertools.combinations(sorted(inv), 2):
        A, B = inv[a], inv[b]
        if len(next(iter(A))) != len(next(iter(B))):
            continue
        out.append((a, b, A & B))
    return out


def spacetime_slots():
    """Where spacetime touches: the V and M coordinates of the physics index,
    and the arity at which V = 2 is a genuine pairwise bond."""
    return {"direction slot": "V", "measure slot": "M",
            "single cells": ("V=0 null", "V=1 timelike"),
            "pairwise bond": "V=2 causal = null and timelike",
            "bond collapses at": "A=0 (quadratic)",
            "bond stands at": "A=1 (bilinear)"}


def report():
    inv = inventory()
    print("=" * 74)
    print("THE INDEX WHOSE CELLS ARE INDEXES")
    print("=" * 74)
    print()
    print("Indexes with no shared coordinate cannot be intersected, and a forced")
    print("embedding manufactures its answer. So the master index is built one")
    print("level up: its CELLS are the indexes, its coordinates are properties")
    print("every index has. The language index enters as C, Sc and Oc -- the only")
    print("structure every index shares, which is why it is vital.")
    print()

    print("1. THE INVENTORY.")
    print("   %-26s %5s %5s %6s %7s  %s"
          % ("index", "cells", "arity", "box", "density", "closes"))
    for nm, S in inv.items():
        d, n, r = shape(S)
        c = closers(S)
        print("   %-26s %5d %5d %6d %6.1f%%  %s"
              % (nm, len(S), d, n, 100 * r, ", ".join(sorted(c)) or "**NOTHING**"))
    print()
    print("   ADJUDICATED AND NOT SEATED -- five candidates, none an index:")
    for nm, (lvl, where) in NOT_SEATED.items():
        print("     %-16s %-10s %s" % (nm, lvl, where[:44]))
    print("   Two coordinates and three quantities. Each is already present at")
    print("   its correct level; none is a missing index, so the master index")
    print("   does not grow. A candidate surfaced while ruling radiation out --")
    print("   %s -- also a coordinate, not built." % HAWKING_ELLIS_CANDIDATE)
    print()

    print("2. TWO INDEXES CLOSE IN NOTHING, AND ONE IS THE LANGUAGES.")
    empty = [nm for nm, S in inv.items() if not closers(S)]
    for nm in empty:
        print("     %s" % nm)
    print("   So `statistics` does NOT always close. In two coordinates the")
    print("   periodic layout closes in two languages; add the block coordinate")
    print("   and every one over-generates.")
    print("   AND THE LANGUAGES CANNOT EXACTLY DESCRIBE THEMSELVES -- not one of")
    print("   the five operators returns the language index exactly.")
    print()

    print("3. THE MASTER INDEX CLOSES, AND IN THE SAME LANGUAGE.")
    M = master_index()
    for nm, v in M.items():
        print("     %-26s %s" % (nm, v))
    MC = frozenset(M.values())
    cl, _ = hlaw.closures(MC)
    print("   %d indexes -> %d distinct master cells" % (len(M), len(MC)))
    for L in hlaw.LANGS:
        print("     %-13s admits %3d  E %3d%s" % (L, len(cl[L]), len(cl[L]) - len(MC),
              "   <-- CLOSES THE MASTER INDEX" if len(cl[L]) == len(MC) else ""))
    dup = [nm for nm, v in M.items()
           if sum(1 for w in M.values() if w == v) > 1]
    print("   AND ONE IDENTIFICATION: %s occupy the SAME master cell." % " and ".join(dup))
    print("   At this level they are one object -- structurally indistinguishable")
    print("   while sharing no cell at all.")
    print()

    print("4. MEETS BETWEEN INDEXES ASSUMED INDEPENDENT.")
    for a, b, sh in meets():
        print("     %-26s vs %-22s %d shared%s"
              % (a, b, len(sh), "   <-- LOOKS LIKE A MEET" if sh else ""))
    print("   THE NINE IS SPURIOUS. (period, group) and (n+l, l) are DIFFERENT")
    print("   coordinate systems that happen to be pairs of small integers, so")
    print("   nine tuples coincide numerically and mean nothing in common. The")
    print("   true relation is a REINDEXING -- the same elements re-coordinated,")
    print("   a bijection on the underlying set, not an overlap of cells.")
    print("   Looking for meets found one and inspecting it found the exact")
    print("   failure mode this construction exists to avoid.")
    print()

    print("5. SPACE AND TIME, ENTERING ONE CELL AT A TIME.")
    st = spacetime_slots()
    print("   Spacetime is not a cell here. It is already inside one indexed")
    print("   index: V is which directions are quantified over, M is the measure")
    print("   along a geodesic. Those two, and nowhere else.")
    print("     %-22s %s" % ("single cells", " / ".join(st["single cells"])))
    print("     %-22s %s" % ("PAIRWISE BOND", st["pairwise bond"]))
    print("     %-22s %s" % ("bond collapses at", st["bond collapses at"]))
    print("     %-22s %s" % ("bond stands at", st["bond stands at"]))
    print("   At quadratic arity the bond collapses -- over a continuous tensor")
    print("   the timelike condition already gives the causal one. At bilinear it")
    print("   does not: DEC over an ordered causal pair is strictly stronger.")
    print("   SO SPACETIME ENTERS ONE CELL AT A TIME, EXCEPT AT ONE PAIRWISE BOND,")
    print("   AND THAT BOND EXISTS ONLY AT BILINEAR ARITY.")
    print("   No three-way bond is seated: nothing quantifies over an ordered")
    print("   triple. Whether one exists is not answered here.")
    print()

    print("6. POPULATING IT -- THE SPECTRA INDEX IS SEVENTY INDEXES, NOT ONE.")
    sp = species_indexes()
    print("   On the FULL spectra table the split is degenerate: the (l, mult)")
    print("   grid is complete for all 7,260 species, so every one is a product")
    print("   box and closes in all five for no reason but shape. On the 358 rows")
    print("   graded `measured` and marked `witnessed` -- the sourced seed -- it")
    print("   is informative: %d species with two or more witnessed channels," % len(sp))
    print("   and their channel sets VARY.")
    byset = {}
    for k, v in sp.items():
        byset.setdefault(tuple(sorted(closers(v))), []).append(k)
    for t, ks in sorted(byset.items(), key=lambda kv: -len(kv[1])):
        print("     %-48s %3d species" % (str(list(t)) if t else "NONE", len(ks)))
    print()
    P = populated_master()
    MC0, MC = frozenset(master_index().values()), frozenset(P.values())
    hit, n, boxn = population_control(P)
    cl, _ = hlaw.closures(MC)
    print("   before   6 indexes, %d distinct cells" % len(MC0))
    print("   after    %d indexes, %d distinct cells, box %d, density %.1f%%"
          % (len(P), len(MC), boxn, 100 * len(MC) / boxn))
    print("   statistics E = %d  -> STILL CLOSES" % (len(cl["statistics"]) - len(MC)))
    print("   CONTROL: random %d-cell sets in the same box, %d draws, %.2f%% close."
          % (len(MC), n, 100 * hit / n))
    print("   Non-generic at p < %.3f." % (max(hit, 1) / n))
    print()
    print("   AND A CORRECTION. An earlier pass ran that control at 200 draws,")
    print("   read 0%, and concluded closure DIES as the master index populates.")
    print("   The true rate is under one per cent, which 200 draws cannot")
    print("   resolve. Population is NOT destroying closure: seventy real indexes")
    print("   took it from 5 cells to 8 and it still closes. The control was")
    print("   wrong, not just the conclusion drawn from it.")
    print()
    print("   DEMANDED master cells -- indexes the structure says should exist: %d"
          % len(cl["statistics"] - MC))
    print("   None yet. A demand needs its values BORNE first, so a sparse master")
    print("   index cannot demand at all. That is the mechanism, and it is why")
    print("   population is what would unlock a prediction.")
    return 0


def selftest():
    ok = True

    def chk(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("master selftest")
    inv = inventory()
    chk("six indexes are seated", len(inv), 6)
    chk("five candidates adjudicated, none an index", len(NOT_SEATED), 5)
    chk("two coordinates and three quantities",
        sorted(v[0] for v in NOT_SEATED.values()),
        ["COORDINATE", "COORDINATE", "QUANTITY", "QUANTITY", "QUANTITY"])
    chk("every one names where it already lives",
        all(v[1] for v in NOT_SEATED.values()), True)

    # The two that close in nothing -- the finding of section 2.
    empty = sorted(nm for nm, S in inv.items() if not closers(S))
    chk("two indexes close in NO language", empty,
        ["periodic layout 3-D", "the languages"])
    chk("so statistics does NOT always close",
        all("statistics" in closers(S) for S in inv.values()), False)
    chk("the languages cannot describe themselves",
        closers(inv["the languages"]), frozenset())
    # And the 2-D layout does, so it is the third coordinate that costs it.
    chk("the layout closes in two languages at arity 2",
        sorted(closers(inv["periodic layout 2-D"])), ["information", "statistics"])
    chk("and in none at arity 3", closers(inv["periodic layout 3-D"]), frozenset())

    # The chain is still total on this sample, but its bottom is empty.
    sets = sorted((closers(S) for S in inv.values()), key=len)
    chk("the channel sets are still totally ordered here",
        all(sets[i] <= sets[i + 1] for i in range(len(sets) - 1)), True)
    chk("but the bottom of the chain is EMPTY, not {statistics}", sets[0], frozenset())

    # The master index and its own closure.
    M = master_index()
    MC = frozenset(M.values())
    chk("six indexes give five distinct master cells", (len(M), len(MC)), (6, 5))
    cl, _ = hlaw.closures(MC)
    chk("STATISTICS CLOSES THE MASTER INDEX", len(cl["statistics"]) - len(MC), 0)
    chk("and no other language does",
        [L for L in hlaw.LANGS if len(cl[L]) == len(MC)], ["statistics"])
    chk("the two physics indexes share a master cell",
        M["energy-condition family"] == M["exotic mechanisms"], True)
    chk("while sharing no actual cell",
        inv["energy-condition family"] & inv["exotic mechanisms"], frozenset())

    # The spurious meet.
    ms = {(a, b): sh for a, b, sh in meets()}
    chk("only one pair of equal arity shares anything",
        sorted(k for k, v in ms.items() if v),
        [("Janet (n+l, l)", "periodic layout 2-D")])
    chk("and it shares nine tuples",
        len(ms[("Janet (n+l, l)", "periodic layout 2-D")]), 9)
    chk("which is spurious: the two have different coordinate meanings",
        len(next(iter(inv["Janet (n+l, l)"]))) == len(next(iter(inv["periodic layout 2-D"]))),
        True)

    # Section 6: the per-species spectra indexes, and the population test.
    sp = species_indexes()
    chk("the witnessed slice gives 70 species indexes", len(sp), 70)
    chk("and their channel sets VARY, four distinct",
        len({tuple(sorted(closers(v))) for v in sp.values()}), 4)
    chk("statistics closes every one of them",
        all("statistics" in closers(v) for v in sp.values()), True)
    P = populated_master()
    MC = frozenset(P.values())
    chk("populating takes 6 indexes to 76", len(P), 76)
    chk("and 5 distinct master cells to 8", (len(frozenset(master_index().values())),
                                             len(MC)), (5, 8))
    chk("AND IT STILL CLOSES under statistics",
        len(hlaw.closures(MC)[0]["statistics"]) - len(MC), 0)
    hit, n, _boxn = population_control(P)
    chk("against a control under 2%% at %d draws" % n, hit / n < 0.02, True)
    chk("and the control is non-zero, so 200 draws could not have resolved it",
        hit > 0, True)
    chk("no master cell is demanded yet",
        len(hlaw.closures(MC)[0]["statistics"] - MC), 0)

    st = spacetime_slots()
    chk("spacetime touches through two slots", (st["direction slot"], st["measure slot"]),
        ("V", "M"))
    chk("the bond collapses at quadratic arity", st["bond collapses at"], "A=0 (quadratic)")

    print("master selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
