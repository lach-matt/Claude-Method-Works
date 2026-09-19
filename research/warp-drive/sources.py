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
    print("sources.py -- WITHDRAWN.  See DOCKET 16.")
    print("=" * 74)
    print()
    print("This file's census counted the filing cabinet as subject matter.")
    print("It named six 'unbuilt first-order sources' and every one of them is")
    print("a table about the repository, not about matter:")
    for k2, v in sorted(UNBUILT_FIRST_ORDER.items()):
        print("   %-24s %s" % (k2, v))
    print()
    print("All six were built and seated, along with seven more. The figure's")
    print("demand ran from 9 to 133 and every disruptive vertex was repository")
    print("metadata. The live census is registry.py, which ENFORCES that a")
    print("member carries quantum numbers instead of listing sources.")
    return 0


def selftest():
    """A WITHDRAWN FILE ASSERTS ITS WITHDRAWAL AND MEASURES NOTHING.

    The old fixtures pinned the census this file is withdrawn for: how many
    second-order indexes the pool yields, how many of their vertices the figure
    did not have. Re-running them would re-assert the contamination. They are
    gone, and what is checked is that the withdrawal is real.
    """
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-54s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("this file is withdrawn", WITHDRAWN, True)
    chk("the six it named are all filing cabinet",
        sorted(UNBUILT_FIRST_ORDER), sorted([
            "the BUILD series", "the Register", "the coverage census",
            "the dockets", "the drive manifest", "the recovered ledger"]))
    chk("none of them names a quantum number",
        [k for k in UNBUILT_FIRST_ORDER
         if any(t in k.lower() for t in ("shell", "orbital", "level",
                                         "term", "nuclide"))], [])
    import os
    chk("nothing imports it",
        [f for f in os.listdir(".")
         if f.endswith(".py") and f != "sources.py"
         and "import sources" in open(f, encoding="utf-8").read()], [])
    print("sources selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
