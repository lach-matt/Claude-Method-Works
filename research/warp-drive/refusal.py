"""
===============================================================================
refusal.py -- THE REFUSAL INDEX, AND WHAT IT SURVIVES
===============================================================================

M: "A refusal index is a tremendous amount of information. We need to build it
and populate it, analyze, document and seat it as an extension of the master
index."

    "each index likely shares the same refusal index as us, which means we can
    draw threads that extend through multiple MIs"

Both are right, and the second is right about a SMALLER object than it names.
This file is the build, and the build turned into a measurement of the master
index's own construction.

===============================================================================
0. WHAT A REFUSAL INDEX IS
===============================================================================

A CHANNEL SET is which languages CLOSE an index X -- a property of X.  A REFUSAL
SET is which languages REFUSE a cell c of X's box -- a property of the PAIR
(X, c).  Both are down-sets of the hierarchy law's containment order, by dual
arguments, so both live in the same eight lawful positions K0..K7.  duality.py
establishes that and is the file to read first.

THE REFUSAL INDEX OF X is then the simplest thing in the neighbourhood:

    R(X) = { the refusal set of c : c a cell of X's box }   as a subset of K0..K7

Nine seated indexes, nine subsets of an eight-element lattice.  duality.py's M2
carries a five-coordinate PROFILE (K, W, H, J, A) instead; section 3 is why the
extra four are chart decoration and K is the object.

===============================================================================
1. THE NINE, MEASURED
===============================================================================

    Janet (n+l, l, k)            {0,7}
    periodic layout 2-D          {0,4}
    substances (Hawking-Ellis)   {0,2,7}
    the languages                {0,4,5,7}
    spacetimes (Petrov)          {0,3,4,5,7}
    energy-condition family      {0,2,3,4,5,7}
    bounds                       {0,1,2,3,4,7}
    exotic mechanisms            {0,2,3,4,5,6,7}
    periodic layout 3-D          {0,1,3,4,5,6,7}

    K0 IS UNIVERSAL.  Every seated index has cells that NOTHING refuses -- cells
    inside every one of the five closures.  Nine of nine, no exception.

    K7 IS IN EIGHT OF NINE.  The exception is `periodic layout 2-D`, and it is
    the DENSEST index in the corpus at 71.4 %: too full to have a cell that
    every language refuses.  Dilute it -- see section 3 -- and K7 appears.

    K1 IS IN TWO.  K6 IS IN TWO.  They are the rare ones and section 4 is what
    they connect.

    THE LATTICE.  Minimal: Janet and periodic layout 2-D.  Maximal: bounds,
    exotic mechanisms and periodic layout 3-D.  Twelve of the thirty-six pairs
    are incomparable, so this is a lattice and not a chain -- the same shape the
    channel reading has, and for the same reason.

===============================================================================
2. THE MASTER INDEX INDEXES CHARTS, NOT OBJECTS
===============================================================================

This was not the question.  It is what the question turned up, and everything
after it is conditioned on it.

M asked whether the periodic table is OVER-REPRESENTED, being seated three
times: `periodic layout 2-D` at (period, group), `periodic layout 3-D` at
(period, group, block), and `Janet (n+l, l, k)`.  It is, and worse than that.

    LW1-ground.py stops at Z = 108, so `block_of` returns None for Z 109..118
    and the three-coordinate layout cannot chart them.  On the EIGHTY elements
    all three charts reach:

        (period, group)         INJECTIVE, 80 cells
        (period, group, block)  INJECTIVE, 80 cells
        (n+l, l)                NOT injective -- 80 elements onto 16 cells

    So Janet is a strict COARSENING, and 2-D and 3-D are in BIJECTION via the
    elements.  `block` is a FUNCTION of `(period, group)` on all eighty: the
    three-coordinate layout is the two-coordinate layout PLUS A COORDINATE THAT
    CARRIES ZERO INFORMATION about which element is which.

AND THAT ZERO-INFORMATION COORDINATE CHANGES THE CHANNEL.  Same eighty elements:

        (period, group)                        closes statistics  (1,1,0,0,3)
        + a MONOTONE redundant coordinate      closes statistics  (1,1,0,1,1)
        + the block, a NON-monotone one        closes NOTHING     (0,0,0,1,1)

    The block is order-reversing on 356 pairs.  So D and R move under ANY
    redundant coordinate, which is expected -- they are bands on arity and
    density, and neither is an invariant of anything.  C, Sc and Oc survive a
    MONOTONE redundant coordinate and DO NOT survive a non-monotone one.

    Across the nine, appending the monotone redundant coordinate moves the
    master cell of FIVE and changes the channel of NONE.

    **SO A MASTER CELL IS A PROPERTY OF THE CHART, NOT OF THE OBJECT.**  Nothing
    in the construction prevents one object from occupying several cells, and
    the periodic table occupies three, in three different channels.

AND THE DEMAND IS SATISFIABLE BY RE-CHARTING WHAT IS ALREADY SEATED.  Of 565
re-chartings of the nine -- one redundant coordinate appended, or one coordinate
dropped -- **twenty land exactly on the demanded cell (1,1,0,2,1)**.  Two are
not tricks:

        bounds MINUS its G coordinate   8 cells, arity 5, box 108, density
                                        7.4 %, closes statistics -- THE
                                        WITHDRAWN FILL COMES BACK IF YOU DROP
                                        THE GRAVITY SLOT
        energy-condition family         lands there under FIVE different
                                        single-coordinate drops

    Stated at its true strength: an arbitrary redundant coordinate is not a
    legitimate index, and the right answer to that is a CRITERION FOR A
    LEGITIMATE CHART.  This tree has never stated one.  So "nothing in this
    corpus occupies the demanded cell" is true relative to the chart choices,
    and the demand is exactly as strong as the unstated criterion and no
    stronger.  RECORDED, NOT REPAIRED.

===============================================================================
3. K IS THE OBJECT.  W, H, J AND A ARE CHART DECORATION.
===============================================================================

duality.py's M2 profiles a pair as (K, W, H, J, A).  Put each truncation to the
same monotone redundant coordinate that moved five master cells:

        (K, W, H, J, A)   invariant in 3 of 9
        (K, W, J)         invariant in 6 of 9
        (K, W)            invariant in 6 of 9
        (K)               invariant in 8 of 9, AND THE ONE EXCEPTION ONLY GROWS

The exception is `periodic layout 2-D`, whose {0,4} gains K7 -- the dilution of
section 1.  So K is MONOTONE under monotone re-charting: it never loses a
refusal kind.  H is a capped Hamming distance and A is the host's arity band, so
both are dimension-dependent by construction and it is no surprise they move;
what is worth having is that dropping them is not enough, and only K survives.

    THE SAME LESSON TWICE.  The master index's cells are charts on indexes; the
    refusal profile's coordinates are a chart on the refusal set.  In both cases
    the invariant is the down-set of languages and everything else is bookkeeping
    about how it was written down.

UNDER A NON-MONOTONE re-charting K is not even monotone: the 2-D chart's
refusal profiles are NOT contained in the 3-D chart's.  So the invariance is
conditional and the condition is stated.

===============================================================================
4. THE THREAD, AND IT IS K1
===============================================================================

M: "each index likely shares the same refusal index as us, which means we can
draw threads that extend through multiple MIs."

THEY DO NOT ALL SHARE ONE.  Only K0 is universal.  What exists instead is
better, because it discriminates: a K value present in FEW indexes is a thread
between exactly those.

    K1 {information refuses, everything else admits} occurs in TWO indexes:

        bounds                  at (2,1,0,0,0,2) and (2,1,0,0,1,2) -- a
                                non-gravitational entropy bound with a constant
                                RHS on a spacelike region
        periodic layout 3-D     at (4, 11, 0) -- period 4, group 11, s-block

    Two indexes with no other relation, sharing the corpus's rarest refusal
    kind, WHICH IS THE WARP OBSTRUCTION'S KIND: every pair of requirements
    jointly satisfiable, the full combination not.

    K6 occurs in two: exotic mechanisms and periodic layout 3-D.  So the
    periodic layout in three coordinates is the ONLY index carrying BOTH rare
    kinds, and at seven of eight it is the richest refusal structure in the
    corpus.

        (A first draft here added "and the only one missing K2".  That is
        FALSE -- five of the nine lack K2, spacetimes among them -- and it
        survived a paragraph only because an ad-hoc size filter in the pin was
        doing the work.  Its own selftest caught it.  Withdrawn.)

CAUTION, AND IT MATTERS.  `bounds` acquired K1 only when completing that family
stopped it closing, in the commit immediately before this file.  Before that K1
was in the periodic layout alone.  THE THREAD IS ONE COMMIT OLD, and a reader
should weigh it accordingly.

AND THE OTHER END OF THE THREAD IS CONVENTION-DEPENDENT.  A separate pass put
the periodic K1 to the decisive test: recompute the three-coordinate layout with
the block read off the DRAWN layout (group -> block) instead of the
differentiating electron.  **K1 VANISHES**, becoming K4 {information,
statistics}, and the index has no K1 cell at all.  Same 80 cells, same box, same
density, same master cell (0,0,0,1,1) -- only the refusal moves.  So the
corpus's rarest refusal is a fact about the block CONVENTION as much as about
the elements, and populate.py's `block_of` asserts its convention in a docstring
without citing a register, where `period_of` and `group_of` are pinned to
section 6's ninety cells.  WHICH CONVENTION THE CORPUS RULES FOR IS OPEN, and
the whole periodic half of this thread turns on it.

WHAT THE PERIODIC K1 ACTUALLY RESTS ON, measured over all 160 single-cell
perturbations of the seated layout: **exactly two elements, copper and silver**,
and 157 of the 160 leave K1 where it is.  Copper d->s kills it by MEMBERSHIP
(the cell becomes occupied); silver s->d kills it by WITNESS (statistics stops
admitting).  The causal chain is palladium's empty valence 5s -> silver alone in
the s-block at group 11 -> statistics admits (4,11,0) -> K1.  Give palladium its
Madelung configuration and K1 RELOCATES to (4,10,0) rather than vanishing.

    A FRAMING OF MINE, CORRECTED BY THAT PASS.  I wrote that (4,11,0) is absent
    because "copper's anomaly and palladium's anomaly are different anomalies".
    True and not the operative cause: copper's anomaly is IRRELEVANT to the
    absence, and what does the work is NICKEL'S NORMALITY -- nickel keeps its
    4s2, so copper's differentiating electron is 3d.  And "palladium is the only
    element with an empty outermost s subshell" is false as usually stated: of
    four natural readings of "outermost", two return no element at all, and Pd
    is unique only under "the valence s shell the period assigns".

A SECOND CAUTION.  The two minimal refusal sets are Janet and periodic layout
2-D -- exactly the two charts section 2 finds redundant.  That is a convergence
of two independent measurements and not a proof of either: the redundant charts
are also the coarse ones, and coarse sets have fewer refusal kinds for reasons
that have nothing to do with being redundant.

===============================================================================
5. WHY IT IS NOT SEATED AS A TENTH INDEX
===============================================================================

M asked for it seated "as an extension of the master index", and extension is
the right word rather than member.

R is computed FROM the inventory.  Seating it as a tenth member changes the
inventory, which changes R, which changes what was seated.  That is a fixed-point
problem and not a formality.  This file therefore seats R as a FUNCTION ON THE
MEMBERS -- an added structure over the master index, addressable by name, with
its own lattice -- and does not add a row.  Whether the iteration converges is
open here and is the first thing to settle next.

    AND SECTION 2 IS A SECOND REASON TO WAIT.  Seating anything new into a master
    index whose cells are charts rather than objects seats a chart.  The criterion
    for a legitimate chart is the prior question.

===============================================================================
WHAT THIS FILE REFUSES TO CONCLUDE
===============================================================================

    That the master index is WRONG.  It is chart-dependent, which is a fact
    about what it measures, not an error in the measuring.  A closure operator
    over ordinal coordinates CANNOT be invariant under arbitrary relabelling --
    that is what makes it informative.

    That periodic layout 2-D or Janet should be DROPPED.  Section 2 establishes
    redundancy of information, and registers 35, 50 and 51 rule that the 2-D
    layouts are shadows of a three-dimensional object.  Neither settles which
    chart a master index ought to seat, and the two senses of "supersede" point
    opposite ways: informationally 2-D reaches ten elements 3-D cannot, and
    explanatorily 3-D derives the period lengths 2-D must impose.

    That the K1 thread MEANS anything.  Two indexes share a rare refusal kind.
    That is a fact about two boxes.  Nothing here connects a bound on entropy to
    a group-11 metal, and reading one into it would be exactly the H97 hazard
    this tree keeps naming -- a measurement on a re-coordinated index read as a
    property of the object.
"""

