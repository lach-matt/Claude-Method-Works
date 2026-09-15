#!/usr/bin/env python3
r"""
sources.py -- WITHDRAWN.  Its census counted the filing cabinet as subject
matter.

M: "Remove any index in the project whose members do not have quantum numbers."

This file named six "unbuilt first-order sources" -- the BUILD series, the drive
manifest, the Register, the recovered ledger, the coverage census, the dockets --
and I built all six and seven more besides.  NONE OF THEM IS AN INDEX OF THE
PERIODIC ELEMENTS.  Every member is a file, a conversation, an archive or a
docket, and the figure ran E from 9 to 133 on the mixture.

It also measured a "second-order supply" of 84 indexes over 21 vertices by
charting the seated indexes against each other.  Those members are indexes, not
elements, so that count is off-subject too.

    THE LIVE CENSUS IS `registry.py`, which ENFORCES the criterion rather than
    listing sources: every index names the quantum numbers its members carry,
    and a module exposing an index that is neither registered nor excused fails
    the selftest.

Nothing here is imported by anything.  It is kept only because DOCKET 16 cites
it as the origin of the contamination; read it as a record of a mistake, not as
a census.  See DOCKET 16.
"""

import itertools
import sys

import hlaw
import mi

import entropy as _entropy
import refusal as _refusal

OUT_OF_SCOPE_IS_A_RULING = True
WITHDRAWN = True  # DOCKET 16: this census counted the filing cabinet

FIRST_ORDER = {
    "shell fibration": "fibred.py",
    "Janet fibration": "madelung.py",
    "ionisation ladder": "ions.py",
    "provenance": "axes.py",
    "channel index": "channels.py",
    "inversion index": "inversion.py",
    "probability index": "probability.py",
}
SECOND_ORDER = {
    "the master index": "mi.py",
    "the refusal index": "rindex.py",
    "the entropy index": "entropy.py",
}

# THE SCOPE MOVED ON 2026-09-15 AND THIS CONSTANT IS NOW CONTESTED.
# M: "Whatever the final shape and its vertexes are is the scope."  occupy.py
# then measured that EIGHT of the ten cells the figure demands need 18 to 30
# members, which no second-order index over the seated vertices can reach -- so
# they can only be first-order, and the six below are the first-order sources
# this tree has named and not built.  OUT_OF_SCOPE_IS_A_RULING was a decision
# taken under the old scope; it is left standing rather than flipped here,
# because flipping a ruling is not an instrument's job.  See DOCKET 13.
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
    import figure as _fig
    print("   of which NOT already hexad vertices       %d"
          % len(verts - _fig.hexad()))
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

    chk("seven first-order indexes seated", len(FIRST_ORDER), 7)
    chk("three second-order", len(SECOND_ORDER), 3)
    chk("ten in all", len(seated()), 10)
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
    import figure as _fig
    chk("NEW vertices, not already in the hexad",
        len(verts - _fig.hexad()), 20)
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
