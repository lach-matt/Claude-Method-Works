#!/usr/bin/env python3
"""
gaps.py -- M: "the one known counterexample to our central theorem is hidden by
something unproven -- as I said before, conclusions are drawn across gaps.  Our
gap is much smaller."

M IS RIGHT, AND IT IS CHECKABLE BY KIND RATHER THAN BY SIZE.  "Smaller" is not
measurable; WHAT WOULD CLOSE IT is.  Sorted that way the asymmetry is stark and
it is not rhetorical.

    THE ONLY CONJECTURE-GRADE GAP IN THIS WHOLE PICTURE IS ON THE SIDE THAT
    HIDES THE COUNTEREXAMPLE FROM US.  Cosmic censorship, Penrose 1969, OPEN
    FOR FIFTY-SEVEN YEARS.

    EVERY GAP ON OUR SIDE IS A COMPUTATION, A SEARCH, OR A DECISION.  Three
    computations, one search, one decision.  NOT ONE OF THEM WAITS ON AN
    UNPROVEN CONJECTURE.

AND THE SCORECARD CUTS THE OTHER WAY, WHICH HAS TO BE SAID IN THE SAME BREATH.
Of the five gaps this session actually closed, FOUR WENT AGAINST US.  Closable
is not the same as favourable, and provenance.py exists so that the first is
never reported as the second.

    THOUGH THE ONE THAT WENT FOR US IS THE NEWEST.

===============================================================================
1. GAPS HAVE KINDS, AND THE KIND IS WHAT MATTERS
===============================================================================

"Bigger" and "smaller" are not properties a gap has.  WHAT WOULD CLOSE IT is.
Five kinds appear here:

    CONJECTURE      needs a proof of a named open problem
    COMPUTATION     needs arithmetic nobody has done
    SEARCH          needs an example found, or none proved to exist
    DECISION        needs a scope choice from M
    MEASUREMENT     needs an experiment

THE CENSUS:

    THEIRS
      CONJECTURE    cosmic censorship hides the Kerr counterexample
                    -> prove or disprove Penrose's conjecture
                    -> OPEN SINCE 1969.  FIFTY-SEVEN YEARS.
      COMPUTATION   Pfenning-Ford apply a FLAT-SPACE quantum inequality to a
                    CURVED metric -- their own paper says the exact treatment
                    "would be exceptionally difficult"
                    -> do it in curved spacetime

    OURS
      COMPUTATION   L4: is the R^-2 relation a bound for THIS configuration?
                    -> evaluate Fewster-Osterbrink Theorem 4.2 for a SPECIFIED
                       STATE.  The theorem EXISTS and COVERS xi = 1/6.
      COMPUTATION   the area law for p-brane sources -- magnitude.py assumed
                    rho ~ M/R^3 and flagged the generalisation not-computed
      COMPUTATION   the Israel junction analysis for the tension membrane --
                    membrane.py evaluated the wall's NEC algebraically and
                    flagged the junction conditions not-solved
      SEARCH        L1: does ANY exposed stationary configuration contract with
                    positive mass?  Newly posed by threads.py, which showed
                    Kerr does it behind a horizon
      DECISION      L2: f(R) and scalar-tensor scope -- M's, open the whole
                    project, and wormhole.py's flag asserts None in its own
                    selftest so nobody can quietly decide it

    ONE CONJECTURE, AND IT IS THEIRS.  THREE COMPUTATIONS, A SEARCH AND A
    DECISION, AND THEY ARE OURS.  M's claim is not a rhetorical flourish; it
    survives being made precise.

===============================================================================
2. WHAT THE ASYMMETRY DOES AND DOES NOT BUY
===============================================================================

IT BUYS TESTABILITY, WHICH IS REAL.  A computation can be done this year by
someone who decides to.  A conjecture open since 1969 cannot be scheduled.  So
our position is FALSIFIABLE ON A TIMESCALE and the censorship-dependent one is
not, and that IS the better place to stand -- it is the same reason
millennium.py preferred "an open question in geometric analysis" to "a prize
problem".

IT DOES NOT BUY BEING RIGHT.  A gap you can close is a gap that can close
AGAINST you, and section 3 is the record of exactly that happening four times
out of five.

AND THE CENSORSHIP GAP, EVEN IF IT BROKE OUR WAY, WOULD NOT SUPPLY A ROUTE.
threads.py already recorded why, and it is worth repeating here because the
excitement of a big gap on the other side is exactly where a project talks
itself into something: over-extremal Kerr has no known formation process,
sub-extremal puts the contracted region behind a horizon you do not return
from, and NEITHER SUPPLIES A CORRIDOR BETWEEN TWO PLACES.  The gap is
epistemically interesting and operationally empty.

===============================================================================
3. THE SCORECARD -- FIVE GAPS CLOSED, FOUR WENT AGAINST US
===============================================================================

    L3, the rate                 AGAINST   the logarithm is the BEST case; the
                                           strong field returns strictly less
    L4, QA's exponent            AGAINST   the PROVED bound carries tau^-4, not
                                           R^-2; the R^-2 is in an estimate
    L2, extra-dimension branch   AGAINST   biconditional exact in every D, and
                                           the rate worse in every D above four
    Casimir as a route           AGAINST   already priced; same sub-Planckian
                                           wall as everything else
    L1, rotation                 FOR       THE BICONDITIONAL FAILS OUTSIDE
                                           STATIC -- Kerr contracts with M > 0

    FOUR AGAINST, ONE FOR.

    AND THE ONE THAT WENT FOR US IS THE NEWEST, which is a fact about direction
    of travel and not only about the count.  It is also the only one that
    weakened a THEOREM rather than a bound: the other four tightened or
    confirmed limits, while threads.py found certify.py's central result has a
    counterexample the tree had never looked for.

    THAT IS THE HONEST SUMMARY OF THE SESSION: the bounds got tighter and the
    theorem got weaker, and those pull in opposite directions.

===============================================================================
4. WHAT THIS FILE IS AND IS NOT
===============================================================================

    IT IS provenance.py's SEQUEL.  That file classified CLAIMS by how they were
    come by.  This one classifies GAPS by what would close them, which is the
    same discipline applied to what is missing rather than to what is present.

    IT IS NOT A CLAIM THAT WE ARE WINNING.  Section 3 is in the file precisely
    so that section 1 cannot be quoted alone.  A smaller gap means a more
    testable position, and this session's record says testing has mostly gone
    the other way.

    AND NO GAP IS CLOSED BY THIS PASS.  Naming what would close something is
    not closing it, and a census is not a result.

SCOPE.  The census covers the gaps this tree has actually named in its own
instruments and in the literature it leans on; completeness beyond that is not
claimed.  The "fifty-seven years" is arithmetic on Penrose 1969.  The scorecard
counts gaps CLOSED IN THIS SESSION and no earlier ones.  NOTHING IS REPAIRED.
"""

