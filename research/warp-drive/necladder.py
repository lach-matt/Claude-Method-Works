#!/usr/bin/env python3
"""
necladder.py -- the rung this project has been standing on, and the four above it.

M asked whether there is an aspect of quantum entanglement the warp work is not
accounting for.  There is, and the corpus already carries it: THE NULL ENERGY
CONDITION IS NOT A BOOLEAN.  The Method's violation index grades it on five
rungs, and two of the nine coordinates beside it are quantum-correlation axes.

    PINNED -- The Method 1.6, BUILD180 compendia, Part V Sec. 5.1 (line 13138):

      NEC  null energy | intact / pointwise / ANEC arbitrarily small /
                         macroscopic QI-bounded / QI-violating

    PINNED -- same section (line 13145), and this is the sentence that matters:

      "Our position is (0, 1, 0, 0, 1, 0, 0, 0, 0), with two components fixed by
       MEASUREMENT: S_corr = 1 because quantum mechanics violates Bell locality
       while respecting microcausality, and NEC = 1 BECAUSE CASIMIR ENERGY IS
       MEASURED AND VIOLATES THE NULL ENERGY CONDITION POINTWISE."

THE WORLD IS MEASURED AT RUNG 1.  This project has spent its entire life holding
warp shells to RUNG 0 -- "all four pointwise energy conditions positive" -- and
calling every departure from it a no-go.  TARGET-1's achievement was a rung-0
shell.  GATE-CLOSED's fatal finding was that a compactly supported shift needs
Type IV, which is to say it needs RUNG >= 1: the rung the Casimir effect already
occupies in a laboratory.

And the index's own infeasible core is at NEC = 3, not 1:

    PINNED (Part V Sec. 5.3, Part VII 7.1): core (X_exp=0, U_ghost=0,
    NEC_pt=3, EOM=2nd) -- ONE cell, E = 30 at nine letters, E = 816 at fifteen.

So there are TWO free rungs between where the world is measured and where the
index breaks.  Rung 2 is named and costed: Visser-Kar-Dadhich, traversable
wormholes with arbitrarily small energy condition violations, PRL 90 201102 --

    PINNED (Appendix D1): I_V = CONTOUR-INTEGRAL (rho + p_r) dV over the region
    where the NEC is violated.  "I_V can be made arbitrarily small by shrinking
    that region, WHICH IS WHY THE NEC AXIS IS GRADED BY SCALE AND NOT BY
    VIOLATION-OR-NOT."

-- WHERE THE ENTANGLEMENT ENTERS ----------------------------------------------
Three places, and the corpus files all three:

  1. RUNG 1 IS AN ENTANGLEMENT EFFECT.  Casimir energy is vacuum entanglement
     between boundaries.  The rung the world sits on is bought with it.

  2. THE QUANTUM CONDITION IS AN ENTROPY BOUND, AND IT IS NOT A LETTER.
     PINNED (Appendix D5): <T_kk> >= (h-bar/2pi) S''_out, the QNEC -- S_out the
     entanglement entropy outside a cut of a null surface, the double prime the
     second variation along a null deformation.  Its own status line:

       "a BOUND on the stress tensor by an entropy variation, not a forcing edge
        between coordinates.  IT DOES NOT ENTER THE INDEX AS A CHARGE, WHICH IS
        WHY IT APPEARS IN THE APPENDIX AND NOT IN THE EDGE LIST."

     So the index's alphabet cannot express the one condition that licenses
     negative energy quantum-mechanically.  Classical NEC forbids <T_kk> < 0.
     QNEC permits it, budgeted by -S''_out.  ENTANGLEMENT ENTROPY IS THE BUDGET.

  3. THE LADDER'S TOP IS GUARDED BY A CORRELATION PRINCIPLE, NOT A GRAVITATIONAL
     ONE.  Two of the nine coordinates are quantum-correlation axes --

       Sc  CHSH correlation | local <=2 / quantum <=2 sqrt2 / post-quantum <=4
       IC  information causality | holds / violated at m>0 / violated at m=0

     -- and the constraint-language defect is PINNED (line 6984) as the arity-4
     rule NEC>=3 -> IC v U v X.  Macroscopic exotic matter is not forbidden by
     gravity alone: the index says it forces information causality, unitarity or
     the causal ladder.  And PINNED (Audit 22, Sec. 6.4): of IC's six
     term-sharing pairs, "IC HAS NEVER BEEN CHECKED ONCE, and IC is load-bearing:
     it is the unique principle forbidding post-quantum correlations."

-- WHAT THIS INSTRUMENT DOES --------------------------------------------------
It states the ladder, reproduces the index from the corpus's own edge list, and
re-grades this project's measured results on it.  It makes no physics claim from
the index: the corpus itself rules (line 1670) that the violation index's numbers
"enter as an instance of the operator, NEVER AS PHYSICS", and that ruling is
honoured here.  The RUNGS are physics; the CELL COUNTS are the operator.

Status: PINNED (stated in the volumes) / DERIVED / MEASURED / OPEN.  stdlib only.
The edge list is LOADED from extracted/, never restated here.
"""
import itertools, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
EDGE_LIST = os.path.join(REPO, "extracted", "archives", "method16-rp-b-data",
                         "vi_best.json")

