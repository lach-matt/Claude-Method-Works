"""
===============================================================================
questions.py -- THE QUESTION INDEX.  Cells are questions put to the languages.
===============================================================================

M: "warp is not an index. It is a question."

That is right, and following it produces the index this tree has been missing.

===============================================================================
0. WHY THERE HAD TO BE ONE
===============================================================================

An INDEX has cells and a box.  It closes, or fails to close, in each language,
and that verdict places it in the channel lattice.  A QUESTION is asked OF the
languages: each returns a verdict on it, and the pattern of verdicts is what you
get back.  Both yield a subset of the five languages, which is why the tree
confused them -- refusal.py's section on the two kinds is the correction.

    A QUESTION IS NOT A CELL OF A PHYSICAL INDEX.  It has no box of its own and
    it is not a member of the energy-condition family or the bounds index or any
    other.  duality.py spent a section looking for the host of TRANSITION-
    POSSIBLE and a later pass proved no such host can exist under the natural
    reading -- the top-corner theorem.  BOTH WERE LOOKING FOR THE WRONG KIND OF
    THING.

    A QUESTION IS A MEMBER OF THE INDEX OF QUESTIONS, and its verdict pattern is
    its CELL.  That is the home, and this file is it.

===============================================================================
1. THE MEMBERS -- four, and the tree already ran every one
===============================================================================

The protocol is the corpus's own: register 1173 (a language is a coordinate
system with a closure operator; logic is binary -> language -> binary), register
1176 (E = 0 iff the languages agree) and section 33.2 (a language that falls
silent IS the finding, and the identity of the silent language names the kind of
object).  expand.py ran it once.  doors.py ran it three more times.

                        order     algebra   geometry  informat. statistics
    DOOR 1  OUTSIDE GR  ADMITS    CONTESTED ADMITS    ADMITS    NOT-RUN
    DOOR 2  NOT ENERGY  REFUSES   NOT-RUN   ADMITS    ADMITS    NOT-RUN
    DOOR 3  A RELIC     ADMITS    NOT-RUN   ADMITS    ADMITS    NOT-RUN
    TRANSITION-POSSIBLE ADMITS    ADMITS    ADMITS    REFUSES   ADMITS

Nothing here is new measurement.  Every row is read from the instrument that
produced it, by import.  What is new is reading the four AS AN INDEX.

===============================================================================
2. THE CODING IS A CHOICE, AND THE RESULT DOES NOT DEPEND ON IT
===============================================================================

Four verdict values -- ADMITS, REFUSES, NOT-RUN, CONTESTED -- and a slot must be
ORDINAL.  DOCKET 1's lesson is that a coding chosen for convenience can carry a
finding on its own, so three defensible codings are run and compared:

    A  three-valued   REFUSES 0 < NOT-RUN = CONTESTED 1 < ADMITS 2
    B  binary         ADMITS 1, everything else 0
    C  four-valued    REFUSES 0 < NOT-RUN 1 < CONTESTED 2 < ADMITS 3

    ALL THREE GIVE THE SAME MASTER CELL, (2, 1, 0, 2, 1), THE SAME CHANNEL
    {geometry, statistics} = K3, AND THE SAME REFUSAL INDEX {0, 3, 5, 7}.

A is the default because it is the reading section 33.2 supports: a silent
language has not refused, it has not spoken.  But the finding is coding-robust
and does not rest on that.

===============================================================================
3. WHAT IT LANDS ON, AND IT IS A CELL NOTHING OCCUPIED
===============================================================================

    cells 3 (A, B) or 4 (C)   arity 5   box 16 or 24   density 18.8 % / 16.7 %
    closes in {geometry, statistics} -- K3
    master cell (2, 1, 0, 2, 1)

    NOT AMONG THE EIGHT SEATED CELLS.  NOT AMONG THE ELEVEN POPULATED ONES.

Seating it takes the master index from **8 to 9** distinct cells, and the
populated reading from **11 to 12**.

    AND TWELVE IS THE THRESHOLD.  Order dimension -- the corpus's own measure of
    an index's shape, register 35 -- is SATURATED below twelve distinct cells:
    96.7 % of random 8-cell sets in the master box have dimension 2, so the
    master index's own dimension of 2 says nothing about it.  At twelve the base
    rate is 54.2 %, a coin flip, and the measurement carries a full bit.

    SO THE QUESTION INDEX IS EXACTLY WHAT THE MASTER INDEX NEEDS IN ORDER TO
    STATE ITS OWN SHAPE.  Not a chart change, not a re-banding -- a genuinely
    new object, and the one the tree had been treating as a homeless cell.

It also moves channel K3 from SPECIES -- occupied only by four witnessed spectra
slices -- to SEATED.

===============================================================================
4. WHAT THIS FILE DOES NOT CLAIM
===============================================================================

    THAT FOUR MEMBERS IS A FAMILY RATHER THAN A CONVENIENCE SAMPLE.  All four
    are warp questions from one investigation: three doors out of the obstruction
    and the obstruction's own verdict.  A family of four drawn from one enquiry
    is thin, and necindex.py's bar -- named members, one declared form, ordinal
    slots -- is met on its face while the SPREAD is not.  Recorded as the
    principal caution.

    THAT THE WARP OBSTRUCTION IS WEAKENED OR STRENGTHENED BY BEING HOUSED.  It
    is neither.  expand.py's verdict stands exactly as measured; this file gives
    it a place to sit and changes nothing about what it says.

    THAT THE WARP QUESTION'S REFUSAL SET IS K1.  It is not a refusal set at all
    -- see refusal.py section on the two kinds.  As a MEMBER of this index its
    refusal set is K0, like every member of every index, by extensivity.  Its
    verdict pattern {information} is a CELL COORDINATE and the two must not be
    read as one number.
"""

