#!/usr/bin/env python3
r"""
fibred.py -- THE SHELL FIBRATION: an index whose base is n and whose fibres are
(l, k), and which occupies a channel the master index leaves empty.

M: "The x and y axes are statistics and information. The z axis is the product
of statistics and information - n - geometry, all elements. The l and k are axes
of n, each containing their own indexes at each value of n... And this identifies
which individual atomic value/measurement each index is dependent on n, l, or k.
Same laws and mechanisms apply in this new index as M1. The z axis ends up as a
sliding scale of n and it's indexes ascending."

    python3 fibred.py             the reading
    python3 fibred.py --selftest  fixtures

THE NAME IS OPEN.  M has not named this object.  "The shell fibration" is used
here descriptively -- base n, fibre (l, k) -- and should be replaced when ruled.

===============================================================================
0. THE CONSTRUCTION, AND WHY IT IS NOT JANET RE-LABELLED
===============================================================================

Every element has a DIFFERENTIATING ELECTRON, the one Madelung adds to take
Z - 1 to Z.  Give it its full address:

        n   the principal quantum number -- which shell
        l   the azimuthal quantum number -- which subshell
        k   the slot within that subshell, 0-based (the PRIOR occupancy)

    THE ADDRESS IS EXACT AND INJECTIVE.  Over the last complete n+l shell, 170
    elements map to 170 distinct (n, l, k) triples, one each.  No collision, no
    element unaddressed.  So this index loses nothing about which element is
    which -- unlike Janet, which is the same data re-coordinated as (n+l, l, k)
    and is a COARSENING of nothing but is a DIFFERENT chart.

JANET IS (n+l, l, k) AND THIS IS (n, l, k).  One coordinate differs, and it is
the one that matters: Janet's first coordinate is the FILL ORDER, this one's is
the SHELL.  Janet closes in all five languages; this closes in two.  The same
170 elements, the same three-coordinate shape, and a different channel -- which
is DOCKET 3's point made once more, from the other side.

===============================================================================
1. THE FIBRES ARE A PALINDROME, AND IT IS FORCED
===============================================================================

Read the index as a bundle: at each n, the fibre is the set of (l, k) that
occur there.  Their sizes, at the n+l <= 9 reach:

        n         1    2    3    4    5    6    7    8    9
        cells     2    8   18   32   50   32   18    8    2

    2m^2 ASCENDING, THEN THE MIRROR.  Two constraints bound l: the atom's own
    rule l < n, and the reach n + l <= S.  So l runs 0 .. min(n-1, S-n) and the
    fibre holds 2(min(n-1, S-n) + 1)^2 cells, which is symmetric about the
    middle shell BY CONSTRUCTION.  Where the two constraints change hands is
    where the palindrome turns.

    THE ASCENDING HALF IS THE SHELL CAPACITY 2n^2 -- 2, 8, 18, 32, 50 -- and
    that is the atom's rule alone.  The descending half is the reach.  A reader
    must not take the second half for a fact about elements; it is a fact about
    where the count stopped, and stopping at a COMPLETE shell is what makes it
    symmetric rather than ragged.

===============================================================================
2. THE SLIDING SCALE, AND IT IS THE PERIOD DETECTOR AGAIN
===============================================================================

M asked for "a sliding scale of n and it's indexes ascending".  Sweep n, take
the cumulative index up to each, and measure which languages close it:

        n <= 1   2 cells    K7   all five close
        n <= 2   10         K7
        n <= 3   28         K7
        n <= 4   60         K7
        n <= 5   110        K7
        n <= 6   142        K3   geometry and statistics only
        n <= 7   160        K3
        n <= 8   168        K3
        n <= 9   170        K3

    **K7 THEN K3.  THAT IS shells.py's PERIOD DETECTOR, FIRING ON A DIFFERENT
    SWEEP.**  That file's signature is "K = 7 at reach R and K = 3 at reach
    R + 1 iff R is a shell boundary", measured by sweeping Z over the Janet
    chart.  Here the sweep is over n, on a different chart, and the same
    transition appears -- once, at the turn of the palindrome.

    **AND IT LANDS ON THE FIRST SHRINKING SHELL AT EVERY REACH TESTED, nine of
    nine** -- n = floor(S/2) + 2, which is one past the palindrome's last peak.
    The transition is not near the turn; it IS the turn, taken from the far
    side.  While the fibres are still growing the cumulative index closes
    everything; the shell at which they begin to shrink is the shell at which
    order, algebra and information break, and they never recover.

        A CORRECTION MADE BY THE SELFTEST.  This first read ceil((S+1)/2),
        which is the PEAK, off by one -- the number came from reading the last
        shell still at K7 instead of the first at K3.  The pin failed and the
        formula is now floor(S/2) + 2.  Recorded because the off-by-one had a
        meaning: peak and first-shrink are different claims about what causes
        the break, and only the second is true.

    THE PAIR THAT SURVIVES IS K3 = down(geometry), the principal down-set of
    geometry -- the same pair shells.py finds surviving one past a shell limit,
    and for the same reason: geometry sits above statistics alone, while the
    order/algebra block sits above both minimal languages and takes information
    with it.

===============================================================================
3. IT OCCUPIES A CHANNEL THE MASTER INDEX LEAVES EMPTY
===============================================================================

The whole index closes in {geometry, statistics} -- K3 -- at cell (3, 26, 17)
on mi.py's admissible chart.

    THE MASTER INDEX OCCUPIES K0, K2 AND K7 AND NOTHING ELSE.  Five of the
    eight lawful channels are vacant there, and K3 is one of them.  This
    construction is the first object in this tree to sit in it.

    THE REACH CONTROL PASSES, AND IT HAD TO BE RUN.  The transition sits exactly
    where the reach begins truncating the fibres, so K3 could have been an
    artefact of where the count stopped.  It is not: K3 holds at EVERY complete
    shell reach from n+l <= 3 through n+l <= 11 -- nine consecutive reaches,
    12 cells to 292.  Only the two degenerate reaches (2 and 4 cells) give K7,
    and a two-cell index closes everything for want of room to fail.

===============================================================================
4. ARE l AND k TWO DIFFERENT LANGUAGES?  MEASURED, AND THE ANSWER IS NO
===============================================================================

M: "In this view l and k might each represent a different language of n, order
vs algebra, which is worth knowing."  Put to the test by projecting each axis
out and measuring what breaks:

        chart          cells   closes in                E(ord, alg, info)
        (n, l, k)      170     geometry, statistics     140, 140, 140
        (l, k)         50      ALL FIVE                   0,   0,   0
        (n, k)         82      geometry, statistics      40,  40,  40
        (n, l)         25      geometry, statistics      10,  10,  10

    **ORDER, ALGEBRA AND INFORMATION MOVE AS ONE BLOCK, ALWAYS.**  At every
    projection their deficits are identical -- 140, 140, 140 then 40, 40, 40
    then 10, 10, 10 -- so no projection separates order from algebra, and the
    order-vs-algebra reading of l against k is REFUTED at the closure level.
    Order and algebra agreeing is Clause B, already a theorem; that INFORMATION
    joins them here is the new part, and it is what K3 means.

    **THE LANGUAGE OF n IS CARRIED BY n.**  Drop n and all five close, E = 0
    across the board.  Drop l or drop k and the verdict does not move at all.
    So the three broken languages are broken BY THE SHELL COORDINATE, and l and
    k are not two languages between them -- they are two ways of being inside
    one.

    l AND k ARE STILL NOT INTERCHANGEABLE, and the asymmetry is in magnitude.
    Dropping l leaves a deficit of 40; dropping k leaves 10.  The (n, k) chart
    is four times as far from closing as the (n, l) chart, on 82 cells against
    25.  That is a real difference and it is NOT a difference of language.

===============================================================================
5. WHICH ATOMIC MEASUREMENT DEPENDS ON WHICH AXIS
===============================================================================

M: "this identifies which individual atomic value/measurement each index is
dependent on n, l, or k."  Since (n, l, k) is a bijection onto the elements,
every axis is trivially determined by all three; the question is the MINIMAL
subset that determines it.  Over the 170 addressed elements:

        {l}        capacity 2(2l+1),  magnetic multiplicity 2l+1,  block
        {k}        occupancy k+1
        {l, k}     subshell full?,  which half of the subshell (spin)
        {n, l}     n+l,  subshell label,  period,  Janet cell
        {n, l, k}  Z,  group,  n0,  Pauli B

    THE SHAPE OF A SUBSHELL IS AN l FACT, ITS FILLING IS A k FACT, AND WHETHER
    IT IS FINISHED NEEDS BOTH.  No axis but n itself needs n alone -- n never
    appears without l -- which is the dependence-table form of section 4's
    finding that n is the coordinate carrying the broken languages.

    GROUP NEEDS ALL THREE AND PERIOD NEEDS ONLY (n, l).  That is the sharpest
    row: the two coordinates of the drawn layout have different depths in this
    bundle, and the layout does not say so.

    AND n0 NEEDS ALL THREE, which is worth flagging because it reads as an l
    quantity: register 1141's n0 is "the first entirely unoccupied n AT THIS l",
    so the l is in its statement.  It still needs the whole address, because
    `populate.n0_of(Z, l)` reads the OBSERVED configuration of that particular
    element and two elements at the same (n, l) do not have the same one.  The
    Pauli bound B = min(p, n0-l-1) inherits the dependence.  A quantity's name
    is not its dependence.

===============================================================================
6. WHAT THIS FILE REFUSES TO MEASURE
===============================================================================

M offered two examples.  NEITHER IS TESTABLE HERE, and saying so is the point.

    "GRAVITY MAY BE A PRODUCT OF THE l AXIS OF n."  There is no gravitational
    measurement per element anywhere in this corpus.  The G slot in bounds.py is
    a CODING of whether a bound mentions gravity -- DOCKET 4 re-coded one
    integer in it -- not a quantity an atom has.  To test this an atomic
    gravitational axis would have to exist and be banked; none is.  NOT
    MEASURED, and not because the answer is no.

    "THE SPECTRA INDEXES ARE A PRODUCT OF THE k AXIS OF n."  The spectra axis is
    the series limit, and `tools/populate.LIMITS` banks FOUR of them --
    (Z, charge) = (3,3), (5,4), (5,5), (15,4) -- with three more reachable
    through banked deficits.  All are IONS at charges 3 to 5; not one is a
    neutral atom, and no two share an n.  Four points cannot establish a
    functional dependence on anything.  populate.py's own docstring says it
    first: "None is the honest answer and the common one."

    WHAT WOULD SETTLE THE SECOND: series limits banked for a run of neutral
    atoms spanning at least two subshells at one n, and two n at one l.  Twelve
    would probably do it.  The measurement is cheap once the data exists; it
    does not exist.

===============================================================================
7. SAME LAWS, CHECKED RATHER THAN ASSUMED
===============================================================================

M: "Same laws and mechanisms apply in this new index as M1."  They do, and the
check is not a formality -- it is what makes the object comparable at all.

    The seven lawful containments hold on this index and on every fibre.
    The channel is a lawful down-set (K3 = down(geometry)).
    Dilworth's |X| <= height x width holds: 170 <= 26 x 17.

    Every one of the nine fibres closes in ALL FIVE languages, without
    exception.  A fibre is a complete rectangle of slots -- l runs 0..L and k
    runs 0..2(2l+1)-1 with nothing missing -- and a complete staircase closes
    everything.  So the fibres carry no obstruction and ALL of the index's
    structure lives in how the fibres STACK, not in what they contain.
"""