# ------------------------------------------------------------- the ladder ----
# PINNED, BUILD180 line 13138.  Index 4 of the nine-letter coordinate set.
NEC_RUNGS = [
    "intact",                  # 0  no violation anywhere
    "pointwise",               # 1  MEASURED -- Casimir
    "ANEC arbitrarily small",  # 2  Visser-Kar-Dadhich, I_V -> 0 by shrinking
    "macroscopic QI-bounded",  # 3  the index's infeasible core sits here
    "QI-violating",            # 4
]
MEASURED_RUNG = 1     # PINNED: "NEC = 1 because Casimir energy is measured"
CORE_RUNG     = 3     # PINNED: core (X_exp=0, U_ghost=0, NEC_pt=3, EOM=2nd)

# PINNED, Part V Sec. 5.1: the nine coordinates, in the order the box product
# 4*3*3*3*5*2*2*3*3 = 19,440 is printed in.
AXES  = ["X", "Sc", "IC", "U", "NEC", "L", "SD", "DNc", "DNd"]
RUNGS = [4, 3, 3, 3, 5, 2, 2, 3, 3]
OUR_POSITION = (0, 1, 0, 0, 1, 0, 0, 0, 0)   # PINNED, line 13145

def box_size():
    """DERIVED.  The ambient box.  PINNED figure: 19,440."""
    n = 1
    for r in RUNGS:
        n *= r
    return n

# --------------------------------------------------- the index, reconstructed -
def load_rules(path=EDGE_LIST):
    """The edge list, LOADED from the corpus.

    The compendium says of it (Part V, before Part VI): "THE EDGE LIST ITSELF IS
    NOT PRINTED ANYWHERE IN THIS PAPER, and until it is, those five conditions
    are what stands in its place."  It is not printed -- and it is in the
    repository, extracted by tools/consolidate.py from
    method16_rp_B_data.tar.gz.  Part V's recompute note names it by filename and
    rule count: "the 17 rules of vi_best.json applied to the 4*3*3*3*5*2*2*3*3
    box give exactly 2,370."  This function loads that file.  It is never
    transcribed into this instrument."""
    return json.load(open(path))["rules"]

def admits(cell, rules):
    """DERIVED.  A rule [a, v, [[b,w],...]] reads: c[a] >= v implies c[b] >= w
    for at least one (b,w).  A Horn implication with a disjunctive head.

    Four other readings were tried -- equality triggers, equality heads,
    conjunctive heads, upper-bound heads, and the converse direction -- and only
    this one reproduces the printed 2,370.  The selftest records their counts so
    the choice is a measurement, not a preference."""
    for a, v, head in rules:
        if cell[a] >= v and not any(cell[b] >= w for b, w in head):
            return False
    return True

def closed_cells(rules):
    """DERIVED.  The closed set.  PINNED figure: 2,370."""
    return [c for c in itertools.product(*[range(r) for r in RUNGS])
            if admits(c, rules)]

