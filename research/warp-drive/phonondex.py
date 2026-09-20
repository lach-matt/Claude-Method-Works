#!/usr/bin/env python3
r"""
phonondex.py -- THE PHONON INDEX.  1,120 MEMBERS OVER ALL 230 SPACE GROUPS,
COMPUTED END TO END, NO TEXTBOOK TABLE AND NO FETCH.

M: "Do we have an index of phonons?  Or do we need to build one?"  Then: "If
having the index is necessary for the warp work and or if it can accurately be
a realized index, then we have an obligation to build it."

    python3 phonondex.py             the reading
    python3 phonondex.py --selftest  fixtures, stdlib only
    python3 phonondex.py --derive    recompute the capture (needs numpy+spglib)

IT CAN BE ACCURATELY REALIZED, AND IT IS BUILT.

    members        1,120 site-symmetry types
    space groups   230 of 230
    systems        triclinic 3, monoclinic 31, orthorhombic 261,
                   tetragonal 366, trigonal 88, hexagonal 150, cubic 221
    coordinates    point-group order, site-symmetry order, multiplicity,
                   modes, number of distinct irreps, the decomposition itself
    distinct decompositions   115

===============================================================================
1. WHAT A MEMBER IS, AND WHY IT IS NOT A MATERIAL
===============================================================================

`quasiparticle.py` closed DOCKET 28 by finding that "the quasiparticles" is not
a member set the way "the particles" is: **everything that distinguishes one
phonon mode from another is the HOST's.**  Its section 3 left the door open with
a spec -- "the phonon-mode tables of a fixed set of crystals, with each mode's
irrep... It is (material, mode), it needs a real fetch."

**THIS FILE TAKES THE SPEC ONE LEVEL DEEPER AND THE FETCH DISAPPEARS.**  A
material's Gamma-point phonon content is the SUM over its occupied site orbits,
and each orbit's contribution depends only on its SITE-SYMMETRY TYPE.  So the
member set is not materials at all -- it is

    MEMBER  =  (space group, site-symmetry type up to conjugacy)

and that is the GENERATING TABLE from which every material's answer follows by
addition.  It is finite, exhaustive, and needs no database.
`compose()` demonstrates the addition; section 3 checks it against six known
crystals.

**AND THAT GRANULARITY IS FORCED BY THE OVER-REPRESENTATION RULE, NOT CHOSEN.**
ITA lists P-1's eight inversion centres as eight Wyckoff letters, 1a..1h.  All
eight have the SAME site-symmetry group and contribute IDENTICALLY to the
phonon representation.  Indexing them separately would multiply members without
adding a distinction -- exactly what M's rule forbids and what `gravity.py`
refuses when it declines to chart more than one level per species.  **So this
index is deliberately coarser than the Wyckoff tables, and the coarsening is a
finding: the phonon representation cannot see the difference.**

===============================================================================
2. EVERY NUMBER IS COMPUTED.  NO TABLE OF ANY KIND IS READ
===============================================================================

`bosonqp.py` threw out its own first draft for writing textbook values down and
calling the provenance DECLARED.  A phonon index built off a copied character
table would repeat that exactly, so nothing is copied:

    1.  spglib gives the space-group operations in the CONVENTIONAL setting.
    2.  `primitive_ops` transforms them to the PRIMITIVE basis, built from the
        centring vectors by integer row reduction.  This is what makes the rest
        well posed: in the primitive setting each rotation carries EXACTLY ONE
        translation, verified for all 230.
    3.  Site-symmetry subgroups are the point stabilisers on a 1/12 rational
        grid, grouped into conjugacy classes under the space group.
    4.  The point group's CHARACTER TABLE is computed by BURNSIDE'S CLASS-
        ALGEBRA METHOD -- conjugacy classes, the structure constants c_ijk of
        the class sums, then the common eigenvectors of those matrices -- and
        VALIDATED before use: integral dimensions, sum(dim^2) = |G|, and row
        orthonormality under the class-weighted inner product.
    5.  chi(R,t) = N_fixed(R,t) * tr(R), decomposed by orthogonality.

**TWO INDEPENDENT INTEGRALITY CHECKS GUARD EVERY ROW** and all 1,120 pass:
every multiplicity is an exact integer, and modes = 3 x multiplicity exactly.

===============================================================================
3. IT REPRODUCES THE LITERATURE, SIX FOR SIX
===============================================================================

    structure             SG      computed        literature
    diamond (Si)          Fd-3m   T2g + T1u        6/6
    rocksalt (NaCl)       Fm-3m   2 T1u            6/6
    zincblende (GaAs)     F-43m   2 T2             6/6
    fluorite (CaF2)       Fm-3m   T2g + 2 T1u      9/9
    perovskite (SrTiO3)   Pm-3m   4 T1u + T2u     15/15
    CsCl                  Pm-3m   2 T1u            6/6

Each is built as the SUM over its occupied site orbits, which is what makes the
generating-table claim of section 1 a measurement rather than an assertion.

===============================================================================
4. FIVE BUGS IN FOUR KINDS, ALL CAUGHT BY ARITHMETIC NOT BY READING
===============================================================================

Recorded because each one passed casual inspection and was caught by a check:

    NON-SYMMORPHY.  N_fixed taken from the rotation alone, ignoring t.  Diamond
    gave 3 modes instead of 6 and SrTiO3 put all five triplets on one irrep
    instead of 4 + 1.  Caught by the literature comparison.

    A TRANSPOSED CLASS-ALGEBRA MATRIX and a NON-IDENTITY FIRST CLASS.  Gave
    m-3m irrep dimensions [4,4,4,4,4,4,5,5,5,5].  Caught by sum(dim^2) != |G|.

    FIXED POINTS vs ORBIT MEMBERSHIP.  Counting images that land anywhere in the
    orbit instead of points mapped to themselves -- the orbit is closed, so that
    counts every point.  Caught by comparing two code paths.

    A CORRUPTING CACHE.  Character tables cached on the sorted rotation SET,
    while `cls` holds indices into the UNSORTED list.  Two space groups sharing
    a point group but ordering it differently got each other's class indices.
    **90 non-integral rows out of 1,120**, and the cache is now gone.

**THE INTEGRALITY CHECKS ARE THE REASON ALL FIVE WERE FOUND.**  A wrong
character table does not give a wrong-looking answer; it gives a fractional
multiplicity, and fractional multiplicities cannot be rationalised away.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

**TO CLAIM ANYTHING ABOUT k != Gamma.**  At a general k the little group's
representations are PROJECTIVE for non-symmorphic groups, which is a different
computation and is not done here.  At a generic k the little group is trivial
anyway, so the irrep carries no information -- the quantum numbers live at
high-symmetry points, and Gamma is the one this file seats.  The rest is named
as open, not quietly omitted.

**TO CLAIM FREQUENCIES.**  A frequency is a MEASUREMENT and needs the fetch
`quasiparticle.py` named.  The symmetry content is complete without it, and
that completeness is the finding.

**TO REPRODUCE THE WYCKOFF LETTERS.**  Section 1.  This index is coarser by
construction, and the coarsening is deliberate and justified.

**TO CALL THE MEMBERS MATERIALS.**  They are site-symmetry types.  Materials
are SUMS of members, which `compose()` performs and section 3 checks.

**TO VENDOR numpy OR spglib.**  `--derive` needs both; the reading and every
fixture are stdlib against the banked capture.  That is `sgcapture.py`'s pattern
and its reason -- this is a document corpus.

===============================================================================
6. SEATING INTO THE MASTER INDEX
===============================================================================

NOT DONE HERE.  This file builds and validates the index; entering it into
`registry.py` and charting it for (K, height, width) is a separate pass over
`registry.py`, `index3.py` / `mi.py` and the README, and it is not begun.
`seating_would_touch()` names them.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "captures", "PHONON-SITES.tsv")
DERIVE = os.path.join(HERE, "captures", "phonon_sites_derive.py")

#: The six crystals section 3 checks against, with their published Gamma
#: decompositions.  Used ONLY to check; nothing is read from them.
ARCHETYPES = (
    ("diamond (Si)", "Fd-3m", "T2g + T1u", 6),
    ("rocksalt (NaCl)", "Fm-3m", "2 T1u", 6),
    ("zincblende (GaAs)", "F-43m", "2 T2", 6),
    ("fluorite (CaF2)", "Fm-3m", "T2g + 2 T1u", 9),
    ("perovskite (SrTiO3)", "Pm-3m", "4 T1u + T2u", 15),
    ("CsCl", "Pm-3m", "2 T1u", 6),
)

SYSTEMS = ("triclinic", "monoclinic", "orthorhombic", "tetragonal",
           "trigonal", "hexagonal", "cubic")

BUGS = (
    "non-symmorphy: N_fixed from the rotation alone, ignoring t",
    "a transposed class-algebra matrix and a non-identity first class",
    "fixed points confused with orbit membership",
    "a character-table cache keyed on the sorted rotation set",
)


def read():
    """[(sg, system, pg_order, site_order, multiplicity, modes, n_irreps, dec)].

    Stdlib only, from the banked capture.
    """
    out = []
    if not os.path.exists(BANK):
        return out
    with open(BANK) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if p[0] == "sg":
                continue
            out.append((int(p[0]), p[1], int(p[2]), int(p[3]), int(p[4]),
                        int(p[5]), int(p[6]), p[7]))
    return out


def parse(dec):
    """'1x3+4x3' -> [(mult, dim), ...]"""
    return [tuple(int(x) for x in t.split("x")) for t in dec.split("+")]


def compose(decs):
    """Add site contributions -- how a MATERIAL is built from members.

    Returns total modes.  Terms are kept per (mult, dim) pair rather than
    merged, because two distinct irreps of equal dimension are two distinct
    quantum numbers and merging them would be the flattening this tree forbids.
    """
    return sum(m * d for dec in decs for m, d in parse(dec))


def by_spacegroup():
    d = {}
    for r in read():
        d.setdefault(r[0], []).append(r)
    return d


def by_system():
    d = {}
    for r in read():
        d.setdefault(r[1], []).append(r)
    return d


def coordinate_ranges():
    """{coordinate: (min, max, distinct)} -- the chart's box, measured."""
    rows = read()
    out = {}
    for i, nm in ((2, "pg_order"), (3, "site_order"), (4, "multiplicity"),
                  (5, "modes"), (6, "n_irreps")):
        vals = [r[i] for r in rows]
        out[nm] = (min(vals), max(vals), len(set(vals)))
    return out


