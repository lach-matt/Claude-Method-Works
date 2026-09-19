#!/usr/bin/env python3
r"""
charts3.py -- ARE THERE OTHER MASTER INDEXES?  A census of every chart the
seated element address admits, and the law that decides each one's channel.

M: "are there any other MIs we can derive from given information?"

    python3 charts3.py             the reading
    python3 charts3.py --selftest  fixtures

THE SHORT ANSWER IS NO, AND THE LONG ANSWER IS A LAW.  Every chart built from
the differentiating electron's own coordinates lands in one of five channels;
only three of those are reachable without throwing away which element is which;
and WHICH ONE a faithful chart lands in is decided by a single feature of its
coordinate list.  The three master indexes already built are representatives of
that classification, not arbitrary picks from an open field.

===============================================================================
1. THE COORDINATE POOL, AND WHY THESE NINE
===============================================================================

Every coordinate here is a function of the address (n, l, k) alone -- no new
data, no new convention, nothing fetched.  That is the whole point: the question
is what is DERIVABLE FROM GIVEN INFORMATION.

        n       the shell                     l       the subshell
        k       the slot, 0-based             n+l     the Madelung fill order
        n-l     the radial-node count         cap     2(2l+1), subshell capacity
        occ     k+1, the occupancy            m       k mod (2l+1), magnetic slot
        spin    k div (2l+1), which half of the subshell

    `cap` is a function of l alone and `occ` of k alone, so they are MONOTONE
    RELABELLINGS of those axes and are included to test exactly that.  `m` and
    `spin` decompose k and are NOT monotone in it; `n-l` is included because it
    is the only other linear combination of n and l the corpus names.

===============================================================================
2. THE CENSUS
===============================================================================

Over every subset of size 2 to 5 -- 372 charts:

        channels reached by ANY chart        K0, K2, K3, K6, K7
        channels reached INJECTIVELY         K0, K3, K7
        NEVER reached at all                 K1, K4, K5
        reachable ONLY by coarsening         K2, K6

    **THREE OF THE EIGHT LAWFUL CHANNELS CANNOT BE REACHED AT ALL** from this
    address, by any chart in the pool.  K1 = down(information), K4 and K5 are
    lawful positions in the lattice and no arrangement of these coordinates
    produces one.  That is a statement about the ELEMENTS, not about the
    lattice: information alone never closes an element chart here.

    **AND TWO MORE COST YOU THE ELEMENTS.**  K2 and K6 occur, but never on a
    chart that keeps 170 distinct cells.  Every chart reaching them collapses
    elements together.  DOCKET 10 turns on exactly this for K6.

===============================================================================
3. THE LAW: A FAITHFUL CHART'S CHANNEL IS DECIDED BY ITS SHELL COORDINATES
===============================================================================

Call n, n+l and n-l the SHELL COORDINATES -- the three the pool offers for
"which shell", differing only in how l is mixed in.  Then, for every injective
chart carrying no non-monotone redundancy:

        carries n+l and neither other        ->  K7   all five close
        carries n or n-l and neither other   ->  K3   geometry, statistics
        carries two or more of the three     ->  K0   nothing closes

    **86 INJECTIVE CHARTS, ARITY 2 TO 5, NO EXCEPTIONS.**  The rest of the
    coordinate list -- which of l, k, cap, occ, m, spin you take -- does not
    affect the channel at all.  Only the shell coordinate does.

    WHY TWO IS WORSE THAN ONE.  Carrying two shell coordinates determines both
    n and l outright, so the chart has a redundancy between its own axes, and
    the redundancy is not monotone: n and n-l disagree in direction as l grows.
    A non-monotone redundant coordinate destroys closure -- that is DOCKET 3's
    finding, arrived at here from the other end.

    THE EXCLUDED CHARTS ARE THE SAME EFFECT.  112 charts are set aside: those
    carrying both a k-DETERMINANT (k or occ) and a k-DECOMPOSITION (m or spin).
    `m` is k mod (2l+1) and is non-monotone in k, so such a chart carries a
    non-monotone redundancy by construction and falls to K0 whatever its shell
    coordinate.  They are excluded from the law rather than counted against it,
    and the exclusion is stated so a reader can check it is not curve-fitting:
    the rule that excludes them is DOCKET 3's, written before this census.

===============================================================================
4. SO WHAT ARE THE OTHER MASTER INDEXES?
===============================================================================

    THERE IS NO FOURTH FAITHFUL CHANNEL.  The two fibrations already occupy the
    only two channels a faithful element chart can reach that close anything:
    fibred.py at K3 and madelung.py at K7.  The third reachable channel is K0,
    which closes nothing, and every chart landing there does so because it
    carries a redundancy.

    WHAT IS GENUINELY NEW IS THE CLASSIFICATION, not another index.  Before this
    census the two fibrations were two constructions that happened to differ.
    After it they are REPRESENTATIVES OF A COMPLETE CLASSIFICATION of what the
    seated address can produce.  There are 8 injective K3 charts and 4 injective
    K7 charts at arity 3; picking a different member of either class changes
    nothing measurable.

    AND THE HONEST QUALIFICATION: this is a census of ONE POOL.  A coordinate
    outside it -- anything needing data the address does not carry -- is not
    covered, and section 5 names the ones that would matter.

===============================================================================
5. WHAT A GENUINELY NEW MASTER INDEX WOULD NEED
===============================================================================

Not a new arrangement of these coordinates.  A new SOURCE.  Three exist in the
corpus and each is a real candidate this file does not build:

    THE IONISATION LADDER.  `populate.ionisation_cells(Z)` returns a cell per
    charge stage -- an index over IONS, not neutral elements, and therefore a
    different object with a different member set.  It is the strongest
    candidate: the data is banked and computable for Z <= 108.

    THE 26 AXES THEMSELVES.  An index whose members are the MEASUREMENTS rather
    than the things measured, charted by status (READ, DERIVED, PINNED, RECON)
    and by which axis they depend on.  fibred.py's dependence table is the first
    row of it.

    THE REFUSAL INDEX.  refusal.py computes R(X) for every seated index and
    explicitly declines to seat it, because R is computed FROM the inventory and
    seating it changes the inventory -- a fixed point, not a formality.  That
    refusal stands.

NOTHING IS SEATED ON THE STRENGTH OF THIS FILE.  It is a census and a law about
what the existing address can produce, and its main use is negative: it says
where NOT to look for a fourth index.
"""

