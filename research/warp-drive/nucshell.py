#!/usr/bin/env python3
r"""
nucshell.py -- THE NUCLEAR SUBSHELL INDEX: the single-particle subshells of the
shell model, to the 126 closure.

    python3 nucshell.py             the reading
    python3 nucshell.py --selftest  fixtures

===============================================================================
0. WHY IT IS A DIFFERENT INDEX AND NOT A RE-CHART
===============================================================================

**THE SENTENCE "EVERY OTHER INDEX SEATED HERE HAS ATOMIC MEMBERS" IS
WITHDRAWN.**  It stood here, it was TRUE WHEN WRITTEN -- registry.py still
records this index as "the exception that proved the old subject too narrow"
-- and it was falsified by two LATER, CORRECT seatings: `nucbands` (DOCKET 35,
2,145 nuclear excited states in magnetic and antimagnetic rotational bands)
and `deformedbands` (DOCKET 36b, 1,907 excited states in two-quasiparticle
rotational bands of deformed odd-odd nuclei).  **BOTH ARE GENUINELY NUCLEAR.**
Neither is a re-chart of this index, and the withdrawal costs section 0
nothing, because what section 0 needs was never nuclear EXCLUSIVITY -- see the
restatement in `member_types()`.

The other seated indexes have ATOMIC members: electrons, subshells of the
electron cloud, transitions between ionisation stages, spectroscopic channels,
Rydberg series, nuclides in charge states.  **THESE MEMBERS ARE NUCLEONS IN A
MEAN FIELD**, which is the distinction the two band indexes do not cross: a
band level is a state of the WHOLE nucleus carrying (2I, parity) at arity 2,
and each of the two shares ZERO members with these 22 subshells.

    NO SEATED INDEX CARRIES A SINGLE-PARTICLE HALF-INTEGER j ANYWHERE.
    `gravity` carries 2Je, which is the whole electron cloud's angular momentum
    for a nuclide-charge state; it is not a single-particle j and its members
    are attached to a Z.  Measured rather than argued: the full-arity
    intersection of this member set with every one of the eight seated indexes
    is EMPTY, and the five (n, l) pairs it shares with `probability` are
    homographs -- an electronic 2s and a nuclear 2s are different objects that
    print the same.

    [THE EMPTINESS CLAUSE IS SUPERSEDED, and `cell_homographs()` records why:
    the tree has grown from those eight seated indexes to 27 registry rows, and
    TEN of them now share full-arity cell tuples with this one.  The
    half-integer-j claim stands -- 2I is a whole-nucleus quantum number, not a
    single-particle j -- and it is homographs, not emptiness, that carry the
    argument.]

So the criterion is met in the strongest way available: not a new chart over
seated members, a new KIND of member.  `n`, `l` and `j` are quantum numbers of
a nucleon in a mean field, which is what the criterion asks for.

===============================================================================
1. THERE ARE TWO BANKED ORDERS AND THEY DISAGREE
===============================================================================

    A   `extracted/archives/restore-point-2-13/nuclear_corridor.py`, `ORD`
    B   `recovered/nuccorr.py`, `ORDER`

**THEY ARE THE SAME TWENTY-TWO SUBSHELLS IN A DIFFERENT SEQUENCE.**  set(A) ==
set(B) is True and A == B is False; they differ at EIGHT of the twenty-two
positions.  Membership is therefore not in question and only the order is.

**THE MAGIC NUMBERS DO NOT DECIDE IT, AND THAT IS THE FIRST FINDING.**  A's own
header calls itself "CORRECTED standard order, capacities verified to close at
2, 8, 20, 28, 50, 82, 126".  The check passes -- and it passes for B as well.
Both orders hit ALL SEVEN closures on cumulative 2j+1, and both total 126.

    THE REASON IS VISIBLE ONCE THE DISAGREEMENTS ARE LISTED: every one of the
    eight lies strictly INSIDE a closed block.  A permutation within a block
    cannot move the cumulative sum at that block's boundary, so the magic
    numbers verify the BLOCK PARTITION and say nothing whatever about the
    sequence inside a block.  `magic_is_null()` runs both and returns the pair.

    A test that passes for both candidates is not evidence for either, and the
    file refuses to quote the closure check as though it were.

**WHAT DOES DECIDE IT IS CORROBORATION, AND IT IS ONE-SIDED.**  Four further
files in this repository carry a subshell sequence:

    recovered/c3.py                  22 of 22 match A       B: 11
    recovered/c4.py                  22 of 22 match A       B: 11
    recovered/corridor_identity.py   22 of 22 match A       B: 11
    method/members/r2-ch16e.py       16 of 16 match A       B: 11   SEATED

The eleven is not corroboration of B: positions 0 to 10 are where A and B
AGREE, so eleven is the length of the common prefix and every file stops
matching B exactly where the two diverge.  **Not one file in the repository
follows B past the point of disagreement**, and one of the four that follow A is
a SEATED MEMBER of The Method -- the strongest source class here.

So membership comes from A and A is the seated order.  **B IS NOT CALLED
FABRICATED OR WRONG.**  It is coherent, it reproduces the magic numbers, and it
is a different shell-model parameterisation; its status is RECOVERED,
UNCORROBORATED and SUPERSEDED, and it is kept because a superseded record is
kept.  A's own `(standard)` self-label is likewise not repeated as a finding.

===============================================================================
2. THE THREE COORDINATES
===============================================================================

    nr      the radial quantum number, 1-based    {1, 2, 3}
    l       orbital angular momentum              {0 .. 6}
    sigma   sign(j - l): +1 for j = l + 1/2, -1 for j = l - 1/2

`sigma` rather than j itself, because j is determined by (l, sigma) and a
coordinate the others already fix is over-representation.  Spin-orbit splitting
is exactly the sigma = +1 member lying below its sigma = -1 partner, so the
coordinate is the physics rather than a re-encoding of it.

    22 members, 22 distinct cells -- the chart is FAITHFUL -- box 42.
    No coordinate is a LABEL: nr 0.1364, l 0.3182, sigma 0.0909.

**IT CLOSES UNDER GEOMETRY AND STATISTICS.**  That is channel K3 in this tree's
numbering -- NOT K7, and it is not alone there: `fibred.index` is a second
seated arity-3 index at K3.  (Both halves of the old sentence were false and
this file's own selftest already pinned the cell at (3, 7, 6), which is K3.
DOCKET 22 found it.)

===============================================================================
3. WHAT WAS MEASURED AND REFUSED AS A COORDINATE
===============================================================================

    rank                position in the order        22/22 = 1.0000  LABEL
    cumulative 2j+1     occupancy to that shell      22/22 = 1.0000  LABEL

Both are row labels: they separate every member and group nothing, which is the
expensive-and-uninformative case `overlap.py` exists to catch.

    delta               A's position minus B's       alphabet {-3,-2,0,1,2},
                                                     ratio 0.2273

**`delta` IS A LEGITIMATE MEASUREMENT AND STILL DOES NOT GO ON AN AXIS.**  It is
not a label and it is not constant.  But appending it takes the index from
closing under geometry and statistics to **closing NOTHING**, and takes the box
from 42 to 210; and no three-coordinate chart containing it is faithful -- the
three that exist hold 17, 10 and 17 cells against 22.  So it is banked as a
LEDGER COLUMN, one row per subshell, and never charted.  `delta_is_not_an_axis()`
returns the measurement rather than the assertion.

===============================================================================
4. WHAT THIS FILE REFUSES
===============================================================================

**TO PRINT A CANONICAL ORDER.**  It seats A's membership and records A's order
as corroborated; it does not rule that A is the shell model's order.

**TO OFFER THE MAGIC NUMBERS AS EVIDENCE ABOUT SEQUENCE.**  They verify the
block partition.  Section 1 is the whole of what they support.

**TO NAME A SPIN-ORBIT STRENGTH.**  Neither order is reproduced by a one- or
two-parameter mean field over this member set, and no value is fitted here.

**TO CALL B FABRICATED.**  Superseded and uncorroborated is what is measured;
wrong is not.

**TO IDENTIFY NUCLEAR nr WITH ELECTRONIC n.**  They are different quantum
numbers over different mean fields.  The (n, l) collisions with `probability`
are homographs and are reported as such.

**TO EXTEND PAST THE 126 CLOSURE.**  The banked orders stop there.
"""