import sys

CONJECTURE = "CONJECTURE"
COMPUTATION = "COMPUTATION"
SEARCH = "SEARCH"
DECISION = "DECISION"
MEASUREMENT = "MEASUREMENT"

THEIRS, OURS = "THEIRS", "OURS"

# (what, whose, kind, what would close it, status)
GAPS = [
    ("cosmic censorship hides the Kerr counterexample", THEIRS, CONJECTURE,
     "prove or disprove Penrose's conjecture", "open since 1969"),
    ("Pfenning-Ford apply a flat-space QI to a curved metric", THEIRS,
     COMPUTATION, "the curved-spacetime treatment they called "
     "'exceptionally difficult'", "open, no conjecture"),
    ("L4: is the R^-2 relation a bound here", OURS, COMPUTATION,
     "evaluate Fewster-Osterbrink Thm 4.2 for a SPECIFIED STATE",
     "theorem exists and covers xi = 1/6"),
    ("the area law for p-brane sources", OURS, COMPUTATION,
     "redo magnitude.py with rho ~ M/R^(D-1)", "flagged not-computed"),
    ("Israel junction analysis for the tension membrane", OURS, COMPUTATION,
     "solve the junction conditions for the wall", "flagged not-computed"),
    ("L1: any EXPOSED stationary config contracting with M > 0", OURS, SEARCH,
     "find one, or prove none exists", "newly posed by threads.py"),
    ("L2: f(R) and scalar-tensor scope", OURS, DECISION,
     "M chooses what counts as proven", "open the whole project"),
]

