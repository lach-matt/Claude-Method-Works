#!/usr/bin/env python3
"""
expand.py -- one binary, expanded through the hierarchy, reduced back to one
binary of the same shape.

M: "the code has to be written expansively from binary through the hierarchy to
a logic expansion of the original binary statement, and then reduced back down
to a similar output of the same binary structure as the initial input."

That is register 1173's own hierarchy and I have not been writing it:

    BINARY is the type -- a cell is admitted or it is not.
    A LANGUAGE is a coordinate system with a closure operator.
    LOGIC is binary -> language -> binary.
    A language earns its row when logic can operate on it and get a binary back.

EVERY HEADLINE NUMBER THIS PROJECT HAS PRODUCED IS AN ANALYSIS ANSWER.  65
orders, 2 pi^2, 4.387e71 D^2 -- magnitudes, every one, and by 1173 analysis
earns no row because logic cannot get a binary back from it.  I have been
answering a binary question in a language that cannot answer it, for twenty-odd
passes, and achronal.py caught me doing it once already with ANEC.

This file does it the stated way.

-- THE INPUT: ONE BINARY ------------------------------------------------------
        TRANSITION-POSSIBLE.  Admitted, or not.

-- THE EXPANSION: EACH LANGUAGE ASKS ITS OWN QUESTION OF THAT CELL ------------
  ORDER        is the causal structure admissible?  Can a non-achronal
               connection exist between the endpoints?
               GJW: YES -- by an external causal path, not through the matter.
               achronal.py proved the matter route closed; gjw.py found the
               other one.                                     ADMITS

  GEOMETRY     does the configuration embed?  Monotone areal radius (no
               throat), g_tt < 0 everywhere (no horizon), M_ADM = 0.
               transition.py and concentric.py measured all three.  ADMITS

  ALGEBRA      is it closed under its operation?  The Israel junction closes,
               sigma > 0, DEC holds, and the shell is radially stable at
               beta^2 = 0 where the textbook shell is not.
               stability.py.                                    ADMITS

  INFORMATION  does the object need a coordinate that is not available?
               Phi > 0 requires rho < 0, and no value of rho < 0 is on hand at
               the magnitude required.  achievable.py, charge.py.
                                                                REFUSES

  STATISTICS   are the configurations drawn from a distribution?  RUN at last,
               by declaring one: uniform on the core mass at the seated
               defaults.  The working set is an INTERVAL of positive measure,
               3.5e-3 to 4.05e-2, with both edges located and an interior
               optimum at 2.0e-2.  The device is not fine-tuned.  statrow.py.
                                                                ADMITS

  ANALYSIS     is there a continuous law?  Yes, and it returns 4.387e71 D^2 --
               A MAGNITUDE.  By register 1173 it earns NO ROW.   (no row)

-- THE LOGIC EXPANSION: THE PAIRS --------------------------------------------
FIVE languages now hold rows, so C(5,2) = 10 pairs.  Four agree with each other
and one dissents from all four, so SIX PAIRS AGREE AND FOUR DISAGREE.

AND THE PATTERN OF ROWS IS NOT FREE.  Because cl_a is contained in cl_b for each
lawful containment, whatever a admits b admits: THE ADMITTING SET IS AN UP-SET
and the REFUSING SET IS A DOWN-SET, and the down-sets are exactly the eight
lawful channel sets of master.py section 6b.  Five binaries would be 32
patterns; the law allows EIGHT.  This file never checked that, and now does.
The refusing set {information} is K1 -- one of only two channels nothing in this
corpus occupies -- and had statistics refused it would have been K4, which is
occupied.  RUNNING THE ROW DECIDED WHICH.

-- THE REDUCTION: BACK TO ONE BINARY OF THE SAME SHAPE ------------------------
Register 1176: E(X) = 0 IF AND ONLY IF THE LANGUAGES AGREE.  They do not.

        E = 1.  TRANSITION-POSSIBLE is NOT ADMITTED.

which is the same answer the magnitudes gave -- and that is the point, not a
disappointment.  THE VALUE OF DOING IT THIS WAY IS WHERE THE DISSENT SITS.

    Section 33.2: "a language that falls silent is the finding, and the identity
    of the silent language names the kind of object."

    THE DISSENT IS IN INFORMATION ALONE.  Order admits, geometry admits, algebra
    admits, and statistics now admits too.  The causal structure is fine, the
    geometry embeds, the junction closes, the shell holds, and the working
    configurations are an interval rather than a point.  WHAT IS MISSING IS A
    VALUE, NOT A STRUCTURE.

    AND THE OBSTRUCTION IS ATOMIC.  The only lawful down-set strictly below
    {information} is the empty one, so there is no refusal pattern between
    "information refuses" and "nothing refuses".  No partial credit: the
    obstruction cannot be reduced, only removed.

-- WHAT THAT DOES AND DOES NOT LICENSE ---------------------------------------
DOES: it localises the obstruction exactly, and it says the three things a
"faster and cheaper" route would have to fight are NOT fighting.  Speed is an
order question and order admits.  Cost is an algebra question and algebra
admits.  Embedding is a geometry question and geometry admits.  Nothing
structural stands in the way of faster or cheaper.

DOES NOT: make anything faster or cheaper.  Information's refusal is a measured
refusal -- rho < 0 at the required magnitude is not available, and 4.387e71 is a
real number about the real world.  A language having no row in the cypher does
not make its measurement false; register 1173 governs WHICH LANGUAGE ANSWERS A
BINARY, not which measurements are true.

    SO THE HONEST READING IS: three of the four rows are already yes, the
    fourth is a missing VALUE rather than a missing STRUCTURE, and that is the
    narrowest the obstruction has ever been stated.  It is not permission to
    ignore the magnitude.

-- AND ONE THING THE EXPANSION SURFACES THAT THE MAGNITUDES HID --------------
ORDER ADMITS BECAUSE OF GJW, AND ONLY BECAUSE OF GJW.  Before pass 27 this row
was a refusal too -- achronal.py had closed the matter route and nothing else was
known.  So the expansion has ALREADY moved once this session, from two refusals
to one, and it moved in the row that governs SPEED.

That is the only structural change the project has made to the speed question,
and it is worth recording as the thing to push on rather than the magnitude.

stdlib only.  Every row is recomputed from the instrument that owns it.
"""
import math, sys