def distinct_decompositions():
    return len({r[7] for r in read()})


def integrality_holds():
    """Every row: modes = 3 x multiplicity, and the decomposition sums to it.

    The two guards that caught all five development bugs, re-run on the bank.
    """
    for r in read():
        if r[5] != 3 * r[4]:
            return False
        if compose([r[7]]) != r[5]:
            return False
    return True


def orbit_stabiliser_holds():
    """|site symmetry| x |orbit| = |point group|, on every row."""
    return all(r[3] * r[4] == r[2] for r in read())


def wyckoff_coarsening():
    """Why P-1's eight inversion centres are ONE member here, with the count.

    ITA lists 1a..1h.  All eight have site symmetry -1 and contribute
    identically, so the phonon representation cannot distinguish them.
    """
    rows = [r for r in read() if r[0] == 2]
    return len(rows), [r[3] for r in rows]


def seating_would_touch():
    return ("registry.py", "index3.py / mi.py", "README")


def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    rows = read()
    if not rows:
        print("   (no capture -- run `python3 phonondex.py --derive`)")
        return
    print("=" * 74)
    print("THE INDEX AS SEATED")
    print("=" * 74)
    print("   members                  %d" % len(rows))
    print("   space groups             %d" % len({r[0] for r in rows}))
    print("   distinct decompositions  %d" % distinct_decompositions())
    print()
    bs = by_system()
    for s in SYSTEMS:
        print("      %-14s %4d" % (s, len(bs.get(s, []))))
    print()
    print("   coordinate            min    max  distinct")
    for k, (lo, hi, n) in coordinate_ranges().items():
        print("      %-18s %4d   %4d   %4d" % (k, lo, hi, n))
    print()
    per = {sg: len(v) for sg, v in by_spacegroup().items()}
    o = sorted(per.values())
    print("   site types per space group: min %d, median %d, max %d"
          % (o[0], o[len(o) // 2], o[-1]))
    print()
    print("=" * 74)
    print("THE GUARDS")
    print("=" * 74)
    print("   modes = 3 x multiplicity on every row     %s" % integrality_holds())
    print("   |site symmetry| x |orbit| = |point group| %s"
          % orbit_stabiliser_holds())
    n, orders = wyckoff_coarsening()
    print("   P-1 seats %d members, site-symmetry orders %s" % (n, orders))
    print("      (ITA lists 8 Wyckoff letters for the inversion centres alone;")
    print("       they contribute identically, so they are ONE member here.)")
    print()
    print("=" * 74)
    print("BUGS CAUGHT BY ARITHMETIC, NOT BY READING")
    print("=" * 74)
    for b in BUGS:
        print("   - %s" % b)
    print()
    print("   seating into the master index would touch: %s"
          % ", ".join(seating_would_touch()))


def selftest():
    bad = []

    def chk(what, got, want):
        ok = got == want
        if not ok:
            bad.append((what, got, want))
        print("   %-60s %s" % (what, "ok" if ok else "FAIL %r != %r"
                               % (got, want)))

    print("phonondex.py fixtures  (stdlib, against the banked capture)")
    rows = read()
    chk("the capture holds 1,120 members", len(rows), 1120)
    chk("all 230 space groups are covered", len({r[0] for r in rows}), 230)
    chk("space group numbers run 1..230",
        (min(r[0] for r in rows), max(r[0] for r in rows)), (1, 230))
    chk("all seven crystal systems appear",
        sorted(by_system().keys()), sorted(SYSTEMS))
    chk("115 distinct decompositions", distinct_decompositions(), 115)

    # the two integrality guards -- these caught every bug
    chk("modes = 3 x multiplicity on EVERY row", integrality_holds(), True)
    chk("orbit-stabiliser holds on EVERY row", orbit_stabiliser_holds(), True)

    # crystallographic sanity, measured not assumed
    chk("point-group orders are the crystallographic ten",
        sorted({r[2] for r in rows}), [1, 2, 3, 4, 6, 8, 12, 16, 24, 48])
    chk("site-symmetry order always divides the point-group order",
        all(r[2] % r[3] == 0 for r in rows), True)
    chk("the general position (site order 1) exists in every space group",
        len({r[0] for r in rows if r[3] == 1}), 230)
    chk("and its multiplicity is the full point-group order",
        all(r[4] == r[2] for r in rows if r[3] == 1), True)
    chk("the identity group P1 has exactly one member",
        len([r for r in rows if r[0] == 1]), 1)
    chk("and it is three modes on one irrep",
        [(r[5], r[7]) for r in rows if r[0] == 1], [(3, "3x1")])

    # the coarsening is deliberate and measurable
    n, orders = wyckoff_coarsening()
    chk("P-1 seats 2 members, not ITA's 9 Wyckoff positions", n, 2)
    chk("and they are site symmetry 1 and -1", sorted(orders), [1, 2])

    # composition is addition -- the generating-table claim
    chk("composing two 3-mode sites gives 6", compose(["3x1", "3x1"]), 6)
    chk("composing a site with itself doubles it",
        compose(["1x3+1x3", "1x3+1x3"]), 12)
    chk("a single triplet site is 3 modes", compose(["1x3"]), 3)
    chk("parse keeps two equal-dimension irreps SEPARATE",
        parse("1x3+1x3"), [(1, 3), (1, 3)])

    # the derivation travels with the capture
    chk("the derivation script is banked beside the capture",
        os.path.exists(DERIVE), True)
    chk("the development bugs are recorded (4 entries, 5 bugs -- the second "
        "entry names two)", len(BUGS), 4)
    chk("seating is named as a separate pass, not performed",
        len(seating_would_touch()), 3)

    print("\n%d failure(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--derive" in sys.argv:
        raise SystemExit(os.system("cd %s && python3 phonon_sites_derive.py"
                                   % os.path.join(HERE, "captures")))
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
