#!/usr/bin/env python3
r"""
madelung.py -- THE JANET PERSPECTIVE: the same 170 electrons fibred over the
FILL ORDER instead of the shell, and the third of three master indexes.

M: "Now we need the Janet version of this. 3 master indexes. Each a perspective
of the same definition."

    python3 madelung.py             the reading
    python3 madelung.py --selftest  fixtures

THE THREE PERSPECTIVES, AND THEY ARE ONE DEFINITION SEEN THREE WAYS:

    mi.py         THE MASTER INDEX -- nine indexes charted by which languages
                  close them.  The object is the CORPUS.
    fibred.py     THE SHELL FIBRATION -- 170 elements as (n, l, k), fibred over
                  n.  The object is the ELEMENTS, addressed by shell.
    madelung.py   THE JANET FIBRATION -- the same 170 as (n+l, l, k), fibred
                  over n+l.  The object is the ELEMENTS, addressed by fill
                  order.

The second and third differ in ONE COORDINATE and share the other two.  Nothing
else about them differs -- same electrons, same fibres, same operators, same
laws.  And they land in different channels, which is the whole point.

===============================================================================
0. ONE COORDINATE, AND IT IS THE BASE
===============================================================================

    fibred.py     (n,   l, k)      n   = which shell the electron is in
    madelung.py   (n+l, l, k)      n+l = when the electron is added

`l` and `k` are IDENTICAL between them.  Only the base changes, from the shell
an electron occupies to the shell-plus-subshell that orders the filling.  This
file builds its index by RE-CHARTING fibred.py's, never by re-deriving it:
`janet()` is one comprehension over `fibred.index()`, so the two perspectives
cannot drift apart.

    AND IT REPRODUCES A SEATED INDEX EXACTLY.  `janet() == mi.janet()`, cell
    for cell.  The Janet chart is already the ninth member of the master index;
    this file does not seat a new object, it reads a seated one as a bundle.

===============================================================================
1. THE FIBRES DOUBLE.  THEY DO NOT MIRROR.
===============================================================================

        base n      2    8   18   32   50   32   18    8    2      PALINDROME
        base n+l    2    2    8    8   18   18   32   32   50      DOUBLED

Same 170 cells, same fibres, redistributed.  At n+l = S the subshells are the
(n, l) with n + l = S and l < n, so l runs 0 .. ceil(S/2) - 1 and the fibre
holds 2(2l+1) summed over those -- which is 2m^2 with m = ceil(S/2), and
therefore takes each value TWICE as S increases by one.

    **THE JANET FIBRES NEVER SHRINK.**  The shell fibration's do: they peak at
    n = 5 and mirror back down.  This one is monotone non-decreasing all the way
    to the reach.  That single difference explains everything below.

===============================================================================
2. THE SLIDING SCALE NEVER TRANSITIONS, AND THAT CONFIRMS THE LAW
===============================================================================

Sweep the base, take the cumulative index, measure the channel:

        n+l <= 1    2 cells   K7          n+l <= 6    56 cells   K7
        n+l <= 2    4         K7          n+l <= 7    88         K7
        n+l <= 3   12         K7          n+l <= 8   120         K7
        n+l <= 4   20         K7          n+l <= 9   170         K7
        n+l <= 5   38         K7

    ALL FIVE LANGUAGES CLOSE AT EVERY STOP.  No transition, ever.

    **AND fibred.py PREDICTED THIS BEFORE IT WAS MEASURED.**  That file's law is
    that the K7 -> K3 transition lands on THE FIRST SHRINKING SHELL -- verified
    at nine reaches there.  The Janet fibres never shrink.  So the law says this
    sweep can have no transition, and it has none.

        THIS IS THE ONLY CROSS-PREDICTION IN THIS TREE THAT WAS MADE FROM A LAW
        AND THEN CHECKED ON AN INDEX THE LAW WAS NOT FITTED TO.  It is weaker
        than it sounds -- a law fitted on one family and confirmed on a close
        relative is corroboration, not independent test -- and it is stronger
        than nothing, because the law could have failed and did not.

===============================================================================
3. THE SAME PROJECTION, THE COMPLEMENTARY CHANNEL
===============================================================================

Drop `l` from each perspective.  Both give 82 cells.  They are DIFFERENT
82-cell sets, and their channels are complementary:

        (n,   k)     82 cells    K3 = {geometry, statistics}
        (n+l, k)     82 cells    K6 = {order, algebra, information, statistics}

        union = all five        intersection = {statistics}, the poset minimum

    **K3 = down(geometry) AND K6 = down(order) = down(algebra).**  Those are the
    principal down-sets of the TWO MAXIMAL LANGUAGES -- the two switches of
    mi.py's phase square, the (geometry ON, order/algebra off) quadrant and the
    (geometry off, order/algebra ON) quadrant.

    SO THE CHOICE OF BASE SELECTS A MAXIMAL LANGUAGE.  Address the electron by
    the shell it occupies and drop the subshell: geometry survives.  Address it
    by when it is added and drop the subshell: the order/algebra block survives
    instead, and geometry is the one thing lost.  One coordinate, and it decides
    which half of the top of the poset you keep.

===============================================================================
4. AND K6 IS THE CHANNEL THE MASTER INDEX LEAVES EMPTY
===============================================================================

M, on K6: "an object supplied by necessity as an observer and that cannot be
observed itself... it's a proof of governing dynamics, a hierarchical order to
applied mathematics. A Law."

The master index occupies K0, K2 and K7 and nothing else.  K6 is vacant there,
and K6 is the channel that is ALONE in its phase -- join-irreducible,
meet-irreducible, a co-atom.

    **(n+l, k) SITS IN IT, AND THE REACH CONTROL PASSES.**  K6 at every complete
    shell reach from n+l <= 3 through n+l <= 11 -- nine consecutive reaches, 10
    cells to 122.  Only the two degenerate reaches give K7.

    **BUT IT IS A COARSENING, AND THAT IS THE PRICE.**  (n+l, k) maps 170
    elements onto 82 cells: eighty-eight elements share an address with another.
    The chart cannot say which element is which.  Every other index in this tree
    that reaches K7 or K3 is INJECTIVE on its elements; this one is not, and the
    K6 verdict is a fact about a chart that has thrown information away.

    WHETHER TO SEAT IT IS A RULING AND NOT A MEASUREMENT.  This file does not
    seat it.  What is measured is that a chart of the corpus's own element data
    lands in K6 and stays there across an order of magnitude of reach -- so K6
    is REACHABLE, which was open before.  What is NOT measured is that it
    deserves a seat: a non-injective chart of 170 elements is a weaker object
    than the nine already seated, and DOCKET 3's criterion governs coordinates
    of the master index, not the legitimacy of a coarsening.  See DOCKET 10.

===============================================================================
5. THE THREE PERSPECTIVES, SIDE BY SIDE
===============================================================================

                        base        cells   injective   channel   fibres
    shell fibration     n           170     yes         K3        palindrome
    Janet fibration     n+l         170     yes         K7        doubled
    ---- and their shared projection, l dropped ----
    (n, k)              n            82     no          K3        --
    (n+l, k)            n+l          82     no          K6        --

    THE MASTER INDEX IS NOT A FOURTH ROW.  It charts INDEXES, not elements; its
    cells are (K, height, width) of other objects.  The three are perspectives
    of one definition in the sense that the same five closure operators run on
    all of them, not in the sense that they have the same members.

    WHAT THE THREE AGREE ON: the seven lawful containments hold everywhere, on
    every index and every fibre of both bundles.  Dilworth holds on all of them.
    Every fibre of both bundles closes in all five.
    WHAT THEY DISAGREE ON: the channel, and only the channel.

===============================================================================
6. WHAT THIS FILE REFUSES TO CONCLUDE
===============================================================================

    THAT THE JANET PERSPECTIVE IS THE RIGHT ONE because it reaches K7.  Closing
    in more languages is not being more true; K7 means every operator is
    satisfied, which a complete rectangle achieves trivially.  The shell
    fibration's K3 is a stronger statement about structure, not a weaker one.

    THAT K6 IS NOW OCCUPIED.  A projection is not a seated index.  See section 4.

    THAT THE BASE IS THE ONLY THING THAT MATTERS.  It is the only thing that
    differs HERE, between two charts that share `l` and `k`.  Nothing measured
    here says a third base would not behave differently again, and one is
    obvious and untried: `l` itself.
"""

