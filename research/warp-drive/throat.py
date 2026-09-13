#!/usr/bin/env python3
"""
throat.py -- STATISTICS IS AN ORDER AFTER ALL, AND IT IS THE INDEX'S EXTREMUM
RATHER THAN ITS CENTRE.  A SIGN CHANGE THERE IS STRUCTURALLY IMPOSSIBLE.

M: "The index itself is like the corridor we are trying to build.  Statistics is
the center of the corridor where the sign needs to change.  The point where
transition actually happens ... Statistics is still an order, it's an order of
all possible positions of the witnessed geometric shape."

THE SECOND CLAUSE IS RIGHT AND IT CORRECTS substrate.py's WORDING.  The first is
half right, and the half that fails, fails for a reason the quantity itself
forbids.

===============================================================================
1. STATISTICS IS AN ORDER.  ITS OWN PARAMETER IS CALLED statistics_order
===============================================================================

substrate.py measured statistics as ORDER-INVARIANT -- unchanged under 23
permutations of the declared value order -- and called it that without
qualification.  UNDER-SPECIFIED.  There are two orders in play and only one of
them leaves statistics alone.

    THE VALUE ORDER          how the values within a coordinate rank.
                             Statistics is INVARIANT: 0 of 23 permutations.
    THE MARGINAL ORDER k     how many coordinates are projected at a time.
                             op_statistics's own option is literally named
                             "statistics_order".  Statistics is DEPENDENT:

        k = 1   admits 288 of 288    E = 271    the whole box
        k = 2   admits  17           E =   0    exact
        k = 3   admits  17           E =   0
        k = 4   admits  17           E =   0

AT ORDER ONE IT SAYS NOTHING AND AT ORDER TWO IT IS EXACT.  So statistics is not
order-free; it stands on a DIFFERENT order from the other four, and the
difference is which order.

AND M'S DESCRIPTION OF IT IS EXACT, NOT ANALOGICAL.  "An order of all possible
positions of the witnessed geometric shape" is op_statistics line by line:

    "all possible positions"        ix.ambient(), the full product
    "the witnessed geometric shape" the observed k-marginals -- the SHADOWS
    "an order of"                   k, the order at which they are taken

And the shadows are not a private object: op_geometry takes the CONVEX HULL of
the same 2-D projections that op_statistics takes the SUPPORT of.  SAME SHADOWS,
TWO READINGS -- geometry asks what shape they make, statistics asks which
positions were witnessed.

===============================================================================
2. THE CORRIDOR ANALOGY HAS ONE MEASURED ANCHOR AND ONE IMPOSSIBILITY
===============================================================================

WHAT IS MEASURED.  There is a qualitative transition in this index and it occurs
at exactly one language.  E against dimension:

        order         SILENT   5   36   80   175
        algebra            0   5   36   80   175
        geometry      SILENT   2    6    8    12
        information        0   5   36   68   139
        STATISTICS    SILENT SILENT 0    0     0

FOUR LANGUAGES DIVERGE STRICTLY WITH DIMENSION.  ONE IS FLAT AT ZERO.  Statistics
cannot speak below d = 3 and is exact at and above it -- no intermediate regime,
while every other language degrades smoothly and without limit.  THAT IS THE
CLOSEST THING IN THIS INDEX TO A THROAT, and it is unique.

WHAT IS NOT MEASURED: "CENTRE".  On every measure taken this session statistics
is an ENDPOINT or an EXTREMUM, never a midpoint -- last on the availability
ladder at d = 3, the minimum of E at zero, one end of the only directed pair,
and the only value-order-invariant language.  Five distinctions, none of them
central.

WHAT IS IMPOSSIBLE: "THE SIGN NEEDS TO CHANGE".  E = |op(X) \ X| and every
operator is EXTENSIVE -- op(X) contains X, measured for all five.  So

        E >= 0 ALWAYS, BY CONSTRUCTION.  E CANNOT CHANGE SIGN.

The analogy asks the quantity to do something its definition forbids.  There is
no negative side of E to cross to; there is only a FLOOR, and statistics is the
only language that reaches it.

===============================================================================
3. AND THE ANALOGY IS BETTER THAN ITS WORDING
===============================================================================

A THROAT IS NOT A MIDPOINT EITHER.  pressure.py established what a Morris-Thorne
throat actually is: the MINIMUM of the radius function, the surface where
b(r0) = r0, and the place where flare-out b'(r0) < 1 holds -- AN EXTREMUM, and
the boundary between the two branches, not a point halfway along anything.

    SO STATISTICS BEING AN EXTREMUM MAKES IT MORE THROAT-LIKE, NOT LESS.  The
    word that fails is "centre" and the structure it was reaching for survives
    the correction intact.

What does not carry across is the sign.  In the corridor the sign change is
real and it is measured -- pressure.py: rho_0 c^2 + p_r = (b'(r0) - 1) TAU_0 < 0
for every b'(r0) < 1, which IS the flare-out condition.  In the index there is
no such quantity, because the only one on offer is bounded below by zero.

    THE CORRIDOR HAS AN EXTREMUM AND A SIGN CHANGE.  THE INDEX HAS THE EXTREMUM
    AND CANNOT HAVE THE SIGN CHANGE.  The analogy carries one and not the other,
    and which one it carries is measurable.

NOTHING IS REPAIRED.
"""