import itertools
import sys

import hlaw
import master
import mi

# The last complete n+l shell, matching mi.JANET_REACH so the two charts are
# built over exactly the same elements and the comparison in section 0 is fair.
REACH = mi.JANET_REACH                      # 170

FIBRE_SIZES = (2, 8, 18, 32, 50, 32, 18, 8, 2)
TRANSITION_N = 6      # first n whose cumulative index is K3 -- and the first
                      # shell whose fibre SHRINKS. floor(S/2) + 2 at every reach.
LSYM = "spdfghi"

_pop = master._populate()


# ---------------------------------------------------------------------------
# the construction
# ---------------------------------------------------------------------------

def address(Z):
    """(n, l, k) of Z's differentiating electron, or None.

    k is the PRIOR occupancy of the subshell -- the 0-based slot this electron
    takes.  Identical to the k of mi.janet(), which reads the same triple and
    charts it as (n+l, l, k); this is the one place the two charts agree.
    """
    now = {(n, l): o for n, l, o in _pop.aufbau_config(Z)}
    prev = ({(n, l): o for n, l, o in _pop.aufbau_config(Z - 1)}
            if Z > 1 else {})
    g = sorted((n, l) for (n, l), o in now.items() if o > prev.get((n, l), 0))
    if not g:
        return None
    n, l = g[-1]
    return (n, l, prev.get((n, l), 0))


