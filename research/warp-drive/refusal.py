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
    substances (Hawking-Ellis)   {0,2,7}
    the languages                {0,4,5,7}
    bounds                       {0,2,3,4,7}      <- lost K1 to DOCKET 4
    questions                    {0,2,4,5,7}      <- seated by DOCKET 8
    spacetimes (Petrov)          {0,3,4,5,7}
    energy-condition family      {0,2,3,4,5,7}
    periodic layout 3-D          {0,3,4,5,6,7}    <- lost K1 to DOCKET 2
    exotic mechanisms            {0,2,3,4,5,6,7}

    NINE, NOT TEN.  DOCKET 2 withdrew `periodic layout 2-D` as
    over-representation, and it was this section's most quoted row twice over:
    the poorest refusal index at {0,4} and the sole exception to K7.

    K0 AND K7 ARE BOTH UNIVERSAL.  Every seated index has cells that NOTHING
    refuses -- inside every one of the five closures -- and cells that
    EVERYTHING refuses.  Nine of nine both ways.

        K7'S UNIVERSALITY IS ONE COMMIT OLD, and it was bought rather than
        found.  The exception was `periodic layout 2-D`, the densest index in
        the corpus at 71.4 %: too full to have a cell every language refuses.
        Withdrawing the chart removed the counterexample instead of explaining
        it, so this is a fact about the seated nine and NOT a law about indexes.
        Section 3's dilution test is the reason to think it would have gone
        anyway -- dilute that chart and K7 appears -- but the test was run on
        the chart, not on the claim.

    K1 IS IN NOTHING, and section 4 is why it used to be two and then one.
    K6 IS IN TWO, and is now the rarest kind any index holds.

    THE LATTICE.  Minimal: Janet alone.  Maximal: exotic mechanisms alone --
    bounds was a maximum until DOCKET 4 took K1 off it, and periodic layout 3-D
    until DOCKET 2 did the same.  TEN of the thirty-six pairs are incomparable,
    so this is a lattice and not a chain -- the same shape the channel reading
    has, and for the same reason.

===============================================================================
2. THE MASTER INDEX INDEXES CHARTS, NOT OBJECTS
===============================================================================

This was not the question.  It is what the question turned up, and everything
after it is conditioned on it.

M asked whether the periodic table is OVER-REPRESENTED, being seated three
times: `periodic layout 2-D` at (period, group), `periodic layout 3-D` at
(period, group, block), and `Janet (n+l, l, k)`.  It is, and worse than that.

    RE-MEASURED ON THE COMPLETED CHARTS, AND THE FINDING SURVIVES INTACT.  This
    section originally ran on EIGHTY elements, because `populate.block_of`
    takes the differentiating electron from LW1-ground.py's OBSERVED
    configurations, which stop at Z = 108 -- so the three-coordinate layout
    could not chart 109..118 and the comparison was made on the eighty all
    three reached.  M called that the wrong index for 3-D and was right.  Taken
    from Madelung, which needs no observation, both charts reach NINETY-TWO
    positions, and on all ninety-two:

        (period, group)         INJECTIVE, 92 cells, one element each
        (period, group, block)  INJECTIVE, 92 cells, one element each
        (n+l, l)                NOT injective -- 92 elements onto 20 cells

    3-D projected onto (period, group) IS 2-D, cell for cell.  So Janet is a
    strict COARSENING, and 2-D and 3-D are in BIJECTION via the elements.
    `block` is a FUNCTION of `(period, group)` with ZERO exceptions on all
    ninety-two -- not one (period, group) pair carries two blocks: the
    three-coordinate layout is the two-coordinate layout PLUS A COORDINATE THAT
    CARRIES ZERO INFORMATION about which element is which.

        THE OLD FIGURES WERE MEASURED ON A TRUNCATED CHART AND STILL GAVE THE
        RIGHT ANSWER.  That is luck, not method, and it is recorded as such:
        the eighty-element comparison could not have detected a block that
        separates only among the twelve elements it could not see.  The
        ninety-two-element re-measurement is what the finding now rests on.

AND THAT ZERO-INFORMATION COORDINATE CHANGES THE CHANNEL.  Same ninety-two:

        (period, group)                        closes statistics  (1,1,0,0,3)
        + a MONOTONE redundant coordinate      closes statistics  (1,1,0,1,1)
        + the block, a NON-monotone one        closes NOTHING     (0,0,0,1,1)

    The three cells are unchanged from the eighty-element reading; only the
    order-reversal count moved, 356 -> 627, of 2,294 comparable ordered pairs.
    The block is order-reversing on 627 pairs.  So D and R move under ANY
    redundant coordinate, which is expected -- they are bands on arity and
    density, and neither is an invariant of anything.  C, Sc and Oc survive a
    MONOTONE redundant coordinate and DO NOT survive a non-monotone one.

    Across the nine, appending the monotone redundant coordinate moves the
    master cell of FIVE and changes the channel of NONE.

    **SO A MASTER CELL IS A PROPERTY OF THE CHART, NOT OF THE OBJECT.**  Nothing
    in the construction prevents one object from occupying several cells, and
    the periodic table occupies three, in three different channels.

