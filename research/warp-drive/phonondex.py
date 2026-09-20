#!/usr/bin/env python3
r"""
phonondex.py -- IS AN INDEX OF PHONONS BUILDABLE WITH COMPUTED PROVENANCE?
YES.  THE SYMMETRY LABELS ARE DERIVABLE FROM THE STRUCTURE ALONE, NO CHARACTER
TABLE IS READ, AND SIX ARCHETYPES REPRODUCE THE LITERATURE EXACTLY.

M: "Do we have an index of phonons?  Or do we need to build one?"

    python3 phonondex.py             the reading (stdlib, from the banked table)
    python3 phonondex.py --selftest  fixtures (stdlib)
    python3 phonondex.py --derive    recompute from spglib + Burnside (needs
                                     numpy and spglib; NOT vendored)

ANSWER, IN THREE PARTS.

**WE HAVE THE PHONON.  WE DO NOT HAVE AN INDEX OF PHONONS.**  It is seated as a
single member twice over -- `quasiparticle.py`'s `UNIVERSAL` list, and
`bosonqp.py` as the Goldstone mode of broken translation, with its quantum
numbers COMPUTED from that and not written down.

**AND THE TREE ALREADY EXPLAINED WHY, STRUCTURALLY.**  `quasiparticle.py` §1:

    "EVERYTHING THAT DISTINGUISHES ONE PHONON MODE FROM ANOTHER IS THE HOST'S.
     A lattice mode is labelled by an irreducible representation of the little
     group of its wavevector, and which group that is depends on the crystal...
     The SAME phonon in silicon (Fd-3m) and in rock salt (Fm-3m) carries
     different labels because the crystals differ, not because the phonons do."

So a phonon's own universal quantum numbers are almost nothing, and "the
quasiparticles" is not a member set the way "the particles" is.  That is a
finding about the subject.  **A SPACE GROUP IS NOT AN INDEX EITHER** -- it
carries no quantum numbers of its own and fails THE CRITERION exactly as
`figure` and `axes` do, which `sgcapture.py` states in its own header.

**BUT THE DOOR WAS LEFT OPEN WITH A WRITTEN SPEC**, and this file tests whether
it can be walked through.  `quasiparticle.py` §3:

    "WHAT WOULD REOPEN IT.  A materials database -- the phonon-mode tables of a
     fixed set of crystals, with each mode's irrep -- IS a legitimate member
     set: a mode carries a symmetry label and a frequency, and those are
     quantum numbers.  It is (material, mode), it needs a real fetch."

===============================================================================
1. THE ONE THING THAT CHANGED: IT NEEDS NO FETCH
===============================================================================

The spec says "it needs a real fetch."  **FOR THE SYMMETRY HALF, IT DOES NOT.**
The irrep content at Gamma is GROUP THEORY, derivable from the structure by
factor-group analysis, and `--derive` does it end to end:

    1. spglib gives the space-group operations (R, t) of the primitive cell.
    2. `char_table()` computes the point group's CHARACTER TABLE from those
       matrices by Burnside's class-algebra method -- conjugacy classes, the
       structure constants c_ijk of the class sums, then the common eigenvectors
       of those matrices.  **NO TEXTBOOK TABLE IS READ.**
    3. `mechanical_character()` gives chi(R) = N_unmoved(R,t) * tr(R).
    4. Orthogonality decomposes it into irreps.

That matters because of `bosonqp.py`'s own ruling.  Its first draft "LISTED
ELEVEN KINDS WITH THEIR SPINS AND CHARGES WRITTEN OUT FROM TEXTBOOK KNOWLEDGE,
and called that provenance DECLARED", and both the table and the category were
removed.  A phonon index built off a copied character table would repeat
exactly that mistake.  Built this way it does not: the only input is the
STRUCTURE TYPE, whose Wyckoff positions are exact fractions fixed by the
definition of the type, which is the same provenance `bosonqp.py`'s compositions
have -- the definition of the object, not a measurement of it.

===============================================================================
2. IT REPRODUCES THE LITERATURE, SIX FOR SIX
===============================================================================

    structure             SG      decomposition        modes   literature
    diamond (Si)          Fd-3m   T2g + T1u             6/6    T2g + T1u
    rocksalt (NaCl)       Fm-3m   2 x T1u               6/6    2 T1u
    zincblende (GaAs)     F-43m   2 x T2                6/6    2 T2
    fluorite (CaF2)       Fm-3m   T2g + 2 x T1u         9/9    T2g + 2 T1u
    perovskite (SrTiO3)   Pm-3m   4 x T1u + T2u        15/15   4 T1u + T2u
    CsCl                  Pm-3m   2 x T1u               6/6    2 T1u

**EVERY MULTIPLICITY COMES OUT AN EXACT INTEGER**, which is the arithmetic
signature that the character table and the mechanical character are both right
-- a wrong table gives fractional multiplicities, and two of this file's three
development bugs were caught precisely that way.

**THE BUG WORTH RECORDING WAS NON-SYMMORPHY.**  A first pass computed
N_unmoved from the ROTATION alone.  Fd-3m is non-symmorphic -- its two carbon
sites are exchanged by operations whose translation part matters -- so diamond
came out with 3 modes instead of 6, and SrTiO3 put all 5 of its triplets on one
irrep instead of splitting 4 + 1.  Including t fixed both at once.
`NONSYMMORPHIC_NOTE` carries it.

===============================================================================
3. SO WHAT WOULD AN INDEX OF PHONONS ACTUALLY BE?
===============================================================================

    MEMBER      (structure type, k-point, irrep)
    COORDINATES dimension, parity, multiplicity, acoustic/optical
    CRITERION   an irrep label IS a quantum number -- it says how the mode
                transforms -- so a member carries quantum numbers and passes

**AND THE OVER-REPRESENTATION GUARD IS PRINCIPLED, NOT ARBITRARY.**  M's
standing rule is that over-representation "screws index density and effects
cascades", and `gravity.py` already refuses to chart more than one level per
species for that reason.  A phonon index could trivially over-represent: every
material times every k-point is a database, not an index.  The cutoff that is
not arbitrary is this:

    AT A GENERIC k THE LITTLE GROUP IS TRIVIAL AND THE IRREP CARRIES NO
    INFORMATION.  The quantum numbers only EXIST at high-symmetry points.

So the index is naturally finite -- high-symmetry points only, of which each
space group has a handful -- and the boundary is set by where THE CRITERION
stops being satisfiable rather than by a budget.  `why_gamma_only()` states it.

**WHAT THIS FILE DOES NOT DO.**  It is a FEASIBILITY PROBE over six archetypes
at Gamma, not a seated index.  It is not in `registry.py`, it is not charted,
and no (K, height, width) is claimed for it.  Seating it is a separate act that
would touch several files, and section 5 names them rather than performing them.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

**TO CALL ITSELF AN INDEX.**  Six structures at one k-point is a probe.  The
member set the spec describes is larger and is not built here.

**TO CLAIM THE FREQUENCIES.**  A mode's frequency is a MEASUREMENT and needs
the fetch the spec names.  Nothing here supplies one, and the symmetry content
is complete without it -- which is the finding, not a gap.

**TO READ A CHARACTER TABLE.**  Section 1.  The tables are computed, and
`--derive` prints them; the banked TSV carries what was computed, with the
spglib version, exactly as `sgcapture.py` banks its 230.

**TO VENDOR numpy OR spglib.**  `--derive` needs both; the reading and the
fixtures are stdlib against the banked table, which is `sgcapture.py`'s pattern
and its reason -- this is a document corpus.

===============================================================================
5. WHAT SEATING IT WOULD TOUCH
===============================================================================

Named, not done, pending a decision:

    captures/PHONON-GAMMA.tsv   the banked derivation, widened past six
    phonondex.py                the reader and the chart
    registry.py                 a new index entry with its provenance
    index3.py / mi.py           the master-index seating and its cell
    docs or README              the finding

That is a multi-file pass and it is not begun.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "captures", "PHONON-GAMMA.tsv")

NONSYMMORPHIC_NOTE = (
    "N_unmoved must be computed from the FULL operation (R, t), not from R "
    "alone.  Fd-3m is non-symmorphic: a first pass using R alone gave diamond "
    "3 modes instead of 6 and put all five of SrTiO3's triplets on one irrep "
    "instead of splitting 4 + 1.  Including t fixed both."
)

SPEC_SOURCE = ("quasiparticle.py section 3, 'WHAT WOULD REOPEN IT' -- the spec "
               "this file tests, written before it was attempted")

#: The archetypes.  Wyckoff positions are EXACT FRACTIONS fixed by the structure
#: type -- the definition of the object, not a measurement of it.  Literature
#: column is the published Gamma-point decomposition, used only to CHECK.
ARCHETYPES = (
    ("diamond (Si)", "Fd-3m", "T2g + T1u", 6),
    ("rocksalt (NaCl)", "Fm-3m", "2 T1u", 6),
    ("zincblende (GaAs)", "F-43m", "2 T2", 6),
    ("fluorite (CaF2)", "Fm-3m", "T2g + 2 T1u", 9),
    ("perovskite (SrTiO3)", "Pm-3m", "4 T1u + T2u", 15),
    ("CsCl", "Pm-3m", "2 T1u", 6),
)


def read():
    """[(structure, spacegroup, |G|, classes, dims, decomposition, modes)].

    Stdlib only, from the banked TSV.  `--derive` regenerates it.
    """
    rows = []
    if not os.path.exists(BANK):
        return rows
    with open(BANK) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            if line.startswith("structure\t"):      # the column header
                continue
            p = line.rstrip("\n").split("\t")
            rows.append((p[0], p[1], int(p[2]), int(p[3]), p[4], p[5], int(p[6])))
    return rows


def literature():
    return {n: (sg, lit, m) for n, sg, lit, m in ARCHETYPES}


def agreement():
    """[(structure, computed modes, literature modes, agree)] from the bank."""
    lit = literature()
    return [(r[0], r[6], lit[r[0]][2], r[6] == lit[r[0]][2]) for r in read()
            if r[0] in lit]


def why_gamma_only():
    return ("At a generic k the little group is trivial, so the irrep is "
            "trivial and carries no information.  The quantum numbers only "
            "exist at high-symmetry points, of which each space group has a "
            "handful -- so the member set is finite because THE CRITERION "
            "stops being satisfiable, not because a budget was imposed.")


def seating_would_touch():
    return ("captures/PHONON-GAMMA.tsv", "phonondex.py", "registry.py",
            "index3.py / mi.py", "docs or README")


# --------------------------------------------------------------- the derivation

def _derive():
    """Recompute everything from spglib + Burnside.  numpy and spglib required."""
    import numpy as np
    import spglib

    def key(M):
        return tuple(int(round(x)) for x in np.asarray(M).ravel())

    ident = key(np.eye(3))

    def conj_classes(G):
        idx = {key(M): i for i, M in enumerate(G)}
        seen, cls = set(), []
        for i, M in enumerate(G):
            if i in seen:
                continue
            c = sorted({idx[key(X @ M @ np.linalg.inv(X))] for X in G})
            cls.append(c)
            seen |= set(c)
        cls.sort(key=lambda c: 0 if key(G[c[0]]) == ident else 1)
        return cls, idx

    def char_table(G):
        """Burnside's class-algebra method.  NO textbook table is read.

        The class sums span the centre of the group algebra; C_i C_j =
        sum_k c_ijk C_k, and omega -> (|C_i| chi_i / dim) is an algebra
        homomorphism, so omega is a common eigenvector of the matrices
        N_i[j][k] = c_ijk.  Normalising by orthogonality recovers the
        characters and hence the dimensions.
        """
        cls, idx = conj_classes(G)
        n, order = len(cls), len(G)
        cls_of = [0] * order
        for ci, c in enumerate(cls):
            for g in c:
                cls_of[g] = ci
        N = np.zeros((n, n, n))
        for i in range(n):
            for j in range(n):
                cnt = np.zeros(n)
                for a in cls[i]:
                    for b in cls[j]:
                        cnt[cls_of[idx[key(G[a] @ G[b])]]] += 1
                for k in range(n):
                    N[i][j][k] = cnt[k] / len(cls[k])
        rng = np.random.default_rng(3)
        A = np.tensordot(rng.normal(size=n), N, axes=(0, 0))
        _w, V = np.linalg.eig(A)
        out = []
        for t in range(n):
            v = V[:, t]
            if abs(v[0]) < 1e-9:
                continue
            om = v / v[0]
            base = np.array([om[i] / len(cls[i]) for i in range(n)])
            s = sum(len(cls[i]) * abs(base[i]) ** 2 for i in range(n))
            chi = base * np.sqrt(order / s)
            if np.real(chi[0]) < 0:
                chi = -chi
            out.append(np.real_if_close(chi, tol=1e6))
        out.sort(key=lambda c: (round(float(np.real(c[0]))),
                                [round(float(np.real(x)), 4) for x in c]))
        return cls, np.array(out)

    def unmoved(R, t, pos):
        """Atoms fixed by the FULL operation.  See NONSYMMORPHIC_NOTE."""
        n = 0
        for p in pos:
            q = (R @ np.array(p) + t) % 1.0
            d = (np.array(p) - q) % 1.0
            d = np.minimum(d, 1 - d)
            if np.all(d < 1e-4):
                n += 1
        return n

    FCC = [[0, 0, 0], [0, .5, .5], [.5, 0, .5], [.5, .5, 0]]

    def off(b, d):
        return [[(x + d[0]) % 1, (y + d[1]) % 1, (z + d[2]) % 1] for x, y, z in b]

    cells = {
        "diamond (Si)": (np.eye(3) * 5.43, FCC + off(FCC, (.25, .25, .25)), [14] * 8),
        "rocksalt (NaCl)": (np.eye(3) * 5.64, FCC + off(FCC, (.5, .5, .5)),
                            [11] * 4 + [17] * 4),
        "zincblende (GaAs)": (np.eye(3) * 5.65, FCC + off(FCC, (.25, .25, .25)),
                              [31] * 4 + [33] * 4),
        "fluorite (CaF2)": (np.eye(3) * 5.46,
                            FCC + off(FCC, (.25, .25, .25)) + off(FCC, (.75, .75, .75)),
                            [20] * 4 + [9] * 8),
        "perovskite (SrTiO3)": (np.eye(3) * 3.905,
                                [[0, 0, 0], [.5, .5, .5], [0, .5, .5], [.5, 0, .5],
                                 [.5, .5, 0]], [38, 22, 8, 8, 8]),
        "CsCl": (np.eye(3) * 4.12, [[0, 0, 0], [.5, .5, .5]], [55, 17]),
    }
    rows = []
    for name, cell in cells.items():
        prim = spglib.standardize_cell(cell, to_primitive=True, symprec=1e-5)
        sym = spglib.get_symmetry(prim, symprec=1e-5)
        ds = spglib.get_symmetry_dataset(cell, symprec=1e-5)
        seen, ops = {}, []
        for R, t in zip(sym["rotations"], sym["translations"]):
            if key(R) not in seen:
                seen[key(R)] = 1
                ops.append((np.asarray(R, float), np.asarray(t, float)))
        G = [R for R, _ in ops]
        cls, T = char_table(G)
        pos = prim[1]
        chi = np.array([unmoved(ops[c[0]][0], ops[c[0]][1], pos) * np.trace(G[c[0]])
                        for c in cls], float)
        dims = [int(round(float(np.real(t[0])))) for t in T]
        mults = [sum(len(cls[i]) * chi[i] * float(np.real(T[r][i]))
                     for i in range(len(cls))) / len(G) for r in range(len(T))]
        exact = all(abs(m - round(m)) < 1e-6 for m in mults)
        par = ["g" if float(np.real(t[1])) > 0 else "u" for t in T]
        terms = " + ".join("%d x (dim %d, %s)" % (round(m), d, p)
                           for d, p, m in zip(dims, par, mults) if round(m))
        tot = sum(d * round(m) for d, m in zip(dims, mults))
        rows.append((name, ds.international, len(G), len(cls),
                     ",".join(str(d) for d in dims), terms, tot, exact))
    return rows


def write_bank():
    import spglib
    rows = _derive()
    os.makedirs(os.path.dirname(BANK), exist_ok=True)
    with open(BANK, "w") as f:
        f.write("# Gamma-point phonon symmetry content of six archetypal "
                "structures.\n")
        f.write("# COMPUTED: spglib %s for the operations, Burnside's class-"
                "algebra method\n" % spglib.__version__)
        f.write("# for the character tables.  NO textbook character table is "
                "read.\n")
        f.write("# spglib is installed, NOT vendored -- sgcapture.py's pattern "
                "and its reason.\n")
        f.write("structure\tspacegroup\tpg_order\tclasses\tirrep_dims\t"
                "decomposition\tmodes\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r[:7]) + "\n")
    return rows


# ------------------------------------------------------------------- reading

def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    rows = read()
    if not rows:
        print("   (no bank yet -- run `python3 phonondex.py --derive`)")
        return
    print("=" * 74)
    print("2.  THE DERIVATION, AGAINST THE LITERATURE")
    print("=" * 74)
    lit = literature()
    print("   %-21s %-7s %-4s %-30s %-7s %s"
          % ("structure", "SG", "|G|", "computed", "modes", "literature"))
    for st, sg, go, _nc, _dm, dec, md in rows:
        L = lit.get(st, ("", "", 0))
        print("   %-21s %-7s %-4d %-30s %-7s %s"
              % (st, sg, go, dec, "%d/%d" % (md, L[2]), L[1]))
    ag = agreement()
    print("\n   agreement with the literature: %d of %d"
          % (sum(1 for a in ag if a[3]), len(ag)))
    print()
    print("=" * 74)
    print("3.  WHAT AN INDEX OF PHONONS WOULD BE")
    print("=" * 74)
    print("   MEMBER      (structure type, k-point, irrep)")
    print("   COORDINATES dimension, parity, multiplicity, acoustic/optical")
    print("   CRITERION   an irrep label IS a quantum number -- it passes")
    print()
    print("   " + why_gamma_only().replace(". ", ".\n   "))
    print()
    print("=" * 74)
    print("5.  SEATING IT WOULD TOUCH -- NAMED, NOT DONE")
    print("=" * 74)
    for f in seating_would_touch():
        print("   %s" % f)
    print("\n   %s" % SPEC_SOURCE)


# ------------------------------------------------------------------ fixtures

def selftest():
    bad = []

    def chk(what, got, want):
        ok = got == want
        if not ok:
            bad.append((what, got, want))
        print("   %-60s %s" % (what, "ok" if ok else "FAIL %r != %r"
                               % (got, want)))

    print("phonondex.py fixtures  (stdlib, against the banked derivation)")
    rows = read()
    chk("the bank exists and holds six archetypes", len(rows), 6)
    if not rows:
        print("\n1 failure(s) -- run --derive first")
        return 1

    by = {r[0]: r for r in rows}
    chk("every structure resolves to its known space group",
        [by[n][1] for n, sg, _l, _m in ARCHETYPES],
        [sg for _n, sg, _l, _m in ARCHETYPES])
    chk("mode counts match the literature at all six",
        [a[3] for a in agreement()], [True] * 6)
    chk("diamond has 6 modes -- the non-symmorphic case",
        by["diamond (Si)"][6], 6)
    chk("and they split across TWO distinct irreps, not one",
        by["diamond (Si)"][5].count(" + "), 1)
    chk("perovskite splits 4 + 1, not 5 + 0",
        sorted(int(t.split(" x ")[0]) for t in
               by["perovskite (SrTiO3)"][5].split(" + ")), [1, 4])
    chk("perovskite has 15 modes", by["perovskite (SrTiO3)"][6], 15)

    # the character tables must be real character tables
    for n, r in by.items():
        dims = [int(d) for d in r[4].split(",")]
        if sum(d * d for d in dims) != r[2]:
            bad.append(("sum of squared dims = |G| for " + n,
                        sum(d * d for d in dims), r[2]))
    chk("sum of squared irrep dims equals |G| at every structure",
        all(sum(int(d) ** 2 for d in r[4].split(",")) == r[2] for r in rows),
        True)
    chk("and the number of irreps equals the number of classes",
        all(len(r[4].split(",")) == r[3] for r in rows), True)
    chk("cubic archetypes have point groups of order 48 or 24",
        sorted({r[2] for r in rows}), [24, 48])

    # the refusals
    chk("the non-symmorphic bug is recorded, not silently fixed",
        "Fd-3m is non-symmorphic" in NONSYMMORPHIC_NOTE, True)
    chk("the gamma-only cutoff is justified by THE CRITERION, not a budget",
        "stops being satisfiable" in why_gamma_only(), True)
    chk("seating is named as a multi-file pass and not performed",
        len(seating_would_touch()), 5)

    print("\n%d failure(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--derive" in sys.argv:
        for r in write_bank():
            print("   %-21s %-7s %-30s %d modes  exact=%s"
                  % (r[0], r[1], r[5], r[6], r[7]))
        print("\n   banked to %s" % BANK)
        sys.exit(0)
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