def addresses(reach=REACH):
    """{Z: (n, l, k)} over the reach."""
    return {Z: a for Z in range(1, reach + 1) if (a := address(Z))}


def index(reach=REACH):
    """The shell fibration as a set of cells."""
    return frozenset(addresses(reach).values())


def fibre(n, reach=REACH):
    """The (l, k) index sitting at shell n."""
    return frozenset((l, k) for a, l, k in index(reach) if a == n)


def cumulative(n, reach=REACH):
    """The index restricted to shells 1..n -- one stop on the sliding scale."""
    return frozenset(t for t in index(reach) if t[0] <= n)


def shells(reach=REACH):
    """The n values the index reaches."""
    return sorted({t[0] for t in index(reach)})


# ---------------------------------------------------------------------------
# measurement
# ---------------------------------------------------------------------------

def closers(X):
    """Which languages close X.  hlaw's operators, never reimplemented."""
    X = frozenset(X)
    cl, _box = hlaw.closures(X)
    return sorted(L for L in hlaw.LANGS if len(cl[L]) == len(X))


def deficits(X):
    """{language: E} -- cells the operator generates that X does not hold."""
    X = frozenset(X)
    cl, _box = hlaw.closures(X)
    return {L: len(cl[L]) - len(X) for L in sorted(hlaw.LANGS)}