AND THE DEMAND IS SATISFIABLE BY RE-CHARTING WHAT IS ALREADY SEATED.  Of 625
re-chartings of the nine -- one redundant coordinate appended, or one coordinate
dropped -- **twenty-eight land exactly on the demanded cell (1,1,0,2,1)**.  Three
are not tricks:

        bounds MINUS its G coordinate   8 cells, arity 5, box 108, density
                                        7.4 %, closes statistics -- THE
                                        WITHDRAWN FILL COMES BACK IF YOU DROP
                                        THE GRAVITY SLOT
        energy-condition family         lands there under FIVE different
                                        single-coordinate drops
        questions                       SEVEN of its own re-chartings land on
                                        the cell it already occupies -- and that
                                        is evidence AGAINST the seating being a
                                        fill, not for it.  A cell reachable
                                        seven ways from one small box is an easy
                                        cell; master.SIGNATURE_CONTROLS reads
                                        the same thing at 22.4 % against 0.02 %
                                        for bounds.

    Stated at its true strength: an arbitrary redundant coordinate is not a
    legitimate index, and the right answer to that is a CRITERION FOR A
    LEGITIMATE CHART.

        **AND THE CRITERION NOW EXISTS.**  This section read "this tree has
        never stated one" from the day it was written until DOCKET 3, and
        `charts.py` states it: a coordinate is admissible iff it is invariant
        under appending a MONOTONE redundant coordinate, which is well-posed
        because for monotone g, (x, g(x)) <= (y, g(y)) iff x <= y -- so such a
        coordinate cannot change the order and anything it moves was reading
        the chart rather than the object.  Measured against it, arity and
        density move on 9 of 9 and are DISQUALIFIED; height, width, cells,
        comparable pairs and join-irreducibles move on 0 of 9 and are admitted.
        That is why mi.py is charted on (K, height, width) and not on this
        file's five-coordinate cell.

    So "nothing in this corpus occupies the demanded cell" was true relative to
    the chart choices, and the demand was exactly as strong as the then-unstated
    criterion.  The criterion is now stated and two of the five coordinates fail
    it.  RECORDED, NOT REPAIRED -- this file keeps its own cells so the record
    of what was measured under them stays readable.

===============================================================================
3. K IS THE OBJECT.  W, H, J AND A ARE CHART DECORATION.
===============================================================================

duality.py's M2 profiles a pair as (K, W, H, J, A).  Put each truncation to the
same monotone redundant coordinate that moved five master cells:

        (K, W, H, J, A)   invariant in 4 of 9
        (K, W, J)         invariant in 7 of 9
        (K, W)            invariant in 7 of 9
        (K)               invariant in 9 of 9 -- NO EXCEPTION IN EITHER DIRECTION

**K IS NOT MERELY MONOTONE.  IT IS INVARIANT.**  This section previously read
"9 of 10, and the one exception only GROWS": the exception was `periodic layout
2-D`, whose {0,4} gained K7, and DOCKET 2 withdrew that chart as
over-representation.  Its exception went with it, and the claim strengthened
from "never loses a kind" to "never changes one".  H is a capped Hamming
distance and A is the host's arity band, so both are dimension-dependent by
construction and it is no surprise they move; what is worth having is that
dropping them is not enough, and only K survives.

    **AND THE (K,W,H,J,A) ROW IS NOT A MEASUREMENT.**  A is master's arity
    band, a function of dimension alone, and appending a coordinate changes
    dimension by construction -- so any index whose band crosses 4 -> 5 MUST
    differ, whatever it holds.  spacetimes (Petrov) and substances differ in
    that slot and no other: twelve gains and eleven losses for Petrov, pairing
    off one-for-one with A going 1 -> 2.  Two of the five non-invariant rows
    are that artefact.  Counted honestly the full profile survives in 4 of 9,
    and two of the five failures are the ruler moving, not the object.

**THE CAP LIED ONCE AND NOW IT REFUSES.**  These four rows were scanned under
`cap = CAP = 3000` until DOCKET 2 completed the periodic chart, which grew its
re-charted box to 4,608 cells.  itertools.product enumerates in a fixed order,
so the cap took a LEXICOGRAPHIC PREFIX, and appending a coordinate reorders the
product -- meaning the two capped scans covered different regions of different
boxes.  The unscanned 35 % came back as `periodic layout 3-D loses K5`, a
refutation of this section's own headline manufactured entirely by truncation.
Exact, it loses nothing.  `truncation_survival` is now exact by default and
`_uncapped()` raises rather than let a prefix pass as a sample.  The old ten
were never affected -- every box among them was under the cap, and the 2-D
exception reproduces exactly at cap=None.

    THE SAME LESSON TWICE.  The master index's cells are charts on indexes; the
    refusal profile's coordinates are a chart on the refusal set.  In both cases
    the invariant is the down-set of languages and everything else is bookkeeping
    about how it was written down.

UNDER A NON-MONOTONE re-charting K is not even monotone: the 2-D chart's
refusal profiles were NOT contained in the 3-D chart's, back when both were
seated.  So the invariance is conditional and the condition is stated -- and
`charts.py` now states the criterion that makes the condition checkable, which
this section could only ask for.

===============================================================================
4. THE THREAD, AND IT IS K1
===============================================================================

M: "each index likely shares the same refusal index as us, which means we can
draw threads that extend through multiple MIs."

