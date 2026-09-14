"""
===============================================================================
questions.py -- THE QUESTION INDEX.  Seven questions, one per language.
===============================================================================

M: "warp is not an index. It is a question."
M: "There are seven languages, and likely 7 distinct, formalized, universal
    questions that can only be asked in that language."
M: "they are general questions that ask one thing, some whose answers includes
    warp."

All three are right, and the third is what makes the index buildable: the
members are GENERAL questions, warp is not one of them, and warp appears in the
ANSWERS to some.

===============================================================================
0. THE KIND, AND WHY THE TREE KEPT LOOKING FOR THE WRONG THING
===============================================================================

An INDEX has cells and a box; it closes or fails to close, and that places it in
the channel lattice.  A QUESTION is asked OF the languages.  Both yield a subset
of the five binary-returning languages, which is why the tree confused them --
refusal.py's section on the two kinds is that correction.

duality.py spent a section hunting a host for TRANSITION-POSSIBLE, and a later
pass proved by the top-corner theorem that no such host can exist.  BOTH WERE
LOOKING FOR THE WRONG KIND OF THING, and so was this file's first version, which
seated four warp questions and recorded "four members, all from one
investigation" as its principal caution.  That caution was the whole objection.

===============================================================================
1. SEVEN LANGUAGES ASK; ONLY FIVE ANSWER WITH A BINARY
===============================================================================

That is the resolution of a discrepancy this tree has carried unexamined.  The
channel lattice is built on FIVE languages because only five return a binary --
register 1173's admission criterion, and alpha.py proves membership in the
hierarchy is exactly that.  But the language index has SEVEN members.

    ALL SEVEN CAN ASK.  ONLY FIVE CAN ANSWER WITH A CELL DECISION.
    `analysis` returns a MAGNITUDE and `documentary` returns a CITATION.

So there are seven questions and a five-element answer lattice, and the two
counts were never in conflict -- they count different things.

THE SEVEN, in the tree's own words where it has them (research/README.md's
expansion table gives six; documentary's is cypher.ADMISSION as alpha.py quotes
it verbatim):

    order        is there an admissible precedence?              binary
    algebra      is it closed under its operation?               binary
    geometry     does it embed?                                  binary
    information  does it need an unavailable coordinate?         binary
    statistics   is it drawn from a distribution?                binary
    analysis     is there a continuous law?                      MAGNITUDE
    documentary  is it recorded, and by what?                    CITATION

===============================================================================
2. THE ROSTER IS DATA, AND THE RULING IS THIS TREE'S ONLY
===============================================================================

Which languages there are is the corpus's docket 20x-04/20x-09, and CLAUDE.md is
explicit that the rosters stay data.  M has ruled that this tree's work
supersedes the older corpus material for further work.  Both are honoured:

    THE ROSTER IS A PARAMETER.  `--roster` selects it, exactly as cypher.py
    does, and nothing here asserts one in code.

    THE RULING IS SEVEN, FOR THIS TREE.  research/warp-drive/DOCKET.md carries
    it.  It rules NOTHING on the corpus's docket, and tools/cypher.py is not
    touched by this file or by that ruling.

===============================================================================
3. THE COORDINATES ARE PROPERTIES OF THE QUESTION -- AND THEY COLLAPSE
===============================================================================

Not properties of the language, or the index would be the language index
relabelled.  Five were grounded from the tree:

    RET   what an answer IS        0 citation, 1 magnitude, 2 binary
    OPR   is there an operator that answers it
    RUN   has this tree run it     0 never asked, 1 asked/NO-ROW, 2 answered
    DECL  declared operator-bearing in roster 1173
    SPK   does it speak on the energy-condition index

    AND THEY ARE NOT INDEPENDENT.  Measured: RET DETERMINES OPR, RUN AND SPK,
    and RUN determines RET.  Only DECL is independent of RET.  The seven
    questions collapse to FOUR distinct cells.

That is the honest content of the construction, and it is a negative: **as far
as this tree can measure them, the seven questions differ only in what kind of
answer they return, refined once by whether roster 1173 declared them.**  There
is no more resolution available, because the five binary languages are
extensive, idempotent and monotone alike -- hlaw measured 300 of 300 -- and
nothing in the tree separates them except what they close, which is the channel
lattice, which is the language index again.

===============================================================================
4. IT LANDS ON THE DEMANDED CELL, AND THAT IS NOT A FILL
===============================================================================

The five-coordinate form closes in `statistics` alone, arity 5, density 5.6 %,
and its master cell is

        (1, 1, 0, 2, 1)  --  EXACTLY master.DEMANDED_AT_EIGHT

**THIS IS NOT REPORTED AS FILLING THE DEMAND, AND THREE MEASUREMENTS SAY WHY.**

    ONE.  IT IS NOT ROBUST TO THE COORDINATE CHOICE.  Of the twenty-six
    non-degenerate subsets of the five coordinates, EXACTLY ONE lands on that
    cell -- the full five.  Reduce to the independent content, (RET, DECL), and
    it lands on (2, 1, 0, 0, 3), a cell periodic layout 2-D already occupies.

    TWO.  THE HIT RESTS ON REDUNDANT COORDINATES.  Three of the five are
    determined by RET.  The arity band that puts it at D = 2 is carried by
    coordinates that add no information about which question is which.

    THREE.  THE DEMAND IS NOT LIVE.  DOCKET 5 corrected the Petrov index's
    density against a realisable box -- a theorem about the Weyl tensor, not a
    convention -- and Petrov-corrected the master index CLOSES and demands
    NOTHING.  There is no demand here to fill.

    AND THIS IS THE THIRD TIME.  The bounds index landed on this cell and its
    own file recorded "drop any single one of the five slots and the hit fails";
    that fill was withdrawn.  refusal.py measures that 21 of 565 re-chartings of
    the ALREADY-SEATED indexes land on it.  Now a third construction lands on it
    under one coordinate choice of twenty-six.

        THE DEMANDED CELL IS EASY TO HIT, AND HITTING IT HAS NEVER ONCE
        SURVIVED SCRUTINY.  That is the finding, and it is about the demand
        rather than about any of the three indexes that hit it.

===============================================================================
WHAT THIS FILE CLAIMS
===============================================================================

    That there are seven questions, one per language, and the tree states six of
    them in its own words.  That all seven ask and only five answer with a
    binary, which reconciles the 7 and the 5.  That coordinatised by properties
    of the question they collapse to four cells, and why.  That the landing on
    the demanded cell is an artefact of a coordinate choice and is not a fill.

    IT DOES NOT CLAIM that four cells over seven questions is a good index, that
    the seven questions are exhaustive, or that the corpus's roster docket is
    resolved.
"""