def sweep(reach=REACH):
    """[(n, cells, K, closers)] -- the sliding scale, ascending."""
    return [(n, len(C), mi.K(C), closers(C))
            for n in shells(reach) for C in [cumulative(n, reach)]]


def fibre_table(reach=REACH):
    """[(n, cells, K, closers)] -- each fibre measured on its own."""
    return [(n, len(F), mi.K(F), closers(F))
            for n in shells(reach) for F in [fibre(n, reach)]]


def projections(reach=REACH):
    """{dropped axis: (cells, K, closers, deficits)} -- section 4's table."""
    X = index(reach)
    out = {"none": (len(X), mi.K(X), closers(X), deficits(X))}
    for name, f in (("n", lambda t: (t[1], t[2])),
                    ("l", lambda t: (t[0], t[2])),
                    ("k", lambda t: (t[0], t[1]))):
        P = frozenset(f(t) for t in X)
        out[name] = (len(P), mi.K(P), closers(P), deficits(P))
    return out


def reach_control(reaches=None):
    """[(shell, reach, cells, K, transition n)] -- is K3 an artefact of where
    the count stopped?

    THIS CONTROL HAD TO BE RUN.  The K7 -> K3 transition sits exactly where the
    reach starts truncating the fibres, so the channel could have been a fact
    about the truncation.  Run over every complete shell.
    """
    import shells as _sh
    ends = _sh.shell_ends()
    reaches = ends[:11] if reaches is None else reaches
    out = []
    for S, R in enumerate(reaches, start=1):
        X = index(R)
        if not X:
            continue
        prev, trans = None, None
        for n in sorted({t[0] for t in X}):
            k = mi.K(frozenset(t for t in X if t[0] <= n))
            if prev is not None and k != prev and trans is None:
                trans = n
            prev = k
        out.append((S, R, len(X), mi.K(X), trans))
    return out


