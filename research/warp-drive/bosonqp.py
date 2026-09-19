#!/usr/bin/env python3
r"""
bosonqp.py -- THE BOSONIC QUASIPARTICLES, AS A SUBLATTICE OF THE BOSONS.
DOCKET 31.

    python3 bosonqp.py             the reading
    python3 bosonqp.py --selftest  fixtures
    python3 bosonqp.py --prove     the z3 pass (needs `pip install z3-solver`)

===============================================================================
0. M'S RULING, AND WHAT IT CORRECTED
===============================================================================

M: "The universal quantum numbers of the textbook kinds are almost nothing --
but not nothing, which means measurable by the z3 machine checker and thus it
is indexable.  1 - it is a sub index/sublattice of bosons."

    DOCKET 28 WROTE "ALMOST NOTHING" AND TREATED IT AS NOTHING.  That was the
    error.  Two coordinates that put eleven kinds on three cells are a
    measurement with low resolution, and `overlap.py` has a name for the case
    where a coordinate says nothing -- LABEL, at 0.9 or above -- which these
    do not meet.  Low resolution is not no resolution.

    AND THE RULING NAMES THE OBJECT, which is the part DOCKET 28 never found.
    Not "an index of quasiparticles" floating free, but A SUBLATTICE OF THE
    BOSONS -- the quasiparticles placed in the frame the tree's own bosons
    already live in, and the question being whether they sit inside it closed.
    That is a checkable claim about a relation, and it is what this file
    measures.

===============================================================================
1. THE MEMBERS, AND WHY THE FERMIONIC ONES ARE NOT HERE
===============================================================================

One member is a BOSONIC collective excitation.  Eleven of them, each with the
spin and charge every textbook gives it.

    THE LIST IS DECLARED, NOT CAPTURED, and that is the honest weak point of
    this index.  There is no Particle Data Group for quasiparticles --
    DOCKET 28 established that and it still stands -- so `KINDS` is a table
    written from physics rather than read from a file, in the way
    `fundamental.colour_rule()` assigns the colour dimension the PDG table
    does not carry.  Every row carries its reason.  A reader who disputes a
    row disputes one line, not the construction.

    THE FERMIONIC QUASIPARTICLES ARE EXCLUDED BY THE RULING ITSELF, not by
    judgement: a sublattice of the BOSONS cannot contain a fermion.  The
    polaron (a dressed electron, spin 1/2), the spinon and the Bogoliubov
    quasiparticle are named in `FERMIONIC` so the exclusion is visible and so
    nobody reads their absence as an oversight.  They are a different index
    and this file does not build it.

===============================================================================
2. THE COORDINATES COME FROM THE RULING, NOT FROM A SEARCH
===============================================================================

    2J   spin, doubled -- 0 for a scalar mode, 2 for a vector one
    Q3   electric charge in thirds, the same column the quark chart uses

These are exactly the two coordinates the tree's own bosons share: every gauge
boson, the Higgs and all 250 mesons carry a 2J and a Q3, and nothing else is
common to all of them.  So the frame is FORCED by "a sublattice of the bosons"
rather than chosen, which is the reason this chart is not fitted.

    WHAT IS REFUSED.  The gap -- whether the mode is gapless (a Goldstone
    mode: phonon, magnon, phason) or gapped (plasmon, exciton, Cooper pair) --
    is a real, measured, total property and it is NOT charted.  It would raise
    the index from three cells to five.  It was not named by the ruling, and
    reaching for it after seeing that three cells is a small index is exactly
    DOCKET 23's fitted move.  `gap_would_give()` measures the price so the
    refusal is on the record with its cost.

===============================================================================
3. THE FINDING: IT IS A SUBLATTICE, AND IT EXTENDS THE BOSONS BY ONE CELL
===============================================================================

    the tree's bosons on (2J, Q3)    15 cells, and ALREADY a sublattice
    the bosonic quasiparticles        3 cells, and a sublattice
    is the second a SUBSET of the first?   NO
    what lies outside                 (0, -6) -- THE COOPER PAIR
    the union                        16 cells, and STILL a sublattice

THE COOPER PAIR CARRIES CHARGE -2e, AND NOTHING ELSE IN THE INDEX DOES.  Every
meson is charged -1, 0 or +1; every gauge boson likewise.  A charge of two
electron charges on a spin-0 boson is a cell no elementary or composite boson
in this tree reaches, and it is reached by a bound pair of electrons in a
metal.  That is the whole content of the ruling, made exact: the
quasiparticles are a sublattice of the bosons ONLY ONCE THE LATTICE IS
EXTENDED TO HOLD THEM, and the extension is one cell wide.

===============================================================================
4. THE CHANNEL IS NOT THE CONTENT, AND THE PROVER SAYS SO
===============================================================================

The chart lands at K7 -- all five languages close.  DO NOT QUOTE THAT AS A
FINDING.  Three cells in a 2x2 box is a chain, and a chain closes almost
everything by being a chain:

    measured over the tree's own small charts, 91% of six-cell charts and
    75% of four-cell charts already close all five

    and `--prove` puts it beyond a sample: z3 shows that over this box EVERY
    chain is closed under both meet and join, quantified over all 2^|box|
    subsets rather than over the handful this tree happens to hold

So the K7 here is a fact about the size and shape of the chart, not about
quasiparticles.  The sublattice relation in section 3 is the finding; the
channel is recorded and disclaimed.  This is the same shape of caution as
`overlaprule.py` section 3c's arity-2 free pass, and it is stated in the same
place for the same reason -- before anyone reads the number.
"""