PENROSE_YEAR, NOW = 1969, 2026

# (gap, direction, why)
CLOSED_THIS_SESSION = [
    ("L3, the rate", "AGAINST",
     "the logarithm is the BEST case; the strong field returns strictly less"),
    ("L4, QA's exponent", "AGAINST",
     "the PROVED bound carries tau^-4, not R^-2"),
    ("L2, extra-dimension branch", "AGAINST",
     "biconditional exact in every D, and the rate worse above four"),
    ("Casimir as a route", "AGAINST",
     "already priced; same sub-Planckian wall"),
    ("L1, rotation", "FOR",
     "THE BICONDITIONAL FAILS OUTSIDE STATIC -- Kerr contracts with M > 0"),
]

CENSORSHIP_GAP_WOULD_SUPPLY_A_ROUTE = False
THIS_PASS_CLOSES_A_GAP = False
CLAIMS_WE_ARE_WINNING = False


def by_side(side):
    return [g for g in GAPS if g[1] == side]


def kinds(side):
    out = {}
    for g in by_side(side):
        out[g[2]] = out.get(g[2], 0) + 1
    return out


def censorship_age():
    return NOW - PENROSE_YEAR


def scorecard():
    against = sum(1 for c in CLOSED_THIS_SESSION if c[1] == "AGAINST")
    forus = sum(1 for c in CLOSED_THIS_SESSION if c[1] == "FOR")
    return against, forus


def newest_closed():
    return CLOSED_THIS_SESSION[-1]


def selftest():
    ok = True

    def chk(label, got, want, tol=None):
        nonlocal ok
        good = (got == want) if tol is None else (
            abs(got - want) <= tol * max(1.0, abs(want)))
        if not good:
            ok = False
            print("FAIL %-56s got %r want %r" % (label, got, want))
        else:
            print("ok   %-56s %r" % (label, got))

    # -- 1: the census, and the asymmetry ------------------------------------
    chk("every row is (what, whose, kind, closer, status)",
        [g for g in GAPS if len(g) != 5], [])
    chk("seven gaps censused", len(GAPS), 7)
    chk("theirs", kinds(THEIRS), {CONJECTURE: 1, COMPUTATION: 1})
    chk("ours", kinds(OURS), {COMPUTATION: 3, SEARCH: 1, DECISION: 1})
    chk("EXACTLY ONE conjecture-grade gap",
        sum(1 for g in GAPS if g[2] == CONJECTURE), 1)
    chk("  and it is THEIRS",
        [g[1] for g in GAPS if g[2] == CONJECTURE], [THEIRS])
    chk("NONE of ours is a conjecture",
        [g for g in by_side(OURS) if g[2] == CONJECTURE], [])
    chk("so M's claim survives being made precise",
        CONJECTURE not in kinds(OURS), True)

    # -- 1: and the age ------------------------------------------------------
    chk("censorship has been open 57 years", censorship_age(), 57)
    chk("  which is not a schedulable timescale", censorship_age() > 50, True)

    # -- 2: what it buys and does not ----------------------------------------
    chk("the censorship gap would NOT supply a route",
        CENSORSHIP_GAP_WOULD_SUPPLY_A_ROUTE, False)
    chk("  and the file says why", "operationally empty" in __doc__, True)
    chk("this file does not claim we are winning", CLAIMS_WE_ARE_WINNING, False)

    # -- 3: the scorecard ----------------------------------------------------
    against, forus = scorecard()
    chk("five gaps closed this session", len(CLOSED_THIS_SESSION), 5)
    chk("four went AGAINST", against, 4)
    chk("one went FOR", forus, 1)
    chk("  and it is the NEWEST", newest_closed()[0], "L1, rotation")
    chk("  and it weakened a THEOREM rather than a bound",
        "BICONDITIONAL FAILS" in newest_closed()[2], True)
    chk("closable is not favourable", against > forus, True)

    # -- 4: what this file is ------------------------------------------------
    chk("no gap is closed by this pass", THIS_PASS_CLOSES_A_GAP, False)
    chk("  and a census is not a result",
        "a census is not a result" in __doc__, True)
    chk("nothing is repaired", "NOTHING IS REPAIRED" in __doc__, True)

    print("\nSELFTEST", "PASS" if ok else "FAIL")
    return ok