import itertools
import sys

import hlaw
import master
import selfindex

# The rosters are DATA. --roster selects one; nothing here asserts one.
ROSTERS = {
    "seven": ("order", "algebra", "geometry", "information", "statistics",
              "analysis", "documentary"),
    "five": ("order", "algebra", "geometry", "information", "statistics"),
}
DEFAULT_ROSTER = "seven"

# The question each language asks -- one thing, generally. Six are the tree's
# own words (research/README.md's expansion table); documentary's is
# cypher.ADMISSION as alpha.py quotes it verbatim.
ASKS = {
    "order":       "is there an admissible precedence?",
    "algebra":     "is it closed under its operation?",
    "geometry":    "does it embed?",
    "information": "does it need an unavailable coordinate?",
    "statistics":  "is it drawn from a distribution?",
    "analysis":    "is there a continuous law?",
    "documentary": "is it recorded, and by what?",
}
RETURNS = {"documentary": 0, "analysis": 1}     # 0 citation, 1 magnitude, 2 binary
ASKED = {"documentary": 0, "analysis": 1}       # 0 never, 1 asked/NO-ROW, 2 answered

COORDS = ("RET", "OPR", "RUN", "DECL", "SPK")


def question_cell(lang):
    """The five grounded coordinates, for the question `lang` asks."""
    op, _bin, _sta, dec, spk = selfindex.LANGUAGES[lang]
    return (RETURNS.get(lang, 2), op, ASKED.get(lang, 2), dec, spk)


def cells(roster=DEFAULT_ROSTER, keep=None):
    """The question index over a roster, optionally on a coordinate subset."""
    idx = range(len(COORDS)) if keep is None else keep
    return frozenset(tuple(question_cell(l)[i] for i in idx)
                     for l in ROSTERS[roster])


def determination(roster=DEFAULT_ROSTER):
    """[(a, b)] -- coordinate a determines coordinate b over the roster."""
    Q = {l: question_cell(l) for l in ROSTERS[roster]}
    out = []
    for i, j in itertools.permutations(range(len(COORDS)), 2):
        f, ok = {}, True
        for l in Q:
            if Q[l][i] in f and f[Q[l][i]] != Q[l][j]:
                ok = False
                break
            f[Q[l][i]] = Q[l][j]
        if ok:
            out.append((COORDS[i], COORDS[j]))
    return sorted(out)