import itertools
import sys

import fibred
import hlaw
import mi

SHELL_COORDS = ("n", "n+l", "n-l")
K_DETERMINANT = ("k", "occ")
K_DECOMPOSITION = ("m", "spin")

COORDS = {
    "n":    lambda n, l, k: n,
    "l":    lambda n, l, k: l,
    "k":    lambda n, l, k: k,
    "n+l":  lambda n, l, k: n + l,
    "n-l":  lambda n, l, k: n - l,
    "cap":  lambda n, l, k: 2 * (2 * l + 1),
    "occ":  lambda n, l, k: k + 1,
    "m":    lambda n, l, k: k % (2 * l + 1),
    "spin": lambda n, l, k: k // (2 * l + 1),
}


_ADDR = {}
_CHART = {}


def _addr(reach):
    """fibred.addresses(), memoised -- it walks 170 aufbau configurations and
    this file asks for it several hundred times."""
    if reach not in _ADDR:
        _ADDR[reach] = fibred.addresses(reach)
    return _ADDR[reach]


def chart(combo, reach=fibred.REACH):
    """The set of cells this coordinate list produces over the address."""
    key = (tuple(combo), reach)
    if key not in _CHART:
        _CHART[key] = frozenset(tuple(COORDS[c](*t) for c in combo)
                                for t in _addr(reach).values())
    return _CHART[key]


def combos(lo=2, hi=5):
    names = list(COORDS)
    return [c for r in range(lo, hi + 1)
            for c in itertools.combinations(names, r)]


def injective(combo, reach=fibred.REACH):
    return len(chart(combo, reach)) == len(_addr(reach))


def excluded(combo):
    """True when the chart carries a NON-MONOTONE redundancy by construction.

    m = k mod (2l+1) is not monotone in k, so a chart holding both k (or occ)
    and m (or spin) has a non-monotone redundant coordinate and falls to K0
    whatever else it holds.  DOCKET 3 established that effect BEFORE this
    census, which is why these are excluded from the law rather than counted
    against it.
    """
    s = set(combo)
    return bool(s & set(K_DETERMINANT)) and bool(s & set(K_DECOMPOSITION))


def predict(combo):
    """The law's prediction, or None where the law does not speak."""
    sh = set(combo) & set(SHELL_COORDS)
    if not sh:
        return None
    if len(sh) >= 2:
        return 0
    return 7 if sh == {"n+l"} else 3