import ast
import os
import sys
from fractions import Fraction as F

import hlaw
import mi
import overlap

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    'A seated member of The Method, imported by path and never copied.',
    (
        'method/members/r2-ch16e.py',
    ),
)


ROOT = "/home/user/Claude-Method-Works"
SRC_A = os.path.join(ROOT, "extracted/archives/restore-point-2-13/"
                           "nuclear_corridor.py")
SRC_B = os.path.join(ROOT, "recovered/nuccorr.py")
CORROB = ("recovered/c3.py", "recovered/c4.py",
          "recovered/corridor_identity.py", "method/members/r2-ch16e.py")
SEATED_CORROBORATOR = "method/members/r2-ch16e.py"

MAGIC = (2, 8, 20, 28, 50, 82, 126)
LN = "spdfghik"
NAMES = ("nr", "l", "sigma")
ARITY = 3

ORDER_A_STATUS = "EMPIRICAL-RULE"       # a shell-model ordering, not a theorem
ORDER_B_STATUS = "RECOVERED / UNCORROBORATED / SUPERSEDED"
DELTA_STATUS = "MEASURED"               # never PINNED, never an axis

_C = {}


# ------------------------------------------------------------------- sources

def _literal(path, name):
    """The named list, read from the SOURCE TEXT and never executed.

    Both source files print at import time and one of them shadows a stdlib
    module name; parsing the literal keeps a data read from becoming a program
    run, which is the right relationship to a capture.
    """
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id == name:
                    return [_tuple(e) for e in node.value.elts]
    raise KeyError("%s not found in %s" % (name, path))