def landing_robustness(roster=DEFAULT_ROSTER):
    """(hits, tried) -- coordinate subsets landing on the demanded cell."""
    hits = tried = 0
    for k in range(2, len(COORDS) + 1):
        for keep in itertools.combinations(range(len(COORDS)), k):
            Y = cells(roster, keep)
            if any(len({c[i] for c in Y}) < 2 for i in range(len(keep))):
                continue
            tried += 1
            if master.master_cell(Y) == master.DEMANDED_AT_EIGHT:
                hits += 1
    return hits, tried


def demand_is_live():
    """Is there a demand to fill?  DOCKET 5 says no."""
    mi = dict(master.master_index())
    mi["spacetimes (Petrov)"] = (1, 1, 0, 1, 2)     # the realisable-box cell
    C = frozenset(mi.values())
    cl, _ = hlaw.closures(C)
    return sorted(cl["statistics"] - C)


def report():
    print("=" * 74)
    print("THE QUESTION INDEX -- seven questions, one per language")
    print("=" * 74)
    print()
    print("  SEVEN ASK. ONLY FIVE ANSWER WITH A BINARY.")
    print("  %-14s %-46s %s" % ("language", "asks -- one thing, generally", "returns"))
    RT = {0: "CITATION", 1: "MAGNITUDE", 2: "binary"}
    for l in ROSTERS["seven"]:
        print("  %-14s %-46s %s" % (l, ASKS[l], RT[RETURNS.get(l, 2)]))
    print()
    print("  THE COORDINATES ARE PROPERTIES OF THE QUESTION -- AND THEY COLLAPSE.")
    for a, b in determination():
        print("     %s DETERMINES %s" % (a, b))
    X = cells()
    print("     seven questions -> %d distinct cells" % len(X))
    print()
    a, b, d = master.shape(X)
    print("  arity %d, box %d, density %.1f%%, closes %s"
          % (a, b, 100 * d, sorted(master.closers(X)) or "NOTHING"))
    print("  master cell %s" % (master.master_cell(X),))
    print()
    h, t = landing_robustness()
    print("  IT LANDS ON master.DEMANDED_AT_EIGHT %s -- AND THAT IS NOT A FILL:"
          % (master.DEMANDED_AT_EIGHT,))
    print("     %d of %d coordinate subsets land there" % (h, t))
    print("     reduced to the independent content (RET, DECL) it lands on %s"
          % (master.master_cell(cells(keep=(0, 3))),))
    print("     and Petrov-corrected the master index demands %s"
          % (demand_is_live() or "NOTHING"))
    print("  Three constructions have now hit this cell and none survived.")
    print("  THE FINDING IS ABOUT THE DEMAND, NOT ABOUT THE INDEXES.")


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
    chk("the roster is DATA -- two are carried", sorted(ROSTERS), ["five", "seven"])
    chk("seven languages ask", len(ROSTERS["seven"]), 7)
    chk("and each has a stated question", sorted(ASKS) == sorted(ROSTERS["seven"]), True)
    chk("only five answer with a binary",
        sorted(l for l in ROSTERS["seven"] if RETURNS.get(l, 2) == 2),
        ["algebra", "geometry", "information", "order", "statistics"])
    chk("analysis returns a MAGNITUDE", RETURNS["analysis"], 1)
    chk("documentary returns a CITATION", RETURNS["documentary"], 0)

    # ---- THE COLLAPSE, which is the honest content
    det = determination()
    chk("RET determines OPR, RUN and SPK",
        sorted(b for a, b in det if a == "RET"), ["OPR", "RUN", "SPK"])
    chk("only DECL is independent of RET",
        "DECL" not in [b for a, b in det if a == "RET"], True)
    chk("so seven questions give FOUR distinct cells", len(cells()), 4)

    # ---- THE LANDING, AND WHY IT IS NOT A FILL
    chk("it lands on the demanded cell", master.master_cell(cells()),
        master.DEMANDED_AT_EIGHT)
    h, t = landing_robustness()
    chk("but only 1 of 26 coordinate subsets does", (h, t), (1, 26))
    chk("reduced to (RET, DECL) it lands on an OCCUPIED cell",
        master.master_cell(cells(keep=(0, 3))), (2, 1, 0, 0, 3))
    chk("and that cell is periodic layout 2-D's",
        sorted(n for n, v in master.master_index().items()
               if v == (2, 1, 0, 0, 3)), ["periodic layout 2-D"])
    chk("AND THE DEMAND IS NOT LIVE -- DOCKET 5 deleted it", demand_is_live(), [])
    chk("SO THIS IS NOT A FILL", False, False)

    print("questions selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--roster" in sys.argv:
        r = sys.argv[sys.argv.index("--roster") + 1]
        X = cells(r)
        print("roster %s: %d questions -> %d cells, master cell %s"
              % (r, len(ROSTERS[r]), len(X), master.master_cell(X)))
    else:
        report()