ADMITS, REFUSES, NOT_RUN, NO_ROW = "ADMITS", "REFUSES", "NOT-RUN", "NO-ROW"

INPUT_BINARY = "TRANSITION-POSSIBLE"


def order_row():
    """Can a non-achronal connection exist?  Matter route closed; external
    causal path open (GJW).  Recomputed from both instruments."""
    import achronal, gjw
    matter_closed = achronal.escapes(achronal.survey()) == []
    external_open = gjw.bank_loan_theorem()      # GJW's mechanism exists
    return (ADMITS if external_open else REFUSES), matter_closed


def geometry_row():
    """Does it embed?  No throat, no horizon, M_ADM = 0."""
    import transition, concentric
    ph = concentric.potential(2.0e-2)
    radii = (0.01, 0.05, 0.5, 5.0, 50.0, 150.0)
    ok = (not transition.has_throat(ph, radii)
          and not transition.has_horizon(ph, radii)
          and abs(concentric.adm_residual(5.0e-3)) < 1e-10)
    return (ADMITS if ok else REFUSES)


def algebra_row():
    """Is it closed under its operation?  Junction closes, DEC holds, and the
    shell is stable with no stiffness where the textbook one is not."""
    import stability
    ok = (stability.dec_holds(*stability.device(0.5))
          and stability.V_second(*stability.device(0.1), beta2=0.0) > 0
          and stability.V_second(*stability.ordinary(0.1), beta2=0.0) < 0)
    return (ADMITS if ok else REFUSES)


def information_row():
    """Does the object need a coordinate that is not available?"""
    import achievable
    missing = achievable.ratio(1.0) < 1.0        # rho < 0 not available at scale
    return (REFUSES if missing else ADMITS)


def statistics_row():
    """RUN, 2026-09-13. statrow.py declares a measure and sweeps it.

    Uniform on the core mass over [-2.0e-2, 8.0e-2] at the seated defaults: the
    working set is an INTERVAL of positive measure with both edges located and
    an interior optimum, so the device is not a measure-zero accident.
    ADMITS. A one-dimensional slice, and statrow.py says so.
    """
    import statrow
    return ADMITS if statrow.VERDICT == "ADMITS" else REFUSES


def analysis_row():
    """Returns a magnitude, so by register 1173 it earns no row."""
    return NO_ROW


def expand():
    """binary -> language.  The rows, each recomputed from its owner."""
    o, _matter = order_row()
    return {
        "order": o,
        "geometry": geometry_row(),
        "algebra": algebra_row(),
        "information": information_row(),
        "statistics": statistics_row(),
        "analysis": analysis_row(),
    }


def rows_with_a_row(state):
    """Only languages logic can get a binary back from."""
    return {k: v for k, v in state.items() if v in (ADMITS, REFUSES)}


def pairs(state):
    """The logic expansion: C(n,2) over the languages that hold rows."""
    r = rows_with_a_row(state)
    names = sorted(r)
    out = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            out.append((a, b, r[a] == r[b]))
    return out


def reduce_back(state):
    """language -> binary.  Register 1176: E = 0 iff the languages agree."""
    r = rows_with_a_row(state)
    e = sum(1 for v in r.values() if v == REFUSES)
    return (e == 0), e