import sys

import decomposable as D
import fundamental
import hlaw
import mesons
import mi

SOURCE = (
    "DECLARED from textbook physics, not captured -- there is no particle "
    "table for quasiparticles and DOCKET 28 established that.  Every row of "
    "KINDS carries its own reason.  The BOSON frame it is placed in is read "
    "from the seated fundamental and mesons indexes.",
    (),
)

NAMES = ("2J", "Q3")
ARITY = len(NAMES)

# (name, 2J, Q3, why those two numbers).  DECLARED -- section 1.
KINDS = (
    ("phonon", 0, 0, "quantised lattice vibration; scalar, neutral"),
    ("magnon", 2, 0, "quantised spin wave; carries one unit of spin, neutral"),
    ("plasmon", 0, 0, "collective charge-density oscillation; scalar, and the "
                      "MODE is neutral though the medium is charged"),
    ("exciton (singlet)", 0, 0, "bound electron-hole pair, spins antiparallel; "
                                "neutral because the pair is"),
    ("exciton (triplet)", 2, 0, "the same pair with spins parallel"),
    ("Cooper pair", 0, -6, "two electrons bound in the s-wave singlet: spin 0, "
                           "and CHARGE -2e, which is Q3 = -6"),
    ("polariton", 2, 0, "photon hybridised with a dipolar mode; inherits the "
                        "photon's spin 1"),
    ("roton", 0, 0, "the short-wavelength minimum of the helium-II dispersion; "
                    "scalar, neutral"),
    ("phason", 0, 0, "Goldstone mode of a density wave's phase; scalar, "
                     "neutral"),
    ("amplitude (Higgs) mode", 0, 0, "amplitude oscillation of an order "
                                     "parameter; scalar, neutral"),
    ("magnon-polaron", 2, 0, "hybridised magnon and phonon; spin follows the "
                             "magnon"),
)

# NOT members, and excluded BY THE RULING rather than by judgement: a
# sublattice of the BOSONS cannot hold a fermion.  Section 1.
FERMIONIC = (
    ("polaron", "a dressed electron -- spin 1/2, charge -e"),
    ("spinon", "the spin half of a spin-charge separated electron"),
    ("holon", "the charge half; a boson in some treatments, and the "
              "disagreement is why it is left out rather than argued over"),
    ("Bogoliubov quasiparticle", "a superposition of electron and hole; "
                                 "fermionic"),
)

# The gap, measured and REFUSED as a coordinate -- section 2.  1 = gapped.
GAP = {"phonon": 0, "magnon": 0, "phason": 0, "plasmon": 1,
       "exciton (singlet)": 1, "exciton (triplet)": 1, "Cooper pair": 1,
       "polariton": 1, "roton": 1, "amplitude (Higgs) mode": 1,
       "magnon-polaron": 1}


def rows():
    """[(name, 2J, Q3, why)] -- the eleven."""
    return list(KINDS)


def index():
    """The quasiparticle sublattice, as a cell set."""
    return frozenset((j, q) for _n, j, q, _w in KINDS)


def boson_frame():
    """The cells the tree's OWN bosons occupy on (2J, Q3).

    Read from the seated indexes, never retyped: every integer-spin member of
    `fundamental` and every meson.  This is the lattice the ruling places the
    quasiparticles in.
    """
    B = {(j, q) for _n, _p, j, q, _c, _g in fundamental.rows() if j % 2 == 0}
    B |= {(j, q) for _n, _p, j, _P, _i, q in mesons.rows()}
    return frozenset(B)


def is_sublattice(S):
    """Closed under componentwise min and max?  `decomposable.gen` is the hull
    and a set is a sublattice exactly when it is its own hull."""
    S = frozenset(S)
    return D.gen(S) == S