import itertools
import sys

import hlaw
import master

CAP = 3000                      # cells scanned per index; duality.py's figure


# ---------------------------------------------------------------------------
# the refusal index
# ---------------------------------------------------------------------------

def refusal_set(X, cap=CAP):
    """R(X) -- which of the eight lawful refusal kinds occur in X's box."""
    X = frozenset(X)
    ks = master.channel_sets()
    cl, box = hlaw.closures(X)
    return frozenset(
        ks.index(frozenset(L for L in hlaw.LANGS if c not in cl[L]))
        for c in itertools.islice(itertools.product(*box), cap))


def refusal_index(inv=None, cap=CAP):
    """{index name: R(X)} over the seated inventory."""
    inv = master.inventory() if inv is None else inv
    return {nm: refusal_set(inv[nm], cap) for nm in inv}


def occurrence(R=None):
    """{K: [index names carrying it]} -- the census the threads come from."""
    R = refusal_index() if R is None else R
    return {k: sorted(nm for nm, s in R.items() if k in s) for k in range(8)}


def universal(R=None):
    """The refusal kinds EVERY seated index carries."""
    R = refusal_index() if R is None else R
    return frozenset.intersection(*R.values())


def lattice(R=None):
    """(minimal, maximal, incomparable pairs) of the nine refusal sets."""
    R = refusal_index() if R is None else R
    nm = sorted(R)
    mins = [a for a in nm if not any(b != a and R[b] < R[a] for b in nm)]
    maxs = [a for a in nm if not any(b != a and R[a] < R[b] for b in nm)]
    inc = [(a, b) for i, a in enumerate(nm) for b in nm[i + 1:]
           if not (R[a] <= R[b] or R[b] <= R[a])]
    return sorted(mins), sorted(maxs), inc