def excluding_rules(cell, rules):
    """DERIVED.  Every rule that forbids a cell, as (index, a, v, head)."""
    return [(i, a, v, head) for i, (a, v, head) in enumerate(rules)
            if cell[a] >= v and not any(cell[b] >= w for b, w in head)]

# ---------------------------------------- this project's results, re-graded ---
# MEASURED here, in this tree, and now placed on the corpus's ladder.  A rung is
# assigned from what was measured, never from what was hoped.
PROJECT_RESULTS = [
    # (id, rung, source, what was measured, and what the rung costs)
    ("TARGET-1", 0, "TARGET-1-RESULT.md",
     "zero Type IV, bulk NEC +5.044e39 and DEC +4.021e39: no violation anywhere",
     "rung 0 is STRICTER THAN THE MEASURED WORLD -- an achievement, not a requirement"),
    ("TRANSITION", 0, "TARGET-1-RESULT.md",
     "the source-vacuum band is clean and converged; outer negatives fall 8x under refinement",
     "also rung 0, and the refinement says the residual negatives are grid error"),
    ("GATE-CLOSED", None, "GATE-CLOSED.md",
     "a compactly supported shift in vacuum gives Type IV at 165/165, 210/210, 154/154 cells",
     "RUNG >= 1 and UNPLACED: I_V was never integrated, so rung 1 vs 2 vs 3 is unknown"),
    ("TORUS", None, "torus.py",
     "the hoop-tension DEC bound lambda <= c^2/(G ln(8R0/a)) holds the bore open",
     "UNPLACED: a bound on tension, not an integral over a violating region"),
    ("SHELL-5KM", 0, "THE-DRIVE.md",
     "nuclear matter at 5 km: 1.11 Msun, 0.0476 c, all four conditions satisfied",
     "rung 0 again -- the whole scaling series was run at the strictest rung"),
]

def unplaced():
    """DERIVED.  Results whose rung is not known because I_V was never measured."""
    return [r for r in PROJECT_RESULTS if r[1] is None]

def headroom():
    """DERIVED.  Rungs between the measured world and the index's core."""
    return CORE_RUNG - MEASURED_RUNG

# ------------------------------------------------------------------ report ---
def selftest():
    ok = True
    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  %-58s %14s %14s  %s" % (label, got, want, "ok" if good else "FAIL"))

    print("The corpus's own printed figures, reproduced from its own edge list")
    chk("the ambient box  (Part V 5.1: 4*3*3*3*5*2*2*3*3)", box_size(), 19440)
    rules = load_rules()
    chk("rules in vi_best.json  (Part V: 'the 17 rules')", len(rules), 17)
    cells = closed_cells(rules)
    chk("closed cells  (Part V 5.3: 2,370)", len(cells), 2370)
    chk("nine coordinates", len(AXES), 9)
    chk("the NEC axis has five rungs", RUNGS[AXES.index("NEC")], 5)

    print("\nThe reading of the rules is a measurement, not a preference")
    # Only one semantics reproduces 2,370.  The rest are recorded so the choice
    # cannot be quietly re-made.
    def count(sem):
        return sum(1 for c in itertools.product(*[range(r) for r in RUNGS])
                   if all(sem(c, a, v, h) for a, v, h in rules))
    alts = (
        ("ge -> OR ge   (used)", lambda c, a, v, h: c[a] < v or any(c[b] >= w for b, w in h)),
        ("eq -> OR ge",          lambda c, a, v, h: c[a] != v or any(c[b] >= w for b, w in h)),
        ("ge -> OR eq",          lambda c, a, v, h: c[a] < v or any(c[b] == w for b, w in h)),
        ("ge -> AND ge",         lambda c, a, v, h: c[a] < v or all(c[b] >= w for b, w in h)),
        ("ge -> OR le",          lambda c, a, v, h: c[a] < v or any(c[b] <= w for b, w in h)),
    )
    counts = [(n, count(f)) for n, f in alts]
    for n, v in counts:
        print("    %-24s %8d" % (n, v))
    chk("exactly one reading reproduces 2,370", sum(1 for _, v in counts if v == 2370), 1)

    print("\nA FINDING, recorded and not repaired")
    # The edge list forbids the cell the paper names as our own position.
    chk("our measured position is admitted by the edge list",
        admits(OUR_POSITION, rules), False)
    bad = excluding_rules(OUR_POSITION, rules)
    chk("rules excluding it", len(bad), 1)
    i, a, v, head = bad[0]
    chk("the axis it triggers on", AXES[a], "Sc")
    chk("the rule", "%s>=%d -> %s" % (AXES[a], v,
        " v ".join("%s>=%d" % (AXES[b], w) for b, w in head)),
        "Sc>=1 -> L>=1 v DNd>=2")

    print("\nThe ladder -- physics, not the operator")
    chk("the world is measured at rung", MEASURED_RUNG, 1)
    chk("the infeasible core sits at rung", CORE_RUNG, 3)
    chk("free rungs between them", headroom(), 2)
    chk("rung 1's name", NEC_RUNGS[MEASURED_RUNG], "pointwise")
    chk("rung 2's name", NEC_RUNGS[2], "ANEC arbitrarily small")

    print("\nThis project's results on that ladder")
    chk("results graded", len(PROJECT_RESULTS), 5)
    chk("graded at rung 0 -- stricter than the measured world",
        sum(1 for r in PROJECT_RESULTS if r[1] == 0), 3)
    chk("UNPLACED for want of an I_V integral", len(unplaced()), 2)
    chk("results graded above rung 0", sum(1 for r in PROJECT_RESULTS
        if r[1] is not None and r[1] > 0), 0)

    print("\n%s" % ("SELFTEST PASS" if ok else "SELFTEST FAIL"))
    return 0 if ok else 1