# ---------------------------------------------------------------------------
# section 5 -- which axis determines which measurement
# ---------------------------------------------------------------------------

def _axes():
    """{name: f(Z, n, l, k)} -- the atomic measurements with real coverage.

    EVERY ONE IS EITHER MADELUNG-DERIVED OR READ FROM A SEATED MEMBER.  Nothing
    here is invented, and the two axes M named -- gravity and the spectra -- are
    ABSENT BY MEASUREMENT rather than by oversight.  See section 6.
    """
    def n0(Z, n, l, k):
        try:
            return _pop.n0_of(Z, l)
        except Exception:
            return None

    def pauli_B(Z, n, l, k):
        try:
            v = _pop.n0_of(Z, l)
            return None if v is None else min(l, v - l - 1)
        except Exception:
            return None

    return {
        "Z": lambda Z, n, l, k: Z,
        "n": lambda Z, n, l, k: n,
        "l (block)": lambda Z, n, l, k: l,
        "k (slot)": lambda Z, n, l, k: k,
        "n+l (Madelung)": lambda Z, n, l, k: n + l,
        "capacity 2(2l+1)": lambda Z, n, l, k: 2 * (2 * l + 1),
        "multiplicity 2l+1": lambda Z, n, l, k: 2 * l + 1,
        "occupancy k+1": lambda Z, n, l, k: k + 1,
        "subshell label": lambda Z, n, l, k: "%d%s" % (n, LSYM[l]),
        "subshell full?": lambda Z, n, l, k: k + 1 == 2 * (2 * l + 1),
        "upper half (spin)": lambda Z, n, l, k: k >= (2 * l + 1),
        "period": lambda Z, n, l, k: (_pop.period_of(Z) if Z <= 118 else None),
        "group": lambda Z, n, l, k: (_pop.group_of(Z) if Z <= 118 else None),
        "Janet cell (n+l,l)": lambda Z, n, l, k: (n + l, l),
        "n0 (register 1141)": n0,
        "Pauli B (register 1141)": pauli_B,
    }


def dependence(reach=REACH):
    """{axis: [minimal determining subsets of {n, l, k}]}.

    (n, l, k) is a bijection onto the elements, so EVERY axis is determined by
    all three and that fact is empty.  What is not empty is the MINIMAL subset,
    and this returns every minimal one -- there can be more than a single answer
    and collapsing them to one would be a choice, not a measurement.
    """
    A = addresses(reach)
    subs = [s for r in (1, 2, 3) for s in itertools.combinations("nlk", r)]
    out = {}
    for name, f in _axes().items():
        vals = {}
        for Z, (n, l, k) in A.items():
            v = f(Z, n, l, k)
            if v is not None:
                vals[Z] = v
        if not vals:
            out[name] = None
            continue
        det = []
        for S in subs:
            groups = {}
            ok = True
            for Z, v in vals.items():
                n, l, k = A[Z]
                key = tuple({"n": n, "l": l, "k": k}[c] for c in S)
                if groups.setdefault(key, v) != v:
                    ok = False
                    break
            if ok:
                det.append(S)
        out[name] = [S for S in det if not any(set(T) < set(S) for T in det)]
    return out


# ---------------------------------------------------------------------------
# section 7 -- the laws
# ---------------------------------------------------------------------------