def threads(R=None, most=2):
    """{K: [indexes]} for the refusal kinds carried by at most `most` indexes.

    A kind everything carries connects nothing.  A kind two indexes carry is a
    thread between exactly those two, and that is the discriminating case.
    """
    occ = occurrence(R)
    return {k: v for k, v in occ.items() if 0 < len(v) <= most}


# ---------------------------------------------------------------------------
# section 2 and 3 -- what survives a re-charting
# ---------------------------------------------------------------------------

def recharted(X, g=lambda c: c[0]):
    """X with one redundant coordinate appended.  Adds NO information: g is a
    function of the cell, so the new chart separates exactly what X separated."""
    return frozenset(tuple(c) + (g(c),) for c in X)


def profile_set(X, keep=("K", "W", "H", "J", "A"), cap=CAP):
    """duality.py's profile, restricted to the named coordinates."""
    X = frozenset(X)
    ks = master.channel_sets()
    cl, box = hlaw.closures(X)
    d = len(box)
    prs = list(itertools.combinations(range(d), 2))
    A = 0 if d == 2 else (1 if d <= 4 else 2)
    out = set()
    for c in itertools.islice(itertools.product(*box), cap):
        K = ks.index(frozenset(L for L in hlaw.LANGS if c not in cl[L]))
        hit = [any(x[i] == c[i] and x[j] == c[j] for x in X) for i, j in prs]
        W = 2 if all(hit) else (1 if any(hit) else 0)
        H = min(min(sum(1 for i in range(d) if x[i] != c[i]) for x in X), 3)
        isj = any(tuple(max(a[i], b[i]) for i in range(d)) == c
                  for a in X for b in X)
        ism = any(tuple(min(a[i], b[i]) for i in range(d)) == c
                  for a in X for b in X)
        full = {"K": K, "W": W, "H": H,
                "J": (1 if isj else 0) + (2 if ism else 0), "A": A}
        out.add(tuple(full[k] for k in keep))
    return frozenset(out)