def _tuple(e):
    out = []
    for a in e.elts:
        if isinstance(a, ast.Constant):
            out.append(a.value)
        elif isinstance(a, ast.Call):            # F(p, q)
            out.append(F(a.args[0].value, a.args[1].value))
        else:                                    # pragma: no cover
            raise ValueError(ast.dump(a))
    return tuple(out)


def order_a():
    if "A" not in _C:
        _C["A"] = _literal(SRC_A, "ORD")
    return _C["A"]


def order_b():
    if "B" not in _C:
        _C["B"] = _literal(SRC_B, "ORDER")
    return _C["B"]


def name(t):
    return "%d%s%d/2" % (t[0], LN[t[1]], int(2 * t[2]))


# ------------------------------------------------------ section 1's findings

def same_set():
    return set(order_a()) == set(order_b()), order_a() == order_b()


def disagreements():
    """[(position, A's subshell, B's subshell)] -- the eight."""
    return [(i, name(a), name(b))
            for i, (a, b) in enumerate(zip(order_a(), order_b())) if a != b]


def closures_of(order):
    """(the magic numbers this order hits, its total)."""
    cum, hit = 0, []
    for _nr, _l, j in order:
        cum += int(2 * j) + 1
        if cum in MAGIC:
            hit.append(cum)
    return tuple(hit), cum


def magic_is_null():
    """(A's hits, B's hits, whether the test separates them).

    IT DOES NOT, and the file will not pretend otherwise.
    """
    ha, _ta = closures_of(order_a())
    hb, _tb = closures_of(order_b())
    return ha, hb, ha != hb


def blocks(order):
    """The closed blocks -- every disagreement lies strictly inside one."""
    out, cum, cur = [], 0, []
    for t in order:
        cur.append(t)
        cum += int(2 * t[2]) + 1
        if cum in MAGIC:
            out.append((cum, cur))
            cur = []
    return out


def block_membership_identical():
    """([(closure, same membership?, size)], all identical?) -- WHY magic is null.

    THE FIRST ATTEMPT AT THIS WAS WRONG AND ITS FIXTURE CAUGHT IT.  The claim
    written first was that no disagreement sits at a block-closing position;
    position 21 does, so that was false.  The true statement is stronger: the
    seven blocks have the SAME MEMBERSHIP in both orders, and the orders differ
    only by permutations WITHIN blocks.  A block's closing sum is the sum over
    its members, which is a set, so no permutation inside it can move that sum.
    That is why both orders hit all seven magic numbers, and it is a fact about
    sets rather than about positions.
    """
    ba, bb = blocks(order_a()), blocks(order_b())
    rows = [(ca, frozenset(sa) == frozenset(sb), len(sa))
            for (ca, sa), (_cb, sb) in zip(ba, bb)]
    same = ([c for c, _s, _n in rows] == [c for c, _s, _n in
                                          [(cb, 0, 0) for cb, _sb in bb]]
            and all(s for _c, s, _n in rows))
    return rows, same


def corroboration():
    """[(file, longest prefix matching A, matching B, seated?)]."""
    import re
    na = [name(t) for t in order_a()]
    nb = [name(t) for t in order_b()]
    out = []
    for rel in CORROB:
        txt = open(os.path.join(ROOT, rel), encoding="utf-8",
                   errors="replace").read()
        toks = re.findall(r"[0-9][spdfghik][0-9]+/2", txt)

        def run(target):
            best = 0
            for s in range(len(toks)):
                k = 0
                while s + k < len(toks) and k < len(target) \
                        and toks[s + k] == target[k]:
                    k += 1
                best = max(best, k)
            return best
        out.append((rel, run(na), run(nb), rel == SEATED_CORROBORATOR))
    return out


def common_prefix():
    n = 0
    for a, b in zip(order_a(), order_b()):
        if a != b:
            break
        n += 1
    return n


# --------------------------------------------------------------- the chart

def sigma(l, j):
    return 1 if j > l else -1


def index():
    """The 22 nuclear single-particle subshells as (nr, l, sigma)."""
    if "X" not in _C:
        _C["X"] = frozenset((nr, l, sigma(l, j)) for nr, l, j in order_a())
    return _C["X"]