_CENSUS = {}


def census(lo=2, hi=5, reach=fibred.REACH):
    """{'all': {K: n}, 'inj': {K: n}} -- channels reached, and how often.

    MEMOISED: 372 closures over boxes up to five coordinates wide is about
    seven minutes, and other instruments ask for this result.
    """
    key = (lo, hi, reach)
    if key in _CENSUS:
        return _CENSUS[key]
    allK, injK = {}, {}
    for c in combos(lo, hi):
        X = chart(c, reach)
        k = mi.K(X)
        allK[k] = allK.get(k, 0) + 1
        if len(X) == len(_addr(reach)):
            injK[k] = injK.get(k, 0) + 1
    _CENSUS[key] = {"all": allK, "inj": injK}
    return _CENSUS[key]


def law(lo=2, hi=5, reach=fibred.REACH):
    """([(combo, shell coords, K, predicted)], violations, excluded count)."""
    rows, bad, exc = [], [], 0
    for c in combos(lo, hi):
        if not injective(c, reach):
            continue
        if excluded(c):
            exc += 1
            continue
        want = predict(c)
        if want is None:
            continue
        got = mi.K(chart(c, reach))
        rows.append((c, sorted(set(c) & set(SHELL_COORDS)), got, want))
        if got != want:
            bad.append((c, got, want))
    return rows, bad, exc


def representatives(arity=3, reach=fibred.REACH):
    """{K: [injective charts of that arity]} -- who could stand in for whom."""
    out = {}
    for c in itertools.combinations(list(COORDS), arity):
        if not injective(c, reach):
            continue
        out.setdefault(mi.K(chart(c, reach)), []).append(c)
    return out