def truncation_survival(keep, inv=None, cap=CAP):
    """(invariant count, total, [(name, gained, lost)]) for that truncation."""
    inv = master.inventory() if inv is None else inv
    rows, n = [], 0
    for nm in sorted(inv):
        a = profile_set(inv[nm], keep, cap)
        b = profile_set(recharted(inv[nm]), keep, cap)
        if a == b:
            n += 1
        else:
            rows.append((nm, sorted(b - a), sorted(a - b)))
    return n, len(inv), rows


def cell_survival(inv=None):
    """(master cells moved, channels changed, total) under the re-charting."""
    inv = master.inventory() if inv is None else inv
    moved = sum(1 for nm in inv
                if master.master_cell(inv[nm])
                != master.master_cell(recharted(inv[nm])))
    chg = sum(1 for nm in inv
              if master.closers(inv[nm]) != master.closers(recharted(inv[nm])))
    return moved, chg, len(inv)


# ---------------------------------------------------------------------------
# section 2 -- can a re-charting satisfy the demand?
# ---------------------------------------------------------------------------

def _generators(d):
    for i in range(d):
        yield ("proj%d" % i, lambda c, i=i: c[i])
        yield ("par%d" % i, lambda c, i=i: c[i] % 2)
        yield ("m3_%d" % i, lambda c, i=i: c[i] % 3)
        yield ("neg%d" % i, lambda c, i=i: -c[i])
    for i, j in itertools.combinations(range(d), 2):
        yield ("min%d%d" % (i, j), lambda c, i=i, j=j: min(c[i], c[j]))
        yield ("max%d%d" % (i, j), lambda c, i=i, j=j: max(c[i], c[j]))
        yield ("sum%d%d" % (i, j), lambda c, i=i, j=j: c[i] + c[j])
        yield ("dif%d%d" % (i, j), lambda c, i=i, j=j: abs(c[i] - c[j]))
        yield ("xor%d%d" % (i, j), lambda c, i=i, j=j: (c[i] + c[j]) % 2)