THEY DO NOT ALL SHARE ONE.  TWO are universal -- K0 and K7 -- and neither
discriminates, which is the point.  What exists instead is better, because it
does: a K value present in FEW indexes is a thread between exactly those.

    **"ONLY K0 IS UNIVERSAL" IS SUPERSEDED.**  It held while periodic layout
    2-D was seated -- that chart was the one index with no cell all five
    languages refuse, at 71.4 % the densest in the corpus and too full to have
    one.  DOCKET 2 withdrew it as over-representation, and K7 became universal
    with it.  So every seated index now has BOTH a cell no language refuses and
    a cell every language refuses; the two extremes are free and only the
    middle carries information.

    **AND THE THREAD IS DEAD. BOTH ENDS WERE SEAMS.**  This section reported K1
    in TWO indexes -- the bounds index at (2,1,0,0,0,2) and (2,1,0,0,1,2), and
    the periodic layout in three coordinates at (4, 11, 0).  Neither survived.

        DOCKET 1 ruled the periodic K1 a CONVENTION SEAM: that index mixes the
        drawn layout's period and group with the observed differentiating
        electron's block, and neither pure convention produces a K1 cell.

        DOCKET 4 ruled the bounds K1 a CODING SEAM of the same shape: it existed
        only because Bekenstein was seated at G = 1, and bounds.py's own rule
        for that slot is "a G or an area appears" -- S <= 2 pi R E has neither,
        Bousso says so in print, and the black-hole saturation that motivated
        G = 1 is already carried by the K slot.  Re-code that one integer and
        the bounds index holds NO K1 cell.

    AND DOCKET 2 TOOK THE THIRD.  **THE CORPUS NOW HOLDS NO K1 CELL AT ALL.**
    Completing the three-coordinate layout destroyed (4,11,0) as a K1 cell: the
    cell is still in the box and still vacant, but its refusal set went from
    {information} to {information, statistics} -- K1 to K4.  Statistics stopped
    refusing to admit it.

        **AND THE CAUSE IS THE BLOCK CONVENTION, NOT THE REACH.**  This is worth
        stating exactly, because the two changed together and only one did the
        work.  Four builds, holding one variable at a time:

            reach 108, OBSERVED block    80 cells   K1 at (4,11,0)
            reach 108, MADELUNG block    80 cells   NO K1
            reach 120, OBSERVED block    80 cells   K1 at (4,11,0)
            reach 120, MADELUNG block    92 cells   NO K1

        The reach does nothing on its own -- `populate.block_of` returns None
        past Z = 108, so extending to 120 under the observed convention adds not
        one cell.  The convention does everything.  And the convention was NOT
        optional: reaching past 108 REQUIRES abandoning the observed block,
        because there is no observed differentiating electron to read.  So
        completing the chart FORCED the convention change, and the convention
        change killed K1.

        **THIS SECTION PREDICTED IT.**  Four paragraphs down, written before
        DOCKET 2 existed: recompute the layout with the block read off a
        convention other than the differentiating electron and "K1 VANISHES,
        becoming K4 {information, statistics}".  The measured value of (4,11,0)
        in the completed chart is K4, {information, statistics}, exactly.  The
        prediction was made for the DRAWN block and holds for the MADELUNG one
        too -- two different departures from the observed convention, the same
        destination.  WHICH CONVENTION THE CORPUS RULES FOR WAS RECORDED AS OPEN
        BELOW, AND DOCKET 2 CLOSED IT BY SIDE EFFECT rather than by ruling.
        That is recorded, not repaired: the ruling is still owed.

    SO THE WARP CELL'S OWN K1, measured from the device by statrow.py, now has
    NO instance anywhere in this corpus.  That is lonelier still than the
    one-companion statement this file was built on, and it changes what "the
    rarest refusal kind" means twice over: not rare among several, not unique
    with every companion withdrawn, but the only holder of a kind no seated
    index reaches.

    K6 still occurs in two: exotic mechanisms and periodic layout 3-D, and that
    one is untouched by any docket.  It is now the RAREST kind any seated index
    holds.  The periodic layout is still among the richest refusal structures
    here -- but at six of eight now, not seven, and exotic mechanisms at seven
    has passed it.

        (A first draft here added "and the only one missing K2".  That is
        FALSE -- four of the nine lack K2, spacetimes among them -- and it
        survived a paragraph only because an ad-hoc size filter in the pin was
        doing the work.  Its own selftest caught it.  Withdrawn.)

CAUTION, AND IT MATTERS.  `bounds` acquired K1 only when completing that family
stopped it closing, in the commit immediately before this file.  Before that K1
was in the periodic layout alone.  THE THREAD WAS ONE COMMIT OLD, and every
paragraph below it was written while it was still alive.  THEY ARE KEPT AS THE
RECORD OF A DEAD THREAD: the analysis they contain is what made the death
legible, and the four-build table above is only readable because the copper /
silver / palladium pass had already located exactly what the cell rested on.

AND THE OTHER END OF THE THREAD IS CONVENTION-DEPENDENT.  **THIS IS THE
PARAGRAPH DOCKET 2 CONFIRMED, AND IT WAS WRITTEN FIRST.**  A separate pass put
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

    IT IS STILL OPEN.  DOCKET 2 did not rule on it; it adopted the Madelung
    block because reaching past Z = 108 leaves no alternative, and inherited
    this paragraph's consequence without arguing for it.  A ruling is owed.

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