def ledger():
    """[(subshell, nr, l, 2j, rank in A, rank in B, delta, cumulative)]."""
    pb = {t: i for i, t in enumerate(order_b())}
    out, cum = [], 0
    for i, t in enumerate(order_a()):
        cum += int(2 * t[2]) + 1
        out.append((name(t), t[0], t[1], int(2 * t[2]), i, pb[t], i - pb[t],
                    cum))
    return out


def delta_is_not_an_axis():
    """((cells, box, closers) with delta, and without) -- the measurement."""
    X3 = index()
    pb = {t: i for i, t in enumerate(order_b())}
    X4 = frozenset((nr, l, sigma(l, j), i - pb[(nr, l, j)])
                   for i, (nr, l, j) in enumerate(order_a()))
    return ((len(X3), overlap.box_of(X3), tuple(closers(X3))),
            (len(X4), overlap.box_of(X4), tuple(closers(X4))))


def rejected_coordinates():
    """[(name, distinct, members, ratio, verdict)] for the ones not charted."""
    n = len(order_a())
    pb = {t: i for i, t in enumerate(order_b())}
    cum, occ = 0, []
    for t in order_a():
        cum += int(2 * t[2]) + 1
        occ.append(cum)
    d = [i - pb[t] for i, t in enumerate(order_a())]
    return [("rank", n, n, 1.0, "LABEL"),
            ("cumulative 2j+1", len(set(occ)), n, len(set(occ)) / n, "LABEL"),
            ("delta", len(set(d)), n, len(set(d)) / n, "measurement, ledger")]


def closers(X=None):
    X = frozenset(index() if X is None else X)
    cl, _b = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def cell():
    return mi.cell(index())


def homographs():
    """The (n, l) pairs this index shares with `probability` -- and they are
    different objects that print the same."""
    import probability
    mine = {(nr, l) for nr, l, _s in index()}
    theirs = {(n, l) for n, l in probability.probabilities()}
    return sorted(mine & theirs)


def cell_homographs():
    """{index: numerically equal cell tuples} over the arity-3 seated indexes.

    **THE CELL TUPLES DO COLLIDE, AND SAYING OTHERWISE WOULD BE FALSE.**  This
    was written first as `disjoint_from_seated()` asserting zero, and its
    fixture refused it: `channels` shares thirteen triples, `fibred` five,
    `madelung` and `inversion` four, `laws` one.

    THEY ARE HOMOGRAPHS AT FULL ARITY.  A nuclear (nr, l, sigma) that happens
    to equal an electronic (n, l, k) is two different objects printing the
    same, exactly as a nuclear 2s and an electronic 2s are.  Collisions with
    `fibred` need k = 1 because sigma is +-1; with `channels` they need a Pauli
    bound and a multiplicity that land on l and a sign.  None of them is a
    shared MEMBER.

    THIS IS WHY `overlap.py` HAS TWO TESTS AND CALLS `cell_overlap` THE WEAK
    ONE.  Numeric coincidence between charts of different member types is
    precisely what the weak test cannot distinguish from duplication, and the
    strong test -- identity keys -- is what settles it: no seated index has a
    nuclear member at all.
    """
    import registry
    out = {}
    X = index()
    for nm, mo, _a, _me, _w, _q in registry.rows():
        if mo == "nucshell":
            continue                               # itself is not a collision
        try:
            Y = frozenset(registry.index_of(nm))
        except Exception:                          # pragma: no cover
            continue
        if Y and len(next(iter(Y))) != ARITY:
            continue                               # not comparable, not zero
        n = len(X & Y)
        if n:
            out[nm] = n
    return out


def registry_index(name):
    import registry
    return registry.index_of(name)


def nuclear_member_sets():
    """[(index, what one member is)] for every registry row whose members are
    NUCLEAR -- this index included.

    The detector is a word match on the registry's own member description with
    `nuclide` carved out, because a nuclide-charge state is an ATOM in a charge
    state and not a nucleon in a mean field: `gravity` and
    `overlaprule.gravity_bound` are both of those.  A word match over prose can
    only OVER-include, which makes a property tested against it stricter rather
    than weaker, and that is the direction a guard may err in.
    """
    import registry
    return [(nm, w) for nm, _mo, _a, _me, w, _q in registry.rows()
            if "nucl" in w.lower() and "nuclide" not in w.lower()]


def nuclear_collisions():
    """The restated STRONG test: colliding indexes whose members are nuclear.

    Empty is the claim.  `cell_homographs()` is the weak test and finds ten
    indexes sharing full-arity cell tuples with this one; if a nuclear index
    were among them, a collision could be a shared MEMBER and this index would
    be a re-chart rather than a new member set.  None is -- the two nuclear
    indexes the tree has since gained are arity 2 and cannot reach the weak
    test at all.
    """
    hom = cell_homographs()
    return sorted(nm for nm, _w in nuclear_member_sets() if nm in hom)