import sys

import fibred
import hlaw
import mi

REACH = fibred.REACH                        # 170
JANET_FIBRES = (2, 2, 8, 8, 18, 18, 32, 32, 50)
SHELL_FIBRES = fibred.FIBRE_SIZES           # the palindrome, for comparison


# ---------------------------------------------------------------------------
# the construction -- a RE-CHARTING of fibred.py, never a re-derivation
# ---------------------------------------------------------------------------

def janet(reach=REACH):
    """The same electrons as (n+l, l, k).  Equals mi.janet() exactly."""
    return frozenset((n + l, l, k) for n, l, k in fibred.index(reach))


def fibre(s, reach=REACH):
    """The (l, k) index sitting at fill-order shell s."""
    return frozenset((l, k) for a, l, k in janet(reach) if a == s)


def cumulative(s, reach=REACH):
    """The index restricted to fill-order shells 1..s."""
    return frozenset(t for t in janet(reach) if t[0] <= s)


def bases(reach=REACH):
    """The n+l values the index reaches."""
    return sorted({t[0] for t in janet(reach)})


def sweep(reach=REACH):
    """[(s, cells, K, closers)] -- the sliding scale over fill order."""
    return [(s, len(C), mi.K(C), fibred.closers(C))
            for s in bases(reach) for C in [cumulative(s, reach)]]