def dissent(state):
    """Section 33.2: the identity of the dissenting language names the kind."""
    return sorted(k for k, v in rows_with_a_row(state).items() if v == REFUSES)


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-54s %20s %20s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("THE INPUT: one binary")
    chk("the cell", INPUT_BINARY, "TRANSITION-POSSIBLE")

    print("\nTHE EXPANSION: binary -> language")
    st = expand()
    for lang in ("order", "geometry", "algebra", "information", "statistics", "analysis"):
        print("     %-14s %s" % (lang, st[lang]))
    chk("order admits -- because of GJW, and only because of GJW", st["order"], ADMITS)
    chk("geometry admits", st["geometry"], ADMITS)
    chk("algebra admits", st["algebra"], ADMITS)
    chk("information REFUSES", st["information"], REFUSES)
    # RUN at last, 2026-09-13. It was NOT-RUN for twenty-odd passes because no
    # measure had been declared, which was honest; declaring one runs it.
    chk("statistics is RUN now, and admits", st["statistics"], ADMITS)
    chk("and it is the row that decided the channel -- K1, not K4",
        __import__("statrow").channel_of_refusal(), 1)
    chk("analysis earns NO ROW -- it returns a magnitude (register 1173)",
        st["analysis"], NO_ROW)

    print("\nTHE LOGIC EXPANSION: the pairs")
    pr = pairs(st)
    chk("languages holding a row", len(rows_with_a_row(st)), 5)
    chk("so C(5,2) pairs", len(pr), 10)
    agree = sum(1 for _a, _b, s in pr if s)
    chk("pairs that agree", agree, 6)
    chk("pairs that disagree", len(pr) - agree, 4)
    # AND THE PATTERN IS LAWFUL, which this file never checked before.
    import statrow
    chk("the refusing set is a lawful DOWN-SET of the hierarchy law",
        statrow.refusal_pattern_is_lawful(), True)
    for a, b, s in pr:
        print("     %-12s %-12s %s" % (a, b, "agree" if s else "DISAGREE"))

    print("\nTHE REDUCTION: language -> binary, same shape as the input")
    admitted, e = reduce_back(st)
    chk("E (register 1176: zero iff the languages agree)", e, 1)
    chk("%s admitted?" % INPUT_BINARY, admitted, False)
    chk("and the dissent is in exactly one row", dissent(st), ["information"])
    print("       Section 33.2: the identity of the dissenting language names")
    print("       the kind of object.  Order, geometry and algebra all admit.")
    print("       WHAT IS MISSING IS A VALUE, NOT A STRUCTURE.")

    print("\nWHAT THAT DOES AND DOES NOT LICENSE")
    print("     DOES     nothing structural stands against faster or cheaper --")
    print("              speed is an order question and order admits; cost is an")
    print("              algebra question and algebra admits.")
    print("     DOES NOT make anything faster or cheaper.  Information's refusal")
    print("              is MEASURED, and 4.387e71 is a real number about the")
    print("              real world.  1173 governs which language answers a")
    print("              binary, not which measurements are true.")
    import achievable
    chk("the magnitude is unmoved by any of this", achievable.ratio(1.0) < 1e-60, True)

    print("\nAND THE ROW THAT MOVED THIS SESSION")
    _o, matter_closed = order_row()
    chk("achronal.py closed the MATTER route to non-achronality", matter_closed, True)
    print("       So before pass 27 ORDER refused too, and the expansion stood at")
    print("       TWO refusals.  GJW's external causal path moved it to one -- and")
    print("       it moved the row that governs SPEED.  That is the only")
    print("       structural change this project has made to the speed question,")
    print("       and it is the thing to push on rather than the magnitude.")

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


def report():
    print(__doc__)
    print("=" * 79)
    st = expand()
    print("EXPANSION")
    for lang in ("order", "geometry", "algebra", "information", "statistics", "analysis"):
        print("  %-14s %s" % (lang, st[lang]))
    admitted, e = reduce_back(st)
    print("\nREDUCTION")
    print("  E = %d   %s admitted: %s" % (e, INPUT_BINARY, admitted))
    print("  dissent: %s" % ", ".join(dissent(st)))
    print("\n" + "=" * 79)
    print("VERDICT")
    print("  Three of the four rows already admit.  The causal structure is")
    print("  fine, the geometry embeds, the junction closes and the shell holds.")
    print("  The single dissent is INFORMATION, and by section 33.2 that names")
    print("  the kind of object: one missing a VALUE, not a STRUCTURE.")
    print("\n  Nothing structural stands against faster or cheaper.  That is not")
    print("  permission to ignore the magnitude -- it is the narrowest the")
    print("  obstruction has ever been stated.")
    print("\n  And ORDER moved this session, from refusal to admission, on GJW's")
    print("  external causal path.  It is the row that governs speed, it is the")
    print("  only structural change the project has made to that question, and")
    print("  it is the thing to push on.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
