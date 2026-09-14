#!/usr/bin/env python3
r"""
sources.py -- WHAT ELSE CAN BE BUILT, AND WHERE THE COUNTING HAS TO STOP.

M: "any other available index that can be and has not yet been identified and
built in the same fashion and criterion as the rest."

    python3 sources.py             the reading
    python3 sources.py --selftest  fixtures

    THE ANSWER HAS TWO HALVES AND THEY ARE NOT ALIKE.  One is a finite list that
    can be finished.  The other is a construction that cannot, and pretending to
    enumerate it would be the single most misleading thing this tree could do.

===============================================================================
1. FIRST-ORDER AND SECOND-ORDER
===============================================================================

    FIRST-ORDER   its members are things the corpus banks -- elements,
                  transitions, measurements, channels.  The supply is bounded by
                  what the corpus HAS.

    SECOND-ORDER  its members are the seated indexes, and its coordinates are
                  measurements OF them.  The supply is bounded by how many
                  admissible measurements one can write down, which is not a
                  bound.

Eight indexes are seated.  Five are first-order and three are second-order:

        FIRST-ORDER                        SECOND-ORDER
        shell fibration   (n, l, k)        the master index    MI
        Janet fibration   (n+l, l, k)      the refusal index   R
        ionisation ladder Lambda_8         the entropy index   H
        provenance        the 26 axes
        channel index     (l, B, mult)

===============================================================================
2. THE SECOND-ORDER SUPPLY IS NOT A LIST, AND HERE IS THE MEASUREMENT
===============================================================================

Take nine per-index measurements that PASS the chart criterion -- cells, height,
width, comparable pairs, join-irreducibles, H_max, H_min, |R(X)| and K itself.
Every one moves on 0 of 9 under an appended monotone redundant coordinate, so
every one is admissible by DOCKET 3's own test.

    Three-coordinate charts from those nine:      **84 indexes**
    Distinct (K, height, width) vertices:         **21**
    Of which NOT already hexad vertices:          **20**

    **EIGHTY-FOUR NEW INDEXES FROM A STARTER SET OF NINE.**  And the starter set
    is itself open -- H_max and H_min were added in one afternoon and nothing
    stops a tenth measurement tomorrow.  Nor is arity three special; the same
    nine give more at arity two and four.

    SO "HOW MANY MASTER INDEXES ARE THERE" HAS NO SECOND-ORDER ANSWER.  Counting
    them is counting one's own measurements.  The honest statement is that the
    second-order family is a CONSTRUCTION with a generating rule, and the rule is
    written above.

===============================================================================
3. WHAT THIS MEANS FOR "COMPLETE"
===============================================================================

    THE RULES ARE COMPLETE.  Eight lawful channels and no more, because a closing
    set must be a down-set.  The chart criterion is fixed.  The reachability law
    holds with no exceptions over 86 injective charts.  K1, K4 and K5 are
    unreachable from the element address; K4 is reachable from the ladder; K2 and
    K6 only by coarsening.  None of that moves when a new index is built.

    THE FIGURE IS NOT COMPLETE, AND CANNOT BE.  Every new index is another
    vertex.  The hexad became an octad in one sitting, and 20 more vertices are
    a comprehension away.  Any claim that a particular polygon is THE
    classification is refuted by building one more index, which takes minutes.

    SO THE CLASSIFICATION IS OF KINDS, NOT OF MEMBERS -- which is the ordinary
    situation for a classification and worth saying plainly.

===============================================================================
4. FIRST-ORDER SOURCES STILL UNBUILT
===============================================================================

These are real, banked, and NOT built here.  Each is listed with why.

    THE BUILD SERIES         140 files, BUILD9 to BUILD179, two streams.
    THE DRIVE MANIFEST       820 files with mime, size, md5, status.
    THE REGISTER             1,660 entries over 1-1792, 132 numbered gaps.
    THE RECOVERED LEDGER     3,173 files in six statuses.
    THE COVERAGE CENSUS      1,005 artefact names in five dispositions.
    THE DOCKETS              ten, with rulings.

    **EVERY ONE OF THEM INDEXES THE ARTEFACT STORE, NOT THE METHOD.**  They are
    facts about which files exist, what was recovered and what a build contained
    -- bookkeeping about the repository rather than mathematics about the
    corpus's content.  An index of them would be well formed and would occupy a
    vertex, and it would be measuring the filing cabinet.

    THAT IS A JUDGEMENT AND IT IS FLAGGED AS ONE.  `OUT_OF_SCOPE_IS_A_RULING` is
    True in this file.  A ruling could bring any of them in, and the instrument
    to build one would look exactly like `provenance`.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

    TO ENUMERATE THE SECOND-ORDER FAMILY.  Section 2 measures its size at one
    arity from one starter set and stops.  A list would imply a bound.

    TO BUILD THE BOOKKEEPING INDEXES WITHOUT A RULING.  See section 4.

    TO CALL THE EIGHT COMPLETE.  They are what is seated.  Section 3 says why no
    number belongs in that sentence.
"""