A SECOND CAUTION, NOW HALF WITHDRAWN.  This read: "the two minimal refusal sets
are Janet and periodic layout 2-D -- exactly the two charts section 2 finds
redundant", offered as a convergence of two independent measurements and not a
proof of either.  DOCKET 2 withdrew one of the two, so the convergence is gone
and only Janet is minimal.  What stands is the caution the paragraph carried:
the redundant charts were also the coarse ones, and coarse sets have fewer
refusal kinds for reasons that have nothing to do with being redundant.  Janet
alone at {0,7} is the coarsest chart here -- 92 elements onto 20 cells -- and
its minimality is fully explained by that.

===============================================================================
5. WHY IT IS NOT SEATED AS A MEMBER OF THE INVENTORY
===============================================================================

M asked for it seated "as an extension of the master index", and extension is
the right word rather than member.

R is computed FROM the inventory.  Seating it as a tenth member changes the
inventory, which changes R, which changes what was seated.  That is a fixed-point
problem and not a formality.  DOCKET 2 supplies the empirical case: withdrawing
ONE index moved K1 out of the corpus entirely, made K7 universal, and collapsed
the maximal set from two to one.  R is that sensitive to its own input.  This file therefore seats R as a FUNCTION ON THE
MEMBERS -- an added structure over the master index, addressable by name, with
its own lattice -- and does not add a row.  Whether the iteration converges is
open here and is the first thing to settle next.

    AND SECTION 2 WAS A SECOND REASON TO WAIT.  Seating anything new into a
    master index whose cells are charts rather than objects seats a chart, and
    the criterion for a legitimate chart was the prior question.  DOCKET 3
    answers it -- see charts.py -- so this reason has been discharged and the
    fixed-point reason above is the only one still standing.

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
import math
import sys

import hlaw
import master

CAP = 3000                      # cells scanned per index; duality.py's figure


# ---------------------------------------------------------------------------
# the refusal index
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# THE TWO KINDS, AND THEY MUST NOT SHARE AN IDENTIFIER
# ---------------------------------------------------------------------------
#
# M: "there are two variables sharing one identifier, and that requires
# correction and proper representation in M1."
#
# Correct.  Two different objects in this tree are both called K-something and
# both indexed through master.channel_sets():
#
#   A REFUSAL SET is COMPUTED.  {L : c not in cl_L(X)} for a cell c of an
#   index X's box.  It needs a host index, a box, and five closure operators.
#   Everything duality.py and this file measure is of this kind.
#
#   A VERDICT PATTERN is DECLARED.  The set of languages that return REFUSES
#   on a standalone binary question.  statrow.refusing_set() is three lines and
#   returns the literal frozenset({"information"}); no host, no box, no
#   closure is involved.  expand.py's TRANSITION-POSSIBLE is of this kind.
#
# Both index to a position in the same eight-element lattice, so both print as
# "K<n>", and the tree has been reading one as the other.  THEY ARE NOT THE
# SAME VARIABLE, and the measurement below is how far apart they are.

VERDICT_PATTERN = "declared"      # no host, no box; a pattern of verdicts
REFUSAL_SET = "computed"          # needs a host index and its box


def warp_verdict_vector():
    """The warp verdict as a tuple over the five closure languages, 1 ADMIT.

    expand.py holds it as five rows rather than a tuple; this is the same data
    in the shape a cell would have, so the two readings can be compared.
    """
    import expand
    del expand                     # imported to assert it is seated, not read
    return tuple(0 if L == "information" else 1 for L in hlaw.LANGS)


def the_two_readings():
    """(declared K, computed K, host) -- the same warp data, read both ways.

    THE DECLARED reading is statrow's literal, indexed into the lattice: K1.
    THE COMPUTED reading needs a box.  The language index is the ONLY seated
    box the verdict vector numerically fits -- five binary-ish coordinates --
    and placed there it computes to K5, not K1.

        PLACING IT THERE IS A CATEGORY ERROR AND THAT IS THE POINT.  The
        language index's coordinates are PROPERTIES OF A LANGUAGE (OP, BIN,
        STA, DEC, SPK), not verdicts on a question.  So K5 is not the right
        answer either.  What the pair of numbers shows is that the value
        depends entirely on the reading, which is why the two kinds may not
        share an identifier.
    """
    import selfindex
    import statrow
    ks = master.channel_sets()
    declared = ks.index(statrow.refusing_set())
    X = frozenset(selfindex.LANGUAGES.values())
    cl, box = hlaw.closures(X)
    v = warp_verdict_vector()
    if not all(v[i] in box[i] for i in range(len(v))):
        return declared, None, None
    computed = ks.index(frozenset(L for L in hlaw.LANGS if v not in cl[L]))
    return declared, computed, "the languages"


def boxsize(X):
    """How many cells a scan of X's box must visit."""
    return math.prod(len(b) for b in hlaw.closures(frozenset(X))[1])