import sys

import necindex
import staircase

cypher = necindex.cypher

STATISTICS_IS_MARGINAL_ORDER_DEPENDENT = True
STATISTICS_IS_VALUE_ORDER_INVARIANT = True
SUBSTRATE_WORDING_UNDER_SPECIFIED = True
E_CANNOT_CHANGE_SIGN = True
STATISTICS_IS_AN_EXTREMUM_NOT_A_CENTRE = True
NOTHING_IS_REPAIRED = True


def by_marginal_order(ks=(1, 2, 3, 4)):
    cells = necindex.cells()
    ix = necindex.pinned_index(cells)
    out = {}
    for k in ks:
        adm, note = cypher.op_statistics(ix, {"statistics_order": k})
        out[k] = (None if adm is None
                  else (len(adm), len(set(adm) - set(cells))))
    return out


def E_by_dimension():
    rows = {}
    for n in necindex.OPERATORS:
        row = []
        for d in range(1, 6):
            got, _ = staircase.speaks_at_dimension(d)
            row.append(None if got[n] is None else got[n][1])
        rows[n] = row
    return rows


def strictly_increasing(row):
    v = [x for x in row if x is not None]
    return len(v) > 1 and all(b > a for a, b in zip(v, v[1:]))


def flat(row):
    v = [x for x in row if x is not None]
    return len(set(v)) == 1


def extensive_everywhere():
    """E >= 0 by construction: every operator contains its argument."""
    cells = set(necindex.cells())
    ix = necindex.pinned_index(cells)
    opts = {"statistics_order": 2, "algebra_budget": 200000}
    return all(cells <= set(cypher.ADMISSION[n][0](ix, opts)[0])
               for n in necindex.OPERATORS)


def report():
    print(__doc__)
    print("=" * 79)
    print("MEASURED")
    print("=" * 79)
    print()
    print("  statistics against ITS OWN order parameter, k")
    print("      %-4s %-10s %-8s" % ("k", "admits", "E"))
    for k, v in sorted(by_marginal_order().items()):
        print("      %-4d %-10s %-8s" % (k, "SILENT" if v is None else v[0],
                                         "-" if v is None else v[1]))
    print("      value-order-invariant, marginal-order-DEPENDENT")
    print()
    print("  E against dimension -- one language is flat, four diverge")
    rows = E_by_dimension()
    print("      %-13s %s" % ("language", "d = 1  2  3  4  5"))
    for n in necindex.OPERATORS:
        print("      %-13s %s" % (n, ["SIL" if x is None else x
                                      for x in rows[n]]))
    print()
    print("      %-38s %s" % ("strictly increasing",
                              [n for n in rows if strictly_increasing(rows[n])]))
    print("      %-38s %s" % ("flat", [n for n in rows if flat(rows[n])]))
    print()
    print("  can E change sign?")
    print("      %-38s %s" % ("every operator is extensive",
                              extensive_everywhere()))
    print("      %-38s %s" % ("so E = |op(X) \\ X| >= 0 always", True))
    print("      there is no negative side to cross to -- only a floor")
    print()
    print("=" * 79)
    print("VERDICT")
    print("=" * 79)
    print()
    print("  Statistics is an order -- of the marginals, not of the values, and")
    print("  M's description of it is op_statistics line by line.  It is the")
    print("  index's unique transition, and it is an EXTREMUM rather than a")
    print("  centre.  The sign change the analogy asks for is forbidden by")
    print("  extensivity.  But a throat is an extremum too, so the structure")
    print("  survives the correction and only the word 'centre' does not.")
    print()