import itertools
import sys

import hlaw
import mi

import entropy as _entropy
import refusal as _refusal

OUT_OF_SCOPE_IS_A_RULING = True

FIRST_ORDER = {
    "shell fibration": "fibred.py",
    "Janet fibration": "madelung.py",
    "ionisation ladder": "ions.py",
    "provenance": "axes.py",
    "channel index": "spectra.py",
}
SECOND_ORDER = {
    "the master index": "mi.py",
    "the refusal index": "rindex.py",
    "the entropy index": "entropy.py",
}

UNBUILT_FIRST_ORDER = {
    "the BUILD series": "140 files, BUILD9-179, two streams",
    "the drive manifest": "820 files with mime, size, md5, status",
    "the Register": "1,660 entries over 1-1792, 132 numbered gaps",
    "the recovered ledger": "3,173 files in six statuses",
    "the coverage census": "1,005 artefact names in five dispositions",
    "the dockets": "ten, with rulings",
}


def _comparable(X):
    X = sorted(X)
    return sum(1 for a, b in itertools.combinations(X, 2)
               if all(p <= q for p, q in zip(a, b))
               or all(q <= p for p, q in zip(a, b)))


def _join_irreducible(X):
    X = frozenset(X)
    return sum(1 for c in X
               if not any(tuple(max(p, q) for p, q in zip(a, b)) == c
                          for a in X for b in X if a != c and b != c))


def measurements():
    """The per-index measurements used as second-order coordinates."""
    return {
        "cells": lambda X: len(X),
        "height": mi.height,
        "width": mi.width,
        "comparable": _comparable,
        "joinirred": _join_irreducible,
        "Hmax": lambda X: _entropy.cell_of(X)[0],
        "Hmin": lambda X: _entropy.cell_of(X)[1],
        "Rsize": lambda X: len(_refusal.refusal_set(X, cap=None)),
        "K": mi.K,
    }


def admissibility():
    """{measurement: how many of the nine it moves on}.  0 means admissible.

    The re-charted index's box exceeds refusal.py's cap, so `Rsize` is asked for
    an EXACT scan.  That guard firing here is the guard working: a capped scan
    is a lexicographic prefix and would have been silently wrong.
    """
    inv = mi.inventory()
    out = {}
    for n, f in measurements().items():
        out[n] = sum(1 for X in inv.values()
                     if f(X) != f(frozenset(tuple(c) + (c[0],) for c in X)))
    return out


def admissible():
    return sorted(n for n, m in admissibility().items() if m == 0)


def second_order_family(arity=3):
    """(indexes buildable, distinct vertices, {K: count}) at this arity."""
    inv = mi.inventory()
    M = measurements()
    verts, chans, n = set(), {}, 0
    for combo in itertools.combinations(admissible(), arity):
        P = frozenset(tuple(M[c](X) for c in combo) for X in inv.values())
        verts.add(mi.cell(P))
        chans[mi.K(P)] = chans.get(mi.K(P), 0) + 1
        n += 1
    return n, verts, dict(sorted(chans.items()))