def laws_hold(reach=REACH):
    """(lawful containments broken on the index, on any fibre, Dilworth ok)."""
    X = index(reach)
    def broken(S):
        S = frozenset(S)
        cl, _ = hlaw.closures(S)
        E = {L: len(cl[L]) - len(S) for L in hlaw.LANGS}
        return sorted((a, b) for a, b in hlaw.LAWFUL if E[a] > E[b])
    bad_fibres = sorted(n for n in shells(reach) if broken(fibre(n, reach)))
    return broken(X), bad_fibres, len(X) <= mi.height(X) * mi.width(X)


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("THE SHELL FIBRATION -- base n, fibre (l, k)")
    print("=" * 74)
    print()
    X = index()
    A = addresses()
    print("0. THE ADDRESS. Every element's differentiating electron as (n, l, k).")
    print("   elements addressed  %d" % len(A))
    print("   distinct cells      %d" % len(X))
    print("   injective           %s   (no element shares an address)"
          % (len(A) == len(X)))
    print("   Janet charts the SAME electrons as (n+l, l, k) and closes in all")
    print("   five; this charts them as (n, l, k) and closes in two.")
    print()

    print("1. THE FIBRES ARE A PALINDROME.")
    ft = fibre_table()
    print("   n       " + "".join("%5d" % n for n, _c, _k, _cl in ft))
    print("   cells   " + "".join("%5d" % c for _n, c, _k, _cl in ft))
    print("   2m^2 ascending then the mirror: l runs 0..min(n-1, S-n), so the")
    print("   atom's rule bounds it on the way up and the reach on the way down.")
    print()

    print("2. THE SLIDING SCALE -- cumulative index, n ascending.")
    for n, c, k, cl in sweep():
        print("   n <= %d  %4d cells   K%-2d  %s" % (n, c, k, ", ".join(cl)))
    print("   K7 THEN K3 -- shells.py's period detector, on a different sweep,")
    print("   firing once, exactly at the turn of the palindrome.")
    print()

    print("3. THE CHANNEL, AND THE CONTROL THAT HAD TO BE RUN.")
    print("   whole index   %d cells   K%d   cell %s   closes %s"
          % (len(X), mi.K(X), mi.cell(X), ", ".join(closers(X))))
    occupied = sorted({mi.K(v) for v in mi.inventory().values()})
    print("   the master index occupies K%s and nothing else."
          % ", K".join(map(str, occupied)))
    print("   K%d IS VACANT THERE. This is the first object to sit in it."
          % mi.K(X))
    print()
    print("   reach control -- is K3 an artefact of where the count stopped?")
    for S, R, c, k, t in reach_control():
        print("     n+l <= %-2d  Z <= %-3d  %4d cells   K%-2d  transition n=%s"
              % (S, R, c, k, t if t else "-"))
    print("   K3 at nine consecutive complete reaches. Only the two degenerate")
    print("   ones give K7, and a 2-cell index closes everything for want of")
    print("   room to fail. THE CHANNEL IS NOT AN ARTEFACT OF THE REACH.")
    print()

    print("4. ARE l AND k TWO LANGUAGES? NO.")
    P = projections()
    print("   %-14s %6s  %-4s %-26s %s"
          % ("chart", "cells", "K", "closes in", "E(order, algebra, info)"))
    for key, label in (("none", "(n, l, k)"), ("n", "(l, k)"),
                       ("l", "(n, k)"), ("k", "(n, l)")):
        c, k, cl, E = P[key]
        print("   %-14s %6d  K%-3d %-26s %d, %d, %d"
              % (label, c, k, ", ".join(cl) or "nothing",
                 E["order"], E["algebra"], E["information"]))
    print("   ORDER, ALGEBRA AND INFORMATION MOVE AS ONE BLOCK at every")
    print("   projection, so nothing here separates order from algebra and the")
    print("   order-vs-algebra reading of l against k is REFUTED.")
    print("   Drop n and all five close. THE LANGUAGE OF n IS CARRIED BY n.")
    print("   l and k still differ, in MAGNITUDE not in language: 40 against 10.")
    print()

    print("5. WHICH ATOMIC MEASUREMENT DEPENDS ON WHICH AXIS.")
    dep = dependence()
    for name in sorted(dep, key=lambda s: (len(dep[s][0]) if dep[s] else 9, s)):
        d = dep[name]
        print("   %-26s %s" % (name,
              " or ".join("{" + ",".join(S) + "}" for S in d) if d
              else "NOT DETERMINED"))
    print("   Shape is an l fact, filling is a k fact, finished needs both.")
    print("   NO AXIS BUT n ITSELF needs n alone -- n never appears without l.")
    print("   Group needs all three; period needs only (n,l). And n0 needs all")
    print("   three though its NAME says l: it reads the observed configuration")
    print("   of that element. A quantity's name is not its dependence.")
    print()

    print("6. WHAT THIS FILE REFUSES TO MEASURE.")
    print("   GRAVITY ON THE l AXIS -- there is no gravitational measurement")
    print("   per element in this corpus. bounds.py's G slot codes whether a")
    print("   BOUND mentions gravity, not a quantity an atom has. NOT MEASURED,")
    print("   and not because the answer is no.")
    print("   SPECTRA ON THE k AXIS -- populate.LIMITS banks FOUR series limits,")
    print("   all ions at charges 3 to 5, no two sharing an n. Four points")
    print("   cannot establish a dependence on anything. What would settle it:")
    print("   limits for a run of neutral atoms spanning two subshells at one n")
    print("   and two n at one l. Twelve would probably do.")
    print()

    print("7. SAME LAWS, CHECKED.")
    bad, badf, dil = laws_hold()
    print("   lawful containments broken on the index   %s" % (bad or "none"))
    print("   fibres breaking any lawful containment    %s" % (badf or "none"))
    print("   Dilworth |X| <= h x w                     %s  (%d <= %d x %d)"
          % (dil, len(X), mi.height(X), mi.width(X)))
    print("   Every fibre closes in ALL FIVE. A fibre is a complete rectangle")
    print("   of slots, and a complete staircase closes everything -- so ALL")
    print("   the structure is in how the fibres STACK, not what they contain.")
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

    print("fibred selftest")
    A, X = addresses(), index()

    # ---- the address is exact
    chk("170 elements addressed over the n+l <= 9 reach", len(A), 170)
    chk("and 170 distinct (n, l, k) -- INJECTIVE", len(X), 170)
    chk("hydrogen is (1, 0, 0)", address(1), (1, 0, 0))
    chk("helium is (1, 0, 1) -- same subshell, next slot", address(2), (1, 0, 1))
    chk("lithium opens shell 2", address(3), (2, 0, 0))
    # k IS THE PRIOR OCCUPANCY, not the new one. Off by one here would silently
    # shift every fibre, so it is pinned against a subshell whose end is known.
    chk("neon closes 2p at k = 5, not 6", address(10), (2, 1, 5))

    # ---- the palindrome
    chk("the fibre sizes", tuple(c for _n, c, _k, _cl in fibre_table()),
        FIBRE_SIZES)
    chk("and they are a palindrome",
        tuple(FIBRE_SIZES) == tuple(reversed(FIBRE_SIZES)), True)
    chk("the ascending half is the shell capacity 2n^2",
        [c for c in FIBRE_SIZES[:5]], [2 * n * n for n in range(1, 6)])

    # ---- the sliding scale
    sw = sweep()
    chk("cumulative K, n = 1..9", [k for _n, _c, k, _cl in sw],
        [7, 7, 7, 7, 7, 3, 3, 3, 3])
    chk("the transition is K7 -> K3 and happens ONCE",
        sum(1 for i in range(1, len(sw)) if sw[i][2] != sw[i - 1][2]), 1)
    chk("and it lands at n = 6", next(n for n, _c, k, _cl in sw if k == 3),
        TRANSITION_N)
    # THE TURN OF THE PALINDROME, not merely near it.
    chk("which is the LAST PEAK of the palindrome",
        TRANSITION_N - 1, FIBRE_SIZES.index(max(FIBRE_SIZES)) + 1)

    # ---- every fibre closes everything
    chk("every one of the nine fibres closes in ALL FIVE",
        sorted({k for _n, _c, k, _cl in fibre_table()}), [7])

    # ---- the channel, and the control
    chk("the whole index closes in geometry and statistics",
        closers(X), ["geometry", "statistics"])
    chk("which is K3 = down(geometry)", mi.K(X), 3)
    chk("its cell on the admissible chart", mi.cell(X), (3, 26, 17))
    occupied = sorted({mi.K(v) for v in mi.inventory().values()})
    chk("the master index occupies only K0, K2, K7", occupied, [0, 2, 7])
    chk("SO K3 IS VACANT THERE AND THIS IS THE FIRST OCCUPANT",
        mi.K(X) not in occupied, True)
    # THE CONTROL. K3 could have been a fact about where the count stopped.
    rc = reach_control()
    chk("K3 at every complete reach from n+l <= 3 to <= 11",
        [k for S, _R, _c, k, _t in rc if S >= 3], [3] * 9)
    chk("and the two degenerate reaches are K7 on 2 and 4 cells",
        [(c, k) for S, _R, c, k, _t in rc if S < 3], [(2, 7), (4, 7)])
    # THE TRANSITION IS THE FIRST SHRINKING SHELL, at every reach. An earlier
    # reading of this pin said ceil((S+1)/2), which is the PEAK -- off by one,
    # because it read the last shell still at K7 rather than the first at K3.
    # The selftest caught it. floor(S/2) + 2 is peak + 1 for every S >= 3.
    chk("the transition is at floor(S/2) + 2 at every reach",
        [t for S, _R, _c, _k, t in rc if S >= 3],
        [S // 2 + 2 for S in range(3, 12)])
    chk("and that is always the FIRST SHELL WHOSE FIBRE SHRINKS",
        all(t == 1 + max(range(1, len({x[0] for x in index(R)}) + 1),
                         key=lambda n: (len([1 for x in index(R) if x[0] == n]), n))
            for S, R, _c, _k, t in rc if S >= 3), True)

    # ---- l against k
    P = projections()
    chk("dropping n closes ALL FIVE", P["n"][2],
        ["algebra", "geometry", "information", "order", "statistics"])
    chk("dropping l does not move the verdict", P["l"][2],
        ["geometry", "statistics"])
    chk("nor does dropping k", P["k"][2], ["geometry", "statistics"])
    # THE REFUTATION. If l and k were order and algebra, some projection would
    # separate them. None does -- the three broken languages move as one block.
    chk("order, algebra and information are EQUAL at every projection",
        [len({E["order"], E["algebra"], E["information"]})
         for _c, _k, _cl, E in P.values()], [1, 1, 1, 1])
    chk("so the order-vs-algebra reading of l against k is REFUTED",
        any(P[a][3]["order"] != P[a][3]["algebra"] for a in P), False)
    chk("l and k differ in MAGNITUDE only -- 40 against 10",
        (P["l"][3]["order"], P["k"][3]["order"]), (40, 10))
    chk("and in size -- (n,k) is 82 cells, (n,l) is 25",
        (P["l"][0], P["k"][0]), (82, 25))

    # ---- dependence
    dep = dependence()
    chk("capacity is an l fact alone", dep["capacity 2(2l+1)"], [("l",)])
    chk("multiplicity likewise", dep["multiplicity 2l+1"], [("l",)])
    chk("occupancy is a k fact alone", dep["occupancy k+1"], [("k",)])
    chk("whether the subshell is full needs BOTH l and k",
        dep["subshell full?"], [("l", "k")])
    chk("n+l needs n and l", dep["n+l (Madelung)"], [("n", "l")])
    chk("period needs (n, l)", dep["period"], [("n", "l")])
    chk("but GROUP needs all three", dep["group"], [("n", "l", "k")])
    chk("and Z needs all three, which is injectivity restated",
        dep["Z"], [("n", "l", "k")])
    # NOTHING NEEDS n ALONE. The dependence-table form of section 4's finding.
    chk("NO axis but n itself is determined by n alone",
        [a for a, d in dep.items() if d == [("n",)] and a != "n"], [])
    # NAMED FOR l, DEPENDENT ON ALL THREE. register 1141's n0 is "the first
    # entirely unoccupied n at this l", so l is in its statement -- but n0_of
    # reads the OBSERVED configuration of that element, and two elements at the
    # same (n, l) do not share one. Pinned because the name misleads.
    chk("n0 needs all three despite being named for l",
        dep["n0 (register 1141)"], [("n", "l", "k")])
    chk("and the Pauli bound inherits that",
        dep["Pauli B (register 1141)"], [("n", "l", "k")])

    # ---- the laws
    bad, badf, dil = laws_hold()
    chk("no lawful containment is broken on the index", bad, [])
    chk("nor on any fibre", badf, [])
    chk("Dilworth holds", dil, True)

    print("fibred selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