def nuclear_duplicates():
    """Other nuclear indexes that hold one of THESE 22 members.  Empty.

    The second half of the restatement, and the half that still bites: unlike
    the withdrawn word match, this fires only on an index that actually holds
    single-particle subshells, which is the duplication the strong test exists
    to refuse.
    """
    import overlaprule
    X = index()
    return sorted(nm for nm, _w in nuclear_member_sets()
                  if not overlaprule.holds_members_of(nm, "nucshell")
                  and frozenset(registry_index(nm)) & X)


def member_types():
    """[(index, what one member is)] -- the STRONG test, from the registry.

    Not one of them is nuclear, which is the claim the numeric cell collisions
    cannot touch.

    THE EXCLUSION IS "OVER THESE SAME MEMBERS", NOT "IN THIS MODULE".  It was
    the module until M's overlap ruling seated a coarsening of this index in
    `overlaprule.py`, and the fixture below then reported a nuclear member in
    another index -- correctly, by the letter, and falsely in substance: the
    row is `nucshell (l, sigma)`, these 22 subshells with nr forgotten.  The
    claim was never that one module owns the nuclear members; it is that no
    OTHER MEMBER SET here is nuclear.  `overlaprule.holds_members_of` answers
    that, and the fixture is unweakened -- a genuinely new nuclear index would
    still fire it.

    **AND A GENUINELY NEW NUCLEAR INDEX DULY FIRED IT.  THAT FORM OF THE CLAIM
    IS NOW WITHDRAWN.**  The fixture read "no OTHER MEMBER SET here is nuclear
    -- the STRONG test", asserted [], and today measures
    `['nucbands.index', 'deformedbands.index']`.  It was not loosened to an
    inequality and it was not quietly deleted: it was fired by two CORRECT
    additions to the registry -- `nucbands` (DOCKET 35) and `deformedbands`
    (DOCKET 36b), both genuinely nuclear, both seated after this file was last
    touched.  nucshell.py is byte-unchanged since 519cd55; registry.py is what
    moved.

    WHAT IT WAS GUARDING WAS NEVER "NO NUCLEAR INDEX EXISTS ANYWHERE".  Read it
    beside `cell_homographs()`, which is the only thing that calls on it: the
    WEAK test finds numerically equal cell tuples, and the STRONG test has to
    rule out that such a collision is a SHARED MEMBER -- that this index is a
    duplicate of an atomic one wearing different coordinate names.  The word
    "nuclear" was standing in for "these members".  That proxy was sound while
    this index was the tree's only nuclear one, and the tree has outgrown it.
    Restated as what it was actually asserting, and MEASURED:

        every index whose cell tuples collide with this one has
        NON-nuclear members                      10 of 10, `nuclear_collisions()`
        no OTHER nuclear index holds one of
        these 22 members                         0 shared, both band indexes
                                                 being arity 2 on (2I, parity)

    Both halves are PROPERTIES, not pinned name lists -- the mistake logged
    below at the DOCKET 22 fixture -- so a further correct nuclear seating
    cannot fire them, while a nuclear index that DID hold these subshells still
    would.
    """
    import registry
    import overlaprule
    return [(nm, w) for nm, _mo, _a, _me, w, _q in registry.rows()
            if not overlaprule.holds_members_of(nm, "nucshell")]


# ---------------------------------------------------------------- the reading