def relation():
    """The whole of section 3, as one measurement.

    (boson cells, qp cells, boson is a sublattice, qp is a sublattice,
     qp subset of boson, what lies outside, union cells, union is a sublattice)
    """
    B, Q = boson_frame(), index()
    return (len(B), len(Q), is_sublattice(B), is_sublattice(Q), Q <= B,
            sorted(Q - B), len(B | Q), is_sublattice(B | Q))


def outside():
    """[(cell, [the kinds that sit there])] -- what the bosons do not hold."""
    B = boson_frame()
    out = {}
    for n, j, q, _w in KINDS:
        if (j, q) not in B:
            out.setdefault((j, q), []).append(n)
    return [(k, sorted(v)) for k, v in sorted(out.items())]


def gap_would_give():
    """(cells now, cells with the gap appended) -- section 2's refused price."""
    wide = {(j, q, GAP[n]) for n, j, q, _w in KINDS}
    return (len(index()), len(wide))


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def is_chain(X=None):
    """Width 1 -- every pair comparable.  Section 4's caution."""
    return mi.cell(index() if X is None else X)[2] == 1


def prove():
    """z3, over EVERY subset of the chart's own box -- section 4.

    THE PROVER IS POINTED AT THIS FILE'S OWN RESULT, not in support of it.
    The claim is that a chain is closed under meet and join whatever it
    contains, which is what makes the K7 in section 4 a fact about shape
    rather than about quasiparticles.
    """
    import itertools
    try:
        import z3
    except ImportError:
        return [("z3 is not installed -- pip install z3-solver", None)]

    Q = index()
    Js = sorted({j for j, _q in Q})
    Qs = sorted({q for _j, q in Q})
    box = [(j, q) for j in Js for q in Qs]
    V = {c: z3.Bool("c_%d_%d" % c) for c in box}

    def meet(a, b):
        return (min(a[0], b[0]), min(a[1], b[1]))

    def join(a, b):
        return (max(a[0], b[0]), max(a[1], b[1]))

    comparable = []
    for a, b in itertools.combinations(box, 2):
        comparable.append(z3.Implies(
            z3.And(V[a], V[b]),
            z3.Or(z3.And(a[0] <= b[0], a[1] <= b[1]),
                  z3.And(b[0] <= a[0], b[1] <= a[1]))))
    closed = []
    for a, b in itertools.combinations(box, 2):
        closed.append(z3.Implies(z3.And(V[a], V[b]),
                                 z3.And(V[meet(a, b)], V[join(a, b)])))

    out = []
    # 1. the claim: over this box, EVERY chain is a sublattice
    s = z3.Solver()
    s.add(z3.Not(z3.Implies(z3.And(*comparable), z3.And(*closed))))
    out.append(("every chain in the box is closed under meet and join",
                s.check() == z3.unsat))
    # 2. the VACUITY GUARD -- a chain of three must actually exist in the box,
    #    or the implication above is empty and unsat proves nothing.
    g = z3.Solver()
    g.add(z3.And(*comparable))
    g.add(z3.Sum([z3.If(V[c], 1, 0) for c in box]) == 3)
    out.append(("and a three-element chain EXISTS here, so that is not vacuous",
                g.check() == z3.sat))
    # 3. the contrast: NOT every subset is closed, so the box is not trivial
    t = z3.Solver()
    t.add(z3.Not(z3.And(*closed)))
    out.append(("while some subset of the box is NOT closed -- the box is not "
                "trivially a lattice", t.check() == z3.sat))
    return out