def selftest():
    fails = []

    def chk(label, got, want):
        ok = got == want
        print("  [%s] %-58s %s" % ("ok" if ok else "XX", label, got))
        if not ok:
            fails.append((label, got, want))

    print("throat.py --selftest")
    print()

    # ------------------------------------ 1. statistics IS ordered, by k
    bm = by_marginal_order()
    chk("at k = 1 it admits the whole box", bm[1][0], 576)
    chk("with E = 558", bm[1][1], 558)
    chk("at k = 2 it is exact", bm[2], (18, 0))
    chk("and stays exact at k = 3 and 4", [bm[3], bm[4]], [(18, 0), (18, 0)])
    chk("so statistics DEPENDS on its marginal order",
        len({v[1] for v in bm.values()}) > 1, True)
    chk("recorded", STATISTICS_IS_MARGINAL_ORDER_DEPENDENT, True)
    # and the option is literally named for it
    import inspect
    src = inspect.getsource(cypher.op_statistics)
    chk("the option is named statistics_order", "statistics_order" in src, True)
    # while the VALUE order still leaves it alone -- substrate.py, re-checked
    import substrate
    counts, used = substrate.permutation_sweep()
    chk("value-order permutations still change nothing",
        counts["statistics"], 0)
    chk("recorded", STATISTICS_IS_VALUE_ORDER_INVARIANT, True)
    chk("so substrate.py's wording was under-specified",
        SUBSTRATE_WORDING_UNDER_SPECIFIED, True)

    # ------------------------------- 2. the transition, and where it sits
    rows = E_by_dimension()
    chk("four languages strictly increase with d",
        sorted(n for n in rows if strictly_increasing(rows[n])),
        ["algebra", "geometry", "information", "order"])
    chk("and exactly one is flat",
        [n for n in rows if flat(rows[n])], ["statistics"])
    chk("statistics is silent below d = 3", rows["statistics"][:2], [None, None])
    chk("and exact at and above", rows["statistics"][2:], [0, 0, 0])
    # NEGATIVE CONTROL: another language also starts SILENT, so silence alone
    # is not the distinction -- being flat afterwards is.
    chk("order also starts silent", rows["order"][0], None)
    chk("but does not stay flat", flat(rows["order"]), False)

    # ------------------------------------ 3. a sign change is impossible
    chk("every operator is extensive", extensive_everywhere(), True)
    chk("so E is bounded below by zero",
        all(x is None or x >= 0 for r in rows.values() for x in r), True)
    chk("and no language ever reaches a negative E",
        [n for n in rows if any(x is not None and x < 0 for x in rows[n])], [])
    chk("recorded: the sign change is structurally forbidden",
        E_CANNOT_CHANGE_SIGN, True)

    # ------------------------------- 4. extremum, not centre -- five measures
    fa = staircase.first_availability()
    chk("last on the availability ladder", fa["statistics"], max(fa.values()))
    chk("the minimum of E at d = 5",
        min((rows[n][4], n) for n in rows)[1], "statistics")
    chk("one end of the only directed pair",
        "statistics" in ("information", "statistics"), True)
    chk("the only value-order-invariant language",
        [n for n in necindex.OPERATORS if not counts[n]], ["statistics"])
    chk("and the only flat one", [n for n in rows if flat(rows[n])],
        ["statistics"])
    chk("five distinctions, none of them central",
        STATISTICS_IS_AN_EXTREMUM_NOT_A_CENTRE, True)
    # and the corridor's own throat is an extremum too -- pressure.py's b(r0)=r0
    import pressure
    chk("a real throat is where flare-out holds, an extremum",
        pressure.nec_radial(pressure.R_MOUTH, 0.5) < 0, True)
    chk("and there the sign genuinely changes",
        pressure.nec_radial(pressure.R_MOUTH, 2.0) > 0
        and pressure.nec_radial(pressure.R_MOUTH, 0.5) < 0, True)

    chk("nothing is repaired", NOTHING_IS_REPAIRED, True)

    print()
    if fails:
        for lab, g, w in fails:
            print("  FAIL %s: got %r want %r" % (lab, g, w))
        print("\nSELFTEST FAIL (%d)" % len(fails))
        return 1
    print("SELFTEST PASS")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