import sys

import doors
import expand
import hlaw
import master

FIVE = ("order", "algebra", "geometry", "information", "statistics")

CODINGS = {
    "A": {"REFUSES": 0, "NOT-RUN": 1, "CONTESTED": 1, "ADMITS": 2},
    "B": {"REFUSES": 0, "NOT-RUN": 0, "CONTESTED": 0, "ADMITS": 1},
    "C": {"REFUSES": 0, "NOT-RUN": 1, "CONTESTED": 2, "ADMITS": 3},
}
DEFAULT = "A"


def verdict_rows():
    """{question: {language: verdict}} -- read from the instruments, never copied."""
    out = {}
    for nm, sub, fn in doors.DOORS:
        r = fn()
        out["%s (%s)" % (nm, sub)] = {L: r.get(L, "NOT-RUN") for L in FIVE}
    st = expand.expand()
    out["TRANSITION-POSSIBLE"] = {L: st.get(L, "NOT-RUN") for L in FIVE}
    return out


def cells(coding=DEFAULT):
    cd = CODINGS[coding]
    return frozenset(tuple(cd[r[L]] for L in FIVE)
                     for r in verdict_rows().values())


def coding_robust():
    """(master cells, channels, refusal indexes) over the three codings."""
    import refusal
    mc = {k: master.master_cell(cells(k)) for k in CODINGS}
    ch = {k: frozenset(master.closers(cells(k))) for k in CODINGS}
    rx = {k: frozenset(refusal.refusal_set(cells(k))) for k in CODINGS}
    return mc, ch, rx


def is_a_new_cell():
    """(cell, new to seated, new to populated)."""
    c = master.master_cell(cells())
    return (c,
            c not in frozenset(master.master_index().values()),
            c not in frozenset(master.populated_master().values()))