def report():
    X = index()
    print("=" * 74)
    print("THE NUCLEAR SUBSHELL INDEX")
    print("=" * 74)
    print()
    print("Every other seated index has ATOMIC members. These are nuclear:")
    print("a single-particle subshell of the shell model, carrying (nr, l, j).")
    print()
    print("-" * 74)
    print("1. TWO BANKED ORDERS, THE SAME TWENTY-TWO SUBSHELLS.")
    print("-" * 74)
    same, ident = same_set()
    print("   A  %s" % os.path.relpath(SRC_A, ROOT))
    print("   B  %s" % os.path.relpath(SRC_B, ROOT))
    print("   same SET of subshells        %s" % same)
    print("   same SEQUENCE               %s" % ident)
    print("   positions differing          %d of %d"
          % (len(disagreements()), len(order_a())))
    print()
    for i, a, b in disagreements():
        print("      %2d   A %-8s   B %s" % (i, a, b))
    print()
    ha, hb, sep = magic_is_null()
    print("-" * 74)
    print("2. THE MAGIC NUMBERS DO NOT DECIDE IT.")
    print("-" * 74)
    print("   A hits  %s" % (list(ha),))
    print("   B hits  %s" % (list(hb),))
    print("   does the closure test separate them?   %s" % sep)
    rows, allsame = block_membership_identical()
    print("   THE SEVEN BLOCKS HAVE THE SAME MEMBERSHIP IN BOTH: %s" % allsame)
    for c, same, n in rows:
        print("      closure %3d   same membership %-5s   %d subshells"
              % (c, same, n))
    print("   The orders differ only by permutations WITHIN blocks. A block's")
    print("   closing sum is the sum over its members, which is a SET, so no")
    print("   permutation inside it can move that sum. The magic numbers")
    print("   verify the BLOCK PARTITION and say nothing about sequence.")
    print("   A's own header calls itself 'CORRECTED ... verified to close at")
    print("   2, 8, 20, 28, 50, 82, 126'. It does. So does B.")
    print()
    print("-" * 74)
    print("3. WHAT DOES DECIDE IT IS CORROBORATION, AND IT IS ONE-SIDED.")
    print("-" * 74)
    print("   %-38s %-8s %-8s %s" % ("file", "match A", "match B", ""))
    for rel, a, b, seated in corroboration():
        print("   %-38s %-8d %-8d %s" % (rel, a, b, "SEATED MEMBER" if seated else ""))
    print()
    print("   The %d is the COMMON PREFIX: positions 0..%d are where A and B"
          % (common_prefix(), common_prefix() - 1))
    print("   agree, so every file stops matching B exactly where they diverge.")
    print("   NOT ONE FILE FOLLOWS B PAST THE DISAGREEMENT.")
    print()
    print("   B is not called wrong. Status: %s" % ORDER_B_STATUS)
    print("   A's order status: %s" % ORDER_A_STATUS)
    print()
    print("-" * 74)
    print("4. THE CHART.")
    print("-" * 74)
    doc = {"nr": "radial quantum number", "l": "orbital angular momentum",
           "sigma": "sign(j - l): +1 is j = l+1/2"}
    for i, nm in enumerate(NAMES):
        vals = sorted({c[i] for c in X})
        d = len(vals)
        print("   %-6s %-32s %-22s %d/%d = %.4f"
              % (nm, doc[nm], vals, d, len(X), d / len(X)))
    print()
    print("   members        %d" % len(order_a()))
    print("   distinct cells %d   FAITHFUL" % len(X))
    print("   box            %d" % overlap.box_of(X))
    cl, _b = hlaw.closures(X)
    for L in hlaw.LANGS:
        e = len(cl[L]) - len(X)
        print("     %-13s admits %3d   E %3d%s"
              % (L, len(cl[L]), e, "   <-- CLOSES" if e == 0 else ""))
    print()
    print("   closers  %s" % (closers() or "NONE"))
    print("   CELL     %s" % (cell(),))
    print()
    print("-" * 74)
    print("5. MEASURED AND REFUSED AS A COORDINATE.")
    print("-" * 74)
    for nm, d, n, r, v in rejected_coordinates():
        print("   %-18s %2d/%2d = %.4f   %s" % (nm, d, n, r, v))
    a3, a4 = delta_is_not_an_axis()
    print()
    print("   delta IS a legitimate measurement and still does not go on an")
    print("   axis. Appending it:")
    print("        without delta   %d cells, box %3d, closers %s"
          % (a3[0], a3[1], list(a3[2]) or "NONE"))
    print("        with delta      %d cells, box %3d, closers %s"
          % (a4[0], a4[1], list(a4[2]) or "NONE"))
    print("   It closes nothing and the box multiplies. Banked as a ledger")
    print("   column instead. Status %s." % DELTA_STATUS)
    print()
    print("-" * 74)
    print("6. THE MEMBERS.")
    print("-" * 74)
    print("   %-9s %-3s %-3s %-4s %-6s %-6s %-6s %s"
          % ("subshell", "nr", "l", "2j", "rank A", "rank B", "delta", "cumul"))
    for nm, nr, l, tj, ra, rb, d, cum in ledger():
        print("   %-9s %-3d %-3d %-4d %-6d %-6d %-+6d %s%s"
              % (nm, nr, l, tj, ra, rb, d, cum,
                 "   <-- MAGIC" if cum in MAGIC else ""))
    print()
    print("-" * 74)
    print("7. THE MEMBER TYPE IS NEW -- AND THE CELL TUPLES DO COLLIDE.")
    print("-" * 74)
    print("   What one member is, in each seated index:")
    for nm, w in member_types():
        print("      %-20s %s" % (nm, w))
    print("   NONE OF THEM HOLDS A NUCLEON IN A MEAN FIELD. That is the strong")
    print("   test, and it settles it.")
    print()
    print("   (\"NOT ONE IS NUCLEAR\" stood here and is WITHDRAWN. It was true")
    print("   when written and two LATER, CORRECT seatings falsified it:")
    for nm, w in nuclear_member_sets():
        if nm == "nucshell.index":
            continue
        print("      %-20s %s" % (nm, w.split(";")[0].split(" -- ")[0]))
    print("   Both ARE nuclear. Neither is a re-chart of this index: they are")
    print("   arity 2 on (2I, parity), a WHOLE-NUCLEUS quantum number, they")
    print("   share %d members with these 22, and no colliding index above is"
          % len(nuclear_duplicates()))
    print("   nuclear -- %s. That is what the test was guarding.)"
          % (nuclear_collisions() or "none of the %d" % len(cell_homographs())))
    print()
    hom = cell_homographs()
    print("   Numerically equal CELL TUPLES, which is the weak test:")
    for nm, n in sorted(hom.items()):
        print("      %-20s %d colliding triples" % (nm, n))
    print("   THOSE ARE HOMOGRAPHS AT FULL ARITY, not shared members. A nuclear")
    print("   (nr, l, sigma) that happens to equal an electronic (n, l, k) is")
    print("   two different objects printing the same -- and it is exactly why")
    print("   overlap.py calls cell_overlap the WEAK test.")
    print("   (n, l) pairs shared with probability: %s -- same reason."
          % (homographs(),))
    print()
    print("-" * 74)
    print("8. REFUSED.")
    print("-" * 74)
    print("   To print a canonical order.")
    print("   To offer the magic numbers as evidence about sequence.")
    print("   To name a spin-orbit strength -- none is fitted here.")
    print("   To call B fabricated. Superseded and uncorroborated is what is")
    print("     measured; wrong is not.")
    print("   To identify nuclear nr with electronic n.")
    print("   To extend past the 126 closure.")
    return 0