def seated_are_members():
    """(the shell fibration's combo and channel, Janet's) -- both in the census."""
    return ((("n", "l", "k"), mi.K(chart(("n", "l", "k")))),
            (("l", "k", "n+l"), mi.K(chart(("l", "k", "n+l")))))


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("ARE THERE OTHER MASTER INDEXES?  A census of the seated address")
    print("=" * 74)
    print()
    print("1. THE POOL. Nine coordinates, every one a function of (n, l, k)")
    print("   alone -- no new data, no new convention.")
    print("   " + "  ".join(COORDS))
    print()

    c = census()
    tot = len(combos())
    print("2. THE CENSUS, over %d charts of arity 2 to 5." % tot)
    print("   channels reached by ANY chart   %s"
          % ", ".join("K%d" % k for k in sorted(c["all"])))
    print("   reached INJECTIVELY             %s"
          % ", ".join("K%d" % k for k in sorted(c["inj"])))
    print("   NEVER reached at all            %s"
          % ", ".join("K%d" % k for k in range(8) if k not in c["all"]))
    print("   reachable ONLY by coarsening    %s"
          % ", ".join("K%d" % k for k in sorted(c["all"]) if k not in c["inj"]))
    print()
    print("   THREE LAWFUL CHANNELS CANNOT BE REACHED. K1 = down(information),")
    print("   K4 and K5 are lawful lattice positions and no arrangement of")
    print("   these coordinates produces one. That is a fact about the")
    print("   elements, not the lattice.")
    print()

    rows, bad, exc = law()
    print("3. THE LAW. For an injective chart with no non-monotone redundancy,")
    print("   the channel is decided by its SHELL COORDINATES and nothing else.")
    print("     carries n+l alone            -> K7")
    print("     carries n or n-l alone       -> K3")
    print("     carries two or more of three -> K0")
    print("   tested on %d injective charts, arity 2 to 5" % len(rows))
    print("   violations: %s" % (bad or "NONE"))
    print("   excluded (k with its own non-monotone decomposition): %d" % exc)
    print()
    by = {}
    for combo, sh, got, _w in rows:
        by.setdefault(got, []).append(combo)
    for k in sorted(by):
        print("   K%d: %d charts" % (k, len(by[k])))
    print()

    print("4. THE THREE INDEXES ARE REPRESENTATIVES, NOT PICKS.")
    for combo, k in seated_are_members():
        who = "fibred.py" if combo == ("n", "l", "k") else "madelung.py"
        print("   %-12s (%-12s) -> K%d" % (who, ", ".join(combo), k))
    reps = representatives(3)
    for k in sorted(reps):
        print("   K%d at arity 3: %d injective charts, any one interchangeable"
              % (k, len(reps[k])))
    print("   THERE IS NO FOURTH FAITHFUL CHANNEL. The only channels a faithful")
    print("   element chart reaches are K0 (closes nothing), K3 and K7, and the")
    print("   two fibrations already hold the two that close something.")
    print()

    print("5. A GENUINELY NEW INDEX NEEDS A NEW SOURCE, NOT A NEW ARRANGEMENT.")
    print("   THE IONISATION LADDER -- populate.ionisation_cells(Z), an index")
    print("   over IONS rather than neutral elements. Banked, computable for")
    print("   Z <= 108, and the strongest candidate. NOT BUILT HERE.")
    print("   THE 26 AXES THEMSELVES -- an index whose members are the")
    print("   measurements. fibred.py's dependence table is its first row.")
    print("   THE REFUSAL INDEX -- refusal.py declines to seat it, because R is")
    print("   computed FROM the inventory. That refusal stands.")
    print()
    print("   Nothing is seated on the strength of this file. Its main use is")
    print("   negative: it says where NOT to look for a fourth index.")
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

    print("charts3 selftest")

    chk("nine coordinates in the pool", len(COORDS), 9)
    chk("and every one is a function of the address alone",
        all(callable(f) and f(3, 1, 2) is not None for f in COORDS.values()),
        True)
    chk("charts of arity 2 to 5", len(combos()), 372)

    # ---- the census
    c = census()
    chk("channels reached by ANY chart", sorted(c["all"]), [0, 2, 3, 6, 7])
    chk("channels reached INJECTIVELY", sorted(c["inj"]), [0, 3, 7])
    # THE NEGATIVE RESULT, and it is the strongest thing here.
    chk("K1, K4 and K5 are NEVER reached",
        [k for k in range(8) if k not in c["all"]], [1, 4, 5])
    chk("K2 and K6 are reachable ONLY by coarsening",
        [k for k in sorted(c["all"]) if k not in c["inj"]], [2, 6])

    # ---- the law
    rows, bad, exc = law()
    chk("the law is tested on this many injective charts", len(rows), 86)
    chk("AND HAS NO VIOLATIONS", bad, [])
    chk("charts excluded for carrying a non-monotone redundancy", exc, 112)
    # The exclusion rule is DOCKET 3's and predates this census, so it is not
    # curve-fitting. Pinned by showing an excluded chart really does fall to K0.
    chk("an excluded chart falls to K0, as DOCKET 3 predicts",
        (excluded(("n", "l", "k", "m")), mi.K(chart(("n", "l", "k", "m")))),
        (True, 0))
    chk("while the same chart without m is K3",
        mi.K(chart(("n", "l", "k"))), 3)

    # ---- the law's three clauses, each witnessed
    chk("n+l alone -> K7", mi.K(chart(("l", "k", "n+l"))), 7)
    chk("n alone -> K3", mi.K(chart(("n", "l", "k"))), 3)
    chk("n-l alone -> K3 too", mi.K(chart(("l", "k", "n-l"))), 3)
    chk("two shell coordinates -> K0", mi.K(chart(("n", "k", "n+l"))), 0)
    chk("and all three -> K0", mi.K(chart(("n", "k", "n+l", "n-l"))), 0)

    # ---- the seated indexes are members of the census
    sh, ja = seated_are_members()
    chk("fibred.py's chart is in the census at K3", sh, (("n", "l", "k"), 3))
    chk("madelung.py's is at K7", ja, (("l", "k", "n+l"), 7))
    chk("and they agree with the instruments themselves",
        (mi.K(fibred.index()), mi.K(chart(("l", "k", "n+l")))), (3, 7))

    # ---- representatives
    reps = representatives(3)
    chk("injective arity-3 charts by channel",
        {k: len(v) for k, v in sorted(reps.items())}, {0: 6, 3: 8, 7: 4})
    chk("so neither fibration is a unique construction",
        (("n", "l", "k") in reps[3], ("l", "k", "n+l") in reps[7]),
        (True, True))

    # ---- NOT A LAW ABOUT THE LATTICE. The unreachable channels are lawful.
    chk("K1, K4, K5 are lawful lattice positions all the same",
        [len(mi.channels()[k]) for k in (1, 4, 5)], [1, 2, 3])

    print("charts3 selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