def _uncapped(X, cap, what):
    """Refuse a capped scan rather than report its prefix as a measurement.

    A CAP IS NOT A SAMPLE.  itertools.product enumerates in a fixed order, so a
    truncated scan is the box's LEXICOGRAPHIC PREFIX, not a random one -- and
    appending a coordinate reorders the product, so two capped scans of X and
    of recharted(X) cover different regions.  Comparing them is not a weak
    measurement, it is not a measurement.  This function makes that loud.

    IT EXISTS BECAUSE THE CAP ALREADY LIED ONCE.  Completing the periodic chart
    under DOCKET 2 grew its recharted box from under the cap to 4,608 cells
    against CAP = 3,000, and section 3's scan silently reported the unscanned
    35 % as periodic layout 3-D LOSING K5 -- a refutation of the section's own
    headline, manufactured entirely by the truncation.  Exact, it loses nothing.
    """
    if cap is None:
        return
    n = boxsize(X)
    if n > cap:
        raise ValueError(
            "%s: box is %d cells against a cap of %d. A capped scan is a "
            "lexicographic prefix, not a sample; pass cap=None for an exact "
            "scan rather than accept a truncated one." % (what, n, cap))


def refusal_set(X, cap=CAP):
    """R(X) -- which of the eight lawful refusal kinds occur in X's box."""
    X = frozenset(X)
    _uncapped(X, cap, "refusal_set")
    ks = master.channel_sets()
    cl, box = hlaw.closures(X)
    return frozenset(
        ks.index(frozenset(L for L in hlaw.LANGS if c not in cl[L]))
        for c in itertools.islice(itertools.product(*box), cap))


def refusal_index(inv=None, cap=CAP):
    """{index name: R(X)} over the seated inventory."""
    inv = master.inventory() if inv is None else inv
    return {nm: refusal_set(inv[nm], cap) for nm in inv}


def block_convention_table():
    """[(reach, convention, cells, [K1 cells])] -- what killed the last K1.

    DOCKET 2 completed the three-coordinate layout and the corpus's last K1
    cell died with it.  Two things changed at once -- the reach (108 -> 120) and
    the block convention (the OBSERVED differentiating electron, from
    LW1-ground.py, -> the MADELUNG one) -- so this holds each fixed in turn.

    THE CONVENTION DOES ALL THE WORK.  `populate.block_of` returns None past
    Z = 108, so extending the reach under the observed convention adds not one
    cell; switching the convention at the OLD reach kills K1 by itself.  And the
    convention was not optional: past 108 there is no observed differentiating
    electron to read, so completing the chart forced it.  Section 4 predicted
    the result for a THIRD convention (the drawn block) before DOCKET 2 existed.
    """
    pop = master._populate()

    def madelung(Z):
        now = {(n, l): o for n, l, o in pop.aufbau_config(Z)}
        prev = ({(n, l): o for n, l, o in pop.aufbau_config(Z - 1)}
                if Z > 1 else {})
        g = sorted((n, l) for (n, l), o in now.items() if o > prev.get((n, l), 0))
        return g[-1][1] if g else None

    def build(reach, fn):
        out = set()
        for Z in range(1, reach + 1):
            if pop.set_aside(Z):
                continue
            g = pop.group_of(Z)
            if g is None:
                continue
            b = fn(Z)
            if b is None:
                continue
            out.add((pop.period_of(Z), g, b))
        return frozenset(out)

    ks = master.channel_sets()
    rows = []
    for reach, name, fn in ((108, "observed", pop.block_of),
                            (108, "madelung", madelung),
                            (120, "observed", pop.block_of),
                            (120, "madelung", madelung)):
        X = build(reach, fn)
        cl, box = hlaw.closures(X)
        k1 = [c for c in itertools.product(*box)
              if ks.index(frozenset(L for L in hlaw.LANGS
                                    if c not in cl[L])) == 1]
        rows.append((reach, name, len(X), sorted(k1)))
    return rows


def occurrence(R=None):
    """{K: [index names carrying it]} -- the census the threads come from."""
    R = refusal_index() if R is None else R
    return {k: sorted(nm for nm, s in R.items() if k in s) for k in range(8)}


def universal(R=None):
    """The refusal kinds EVERY seated index carries."""
    R = refusal_index() if R is None else R
    return frozenset.intersection(*R.values())


def lattice(R=None):
    """(minimal, maximal, incomparable pairs) of the seated refusal sets."""
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