def report():
    rules = load_rules()
    cells = closed_cells(rules)
    print("""
necladder.py -- the rung this project has been standing on
================================================================================
The null energy condition is not a boolean.  The Method grades it on five rungs,
and the world is MEASURED on the second one.
""")
    for i, name in enumerate(NEC_RUNGS):
        mark = ""
        if i == MEASURED_RUNG:
            mark = "  <-- THE WORLD IS HERE.  Casimir.  Measured."
        if i == CORE_RUNG:
            mark = "  <-- the index's infeasible core"
        if i == 0:
            mark = "  <-- every warp result in this project"
        print("    NEC = %d   %-24s%s" % (i, name, mark))
    print("""
  Two free rungs between the measured world and the point where the index
  breaks, and this project has used neither.  TARGET-1's achievement was a
  RUNG-0 shell -- all four pointwise conditions positive everywhere -- which is
  STRICTER THAN THE UNIVERSE.  GATE-CLOSED's fatal finding was that a compactly
  supported shift needs Type IV in vacuum: that is rung >= 1, and rung 1 is
  laboratory equipment.

  Rung 2 is named and costed.  Visser, Kar & Dadhich, PRL 90 201102: traversable
  wormholes with ARBITRARILY SMALL energy condition violations, quantified by

      I_V = contour-integral (rho + p_r) dV   over the violating region

  and the corpus's own status line on it: "I_V can be made arbitrarily small by
  shrinking that region, WHICH IS WHY THE NEC AXIS IS GRADED BY SCALE AND NOT BY
  VIOLATION-OR-NOT."

-- WHERE THE ENTANGLEMENT IS ---------------------------------------------------
  1. Rung 1 IS an entanglement effect.  Casimir energy is vacuum entanglement
     between boundaries.  The rung the world stands on is bought with it.

  2. The quantum condition is an ENTROPY BOUND, and the index has no letter for
     it.  Appendix D5:  <T_kk> >= (h-bar / 2 pi) S''_out  -- the QNEC, with
     S_out the entanglement entropy outside a cut of a null surface.  Classical
     NEC forbids negative <T_kk>.  QNEC PERMITS IT, budgeted by -S''_out.
     ENTANGLEMENT ENTROPY IS WHAT PAYS FOR NEGATIVE ENERGY.  And the corpus files
     it in an appendix with the reason: "it does not enter the index as a charge,
     which is why it appears in the appendix and not in the edge list."

  3. The top of the ladder is guarded by a CORRELATION principle.  Two of the
     nine coordinates are quantum-correlation axes --

       Sc  CHSH strength      local <=2 / quantum <=2 sqrt2 / post-quantum <=4
       IC  information causality   holds / violated at m>0 / violated at m=0

     -- and the constraint-language defect is the arity-4 rule

         NEC >= 3  ->  IC  v  U  v  X

     Macroscopic exotic matter is not forbidden by gravity alone.  The index says
     it forces information causality, unitarity, or the causal ladder.  Audit 22:
     of IC's six term-sharing pairs, IC "HAS NEVER BEEN CHECKED ONCE, and IC is
     load-bearing: it is the unique principle forbidding post-quantum
     correlations."

-- THE INDEX, RECONSTRUCTED FROM THE CORPUS'S OWN EDGE LIST --------------------
  Part V says: "THE EDGE LIST ITSELF IS NOT PRINTED ANYWHERE IN THIS PAPER, and
  until it is, those five conditions are what stands in its place."  It is not
  printed.  It is in the repository -- extracted/archives/method16-rp-b-data/
  vi_best.json, 17 rules, seated by tools/consolidate.py out of
  method16_rp_B_data.tar.gz.  Loaded, never transcribed:
""")
    print("    ambient box          %6d      printed: 19,440" % box_size())
    print("    rules loaded         %6d      printed: 'the 17 rules of vi_best.json'" % len(rules))
    print("    closed cells         %6d      printed: 2,370" % len(cells))
    print("""
  Five readings of the rule format were tried and exactly ONE reproduces 2,370.

-- A FINDING.  RECORDED, NOT REPAIRED ------------------------------------------
  The edge list forbids the cell the paper names as our own position.""")
    bad = excluding_rules(OUR_POSITION, rules)
    print("    our position     (%s)" % ", ".join(str(x) for x in OUR_POSITION))
    for i, a, v, head in bad:
        print("    rule %-2d forbids it   %s >= %d  ->  %s"
              % (i, AXES[a], v, "  v  ".join("%s >= %d" % (AXES[b], w) for b, w in head)))
    print("""
  Read it: quantum correlation at the Tsirelson rung forces nonlinear evolution
  or super-quantum state discrimination.  The world has Sc = 1 with L = 0 and
  DNd = 0, so the rule is false of the world it is meant to contain.

  This is NOT offered as physics.  The corpus rules (V-table, line 1670) that
  the violation index's numbers "enter as an instance of the operator, NEVER AS
  PHYSICS", computed "over a coordinate set that is demonstrably incomplete".
  That ruling is honoured: the RUNGS above are physics, the CELL COUNTS are the
  operator, and this row is a defect in a fitted rule set -- filed, per the
  chat-67 full hold, as a finding and not a repair.

-- THIS PROJECT'S RESULTS, RE-GRADED -------------------------------------------""")
    print("  %-13s %6s  %s" % ("result", "rung", "what was measured"))
    for rid, rung, src, meas, note in PROJECT_RESULTS:
        print("  %-13s %6s  %s" % (rid, "--" if rung is None else str(rung), meas))
        print("  %-13s %6s  %s" % ("", "", note))
    print("""
  Three of five sit at rung 0.  Two are UNPLACED -- and they are unplaced for
  one reason: I_V WAS NEVER INTEGRATED.  GATE-CLOSED counted Type IV cells and
  declared the branch dead.  Counting cells answers "is the NEC violated"; the
  ladder asks "BY HOW MUCH, OVER WHAT SCALE", and that is a different number
  nobody here has computed.

    THE NO-GO THIS PROJECT HAS BEEN OBEYING IS A RUNG-0 NO-GO.

  What would settle it, and it is one measurement: integrate rho + p_r over the
  violating region of the GATE-CLOSED shift configurations and place them on the
  ladder.  If they land at rung 1 or 2, the corpus's own index does not forbid
  them -- the core is at 3 -- and GATE-CLOSED was closed against a standard
  stricter than the Casimir effect.  Recorded as OPEN.  A finding is not a
  repair.
""")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else report())