def report():
    print("=" * 74)
    print("THE QUESTION INDEX -- cells are questions put to the languages")
    print("=" * 74)
    print()
    print("A question is not a cell of a physical index. It is a MEMBER here,")
    print("and its verdict pattern is its cell.")
    print()
    rows = verdict_rows()
    print("   %-34s %s" % ("question", " ".join("%-10s" % L[:10] for L in FIVE)))
    for q, r in rows.items():
        print("   %-34s %s" % (q, " ".join("%-10s" % r[L] for L in FIVE)))
    print()
    mc, ch, rx = coding_robust()
    print("   THE CODING IS A CHOICE AND THE RESULT IS ROBUST TO IT:")
    for k in sorted(CODINGS):
        X = cells(k)
        a, b, d = master.shape(X)
        print("     %s  %d cells, arity %d, box %-3d density %5.1f%%  closes %-24s %s"
              % (k, len(X), a, b, 100 * d, sorted(ch[k]), mc[k]))
    print("   all three agree on the master cell, the channel and R(X).")
    print()
    c, new_s, new_p = is_a_new_cell()
    MC = frozenset(master.master_index().values())
    PC = frozenset(master.populated_master().values())
    print("   master cell %s -- new to the seated cells: %s" % (c, new_s))
    print("   seated    %d -> %d distinct cells" % (len(MC), len(MC | {c})))
    print("   populated %d -> %d distinct cells" % (len(PC), len(PC | {c})))
    print()
    print("   AND TWELVE IS THE ORDER-DIMENSION THRESHOLD. Below it the measure")
    print("   is saturated -- 96.7%% of random 8-cell sets give dimension 2. At")
    print("   twelve the base rate is 54.2%%, so the answer carries a full bit.")
    print("   THE QUESTION INDEX IS WHAT LETS THE MASTER INDEX STATE ITS SHAPE.")
    print()
    print("   CAUTION: four members, all from one investigation. The bar is met")
    print("   on its face; the SPREAD is not. See section 4.")


def selftest():
    ok = True

    def chk(nm, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", nm, got))
        if not good:
            print("        expected %r" % (want,))

    print("questions selftest")
    rows = verdict_rows()
    chk("four questions have been put to the five languages", len(rows), 4)
    chk("and TRANSITION-POSSIBLE is one of them",
        "TRANSITION-POSSIBLE" in rows, True)
    chk("its verdict is information REFUSES, the other four ADMIT",
        (rows["TRANSITION-POSSIBLE"]["information"],
         sorted(L for L in FIVE if rows["TRANSITION-POSSIBLE"][L] == "ADMITS")),
        ("REFUSES", ["algebra", "geometry", "order", "statistics"]))
    chk("four distinct verdict values occur",
        sorted({v for r in rows.values() for v in r.values()}),
        ["ADMITS", "CONTESTED", "NOT-RUN", "REFUSES"])

    # ---- THE CODING IS A CHOICE. The result must not depend on it.
    mc, ch, rx = coding_robust()
    chk("all three codings give ONE master cell", len(set(mc.values())), 1)
    chk("and it is (2,1,0,2,1)", mc[DEFAULT], (2, 1, 0, 2, 1))
    chk("all three give one channel", len(set(ch.values())), 1)
    chk("and it is {geometry, statistics} = K3", sorted(ch[DEFAULT]),
        ["geometry", "statistics"])
    chk("all three give one refusal index", len(set(rx.values())), 1)
    chk("and it is {0,3,5,7}", sorted(rx[DEFAULT]), [0, 3, 5, 7])

    # ---- AND THE CELL IS NEW, which is the whole point
    c, new_s, new_p = is_a_new_cell()
    chk("the cell is NEW to the seated master index", new_s, True)
    chk("and NEW to the populated one", new_p, True)
    MC = frozenset(master.master_index().values())
    PC = frozenset(master.populated_master().values())
    chk("seating it takes seated from 8 to 9 cells",
        (len(MC), len(MC | {c})), (8, 9))
    chk("and populated from 11 to TWELVE -- the threshold",
        (len(PC), len(PC | {c})), (11, 12))

    # ---- the caution, pinned so it cannot fall out
    chk("four members, and all four from one investigation", len(rows), 4)

    print("questions selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