def rechartings_hitting(cell=None, inv=None):
    """([(index, how, cells, shape, closers)], number tried) -- re-chartings of
    the SEATED indexes that land on `cell`.  Default: the demanded cell."""
    cell = master.DEMANDED_AT_EIGHT if cell is None else cell
    inv = master.inventory() if inv is None else inv
    hits, tried = [], 0
    for nm in sorted(inv):
        X = inv[nm]
        d = len(next(iter(X)))
        for gname, g in _generators(d):
            Y = recharted(X, g)
            tried += 1
            if master.master_cell(Y) == cell:
                hits.append((nm, gname, len(Y), master.shape(Y),
                             sorted(master.closers(Y))))
        for i in range(d):
            Y = frozenset(tuple(c[:i] + c[i + 1:]) for c in X)
            tried += 1
            if len(Y) > 1 and master.master_cell(Y) == cell:
                hits.append((nm, "drop%d" % i, len(Y), master.shape(Y),
                             sorted(master.closers(Y))))
    return hits, tried


# ---------------------------------------------------------------------------

def report():
    ks = master.channel_sets()
    print("=" * 74)
    print("THE REFUSAL INDEX -- and what it survives")
    print("=" * 74)
    print()
    R = refusal_index()
    print("1. THE NINE, MEASURED.  R(X) = which refusal kinds occur in X's box.")
    for nm in sorted(R, key=lambda n: (len(R[n]), n)):
        print("   %-28s %s" % (nm, "{" + ",".join(map(str, sorted(R[nm]))) + "}"))
    print()
    occ = occurrence(R)
    print("   K   set                                        in  carried by")
    for k in range(8):
        who = occ[k]
        tag = ", ".join(who) if len(who) <= 2 else ""
        print("   K%d  %-42s %d/9 %s"
              % (k, "{" + ", ".join(sorted(ks[k])) + "}", len(who), tag))
    print("   UNIVERSAL: %s -- every index has cells NOTHING refuses."
          % sorted(universal(R)))
    print()
    mins, maxs, inc = lattice(R)
    print("   minimal %s" % mins)
    print("   maximal %s" % maxs)
    print("   incomparable pairs: %d of 36 -- a lattice, not a chain" % len(inc))
    print()

    print("2. THE MASTER INDEX INDEXES CHARTS, NOT OBJECTS.")
    moved, chg, tot = cell_survival()
    print("   Append a coordinate that is a FUNCTION of the existing ones --")
    print("   zero information about which member is which. Over the nine:")
    print("     master cells moved   %d of %d" % (moved, tot))
    print("     channels changed     %d of %d" % (chg, tot))
    print("   So D and R are chart properties. C, Sc, Oc survive a MONOTONE")
    print("   redundant coordinate -- and the periodic table's block, which is")
    print("   a function of (period, group) and order-reversing on 356 pairs,")
    print("   takes that index from closing in statistics to closing in nothing.")
    print()
    hits, tried = rechartings_hitting()
    print("   AND THE DEMAND %s IS SATISFIABLE BY RE-CHARTING:"
          % (master.DEMANDED_AT_EIGHT,))
    print("   %d of %d re-chartings of the SEATED nine land on it." % (len(hits), tried))
    for nm, g, n, sh, clo in hits:
        if g.startswith("drop"):
            print("     %-26s %-8s cells %-3d arity %d density %5.1f%% closes %s"
                  % (nm, g, n, sh[0], 100 * sh[2], clo))
    print("   The gravity slot is what bounds must LOSE to fill its own")
    print("   withdrawn fill. Recorded, not repaired.")
    print()

    print("3. K IS THE OBJECT; W, H, J, A ARE CHART DECORATION.")
    for keep in (("K", "W", "H", "J", "A"), ("K", "W", "J"), ("K", "W"), ("K",)):
        n, tot, rows = truncation_survival(keep)
        extra = ""
        if keep == ("K",) and rows:
            nm, gained, lost = rows[0]
            extra = "   (%s gained %s, lost %s)" % (nm, gained, lost or "nothing")
        print("   %-18s invariant in %d of %d%s"
              % ("(" + ",".join(keep) + ")", n, tot, extra))
    print("   K never LOSES a kind, so it is monotone under monotone")
    print("   re-charting. Under a non-monotone one it is not even that.")
    print()

    print("4. THE THREAD, AND IT IS K1.")
    for k, who in sorted(threads(R).items()):
        print("   K%d carried by exactly %d: %s" % (k, len(who), ", ".join(who)))
    print("   Only K0 is universal, so 'every index shares one refusal index'")
    print("   is FALSE. What exists is sharper: a rare kind is a thread between")
    print("   exactly the indexes carrying it, and K1 -- the warp obstruction's")
    print("   kind -- connects the bounds index to the periodic layout in three")
    print("   coordinates. THE THREAD IS ONE COMMIT OLD: bounds acquired K1 when")
    print("   completing that family stopped it closing.")
    print()
    print("5. NOT SEATED AS A TENTH INDEX. R is computed FROM the inventory, so")
    print("   seating it changes it -- a fixed point, not a formality. And a")
    print("   master index whose cells are charts seats a chart. Both are open.")