# ------------------------------------------------------------------ fixtures

def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    print("nucshell selftest")

    A, B = order_a(), order_b()
    chk("order A is read from the capture, not executed", len(A), 22)
    chk("order B likewise", len(B), 22)
    chk("THE SAME 22 SUBSHELLS", set(A) == set(B), True)
    chk("in a DIFFERENT sequence", A == B, False)
    chk("differing at eight positions", len(disagreements()), 8)
    chk("the common prefix is eleven long", common_prefix(), 11)

    # -- the first finding: the closure test is null
    ha, hb, sep = magic_is_null()
    chk("A hits every magic number", list(ha), list(MAGIC))
    chk("AND SO DOES B", list(hb), list(MAGIC))
    chk("so the closure test does NOT separate them", sep, False)
    chk("both total 126", (closures_of(A)[1], closures_of(B)[1]), (126, 126))
    rows, allsame = block_membership_identical()
    chk("THE SEVEN BLOCKS HAVE IDENTICAL MEMBERSHIP, which is why", allsame,
        True)
    chk("...and a disagreement DOES sit at a closing position, so the first",
        21 in [i for i, _a, _b in disagreements()], True)
    chk("seven closed blocks", len(blocks(A)), 7)

    # -- the second finding: corroboration is one-sided
    cor = corroboration()
    chk("four further files carry a sequence", len(cor), 4)
    chk("every one of them matches A further than B",
        [r for r, a, b, _s in cor if a <= b], [])
    chk("three match A in full", [r for r, a, _b, _s in cor if a == 22],
        ["recovered/c3.py", "recovered/c4.py",
         "recovered/corridor_identity.py"])
    chk("the fourth is a SEATED MEMBER and matches its full 16",
        [(r, a) for r, a, _b, s in cor if s], [(SEATED_CORROBORATOR, 16)])
    chk("NOT ONE follows B past the common prefix",
        [r for r, _a, b, _s in cor if b > common_prefix()], [])
    chk("B is not called wrong, only superseded",
        "SUPERSEDED" in ORDER_B_STATUS and "FABRICAT" not in ORDER_B_STATUS,
        True)

    # -- the chart
    X = index()
    chk("22 members", len(order_a()), 22)
    chk("22 distinct cells -- FAITHFUL", len(X), 22)
    chk("arity 3", len(next(iter(X))), ARITY)
    chk("box", overlap.box_of(X), 42)
    chk("no coordinate is constant",
        [NAMES[i] for i in range(ARITY) if len({c[i] for c in X}) == 1], [])
    chk("no coordinate is a LABEL",
        [NAMES[i] for i, _d, _n, _r, v in overlap.resolution(X)
         if v == "LABEL"], [])
    chk("nr alphabet", sorted({c[0] for c in X}), [1, 2, 3])
    chk("l alphabet", sorted({c[1] for c in X}), [0, 1, 2, 3, 4, 5, 6])
    chk("sigma is exactly the two spin-orbit partners",
        sorted({c[2] for c in X}), [-1, 1])
    chk("j is determined by (l, sigma), which is why j is not a coordinate",
        len({(l, s) for _nr, l, s in X}) == len({(l, F(2 * l + s, 2))
                                                 for _nr, l, s in X}), True)
    chk("IT CLOSES UNDER GEOMETRY AND STATISTICS", closers(),
        ["geometry", "statistics"])
    chk("CELL", cell(), (3, 7, 6))

    # -- what was refused, and why
    rej = dict((r[0], r) for r in rejected_coordinates())
    chk("rank is a LABEL", rej["rank"][4], "LABEL")
    chk("cumulative occupancy is a LABEL", rej["cumulative 2j+1"][4], "LABEL")
    chk("delta is NOT a label", rej["delta"][3] < 0.9, True)
    a3, a4 = delta_is_not_an_axis()
    chk("...and still not an axis: without it, two languages close",
        list(a3[2]), ["geometry", "statistics"])
    chk("...with it, NOTHING closes", list(a4[2]), [])
    chk("...and the box multiplies", (a3[1], a4[1]), (42, 210))
    chk("delta's status is not flattened to PINNED", DELTA_STATUS, "MEASURED")

    # -- the member type is new, measured against the registry
    #
    # WITHDRAWN.  This fixture read
    #     chk("no OTHER MEMBER SET here is nuclear -- the STRONG test",
    #         [nm for nm, w in member_types()
    #          if "nucl" in w.lower() and "nuclide" not in w.lower()], [])
    # asserting [], and it today measures ['nucbands.index',
    # 'deformedbands.index'].  IT WAS FIRED BY TWO CORRECT ADDITIONS, not by a
    # fault: nucbands (DOCKET 35, nuclear excited states) and deformedbands
    # (DOCKET 36b, deformed odd-odd rotational bands) are BOTH GENUINELY
    # NUCLEAR and were both seated after this file was last touched --
    # nucshell.py is byte-unchanged since 519cd55 and registry.py is what
    # moved.  The claim was true when written; registry.py still records this
    # index as "the exception that proved the old subject too narrow", and the
    # word "nuclear" was standing in for "these members" while that held.
    #
    # It is RESTATED, not loosened, as the two things it was actually
    # guarding -- that a cell-tuple collision here cannot be a shared member.
    # Both are properties over the registry rather than pinned name lists, so
    # a further correct nuclear seating cannot fire them either.  See
    # member_types() and nuclear_collisions().
    chk("the STRONG test, restated: no index whose CELL TUPLES COLLIDE with "
        "this one is nuclear", nuclear_collisions(), [])
    chk("...and no OTHER nuclear index holds ONE of these 22 members -- which "
        "a nuclear index that duplicated them still would fire",
        nuclear_duplicates(), [])
    chk("...the two that falsified the original are nuclear, seated, and "
        "arity 2 on (2I, parity) -- so they cannot reach the weak test",
        sorted(len(next(iter(registry_index(nm)))) for nm, _w in
               nuclear_member_sets() if nm != "nucshell.index"), [2, 2])
    # A PROPERTY, NOT A PIN.  This asserted two excluded rows while the overlap
    # ruling's coarsening of this index was seated; DOCKET 22 unseated it, and
    # a pinned list of names fired on a CORRECT removal.  What must hold is
    # that the excluded rows are EXACTLY the registry rows over these members,
    # however many of them there happen to be.
    import overlaprule as _OR
    chk("the excluded rows are exactly the registry rows over THESE members",
        [nm for nm, *_r in __import__("registry").rows()
         if nm not in {n for n, _w in member_types()}],
        [nm for nm, *_r in __import__("registry").rows()
         if _OR.holds_members_of(nm, "nucshell")])
    chk("and today that is nucshell.index alone -- the ruling's coarsening of "
        "it was unseated by DOCKET 22",
        [nm for nm, *_r in __import__("registry").rows()
         if nm not in {n for n, _w in member_types()}], ["nucshell.index"])
    # A PROPERTY, NOT A PINNED COUNT.  This tree has now made that mistake
    # five times: the first version of this fixture pinned the exact per-index
    # collision counts, and seating two further arity-3 indexes changed them --
    # so a CORRECT addition to the registry fired the fixture.  What must hold
    # is that collisions exist, that every one is with an arity-3 chart, and
    # that none of them is a shared member.
    hom = cell_homographs()
    chk("the CELL TUPLES DO collide, and the file says so", bool(hom), True)
    chk("...and every colliding index is arity 3, which is how they can",
        [k for k in hom if len(next(iter(registry_index(k)))) != ARITY], [])
    chk("...and this index is not counted against itself",
        [k for k in hom if k.startswith("nucshell")], [])
    chk("the (n, l) collisions with probability are homographs too",
        len(homographs()), 5)

    # -- the refusals as facts about the file
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    chk("no spin-orbit strength is fitted",
        bool(__import__("re").search(r"\bSPIN_ORBIT\s*=\s*[-\d.]", src)), False)
    chk("nothing past the 126 closure", max(c for *_r, c in ledger()), 126)
    print("nucshell selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv[1:]:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