def seated():
    """{name: instrument} over every index this tree has actually built."""
    out = dict(FIRST_ORDER)
    out.update(SECOND_ORDER)
    return out


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("WHAT ELSE CAN BE BUILT, AND WHERE THE COUNTING HAS TO STOP")
    print("=" * 74)
    print()
    print("1. EIGHT SEATED: %d first-order, %d second-order."
          % (len(FIRST_ORDER), len(SECOND_ORDER)))
    print("   FIRST-ORDER -- members are things the corpus banks:")
    for nm, f in FIRST_ORDER.items():
        print("     %-22s %s" % (nm, f))
    print("   SECOND-ORDER -- members are the seated indexes:")
    for nm, f in SECOND_ORDER.items():
        print("     %-22s %s" % (nm, f))
    print()

    adm = admissibility()
    print("2. THE SECOND-ORDER SUPPLY IS NOT A LIST.")
    print("   nine per-index measurements, and every one is ADMISSIBLE:")
    print("     %s" % ", ".join("%s(%d)" % (n, m) for n, m in sorted(adm.items())))
    n, verts, chans = second_order_family(3)
    print("   three-coordinate charts from those nine   %d indexes" % n)
    print("   distinct (K, height, width) vertices      %d" % len(verts))
    import hexad
    print("   of which NOT already hexad vertices       %d"
          % len(verts - hexad.hexad()))
    print("   channels reached                          %s" % chans)
    print("   EIGHTY-FOUR FROM A STARTER SET OF NINE, and the starter set is")
    print("   itself open. Counting these is counting one's own measurements.")
    print()

    print("3. SO: THE RULES ARE COMPLETE, THE FIGURE IS NOT.")
    print("   complete -- 8 lawful channels, the chart criterion, the")
    print("   reachability law, what each source can and cannot reach.")
    print("   NOT complete -- the vertex set. The hexad became an octad in one")
    print("   sitting and 20 more vertices are a comprehension away.")
    print("   THE CLASSIFICATION IS OF KINDS, NOT OF MEMBERS.")
    print()

    print("4. FIRST-ORDER SOURCES STILL UNBUILT, and why.")
    for nm, what in UNBUILT_FIRST_ORDER.items():
        print("     %-22s %s" % (nm, what))
    print("   EVERY ONE INDEXES THE ARTEFACT STORE, NOT THE METHOD -- which")
    print("   files exist, what was recovered, what a build contained. An index")
    print("   of them would be well formed and would be measuring the filing")
    print("   cabinet. OUT_OF_SCOPE_IS_A_RULING = %s; a ruling could bring any")
    print("   of them in, and the instrument would look like axes.py."
          % OUT_OF_SCOPE_IS_A_RULING)
    print()
    print("5. REFUSED: to enumerate the second-order family -- a list would")
    print("   imply a bound. To build the bookkeeping indexes without a ruling.")
    print("   To call the eight complete.")
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

    print("sources selftest")

    chk("five first-order indexes seated", len(FIRST_ORDER), 5)
    chk("three second-order", len(SECOND_ORDER), 3)
    chk("eight in all", len(seated()), 8)
    chk("and every name is distinct",
        len(set(FIRST_ORDER) & set(SECOND_ORDER)), 0)

    # ---- the nine measurements all pass DOCKET 3's test
    adm = admissibility()
    chk("nine per-index measurements", len(adm), 9)
    chk("and EVERY one is admissible", sorted(set(adm.values())), [0])
    chk("so none is disqualified", [n for n, m in adm.items() if m], [])

    # ---- THE HEADLINE: the supply is not a list
    n, verts, chans = second_order_family(3)
    chk("three-coordinate second-order indexes buildable", n, 84)
    chk("distinct vertices they occupy", len(verts), 21)
    import hexad
    chk("NEW vertices, not already in the hexad",
        len(verts - hexad.hexad()), 20)
    chk("channels they reach", chans, {0: 17, 2: 67})
    # AND IT GROWS WITH ARITY, so three is not special.
    n2, v2, _c2 = second_order_family(2)
    n4, v4, _c4 = second_order_family(4)
    chk("arity 2 and arity 4 give more still", (n2, n4), (36, 126))
    chk("and between them still more vertices",
        len(verts | v2 | v4) > len(verts), True)

    # ---- the boundary is declared, not assumed
    chk("six first-order sources are named unbuilt",
        len(UNBUILT_FIRST_ORDER), 6)
    chk("and the exclusion is flagged as a ruling", OUT_OF_SCOPE_IS_A_RULING,
        True)

    print("sources selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