def truncation_survival(keep, inv=None, cap=None):
    """(invariant count, total, [(name, gained, lost)]) for that truncation.

    EXACT BY DEFAULT, and the default is the repair.  This took cap=CAP until
    the periodic chart was completed, at which point the recharted box passed
    the cap and the truncation reported itself as a lost refusal kind.  See
    _uncapped().  The largest scan here is 4,608 cells and costs seconds.
    """
    inv = master.inventory() if inv is None else inv
    rows, n = [], 0
    for nm in sorted(inv):
        _uncapped(inv[nm], cap, nm)
        _uncapped(recharted(inv[nm]), cap, nm + " re-charted")
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
    print("1. THE %d SEATED, MEASURED.  R(X) = which refusal kinds occur in its box."
          % len(R))
    for nm in sorted(R, key=lambda n: (len(R[n]), n)):
        print("   %-28s %s" % (nm, "{" + ",".join(map(str, sorted(R[nm]))) + "}"))
    print()
    occ = occurrence(R)
    print("   K   set                                        in  carried by")
    for k in range(8):
        who = occ[k]
        tag = ", ".join(who) if len(who) <= 2 else ""
        print("   K%d  %-42s %d/%d %s"
              % (k, "{" + ", ".join(sorted(ks[k])) + "}", len(who), len(R), tag))
    print("   UNIVERSAL: %s -- every index has cells NOTHING refuses AND"
          % sorted(universal(R)))
    print("   cells EVERYTHING refuses. K7 joined when DOCKET 2 withdrew the")
    print("   2-D chart, the one index too dense to have such a cell.")
    print()
    mins, maxs, inc = lattice(R)
    print("   minimal %s" % mins)
    print("   maximal %s" % maxs)
    print("   incomparable pairs: %d of %d -- a lattice, not a chain"
          % (len(inc), len(R) * (len(R) - 1) // 2))
    print()

    print("2. THE MASTER INDEX INDEXES CHARTS, NOT OBJECTS.")
    moved, chg, tot = cell_survival()
    print("   Append a coordinate that is a FUNCTION of the existing ones --")
    print("   zero information about which member is which. Over the %d:" % len(R))
    print("     master cells moved   %d of %d" % (moved, tot))
    print("     channels changed     %d of %d" % (chg, tot))
    print("   So D and R are chart properties. C, Sc, Oc survive a MONOTONE")
    print("   redundant coordinate -- and the periodic table's block, which is")
    print("   a function of (period, group) and order-reversing on 627 pairs,")
    print("   takes that index from closing in statistics to closing in nothing.")
    print()
    hits, tried = rechartings_hitting()
    print("   AND THE DEMAND %s IS SATISFIABLE BY RE-CHARTING:"
          % (master.DEMANDED_AT_EIGHT,))
    print("   %d of %d re-chartings of the SEATED %d land on it."
          % (len(hits), tried, len(R)))
    print("   SEVEN of them are the QUESTION index re-charted -- the index that")
    print("   OCCUPIES this cell can be re-charted seven ways and still land on")
    print("   it. Read that as the cell being easy, not the seating being right.")
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
        elif keep == ("K",):
            extra = "   -- NO EXCEPTION, either direction"
        print("   %-18s invariant in %d of %d%s"
              % ("(" + ",".join(keep) + ")", n, tot, extra))
    print("   K does not merely fail to LOSE a kind -- it does not CHANGE one.")
    print("   Its one exception was the 2-D chart DOCKET 2 withdrew. Under a")
    print("   non-monotone re-charting it is not even monotone.")
    print("   THESE ARE EXACT SCANS. Under the old cap=3000 the last row read")
    print("   8 of 9 with the 3-D chart LOSING K5 -- which was the unscanned")
    print("   35%% of a 4,608-cell box and nothing else. See _uncapped().")
    print("   AND THE FIRST ROW IS PART ARTEFACT: A is a band on arity and")
    print("   re-charting changes arity, so Petrov and substances MUST differ.")
    print()
    print("3b. WHAT KILLED THE LAST K1 -- the reach or the block convention?")
    for reach, name, cells, k1 in block_convention_table():
        print("     reach %-4d %-9s %3d cells   K1: %s"
              % (reach, name, cells, k1 if k1 else "none"))
    print("   THE CONVENTION, ALONE. block_of is None past Z=108, so the reach")
    print("   adds nothing on its own; switching convention at the OLD reach")
    print("   kills K1 by itself. And past 108 there is no observed")
    print("   differentiating electron, so completing the chart FORCED it.")
    print("   Section 4 predicted this for a THIRD convention before DOCKET 2")
    print("   existed: (4,11,0) survives, vacant, at K4 {information,")
    print("   statistics} -- exactly the destination it named.")
    print()

    print("4. THE THREAD, AND IT IS DEAD -- K1 IS CARRIED BY NOTHING.")
    for k, who in sorted(threads(R).items()):
        print("   K%d carried by exactly %d: %s" % (k, len(who), ", ".join(who)))
    print("   K0 and K7 are BOTH universal, so 'every index shares one")
    print("   refusal index' is FALSE for a different reason than before:")
    print("   two are shared by all nine and neither discriminates. What is")
    print("   sharper: a rare kind is a thread between exactly the indexes")
    print("   carrying it. K1 -- the warp obstruction's kind -- is now carried")
    print("   by NOTHING: completing the periodic chart destroyed the last cell")
    print("   holding it. K6 at two indexes is the rarest kind still held.")
    print()
    d, c, host = the_two_readings()
    print("4b. TWO VARIABLES, ONE IDENTIFIER -- and this is a defect, not a find.")
    print("   A REFUSAL SET is COMPUTED: {L : c not in cl_L(X)}, needs a host,")
    print("   a box and five operators. A VERDICT PATTERN is DECLARED:")
    print("   statrow.refusing_set() is three lines returning a literal.")
    print("   Both index into the same eight-element lattice, so both print")
    print("   as K<n>, and this tree has been reading one as the other.")
    print("     the warp data DECLARED   -> K%s" % d)
    print("     the same data COMPUTED   -> K%s   (in %s, the only seated box"
          % (c, host))
    print("        it numerically fits -- and placing it there is a CATEGORY")
    print("        ERROR, since those coordinates are properties of a language")
    print("        and not verdicts. So K%s is not the right answer either.)" % c)
    print("   THE VALUE DEPENDS ENTIRELY ON THE READING. That is why the two")
    print("   kinds may not share an identifier, and why the warp cell has NO")
    print("   master cell: no host, no box, no cell. Its absence from M1 is the")
    print("   correct representation, not an omission to be filled.")
    print()
    print("5. NOT SEATED AS A MEMBER. R is computed FROM the inventory, so")
    print("   seating it changes it -- a fixed point, not a formality, and")
    print("   DOCKET 2 shows how sharp: withdrawing ONE index took K1 out of")
    print("   the corpus, made K7 universal and halved the maximal set.")
    print("   The second reason -- that a master index whose cells are charts")
    print("   seats a chart -- is DISCHARGED: DOCKET 3 states the criterion")
    print("   (charts.py). The fixed point is the only one still open.")


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
    # NINE. DOCKET 2 withdrew periodic layout 2-D as over-representation, and
    # it was this file's poorest refusal index -- {0,4} -- and the one exception
    # to K7. Both of those pins go with it.
    chk("nine seated indexes carry a refusal index", len(R), 9)
    # DOCKET 8 seated the question index. Its refusal index is measured here
    # like any other -- R(X) is computed from X, never declared.
    chk("questions", sorted(R["questions"]), [0, 2, 4, 5, 7])
    # AND IT LOST K1 WHEN IT WAS COMPLETED. This index carried the corpus's
    # only K1 refusal; rebuilding it from Madelung to its whole period destroyed
    # the cell, and no index carries K1 now. exotic mechanisms is the richest.
    chk("periodic layout 3-D lost K1 when it was completed",
        sorted(R["periodic layout 3-D"]), [0, 3, 4, 5, 6, 7])
    chk("exotic mechanisms is now the richest",
        sorted(R["exotic mechanisms"]), [0, 2, 3, 4, 5, 6, 7])
    chk("and K1 is carried by NOTHING", [n for n in R if 1 in R[n]], [])
    chk("Janet is now the poorest", sorted(R["Janet (n+l, l, k)"]), [0, 7])
    # DOCKET 4: bounds LOST K1 when Bekenstein was re-coded G 1 -> 0.
    chk("bounds", sorted(R["bounds"]), [0, 2, 3, 4, 7])
    chk("the languages", sorted(R["the languages"]), [0, 4, 5, 7])

    # ---- K0 AND K7 BOTH UNIVERSAL NOW
    # This pin read [0] for as long as periodic layout 2-D was seated: it was
    # the one index with no cell all five languages refuse. Withdrawing it
    # under DOCKET 2 made K7 universal too, so the intersection is {0, 7} and
    # section 4's "only K0 is universal" is superseded. Both are exact: every
    # seated box is under CAP, so refusal_set() truncates nothing.
    chk("K0 AND K7 are both universal now", sorted(universal(R)), [0, 7])
    occ = occurrence(R)
    # K7 IS NOW UNIVERSAL. Its one exception was periodic layout 2-D, the
    # densest index in the corpus at 71.4 %: too full to have a cell every
    # language refuses. Withdrawn, and the exception with it.
    chk("K7 is in ALL NINE now -- its one exception was the withdrawn chart",
        len(occ[7]), 9)
    chk("no index lacks it", [nm for nm in R if 7 not in R[nm]], [])
    chk("and the densest index is now substances, which HAS K7",
        (max(R, key=lambda n: master.shape(master.inventory()[n])[2]),
         7 in R["substances (Hawking-Ellis)"]),
        ("substances (Hawking-Ellis)", True))

    # ---- the lattice
    mins, maxs, inc = lattice(R)
    chk("minimal: Janet alone, now that the 2-D chart is withdrawn", mins,
        ["Janet (n+l, l, k)"])
    chk("maximal: exotic mechanisms alone, since 3-D lost K1", maxs,
        ["exotic mechanisms"])
    chk("ten of thirty-six pairs incomparable -- still a lattice",
        len(inc), 10)

    # ---- THE THREAD
    # THE THREAD IS DEAD. DOCKET 4 took bounds off K1, so the corpus holds ONE
    # K1 cell -- and DOCKET 1 already ruled that one a convention seam.
    # THE THREAD IS NOT MERELY DEAD, ITS SUBJECT IS GONE. K1 was carried by one
    # index and completing that index destroyed the cell.
    chk("K1 IS CARRIED BY NOTHING AT ALL", occ[1], [])
    chk("K6 is carried by exactly two, and is now the RAREST kind held", occ[6],
        ["exotic mechanisms", "periodic layout 3-D"])
    chk("periodic layout 3-D no longer carries both rare kinds -- only K6",
        ({1, 6} <= R["periodic layout 3-D"], 6 in R["periodic layout 3-D"]),
        (False, True))
    # WITHDRAWN BY ITS OWN PIN. This first read "and it is the only index
    # missing K2", with an ad-hoc size filter to exclude the small sets. It is
    # false: FIVE of the nine lack K2, spacetimes (Petrov) among them, and the
    # filter was doing the work rather than the fact. The census is what stands.
    chk("K2 is carried by five, and four lack it",
        (len(occ[2]), sorted(nm for nm in R if 2 not in R[nm])),
        (5, ["Janet (n+l, l, k)", "periodic layout 3-D",
             "spacetimes (Petrov)", "the languages"]))
    # NEGATIVE CONTROL: the conjecture as stated is FALSE and the pin says so.
    # AND IT SURVIVED THE TENTH SEATING: ten indexes, ten distinct refusal
    # indexes. No two have ever coincided.
    chk("THE NINE DO NOT SHARE ONE REFUSAL INDEX",
        len(set(map(frozenset, R.values()))), 9)

    # ---- DOCKET 2: what actually killed the last K1 cell
    tbl = block_convention_table()
    chk("the reach alone changes NOTHING -- block_of is None past 108",
        [(r, n, c) for r, n, c, _k in tbl if n == "observed"],
        [(108, "observed", 80), (120, "observed", 80)])
    chk("and both observed builds keep the K1 cell",
        [k for _r, n, _c, k in tbl if n == "observed"],
        [[(4, 11, 0)], [(4, 11, 0)]])
    chk("the CONVENTION alone kills it, at the OLD reach",
        [(r, n, c, k) for r, n, c, k in tbl if (r, n) == (108, "madelung")],
        [(108, "madelung", 80, [])])
    chk("and the completed chart is 92 cells with no K1",
        [(r, n, c, k) for r, n, c, k in tbl if (r, n) == (120, "madelung")],
        [(120, "madelung", 92, [])])
    # SECTION 4 PREDICTED THE DESTINATION. The cell survives in the box and is
    # still vacant; only its refusal moved, to exactly the K4 the section named.
    X3 = master.inventory()["periodic layout 3-D"]
    _cl, _box = hlaw.closures(frozenset(X3))
    chk("(4,11,0) is still a vacant cell of the completed box",
        ((4, 11, 0) in X3, all((4, 11, 0)[i] in _box[i] for i in range(3))),
        (False, True))
    chk("and it is now K4 {information, statistics}, as section 4 predicted",
        sorted(L for L in hlaw.LANGS if (4, 11, 0) not in _cl[L]),
        ["information", "statistics"])

    # ---- section 2, the chart finding
    moved, chg, tot = cell_survival()
    chk("a zero-information coordinate moves five master cells", moved, 5)
    chk("and changes NO channel -- C survives a monotone re-charting", chg, 0)

    hits, tried = rechartings_hitting()
    chk("re-chartings tried", tried, 625)
    chk("re-chartings landing on the demanded cell", len(hits), 28)
    # AND SEVEN OF THE TWENTY-EIGHT ARE THE QUESTION INDEX'S OWN RE-CHARTINGS.
    # That is not extra evidence for the seating -- it is the opposite. The
    # index seated at the demanded cell can be re-charted seven ways and still
    # land there, which says the cell is easy to reach from that box, exactly
    # as master.SIGNATURE_CONTROLS["questions"] reads it at 22.4 %.
    chk("seven of them are the question index re-charted",
        sorted(b for a, b, _c, _s, _k in hits if a == "questions"),
        ["dif01", "dif02", "dif12", "max13", "xor01", "xor02", "xor12"])
    chk("and one is bounds MINUS its gravity slot",
        ("bounds", "drop3") in [(a, b) for a, b, _c, _s, _k in hits], True)
    chk("the energy-condition family lands there five ways",
        sum(1 for a, b, _c, _s, _k in hits
            if a == "energy-condition family"), 5)

    # ---- section 3, K is the object
    # EXACT SCANS. Measured with cap=None -- see _uncapped(). Under the old
    # cap=CAP the last row read 8 of 9 with periodic layout 3-D LOSING K5,
    # which was the unscanned 35 % of a 4,608-cell box and nothing else.
    for keep, want in ((("K", "W", "H", "J", "A"), 4), (("K", "W", "J"), 7),
                       (("K", "W"), 7), (("K",), 9)):
        n, tot, rows = truncation_survival(keep)
        chk("(%s) invariant in %d of 9" % (",".join(keep), want), (n, tot),
            (want, 9))
    # K IS NOT MERELY MONOTONE, IT IS INVARIANT. No index gains a refusal kind
    # and none loses one. This is STRONGER than what this section claimed for
    # the ten, where periodic layout 2-D gained K7; withdrawing that chart took
    # the only exception with it.
    n, _t, rows = truncation_survival(("K",))
    chk("K HAS NO EXCEPTION AT ALL NOW", [(nm, g, l) for nm, g, l in rows], [])
    # AND THE CAP GUARD REFUSES RATHER THAN TRUNCATES.
    try:
        truncation_survival(("K",), cap=100)
        chk("a capped scan is refused, not reported", "no refusal", "refused")
    except ValueError:
        chk("a capped scan is refused, not reported", "refused", "refused")
    # A IS NOT A MEASUREMENT UNDER THIS TEST. master's arity band is a function
    # of dimension and re-charting changes dimension by construction, so every
    # index whose arity band crosses 4 -> 5 must move. Petrov and substances
    # differ ONLY in that slot: their gains and losses pair off one-for-one
    # with A going 1 -> 2. The (K,W,H,J,A) row is that artefact, not a finding.
    _n, _t, full = truncation_survival(("K", "W", "H", "J", "A"))
    petrov = [r for r in full if r[0] == "spacetimes (Petrov)"][0]
    chk("Petrov's whole difference is the arity slot moving 1 -> 2",
        (sorted({g[-1] for g in petrov[1]}), sorted({l[-1] for l in petrov[2]})),
        ([2], [1]))

    print("refusal selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    report()