def fibre_table(reach=REACH):
    """[(s, cells, K, closers)] -- each fibre on its own."""
    return [(s, len(F), mi.K(F), fibred.closers(F))
            for s in bases(reach) for F in [fibre(s, reach)]]


def projections(reach=REACH):
    """{dropped: (cells, K, closers, deficits)} for the Janet chart."""
    X = janet(reach)
    out = {"none": (len(X), mi.K(X), fibred.closers(X), fibred.deficits(X))}
    for name, f in (("n+l", lambda t: (t[1], t[2])),
                    ("l", lambda t: (t[0], t[2])),
                    ("k", lambda t: (t[0], t[1]))):
        P = frozenset(f(t) for t in X)
        out[name] = (len(P), mi.K(P), fibred.closers(P), fibred.deficits(P))
    return out


def k6_chart(reach=REACH):
    """(n+l, k) -- the chart that lands in K6.  NOT INJECTIVE; see section 4."""
    return frozenset((n + l, k) for n, l, k in fibred.index(reach))


def k3_chart(reach=REACH):
    """(n, k) -- the same projection on the other base, and it lands in K3."""
    return frozenset((n, k) for n, l, k in fibred.index(reach))


def principal_downsets():
    """{language: (its principal down-set, that set's channel or None)}.

    Birkhoff: the join-irreducible channels are exactly these.  Section 3's
    finding is that the two 82-cell charts realise the down-sets of the two
    MAXIMAL languages, so this is computed rather than asserted.
    """
    law = set(hlaw.LAWFUL)
    ch = mi.channels()
    out = {}
    for L in sorted(hlaw.LANGS):
        d = frozenset({M for M in hlaw.LANGS if M == L or (M, L) in law})
        out[L] = (sorted(d), ch.index(d) if d in ch else None)
    return out


def maximal_languages():
    """The maximal elements of the language poset -- the phase square's switches."""
    law = set(hlaw.LAWFUL)
    return sorted(L for L in hlaw.LANGS
                  if not any((L, M) in law and (M, L) not in law
                             for M in hlaw.LANGS if M != L))


def k6_reach_control():
    """[(shell, reach, cells, K)] -- is the K6 chart's channel an artefact?"""
    import shells as _sh
    out = []
    for S, R in enumerate(_sh.shell_ends()[:11], start=1):
        P = k6_chart(R)
        if len(P) < 2:
            continue
        out.append((S, R, len(P), mi.K(P)))
    return out