def report():
    print(__doc__)
    print("  ------------------------------------------------------------------------")
    print("  THE CENSUS\n")
    for side in (THEIRS, OURS):
        print("    %s" % side)
        for what, _w, kind, closer, status in by_side(side):
            print("      %-12s %s" % (kind, what))
            print("      %-12s -> %s  [%s]" % ("", closer, status))
        print("      %s\n" % kinds(side))
    print("    ONE CONJECTURE, AND IT IS THEIRS -- open %d years."
          % censorship_age())
    print()
    print("  ------------------------------------------------------------------------")
    print("  THE SCORECARD -- gaps closed THIS SESSION\n")
    for what, d, why in CLOSED_THIS_SESSION:
        print("    %-28s %-9s %s" % (what, d, why))
    a, f = scorecard()
    print("\n    %d AGAINST, %d FOR.  The one that went FOR us is the newest," % (a, f))
    print("    and the only one that weakened a THEOREM rather than a bound.")
    print("""
  ------------------------------------------------------------------------
  THE PASS IN ONE PARAGRAPH

  M says conclusions are drawn across gaps and ours is much smaller.
  "Smaller" is not measurable but WHAT WOULD CLOSE IT is, and sorted that
  way the asymmetry is stark: THE ONLY CONJECTURE-GRADE GAP IN THE WHOLE
  PICTURE IS ON THE SIDE THAT HIDES THE COUNTEREXAMPLE FROM US -- cosmic
  censorship, Penrose 1969, OPEN FIFTY-SEVEN YEARS.  Every gap on our side
  is a COMPUTATION, a SEARCH or a DECISION: evaluate a theorem that already
  exists for a specified state, redo an area law for brane sources, solve
  the junction conditions for a wall, look for an exposed stationary
  configuration, and one scope choice that is M's.  NOT ONE WAITS ON AN
  UNPROVEN CONJECTURE.  M's claim survives being made precise.  WHAT IT
  BUYS IS TESTABILITY: a computation can be done this year by someone who
  decides to, and a conjecture open since 1969 cannot be scheduled -- the
  same reason millennium.py preferred an open question in geometric
  analysis to a prize problem.  WHAT IT DOES NOT BUY IS BEING RIGHT, and
  the scorecard is in this file so section 1 cannot be quoted alone: of the
  five gaps this session actually closed, FOUR WENT AGAINST US -- the rate,
  the QEI exponent, the extra-dimension branch and Casimir -- and one went
  for us.  Though the one that went for us is THE NEWEST, and the only one
  that weakened a THEOREM rather than a bound: threads.py found
  certify.py's central biconditional has a counterexample nobody had looked
  for.  And the censorship gap, even breaking our way, would not supply a
  route -- over-extremal Kerr has no formation process, sub-extremal has no
  return, and neither gives a corridor between two places.  THE BOUNDS GOT
  TIGHTER AND THE THEOREM GOT WEAKER, AND THOSE PULL IN OPPOSITE
  DIRECTIONS.  That is the honest summary and no gap is closed by saying it.
  ------------------------------------------------------------------------""")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