def report():
    X = index()
    print("=" * 74)
    print("THE BOSONIC QUASIPARTICLES -- a sublattice of the bosons.  DOCKET 31")
    print("=" * 74)
    print()
    print("M: \"almost nothing -- but not nothing ... it is a sub index/")
    print("sublattice of bosons.\"")
    print()
    print("1. THE MEMBERS: %d bosonic collective excitations.  DECLARED." % len(KINDS))
    print("   %-24s %-4s %-5s %s" % ("kind", "2J", "Q3", "why"))
    for n, j, q, w in KINDS:
        print("   %-24s %-4d %-5d %s" % (n, j, q, w))
    print()
    print("   EXCLUDED BY THE RULING -- a sublattice of the bosons holds no")
    print("   fermion:")
    for n, w in FERMIONIC:
        print("     %-26s %s" % (n, w))
    print()
    nb, nq, bsub, qsub, subset, out, nu, usub = relation()
    print("2. THE FINDING.")
    print("   the tree's bosons on (2J, Q3)   %2d cells, sublattice: %s"
          % (nb, bsub))
    print("   the bosonic quasiparticles      %2d cells, sublattice: %s"
          % (nq, qsub))
    print("   is the second inside the first? %s" % subset)
    print("   what lies outside               %s" % out)
    for k, ns in outside():
        print("     %s  %s" % (k, ", ".join(ns)))
    print("   the union                       %2d cells, sublattice: %s"
          % (nu, usub))
    print()
    print("   THE COOPER PAIR CARRIES CHARGE -2e AND NOTHING ELSE HERE DOES.")
    print("   Every meson and every gauge boson is charged -1, 0 or +1.  The")
    print("   quasiparticles are a sublattice of the bosons only once the")
    print("   lattice is EXTENDED to hold them, and it is one cell wide.")
    print()
    print("3. THE CHANNEL, RECORDED AND DISCLAIMED.")
    print("   cells %d   cell %s   closes %s"
          % (len(X), cell(), ", ".join(closers()) or "NOTHING"))
    print("   chain (width 1): %s" % is_chain())
    print("   DO NOT QUOTE THE K7.  Three cells in a 2x2 box is a chain, and a")
    print("   chain closes almost everything by being one.  --prove shows it")
    print("   over every subset of the box rather than over a sample.")
    print()
    now, wide = gap_would_give()
    print("4. THE GAP, REFUSED AS A COORDINATE.")
    print("   gapless (Goldstone): %s"
          % ", ".join(n for n in GAP if GAP[n] == 0))
    print("   appending it would take %d cells to %d." % (now, wide))
    print("   It was not named by the ruling, and reaching for it after seeing")
    print("   three cells is DOCKET 23's fitted move.  Recorded, not adopted.")
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    chk("eleven bosonic kinds", len(KINDS), 11)
    chk("every one carries a reason, not just numbers",
        [n for n, _j, _q, w in KINDS if not w.strip()], [])
    chk("every one is a BOSON -- 2J even, no exception",
        sorted({j % 2 for _n, j, _q, _w in KINDS}), [0])
    chk("four fermionic kinds are named as excluded, not omitted",
        len(FERMIONIC), 4)
    chk("and the gap is declared for every member",
        sorted(GAP) == sorted(n for n, _j, _q, _w in KINDS), True)

    # the individual physics, one line each so a dispute is one line
    by = {n: (j, q) for n, j, q, _w in KINDS}
    chk("the phonon is a neutral scalar", by["phonon"], (0, 0))
    chk("the magnon carries one unit of spin", by["magnon"], (2, 0))
    chk("THE COOPER PAIR CARRIES CHARGE -2e -- Q3 = -6",
        by["Cooper pair"], (0, -6))
    chk("and it is the only member that is charged at all",
        sorted(n for n, _j, q, _w in KINDS if q != 0), ["Cooper pair"])

    # section 3, the ruling checked
    nb, nq, bsub, qsub, subset, out, nu, usub = relation()
    chk("the tree's own bosons are 15 cells and ALREADY a sublattice",
        (nb, bsub), (15, True))
    chk("THE QUASIPARTICLES ARE A SUBLATTICE -- M's ruling, measured",
        (nq, qsub), (3, True))
    chk("but they are NOT a subset of the bosons", subset, False)
    chk("and what lies outside is exactly the Cooper pair's cell",
        (out, outside()), ([(0, -6)], [((0, -6), ["Cooper pair"])]))
    chk("the union is 16 cells and is STILL a sublattice", (nu, usub),
        (16, True))
    chk("so the extension is exactly one cell wide", nu - nb, 1)

    # section 4, the disclaimer held to
    X = index()
    chk("arity 2", len(next(iter(X))), 2)
    chk("it closes all five -- K7", closers(),
        ["algebra", "geometry", "information", "order", "statistics"])
    chk("AND IT IS A CHAIN, which is why that is not a finding", is_chain(),
        True)
    chk("the file says so before anyone reads the number",
        "DO NOT QUOTE THAT AS A FINDING" in " ".join(__doc__.split()), True)
    import overlap
    chk("no coordinate is a row LABEL -- low resolution is not none",
        [a for a, _d, _n, _r, v in overlap.resolution(X) if v == "LABEL"], [])

    # section 2's refusal
    chk("the gap would raise three cells to five, and is refused",
        gap_would_give(), (3, 5))
    chk("and it is not among the coordinates", "GAP" in NAMES, False)

    print("bosonqp selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--prove" in sys.argv:
        print("z3, over every subset of the chart's own box:")
        good = True
        for lab, r in prove():
            print("  [%s] %s" % ("PROVED" if r else "  XX  " if r is False
                                 else " SKIP ", lab))
            good &= (r is not False)
        sys.exit(0 if good else 1)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