def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("refusal selftest")
    R = refusal_index()
    chk("nine seated indexes carry a refusal index", len(R), 9)
    chk("periodic layout 3-D, the richest", sorted(R["periodic layout 3-D"]),
        [0, 1, 3, 4, 5, 6, 7])
    chk("periodic layout 2-D, the poorest", sorted(R["periodic layout 2-D"]), [0, 4])
    chk("bounds", sorted(R["bounds"]), [0, 1, 2, 3, 4, 7])
    chk("the languages", sorted(R["the languages"]), [0, 4, 5, 7])

    # ---- K0 universal, K7 all but the densest
    chk("K0 is universal -- every index has a cell NOTHING refuses",
        sorted(universal(R)), [0])
    occ = occurrence(R)
    chk("K7 in eight of nine", len(occ[7]), 8)
    chk("and the exception is the DENSEST index",
        [nm for nm in R if 7 not in R[nm]], ["periodic layout 2-D"])
    chk("which is indeed the densest",
        max(R, key=lambda n: master.shape(master.inventory()[n])[2]),
        "periodic layout 2-D")

    # ---- the lattice
    mins, maxs, inc = lattice(R)
    chk("minimal: the two redundant periodic charts", mins,
        ["Janet (n+l, l, k)", "periodic layout 2-D"])
    chk("maximal", maxs,
        ["bounds", "exotic mechanisms", "periodic layout 3-D"])
    chk("twelve of thirty-six pairs incomparable -- a lattice", len(inc), 12)

    # ---- THE THREAD
    chk("K1 is carried by exactly two", occ[1],
        ["bounds", "periodic layout 3-D"])
    chk("K6 is carried by exactly two", occ[6],
        ["exotic mechanisms", "periodic layout 3-D"])
    chk("so periodic layout 3-D carries BOTH rare kinds",
        {1, 6} <= R["periodic layout 3-D"], True)
    # WITHDRAWN BY ITS OWN PIN. This first read "and it is the only index
    # missing K2", with an ad-hoc size filter to exclude the small sets. It is
    # false: FIVE of the nine lack K2, spacetimes (Petrov) among them, and the
    # filter was doing the work rather than the fact. The census is what stands.
    chk("K2 is carried by four, and five lack it",
        (len(occ[2]), sorted(nm for nm in R if 2 not in R[nm])),
        (4, ["Janet (n+l, l, k)", "periodic layout 2-D", "periodic layout 3-D",
             "spacetimes (Petrov)", "the languages"]))
    # NEGATIVE CONTROL: the conjecture as stated is FALSE and the pin says so.
    chk("THE NINE DO NOT SHARE ONE REFUSAL INDEX",
        len(set(map(frozenset, R.values()))), 9)

    # ---- section 2, the chart finding
    moved, chg, tot = cell_survival()
    chk("a zero-information coordinate moves five master cells", moved, 5)
    chk("and changes NO channel -- C survives a monotone re-charting", chg, 0)

    hits, tried = rechartings_hitting()
    chk("re-chartings tried", tried, 565)
    chk("re-chartings landing on the demanded cell", len(hits), 20)
    chk("and one is bounds MINUS its gravity slot",
        ("bounds", "drop3") in [(a, b) for a, b, _c, _s, _k in hits], True)
    chk("the energy-condition family lands there five ways",
        sum(1 for a, b, _c, _s, _k in hits
            if a == "energy-condition family"), 5)

    # ---- section 3, K is the object
    for keep, want in ((("K", "W", "H", "J", "A"), 3), (("K", "W", "J"), 6),
                       (("K", "W"), 6), (("K",), 8)):
        n, tot, rows = truncation_survival(keep)
        chk("(%s) invariant in %d of 9" % (",".join(keep), want), n, want)
    n, _t, rows = truncation_survival(("K",))
    chk("and K's one exception only GROWS, by K7",
        [(nm, g, l) for nm, g, l in rows], [("periodic layout 2-D", [(7,)], [])])

    print("refusal selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