def perspectives():
    """[(name, base, cells, injective, K)] -- section 5's table."""
    A = fibred.addresses()
    SH, JA = fibred.index(), janet()
    K3, K6 = k3_chart(), k6_chart()
    return [
        ("shell fibration", "n", len(SH), len(SH) == len(A), mi.K(SH)),
        ("Janet fibration", "n+l", len(JA), len(JA) == len(A), mi.K(JA)),
        ("(n, k)", "n", len(K3), len(K3) == len(A), mi.K(K3)),
        ("(n+l, k)", "n+l", len(K6), len(K6) == len(A), mi.K(K6)),
    ]


def laws_hold(reach=REACH):
    """(broken on the index, fibres breaking any, Dilworth ok)."""
    X = janet(reach)

    def broken(S):
        S = frozenset(S)
        cl, _ = hlaw.closures(S)
        E = {L: len(cl[L]) - len(S) for L in hlaw.LANGS}
        return sorted((a, b) for a, b in hlaw.LAWFUL if E[a] > E[b])

    return (broken(X),
            sorted(s for s in bases(reach) if broken(fibre(s, reach))),
            len(X) <= mi.height(X) * mi.width(X))


# ---------------------------------------------------------------------------

def report():
    print("=" * 74)
    print("THE JANET PERSPECTIVE -- base n+l, fibre (l, k)")
    print("=" * 74)
    print()
    J = janet()
    print("0. ONE COORDINATE, AND IT IS THE BASE.")
    print("   shell fibration   (n,   l, k)   n   = which shell it is in")
    print("   Janet fibration   (n+l, l, k)   n+l = when it is added")
    print("   l and k are IDENTICAL between them. This file re-charts")
    print("   fibred.index(); it never re-derives the electrons.")
    print("   cells %d   equals the seated mi.janet(): %s"
          % (len(J), J == mi.janet()))
    print()

    print("1. THE FIBRES DOUBLE. THEY DO NOT MIRROR.")
    print("   base n      " + "".join("%5d" % c for c in SHELL_FIBRES)
          + "   PALINDROME")
    print("   base n+l    " + "".join("%5d" % c for _s, c, _k, _cl in fibre_table())
          + "   DOUBLED")
    print("   Same 170 cells redistributed. The Janet fibres NEVER SHRINK,")
    print("   and that one difference explains everything below.")
    print()

    print("2. THE SLIDING SCALE NEVER TRANSITIONS.")
    for s, c, k, cl in sweep():
        print("   n+l <= %d  %4d cells   K%-2d  %s" % (s, c, k, ", ".join(cl)))
    ks = {k for _s, _c, k, _cl in sweep()}
    print("   channels seen across the whole sweep: %s -- no transition."
          % sorted(ks))
    print("   AND fibred.py PREDICTED IT. Its law is that the K7 -> K3")
    print("   transition lands on the FIRST SHRINKING SHELL. These never")
    print("   shrink, so the law forbids a transition, and there is none.")
    print()

    print("3. THE SAME PROJECTION, THE COMPLEMENTARY CHANNEL.")
    K3, K6 = k3_chart(), k6_chart()
    print("   (n,   k)   %3d cells   K%d = %s"
          % (len(K3), mi.K(K3), ", ".join(fibred.closers(K3))))
    print("   (n+l, k)   %3d cells   K%d = %s"
          % (len(K6), mi.K(K6), ", ".join(fibred.closers(K6))))
    u = set(fibred.closers(K3)) | set(fibred.closers(K6))
    i = set(fibred.closers(K3)) & set(fibred.closers(K6))
    print("   union %s -- all five" % sorted(u))
    print("   intersection %s -- the poset minimum" % sorted(i))
    print()
    print("   and those two channels are the principal down-sets of the")
    print("   TWO MAXIMAL languages, which are %s:" % maximal_languages())
    for L, (d, k) in principal_downsets().items():
        print("     down(%-12s) = K%-4s %s" % (L, k, d))
    print("   SO THE CHOICE OF BASE SELECTS A MAXIMAL LANGUAGE.")
    print()

    print("4. K6 IS THE CHANNEL THE MASTER INDEX LEAVES EMPTY.")
    occ = sorted({mi.K(v) for v in mi.inventory().values()})
    print("   the master index occupies K%s and nothing else."
          % ", K".join(map(str, occ)))
    print("   K6 is vacant there, and it is ALONE in its phase.")
    print("   (n+l, k) sits in it. Reach control:")
    for S, R, c, k in k6_reach_control():
        print("     n+l <= %-2d  Z <= %-3d  %3d cells   K%d" % (S, R, c, k))
    A = fibred.addresses()
    print("   BUT IT IS A COARSENING: %d elements onto %d cells, so %d share"
          % (len(A), len(K6), len(A) - len(K6)))
    print("   an address. Every other index here that reaches K7 or K3 is")
    print("   INJECTIVE; this one is not. K6 is REACHABLE -- that was open.")
    print("   Whether it deserves a SEAT is a ruling, not a measurement.")
    print()

    print("5. THE THREE PERSPECTIVES, SIDE BY SIDE.")
    print("   %-20s %-6s %6s %-11s %s"
          % ("", "base", "cells", "injective", "channel"))
    for nm, b, c, inj, k in perspectives():
        print("   %-20s %-6s %6d %-11s K%d"
              % (nm, b, c, "yes" if inj else "NO", k))
    print("   THE MASTER INDEX IS NOT A FOURTH ROW: it charts INDEXES, not")
    print("   elements. The three share the five operators, not their members.")
    print()

    print("6. SAME LAWS, CHECKED.")
    bad, badf, dil = laws_hold()
    print("   lawful containments broken on the index   %s" % (bad or "none"))
    print("   fibres breaking any lawful containment    %s" % (badf or "none"))
    print("   Dilworth |X| <= h x w                     %s  (%d <= %d x %d)"
          % (dil, len(J), mi.height(J), mi.width(J)))
    print()
    print("7. REFUSED: that Janet is the RIGHT perspective because it reaches")
    print("   K7 -- closing in more languages is not being more true, and a")
    print("   complete rectangle reaches K7 trivially. That K6 is now")
    print("   OCCUPIED -- a projection is not a seated index. That the base is")
    print("   the only thing that matters -- l as a base is obvious and untried.")
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

    print("madelung selftest")
    J, A = janet(), fibred.addresses()

    # ---- the construction is a re-charting, and it lands on a seated index
    chk("170 cells, the same electrons as the shell fibration", len(J), 170)
    chk("still injective -- no element loses its address", len(J), len(A))
    chk("AND IT EQUALS THE SEATED mi.janet() EXACTLY", J == mi.janet(), True)
    chk("l and k are untouched by the re-charting",
        {(l, k) for _s, l, k in J} == {(l, k) for _n, l, k in fibred.index()},
        True)

    # ---- the fibres double rather than mirror
    chk("the Janet fibre sizes",
        tuple(c for _s, c, _k, _cl in fibre_table()), JANET_FIBRES)
    chk("they are NOT a palindrome, unlike the shell fibration's",
        tuple(JANET_FIBRES) == tuple(reversed(JANET_FIBRES)), False)
    chk("and the shell fibration's ARE",
        tuple(SHELL_FIBRES) == tuple(reversed(SHELL_FIBRES)), True)
    # THE PROPERTY THE WHOLE FILE TURNS ON.
    chk("THE JANET FIBRES NEVER SHRINK",
        all(JANET_FIBRES[i] <= JANET_FIBRES[i + 1]
            for i in range(len(JANET_FIBRES) - 1)), True)
    chk("the shell fibration's DO shrink",
        any(SHELL_FIBRES[i] > SHELL_FIBRES[i + 1]
            for i in range(len(SHELL_FIBRES) - 1)), True)
    chk("both redistribute the same 170 cells",
        (sum(JANET_FIBRES), sum(SHELL_FIBRES)), (170, 170))
    chk("each fibre size appears twice, ceil(S/2) driving it",
        [c for c in JANET_FIBRES], [2 * (((s + 1) // 2) ** 2)
                                    for s in range(1, 10)])

    # ---- the sweep, and the cross-prediction
    sw = sweep()
    chk("every stop on the sliding scale is K7",
        sorted({k for _s, _c, k, _cl in sw}), [7])
    chk("so there is NO transition anywhere in the sweep",
        sum(1 for i in range(1, len(sw)) if sw[i][2] != sw[i - 1][2]), 0)
    # fibred.py's law: the transition is at the first shrinking shell. These
    # never shrink, so the law FORBIDS a transition. It is absent. The law was
    # fitted on the other base and is confirmed here without refitting.
    chk("which is what fibred.py's first-shrinking-shell law requires",
        (any(JANET_FIBRES[i] > JANET_FIBRES[i + 1]
             for i in range(len(JANET_FIBRES) - 1)),
         sum(1 for i in range(1, len(sw)) if sw[i][2] != sw[i - 1][2])),
        (False, 0))
    chk("every fibre closes in ALL FIVE, as on the other base",
        sorted({k for _s, _c, k, _cl in fibre_table()}), [7])

    # ---- the whole index
    chk("the Janet chart closes in all five", fibred.closers(J),
        ["algebra", "geometry", "information", "order", "statistics"])
    chk("K7, against the shell fibration's K3",
        (mi.K(J), mi.K(fibred.index())), (7, 3))
    chk("its cell on the admissible chart", mi.cell(J), (7, 30, 12))

    # ---- the complementary projection
    P = projections()
    K3, K6 = k3_chart(), k6_chart()
    chk("both 'drop l' charts are 82 cells", (len(K3), len(K6)), (82, 82))
    chk("but they are DIFFERENT 82-cell sets", K3 == K6, False)
    chk("(n, k) lands in K3", (mi.K(K3), fibred.closers(K3)),
        (3, ["geometry", "statistics"]))
    chk("(n+l, k) lands in K6", (mi.K(K6), fibred.closers(K6)),
        (6, ["algebra", "information", "order", "statistics"]))
    chk("their union is all five",
        sorted(set(fibred.closers(K3)) | set(fibred.closers(K6))),
        ["algebra", "geometry", "information", "order", "statistics"])
    chk("their intersection is statistics alone -- the poset minimum",
        sorted(set(fibred.closers(K3)) & set(fibred.closers(K6))),
        ["statistics"])

    # ---- and those are the two maximal languages' down-sets
    pd = principal_downsets()
    chk("the maximal languages", maximal_languages(),
        ["algebra", "geometry", "order"])
    chk("down(geometry) is K3", pd["geometry"][1], 3)
    chk("down(order) and down(algebra) are both K6",
        (pd["order"][1], pd["algebra"][1]), (6, 6))
    # THE FINDING: the base selects which maximal language survives.
    chk("SO THE BASE SELECTS A MAXIMAL LANGUAGE",
        (mi.K(K3), mi.K(K6)) == (pd["geometry"][1], pd["order"][1]), True)

    # ---- K6, and the price
    occ = sorted({mi.K(v) for v in mi.inventory().values()})
    chk("K6 is vacant in the master index", 6 not in occ, True)
    chk("and it is alone in its phase", mi.phase()[(False, True)], [6])
    rc = k6_reach_control()
    chk("the K6 chart holds K6 at nine consecutive complete reaches",
        [k for S, _R, _c, k in rc if S >= 3], [6] * 9)
    chk("and the two degenerate reaches are K7", [k for S, _R, _c, k in rc
                                                  if S < 3], [7, 7])
    # THE PRICE, PINNED SO IT CANNOT BE QUOTED WITHOUT IT.
    chk("BUT THE K6 CHART IS NOT INJECTIVE -- 88 elements lose their address",
        (len(A), len(K6), len(A) - len(K6)), (170, 82, 88))
    chk("where both fibrations ARE injective",
        (len(fibred.index()) == len(A), len(J) == len(A)), (True, True))

    # ---- the three perspectives
    p = perspectives()
    chk("the two fibrations are injective, the two projections are not",
        [inj for _n, _b, _c, inj, _k in p], [True, True, False, False])
    chk("and their four channels", [k for _n, _b, _c, _i, k in p], [3, 7, 3, 6])

    # ---- the laws
    bad, badf, dil = laws_hold()
    chk("no lawful containment is broken on the index", bad, [])
    chk("nor on any fibre", badf, [])
    chk("Dilworth holds", dil, True)

    print("madelung selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
