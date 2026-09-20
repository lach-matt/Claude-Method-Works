#!/usr/bin/env python3
r"""
overlaprule.py -- WHEN AN OVERLAPPING CHART MAY BE SEATED, AND WHEN IT IS ONE
PIECE OF INFORMATION SEATED TWICE.

M: "They can be seated with overlaps so long as it is not an overlap of same
information. An overlap of values in two different languages should tell us two
parts of definition contained in that overlapped position. Information is
information. But its relative position in this index is information about an
object."

    python3 overlaprule.py             the reading
    python3 overlaprule.py --census    re-derive the candidates from all 283
                                       sub-charts rather than checking the
                                       pinned six (about a minute)
    python3 overlaprule.py --selftest  fixtures

===============================================================================
0. WHAT THE RULING CHANGES, AND WHAT IT LEAVES EXACTLY WHERE IT WAS
===============================================================================

`overlap.py` held that two charts of one body of data must not both be seated,
because seating the same information twice moves |J(F)| and |box| in opposite
and wrong directions and every later verdict is re-labelled by it.  THAT
CONCERN IS NOT WITHDRAWN AND THIS FILE DOES NOT WITHDRAW IT.  What the ruling
withdraws is the identification of *overlap* with *same information*.  Overlap
is the premise; sameness is a separate question, and it has an answer that can
be measured.

    THE PROHIBITION NARROWS; IT DOES NOT LAPSE.  A reading of the ruling that
    admits a hundred coarsenings of one parent is not a reading of it -- M
    holds in the same breath that over-representation must be avoided at all
    costs.  Section 1 is the measurement that picks the reading, and it picks
    it by arithmetic rather than by preference.

===============================================================================
1. THE READING IS `NOVEL CHANNEL`, AND THAT IS A MEASUREMENT
===============================================================================

Six readings of "not an overlap of same information" were charted against all
272 proper sub-charts of the eleven seated indexes:

    R1  channel differs from its own parent                    109 admitted
    R2  cell    differs from its own parent                    254
    R3  cell    occupied by NO seated vertex                   252
    R4  CHANNEL occupied by NO seated vertex                     6
    R3 and not a relabelling                                   237
    R4 and not a relabelling                                     6

    R3 ADMITS 252, OF WHICH 117 ARE COARSENINGS OF `gravity` ALONE.  That is
    the explosion overlap.py exists to prevent, arrived at through the front
    door.  R4 admits six.

AND R4 IS WHAT M'S WORDS SAY.  The ruling names LANGUAGES -- "an overlap of
values in two different languages" -- not heights and widths.  The channel is
the set of languages that close the chart; the height and the width are the
Mirsky and Dilworth numbers of its cell poset.  Two charts at different heights
in one channel differ in size, not in language.  So the position that is
"information about an object" is the CHANNEL, and the arithmetic and the text
agree, which is the only reason to believe either.

===============================================================================
2. THE OTHER TWO GROUNDS ARE DOCKET 2'S, ALREADY RULED
===============================================================================

DOCKET 2 withdrew `periodic layout 2-D` and it did NOT do so on bare overlap.
It gave four grounds, and two of them survive the new ruling untouched, because
they are about sameness rather than about overlap:

    BIJECTION.  "Extended to the same reach the two are in exact bijection, and
    `block` is a function of (period, group) with ZERO collisions -- no
    information about which element is which."  A chart with as many cells as
    its parent separates exactly as much: it is the parent relabelled, and a
    relabelling is the same information by any reading.

    THE CHANNEL MOVED.  "At ninety cells it closed in {information,
    statistics}; extended to its own construction's reach it closes in
    {statistics} alone."  A channel that depends on where the construction
    stopped is a fact about the stopping point.

    THE SECOND IS THE ONE WITH TEETH.  All six candidates clear the bijection
    ground -- none is a relabelling -- and three of the six fail the reach
    gate.

===============================================================================
3. THE REACH GATE, IN THE SHAPE OF THE TWO FAILURES THIS TREE HAS SEEN
===============================================================================

DOCKET 2's channel moved as the chart was extended.  `terms.py`'s gate fired on
a cell count that was NON-MONOTONE across tolerances.  Those are the two
failure shapes and these are them as conditions, swept over the construction's
own data reach:

    (a) NO LATE ARRIVAL   the channel holds at more than one reach, and does
                          not first appear at the final one
    (b) NO OSCILLATION    once reached, it holds at every later reach
    (c) MAJORITY          it holds at more than half the swept reaches

    THE SWEEP IS OVER THE DATA, NOT OVER A VARIABLE.  gravity.py: "D NOT
    MEASURED.  It is the index's independent variable."  Restricting D asks a
    different physical question; it does not capture less of the same data.  D
    is swept in section 5 and reported as a finding, and it is a better finding
    than the gate it is not part of.

    THE STRONGEST OBJECTION TO THIS GATE, AND WHY IT DOES NOT LAND.  For
    `ions` the sweep runs to Z <= 108, which is the whole of LW1-ground.py's
    table -- so the intermediate reaches look like truncations this file
    imposed, and the terminal one looks like the complete object whose verdict
    should simply be believed.  If that were right, "K4 only at the terminal
    reach" would be no fault at all.

        IT IS NOT RIGHT, AND M RULED WHY.  mi.py section 3 quotes him: "until
        we can prove that no more elements are left to discover or synthesize,
        the upper bound of the periodic table is open."  SO Z <= 108 IS NOT A
        COMPLETE OBJECT.  It is where the data stops, and a chart whose channel
        first appears at the last element anyone has made is a chart one new
        element can move again.  That is precisely the risk the gate exists to
        price, and DOCKET 2's 2-D chart is the case where it was paid.

        THE OTHER FIVE ARE UNAFFECTED BY THE SAME ARGUMENT, and checking that
        rather than assuming it turned up a distinction worth keeping.  Take
        "holds its channel at its widest TWO reaches" as the open-upper-bound
        test -- a verdict already confirmed by one more element's worth of data
        is not a verdict the next element invents.  All three SEATED charts
        pass it.  Of the refused, ONLY `ions` fails it: K4 appears at Z <= 108
        and at nothing before.  `madrule` holds K4 at both Z <= 103 and
        Z <= 108 and PASSES this test -- it is refused on the majority
        condition alone, 2 of 7, with its other five reaches holding 1, 2, 3, 4
        and 5 cells, sizes at which every language closes for free.

        SO THE TWO K4 REFUSALS ARE NOT THE SAME REFUSAL, and the file should
        not pretend they are.  `ions` is the DOCKET 2 shape.  `madrule` is a
        chart too small to have said anything yet, whose 20 exceptions saturate
        at Z = 103 and which a few new elements could move either way.  Of
        everything refused here, madrule is the one most likely to come back.

    AN EARLIER FORM OF THIS GATE CALLED A REACH DEGENERATE WHEN SOME COORDINATE
    HAD NOT YET TAKEN EVERY VALUE IT TAKES AT FULL REACH.  It is recorded here
    because it is wrong and the way it is wrong is instructive: for a chart
    whose alphabet GROWS with reach -- madelung's `n+l` does, necessarily --
    every proper prefix is degenerate and the gate has one live reach and no
    evidence.  It marked madelung's nine consecutive K6 reaches as no evidence
    at all.  The three conditions above do not depend on alphabet completeness
    and do not have that defect.

===============================================================================
3b. MAXIMALITY, AND WHY THE ORDER OF THE TWO TESTS IS LOAD-BEARING
===============================================================================

An independent pass over the same 272 sub-charts (one agent of a verification
run; the other sixteen died on a quota before reporting -- section 7)
reproduced section 1's counts exactly -- R1 109, R2 254, R3 252, R4 6 -- and
added a clause this file had missed:

    IF A SUPER-CHART OF S INSIDE THE SAME PARENT REACHES THE SAME CHANNEL, S
    REPEATS ITS LANGUAGE SET AND CARRIES NOTHING IT DOES NOT.  Same languages,
    same parent, same members: that is same information by M's own words, and
    the smaller chart is the one to drop.

    gravity (B,F,X) AND gravity (B,F,X,E) ARE EXACTLY THAT PAIR.  Both K1.  So
    maximality says keep the arity-4 one.

    AND THE REACH GATE SAID THE ARITY-4 ONE WAS NOT SOUND -- it oscillated, K1
    then K0 then K1 across the Z sweep.  THAT IS NO LONGER WHAT THE SWEEP
    MEASURES, and section 3f is the measurement that moved it: DOCKET 49b
    widened gravity's capture reader (member rows 3,394 -> 3,663, species
    118 -> 126) and the Z <= 40 reach went 48 cells at K0 to 50 cells at K1.
    All six reaches now read K1, the oscillation ground does not fire, and
    (B,F,X,E) is SOUND.

        WITHDRAWN, and the withdrawal is the point of keeping it: "SO THE ORDER
        DECIDES THE ANSWER.  Maximality first picks (B,F,X,E), the gate then
        kills it, and K1 ENDS UP EMPTY -- the seating list is K6 alone.  Gate
        first kills (B,F,X,E), leaving (B,F,X) the only surviving K1 chart of
        that parent -- maximal among what survived -- and the list is K1 and
        K6."  MEASURED, both orders now return [1, 5, 6]; `order_matters()` is
        re-pinned to that pair of identical lists.  THE PRINCIPLE BELOW IS NOT
        WITHDRAWN -- only this pair's demonstration that the order changes the
        answer, which was the only demonstration the file had.

    THE GATE RUNS FIRST, AND NOT BECAUSE IT GIVES THE FULLER ANSWER.  The gate
    asks whether a channel verdict is a fact about the object; maximality asks
    which of two facts to keep.  A chart that fails the gate has no channel
    verdict to be maximal about.  Soundness before redundancy -- otherwise the
    redundancy test is choosing between one real reading and one artefact.

    THE CLAUSE WAS INERT AND IS NOT ANY MORE.  WITHDRAWN: "HERE THE CLAUSE IS
    INERT.  The rows that pass the gate have different parents, so none
    contains another."  TWO gravity charts now pass the gate, one contains the
    other, and maximality is what decides between them -- it refuses (B,F,X)
    and admits (B,F,X,E).  The sentence was true when written and it was true
    BY MEASUREMENT, which is exactly why it could stop being true; "inert by
    measurement and not by construction" was the right warning and it was not
    heeded for long.

3f. THE OSCILLATION REFUSAL LAPSED, AND A SAMPLE IS NOT THE REACH
===============================================================================

WHAT MOVED, AND IT WAS NOT THIS FILE.  `gravity.py` DOCKET 49b widened its
capture reader: 39 level tables spelled `Level_cm-1` where the reader demanded
`level_cm1` had been invisible, and admitting them took the index from 3,394
member rows over 118 species to 3,663 over 126.  THAT COMMIT MEASURED ITS OWN
BLAST RADIUS AND REPORTED IT AS ZERO -- cells 914 -> 914, cell (0,19,112)
unchanged, channel K0 -> K0, E 1,550 -> 1,550.  Every one of those is a
measurement of the PARENT CHART AT FULL REACH, and this gate does not read the
parent chart at full reach; it reads TRUNCATED sub-charts.  There the blast
radius was not zero:

    (B,F,X,E) at Z <= 40         before  48 cells K0     after  50 cells K1
    (B,F,X,E) over six reaches   before  K1 K0 K1 K1 K1 K1
                                 after   K1 K1 K1 K1 K1 K1
    (B,F,X)   over six reaches   before  K1 K1 K1 K1 K1 K1
                                 after   K1 K1 K1 K1 K1 K1    -- unmoved

MEASURED, NOT INFERRED.  The "before" column is `gravity.py` at commit 7d99aad
read in a detached worktree; the "after" is HEAD.  So the oscillation ground
stops firing, (B,F,X,E) clears all four grounds, and maximality -- the clause
3b called inert -- refuses (B,F,X) and admits (B,F,X,E) in its place.

THE OSCILLATION DID NOT GO AWAY.  IT MOVED BELOW A SAMPLE POINT.  Swept at
every reach the index actually holds a member at, INSIDE THE SPAN `SWEEPS`
already declares (Z = 20 .. 118, 39 such reaches) -- `dense_off_channel()`:

    gravity (B,F,X)     0 of 39 off-channel
    gravity (B,F,X,E)   2 of 39 off-channel, at Z <= 35 and Z <= 36

Before DOCKET 49b the dip covered Z <= 40 and the sample caught it; after, the
dip is 35..36 and the six declared points step over it.  THE GATE'S VERDICT
CHANGED AND THE CHART DID NOT.  A channel verdict that eight new species move
is the thing this gate exists to price, and the instrument lost sight of it.

AND THE OBVIOUS REPAIR IS REFUSED, BECAUSE IT WAS MEASURED FIRST.  Evaluating
the oscillation condition densely, for every candidate, inside each parent's
own declared span -- `dense_off_channel()` again:

    gravity  (B,F,X)       0 of  39      nucshell (l,sigma)     2 of  15
    gravity  (B,F,X,E)     2 of  39      madelung (n+l,k)      54 of 159
    baryons  (2I,Q3)       0 of  75      ions     (sl,tl)      86 of  91
                                         madrule  (S_a,l_d)    67 of  73

`madelung (n+l, k)` IS SEATED and is off-channel at 54 of its 159 dense
reaches, so densifying would unseat it and empty K6.  Section 3 already says
why that reading is wrong: madelung's `n+l` alphabet GROWS with reach, every
proper prefix is a chart that has not finished being itself, and an earlier
form of this gate was withdrawn for precisely the defect densification
reintroduces.  THE DECLARED POINTS ARE CHOSEN REACHES -- complete n+l shells,
Z decades -- NOT SAMPLES OF A CONTINUUM.  So the dense sweep is filed as a
FINDING and is deliberately NOT wired into `grounds()`.

WHAT IS LEFT STANDING, AND WHY.  By the gate as written `admissible()` returns
gravity (B,F,X,E), madelung (n+l,k) and baryons (2I,Q3), while `SEATED_ROWS`
still seats gravity (B,F,X).  The fixture "SEATED_ROWS agrees with what the
gate admits" FAILS, IT IS NOT LOOSENED, and `seating_divergence()` pins the
disagreement to exactly that one row so it cannot widen unnoticed.

    THIS PASS DOES NOT RE-SEAT, AND THAT IS A SCOPE DECISION RATHER THAN A
    VERDICT ON THE CHART.  Moving K1's occupant is a RULING on this file's own
    precedent -- DOCKET 22 unseated one row and took a docket, nine agents and
    three lenses to do it.  It also reaches outside this file: `registry.py`
    pins `overlaprule.gravity_bound` at 26 cells, `figure.py` reads its width,
    and THE PUBLISHED PAPER prints K1's single occupant as 26 cells at
    (1, 8, 5).  A pass repairing a fixture does not get to move that silently.

    AND THE RULING IS NOT OBVIOUS, WHICH IS THE BETTER REASON.  The coordinate
    that would newly enter a seated chart is `E`, and gravity.py's own gloss
    for it is "mass evidence (0 measured, 1 estimated)".  Whether (B,F,X,E)
    holds its channel at a sampled reach turns on which species happen to carry
    an ESTIMATED mass below that Z, and DOCKET 49b moved exactly that by adding
    eight species.  THIS FILE DOES NOT REFUSE THE CHART ON THAT GROUND.  It has
    no such ground, and inventing one after seeing the answer is what section
    3d forbids.  It is recorded so that whoever rules can see it.

    WHAT WOULD SETTLE IT, stated so it can be done properly.  EITHER (a) a
    ruling that the six-point schedule IS gravity's reach, in which case
    (B,F,X,E) is sound, K1 changes hands, and registry.py, figure.py, STATE and
    the paper follow it; OR (b) a ruling on whether a chart may be seated on a
    coordinate that records the EVIDENCE FOR a member rather than a property OF
    one, which refuses (B,F,X,E) and leaves every figure where it is.  Both are
    rulings.  Neither is a repair, and this pass made neither.

===============================================================================
3c. WHY K4 IS THE HARD ONE, AND IT IS NOT AN ACCIDENT
===============================================================================

`statistics` is `D.kdet(S, box, 2)`, and kdet opens with

        if k >= d:
            return True

SO EVERY ARITY-2 CHART CLOSES `statistics`, WHATEVER IT CONTAINS.  Measured
over all 283 charts of the eleven: **72 of 72 arity-2 charts close statistics
and none fails to**, while at arity 3 it is 41 of 82 and by arity 6 it is 0 of
14.  An arity-2 chart therefore cannot be K0 at all -- the census finds zero --
and its channel floor is K2.

    NOW LOOK AT WHICH CHANNELS THE LAW PROTECTS FROM THAT.  `hlaw.LAWFUL` has
    (statistics, geometry), (statistics, algebra) and (statistics, order): if
    geometry closes, statistics must; if algebra or order closes, statistics
    must.  So at K5 and K6 the statistics bit is FORCED BY LAW and the free
    pass changes nothing -- the seatings there stand on geometry and on the
    order/algebra block, which arity buys nobody.

    K4 = {information, statistics} IS THE ONE CHANNEL WITH NEITHER PROTECTION.
    Nothing in the law forces statistics from information.  It is the only
    channel above K1 whose extra content is exactly the bit an arity-2 chart
    gets for free.

    AND BOTH CHARTS THAT REACHED K4 ARE ARITY 2 -- `ions` (sl, tl) and
    `madrule` (S_a, l_d), 7 cells and 6 cells.  **No chart of arity 3 or more,
    anywhere in the 272, reaches K4.**  So neither candidate ever demonstrated
    statistics as a property of its object; both were handed it by their
    coordinate count, and what they actually showed is join-closure, which is
    K1.

    THIS IS NOT A PROOF THAT K4 IS UNREACHABLE and the file does not offer one.
    An arity-3-or-more chart that is join-closed and genuinely 2-determined,
    and neither hull-complete nor meet-closed, would sit in K4 having earned
    every bit of it.  None exists here.  That is what "K4 is empty" means, and
    it is a sharper statement than two candidates having failed a gate: **the
    two that reached it reached it at the one arity where half the channel is
    free.**

3d. DOCKET 23 -- K4 IS REACHABLE AT ARITY 3, AND THAT IS NOT A LICENCE
===============================================================================

Section 3c says K4's statistics bit is free at arity 2 and that both charts
which reached K4 are arity 2.  The obvious next question is whether `madrule`
could reach K4 at an arity where statistics has to be EARNED.  It can.

    madrule (S_a, l_d)          6 cells   arity 2   K4   statistics free
    madrule (S_a, l_d, occ)    13 cells   arity 3   K2   statistics EARNED,
                                                         information lost

    So its own full chart answers the question badly: add the third coordinate
    it already has, and information stops closing.

    BUT madrule MEASURES MORE THAN IT CHARTS.  `madrule.table()` gives every
    exception as (Z, symbol, acceptor, donor, cell) with acceptor and donor
    each a full (n, l).  Ten quantities are available from that: S_a, l_d, occ,
    n_a, l_a, n_d, S_d, dS, dn, dl.  Over all 120 arity-3 charts of those ten:

        K0 16    K2 57    K3 32    K4 3    K5 3    K6 1    K7 8

    THREE REACH K4 AT ARITY 3 -- (S_a, l_d, S_d), (S_a, l_d, dn) and
    (l_d, S_d, dn), each 6 cells.  At arity 3 `kdet` is not trivial, so those
    three earn their statistics.

    AND NOT ONE OF THEM MAY BE SEATED, because of how they were found.  This
    file went looking for K4 and searched 120 charts until three landed there.
    `inversion.py` and `probability.py` both state the rule it breaks: "an
    index built to land on a cell demand.py wants would be fitted, and a fitted
    vertex closes nothing."  A chart selected BECAUSE it lands in a channel is
    the definition of fitted, and the search is on the record above so that
    nobody can later present one of the three as a discovery.

    WHAT WOULD MAKE ONE SEATABLE, stated so it can be done properly.  A
    coordinate justified from the corpus BEFORE the chart is run.  One such
    justification is available and this file will not use it: a Madelung
    exception is a TRANSFER BETWEEN TWO SUBSHELLS, and the seated row charts
    the acceptor by its n+l and the donor by its l -- an asymmetry nothing
    requires.  The symmetric chart is (S_a, l_d, S_d), which is one of the
    three.  THAT ARGUMENT IS SOUND AND IT WAS FORMED AFTER SEEING THE ANSWER,
    which is exactly the order that makes it inadmissible here.  Someone who
    reaches it from the corpus's own account of the transfer, without this
    section in front of them, has a seating; this pass does not.

    SO DOCKET 23 CLOSES, AND NOT AS "WAIT FOR NEW ELEMENTS".  `madrule
    (S_a, l_d)` stays refused on the majority condition, and section 3c stands:
    it could never earn K4 at arity 2 however many elements arrive.  What is
    withdrawn is the stronger reading that K4 needs an arity madrule cannot
    reach -- it can, three ways, and the obstacle is provenance rather than
    arithmetic.

3e. DOCKET 22: THE GROUND THAT UNSEATED ONE OF THIS FILE'S OWN ROWS
===============================================================================

Nine agents, three lenses on each of the three seatings, adversarial and
read-only.  Two survived every test.  ONE DID NOT, and it fell on a measurement
none of the grounds above asks for.

    THE SAME 22 MEMBERS, THE SAME 12-FOLD PARTITION, THREE FAITHFUL ADDRESSES:

        nucshell (l, sigma)   12 cells   K5   geometry+information+statistics
        nucshell (l, 2j)      12 cells   K7   ALL FIVE
        nucshell (2j, sigma)  12 cells   K7   ALL FIVE

    The fibres are identical -- verified, not assumed.  K7 is OCCUPIED, so
    under either alternative `ground_novel_channel` returns False and the chart
    is not a candidate at all.  AND 2j IS THE BANKED PRIMITIVE:
    `nucshell.order_a()` stores (nr, l, Fraction(j)), and sigma is DERIVED from
    it.  nucshell.py's stated reason for preferring sigma -- "j is determined
    by (l, sigma)" -- holds verbatim with the roles swapped, at identical LABEL
    ratios of 0.3182.

    SO THE K5 WAS A FACT ABOUT WHICH NAME WAS WRITTEN DOWN.  `ground_
    coordinate_forced` is that test: two addresses inducing the IDENTICAL
    partition of the IDENTICAL members are one chart written twice, and if one
    reaches an empty channel while the other reaches an occupied one, the
    channel is not a property of the object.

    THE OTHER TWO PASS IT, and that was checked before the unseating rather
    than assumed.  `madelung (n+l, k)`: three alternative pairs over the
    quantities fibred banks -- (k, S), (k, S+k), (S, S+k) -- induce the same
    82 fibres and ALL land at K6.  `gravity (B, F, X)`: the rank encoding and
    the raw-decade encoding induce the same 26 fibres and both land at K1,
    which is `gravity.encoding_sensitivity()`'s question asked of the
    coarsening.

    THE PARENT IS UNTOUCHED.  (nr, l, sigma) and (nr, l, 2j) are both K3, so
    no pre-ruling vertex moves.  The fault was the coarsening's alone.

    WHAT IT COST TO PUT RIGHT: the figure goes 14 -> 13 vertices, E 81 -> 59,
    K5 empties, and BOTH resolution axes stay measurements -- so figure.py
    section 1b's gain was not carried by the vertex that fell.

    AND A SECOND, INDEPENDENT GROUND AGAINST THE SAME ROW, found by the same
    pass: section 5's nucshell part B said "the radial node count is what
    breaks join-closure".  Measured, (nr, sigma) is 6 cells at K7 with ZERO
    join counterexamples -- forgetting `l` restores join-closure exactly as
    forgetting `nr` does.  The attribution was false whatever the channel did.

===============================================================================
4. THE VERDICTS
===============================================================================

    SEATED, three.  RE-PINNED FROM "two": DOCKET 29 seated the baryon row and
    this list was never extended with it.  `SEATED_ROWS` holds three and
    `admissible()` MEASURES three; what they disagree about is the gravity row,
    and that is section 3f.

    madelung (n+l, k)     K6    82 cells    gate 7/7    parent K7 at (n+l,l,k)
    gravity  (B, F, X)    K1    26 cells    gate 6/6    parent K0 at seven
    baryons  (2I, Q3)     K5    16 cells    gate 7/7    DOCKET 29, section 3c

    madelung's "7/7" IS AT COMPLETE n+l SHELL REACHES, which is the schedule
    `SWEEPS` samples.  The two unsampled degenerate reaches (2 and 4 electrons)
    are K7; over all nine it is 7/9 and still passes.  Quoted with its schedule
    because 7/7 reads like seven independent checks and is not.

    REFUSED, four, each recorded so it can be re-adjudicated:

    nucshell (l, sigma) K5  COORDINATE NOT FORCED.  SEATED AND THEN UNSEATED --
                       section 3e.  The identical partition under (l, 2j) is
                       K7, which is occupied, and 2j is the banked primitive.

    gravity (B,F,X,E)  K1   THIS REFUSAL IS WITHDRAWN -- SECTION 3f.  It read
                       "OSCILLATES.  K1, K0, K1, K1, K1, K1 across
                       Z <= 20/40/60/80/100/118.  The arity-4 extension of a
                       chart that passes; the gate refuses the extension and
                       keeps the arity-3 chart, which is the gate working."
                       After DOCKET 49b the same sweep MEASURES
                       K1, K1, K1, K1, K1, K1.  The chart now clears all four
                       grounds and maximality refuses (B,F,X) in its place.
                       THE RULING HAS NOT FOLLOWED THE GATE: `SEATED_ROWS`
                       still seats (B,F,X), the fixture "SEATED_ROWS agrees
                       with what the gate admits" FAILS, and 3f states why that
                       is left standing rather than repaired here.  Densely the
                       chart is still off-channel at Z <= 35 and Z <= 36, so
                       the refusal lapsed as a fact about the SAMPLE and not as
                       a fact about the chart.
    ions (sl, tl)      K4   LATE ARRIVAL.  K2 at Z <= 36, 54, 72, 86, 100 and
                       K4 only at the terminal 108.  This is DOCKET 2's own
                       failure shape, in the same direction.
    madrule (S_a, l_d) K4   NO MAJORITY.  K4 at 2 of 7 reaches.  The five
                       earlier reaches hold 1, 2, 3, 4 and 5 cells and close in
                       all five languages, which a chart that small does for
                       free.  IT IS THE WEAKEST OF THE THREE REFUSALS: it holds
                       K4 at its widest two reaches, so unlike `ions` it passes
                       the open-upper-bound test in section 3, and it is
                       refused on the count alone.  The likeliest of anything
                       here to be re-adjudicated -- though NOT at arity 2, and
                       section 3d shows the three arity-3 charts that do reach
                       K4 and why none of them may be seated.

    SO K1, K5 AND K6 BECOME OCCUPIED AND K4 DOES NOT.  The empty channel that
    remains is the one whose only two candidates both failed on the reach, and
    that is a finding about K4 rather than a gap in this file.

===============================================================================
5. TWO PARTS OF THE DEFINITION, NAMED AS PHYSICS
===============================================================================

M's ruling does not say that a differing channel is sufficient.  It says the
overlap "should tell us two parts of definition contained in that overlapped
position".  For each seated coarsening, part A is what the parent's chart says
about these members and part B is what the coarsening says that the parent's
does not.  Both are statements about electrons and nuclei.  "It closes
information" is not a part of a definition and is not offered as one.

    MADELUNG.  Part A: every one of the 170 electrons has a unique address in
    (fill-order shell, subshell, slot), and the realised addresses close in all
    five languages.  THAT K7 IS NOT FREE, and an earlier draft of this sentence
    said it was: the chart is 170 cells in an 810-cell box, density 0.2099, not
    a complete rectangle and not even a down-set of the product order.  Its
    sibling `fibred` (n, l, k) holds the same 170 members at the same arity and
    the same density and is K3.  (DOCKET 22, correction A.)
    Part B: forget the subshell.  The 170 collapse onto 82 fill-order-shell/slot
    positions, and THAT set closes in order, algebra, information and
    statistics but NOT geometry.  Its sibling (n, k) -- the same collapse from
    the shell base rather than the fill-order base -- closes geometry and
    statistics and none of the other three.  The two coarsenings are
    complementary: union all five, intersection {statistics}.  So the choice of
    base decides WHICH MAXIMAL LANGUAGE survives the collapse, and neither
    chart alone can say that.  madelung.py section 3 measured this and section
    4 declined to seat it, in terms: "WHETHER TO SEAT IT IS A RULING AND NOT A
    MEASUREMENT.  This file does not seat it."  This is that ruling.

        THE OBJECTION, WHICH IS REAL AND IS RECORDED RATHER THAN WAVED AWAY.
        K6 = {algebra, information, order, statistics} is a STRICT SUBSET of K7.
        Relative to its parent this coarsening gains no language at all; it only
        loses geometry.  Every other seating here gains one.  The verification
        pass flagged it as the DOCKET 2 shape -- a two-coordinate projection of a
        chart already seated.

        THE ANSWER IS THAT A K7 PARENT IS THE ONE CASE WHERE LOSING IS THE
        MEASUREMENT.  madelung.py's own refusal section says it: "K7 means every
        operator is satisfied, which a complete rectangle achieves trivially."  A
        chart that closes everything for free says nothing about which of its
        closures the structure earns.  The collapse is the only way to ask, and
        the answer is that the fill-order-shell/slot COLLAPSE carries the
        order and algebra block and does NOT carry geometry.  THE BASE ALONE
        DOES NOT DECIDE THIS -- paired with l instead of k the same base is K7.
        The parent's three arity-2 projections are (n+l, l) 25 cells K7,
        (n+l, k) 82 cells K6 and (l, k) 50 cells K7: ONE K7 PARENT, THREE
        DIFFERENT ANSWERS, and that non-derivability is the measurement the
        argument needs -- not the rectangle premise, which is false.
        (DOCKET 22, correction B.)

        AND THE CHANNEL IS WEAKLY DISCRIMINATING AT THIS SHAPE, which is worth
        saying against this file's own interest.  398 of 400 random monotone
        nine-row staircases summing to 82 in the same box are also K6.  What is
        specific to the electrons was measured separately: remove the flats in
        the row lengths (2,2,6,6,10,10,14,14,18) and it is K7; drop the l < n
        rule so the lengths run 4S-2 and it is K7.  The flats ARE the
        fill-order-shell doubling and l < n IS the hydrogenic constraint, so
        the physics is real -- but it lives in those two facts and not in the
        phrase "closes order, algebra, information, not geometry".
        (Correction C.)  So the second part of the definition
        is not a language gained -- it is WHICH OF THE PARENT'S FIVE WERE REAL,
        and that is information about the electrons, not about the chart.

        WHAT THE ANSWER LEANS ON, STATED SO IT CAN BE ATTACKED.  It is
        strengthened by the sibling (n, k), which collapses the same 170 from the
        shell base to K3 and is exactly complementary.  But (n, k) sits in an
        OCCUPIED channel and this rule will not seat it, so the complementary
        pair is an argument available to a reader, not a vertex in the figure.
        The seating stands on the K7-probe argument alone.

    NUCSHELL -- WITHDRAWN, DOCKET 22.  This paragraph claimed that forgetting
    the radial node count is what restores join-closure in the nuclear shell
    sequence.  IT IS FALSE AS MEASURED: (nr, sigma) is 6 cells at K7 with ZERO
    join counterexamples, so forgetting `l` restores join-closure exactly as
    completely as forgetting `nr` does, and the attribution singles out
    nothing.  The row was unseated for a prior and independent reason --
    section 3e, the coordinate is not forced -- but this physics was wrong on
    its own and would have had to go either way.

    GRAVITY.  Part A: the full seven-coordinate nuclide-dimension chart closes
    in NOTHING -- it is ragged in every language.  Part B: the
    (horizon-bound class, forced angular momentum, spin-decade) triple closes
    information alone, with ZERO join counterexamples and 32 meet
    counterexamples in 325 unordered pairs -- a join-semilattice that is not a
    lattice.  (An earlier draft of this file said 64, which is the ORDERED
    count, printed next to the unordered pair total.  The selftest caught it.)
    Physically:
    for any two realised (bound class, forced J, spin decade) combinations
    there is a realised combination at least as constrained as both, and not
    always one at most as constrained as both.  So the raggedness of the full
    chart is CARRIED BY D, Y, L and E: their own projection has 112 cells, K2,
    and 256 join counterexamples, against the bound triple's ZERO.  That is the
    operative comparison and it is measured.  THE STRONG READING IS FALSE and
    is withdrawn: 509 of the parent's 96,372 join failures are witnessed by
    pairs differing only in (B, F, X), so the bound structure is not innocent.
    Those 509 fail as a CROSS-BLOCK interaction -- the join's own bound triple
    is realised elsewhere in the chart -- which is why the triple's own
    projection still has no join failure of its own.  (DOCKET 22, correction E.)

===============================================================================
6. THE DIMENSION FINDING, WHICH IS NOT PART OF ANY GATE
===============================================================================

Sweeping gravity's D -- its independent variable, not its reach:

    (B, F, X)     D <= 5  K7 (21 cells)    D <= 6 .. 11  K1 (26 cells)
    (B, F, X, E)  D <= 5  K7 (42 cells)    D <= 6 .. 11  K1 (52 cells)

    READ IN FOUR AND FIVE DIMENSIONS, THE BOUND STRUCTURE OF NUCLEAR MATTER
    CLOSES IN ALL FIVE LANGUAGES.  ADMIT THE SIXTH AND FOUR OF THE FIVE BREAK
    AT ONCE, LEAVING INFORMATION ALONE, AND IT NEVER MOVES AGAIN THROUGH D = 11.

    D = 6 IS EXACTLY WHERE MYERS-PERRY LOSES ITS HORIZON BOUND.  Singly-rotating
    Myers-Perry has f(r) = r^(D-3) + a^2 r^(D-5) = mu; D = 4 gives the Kerr
    bound mu >= 2a, D = 5 gives mu >= a^2, and from D = 6 the ultraspinning
    branch has NO bound at all.  gravity.py's `bound_class` is that theorem and
    nothing else.  The channel collapse is therefore not a coincidence of
    charting: the ultraspinning threshold is VISIBLE IN THE CLOSURE ALGEBRA, at
    the dimension the theorem names, without the closure operators being told
    anything about dimension.

    AND THE READING IS OFF CUMULATIVE SWEEPS, WHICH NEVER EXPOSE A K0.  Per
    single dimension the picture is different and is recorded here rather than
    left for someone to find: D = 4 alone is K7 (11 cells), D = 5 alone is K1
    (17), and D = 6 through 11 are EACH K0 (17 cells, 5 join counterexamples).
    The seated K1 is the union over D and holds at no single dimension above
    five.  (DOCKET 22, correction F.)

    THIS FILE DOES NOT CLAIM MORE THAN THAT.  It is one threshold in one index,
    it was found by sweeping a variable rather than predicted, and no mechanism
    is offered for why losing a bound should cost four languages and not three.
    Recorded, not explained.

===============================================================================
7. WHAT THIS FILE REFUSES
===============================================================================

    TO SEAT ON A DIFFERING CHANNEL ALONE.  The channel is necessary; sections 2,
    3 and 5 are the rest, and three of six candidates died in them.

    TO CALL K4 UNREACHABLE.  Two candidates reached it and both failed the
    reach gate.  That is two failures, not a theorem.

    TO REOPEN DOCKET 2.  `periodic layout 2-D` fails the bijection ground and
    the reach ground both, and the ruling touches neither.  It stays withdrawn.

    TO REVIVE ANY FILE DELETED FOR THE CRITERION.  store.py, obstruction.py,
    cross.py, density.py and occupy.py went because their members are not
    elements.  M enforced that criterion and this ruling says nothing about it.

    TO CLAIM THE PER-WITNESS READINGS WERE INDEPENDENTLY CHECKED.  A
    verification run was launched with seventeen agents -- three adversarial
    lenses on each of the six candidates, plus precedent, consequence and
    synthesis passes.  ONE returned before the account hit a weekly quota; it is
    the one quoted in section 3b, and it checked section 1's readings and
    nothing else.  Section 5's physics is therefore THIS FILE'S OWN reading,
    corroborated by madelung.py section 3 for the madelung row and by nothing
    outside this tree for the other two.  It is stated as a claim and is not
    stated as verified.

    TO CLAIM THE SIX ARE ALL THERE ARE.  They are all there are AMONG SUB-CHARTS
    OF THE ELEVEN SEATED INDEXES.  A chart of some other member set may reach
    any channel, and `--census` re-derives the six rather than trusting them.
"""

import importlib
import itertools
import math
import sys

import hlaw
import mi
import registry

# WHERE THE DATA COMES FROM.  registry.sources() reads this, checks every
# path exists and hashes it, and state.py writes the result into STATE.json --
# so provenance is a checked fact in the tree and not a sentence in a chat.
SOURCE = (
    'Inherited: every row here is a coarsening of a parent index and reads exactly what that parent reads.',
    (),
)


# The coordinate order of each seated index's cell tuple.  Five modules declare
# NAMES; the other six do not, and their order is read from the accessor's own
# docstring -- fibred "the shell fibration", madelung.janet "(n+l, l, k)",
# channels.index "(l, B, mult)", laws.index "(span, levels, drift band)",
# probability.probabilities "the marginal and the two conditionals",
# inversion.coords "(depth, span, reach)".
COORDS = {
    "fibred":      ("n", "l", "k"),
    "madelung":    ("n+l", "l", "k"),
    "ions":        ("sn", "sl", "k", "q", "tn", "tl", "g"),
    "channels":    ("l", "B", "mult"),
    "laws":        ("span", "levels", "drift"),
    "probability": ("p", "p_n", "p_s"),
    "inversion":   ("depth", "span", "reach"),
    "gravity":     ("D", "B", "F", "X", "Y", "L", "E"),
    "nucshell":    ("nr", "l", "sigma"),
    "madrule":     ("S_a", "l_d", "occ"),
    "terms":       ("mult", "L", "parity", "completeness"),
    # DOCKET 29.  The three particle parents DOCKET 27 seated.  Added so the
    # ruling's own machinery reaches them; `particlesweep.py` is the caller.
    "fundamental": ("2J", "Q3", "COL", "GEN"),
    "mesons":      ("2J", "P", "2I", "Q3"),
    "baryons":     ("2J", "P", "2I", "Q3", "S", "C", "B"),
    # DOCKET 35.  Two coordinates, so the ruling's own machinery can reach it;
    # a sub-population sweep over an arity-2 chart has one column to hold.
    "nucbands":    ("2I", "par"),
}

# The six candidates R4 admits.  PINNED so the default report runs in a second;
# `--census` re-derives them from all 272 proper sub-charts and asserts this
# tuple, and the selftest runs that assertion.
def coords(mod):
    """The coordinate names of a module's chart -- ASKED, never copied.

    COORDS below was hand-kept, and it stopped at the eleven-index era: six
    seated indexes (observed, fqh, bosonqp, readrezayi, spin4, deformedbands)
    were added later and never got an entry.  Every consumer used
    `COORDS.get(mod)` and skipped a miss SILENTLY, so section 6 of the paper
    swept 15 of 24 seated indexes and said it had swept them all -- and the
    one it most needed, spin4, the K4 occupant, was among the nine dropped.

    Each of those six declares its own NAMES.  This resolves COORDS first (so
    nothing already measured moves: all eight modules that declare both agree,
    and seven declare only COORDS), then the module's NAMES, and RAISES rather
    than returning None, so a future index cannot go missing quietly.

    AND IT DID NOT GO MISSING QUIETLY, WHICH IS THE WHOLE VALUE OF THE RAISE.
    `phonondex` and `kpointdex` were seated as rows 25 and 26 declaring
    neither, so this raised, `coords_reach()` reported them, and
    `particlesweep.py` and `spin4.py` CRASHED on the KeyError rather than
    sweeping 22 of 24 and saying they had swept them all.  Both now declare
    NAMES, read off their own `index()` docstrings.  MEASURED: the sweeps went
    from 440 proper sub-charts over 22 modules to 446 over 24, the six new ones
    are all arity 2, and NOT ONE of them is a candidate -- phonondex reaches
    K2, K7, K2 and kpointdex K2, K2, K2, and K2 and K7 are both occupied.  So
    the repair moved the sweep's reach and moved no verdict.
    """
    if mod in COORDS:
        return tuple(COORDS[mod])
    m = importlib.import_module(mod)
    n = getattr(m, "NAMES", None)
    if n:
        return tuple(n)
    raise KeyError(
        "%s holds a seated index but declares neither a COORDS entry nor "
        "NAMES; the sub-chart sweeps cannot reach it" % mod)


def coords_reach():
    """[] unless some seated index is unreachable by `coords`."""
    bad = []
    for nm, mod, _a, _me, _w, _q in registry.rows():
        if mod == SELF:
            continue
        try:
            coords(mod)
        except Exception as e:
            bad.append((registry.short(nm), mod, str(e)[:40]))
    return bad


CANDIDATES = (
    ("gravity",  ("B", "F", "X"),           1),
    ("gravity",  ("B", "F", "X", "E"),      1),
    ("ions",     ("sl", "tl"),              4),
    ("madrule",  ("S_a", "l_d"),            4),
    ("nucshell", ("l", "sigma"),            5),
    ("madelung", ("n+l", "k"),              6),
    # DOCKET 29.  From the exhaustive sub-chart census of the three particle
    # parents DOCKET 27 seated -- 142 charts, three reaching a channel the
    # census called unoccupied, two refused.  `particlesweep.py` is the
    # census and states both refusals.
    ("baryons",  ("2I", "Q3"),              5),
)

# How each parent's DATA reach is varied.  Every sweep uses the parent's own
# reach parameter -- ions.REACH_Z, madrule.REACH, madelung.REACH -- and never
# an independent variable.  nucshell takes no reach argument, so the sweep is
# over prefixes of its own subshell sequence, which is how that sequence is
# built up in the corpus.
SWEEPS = {
    "gravity":  ("Z", (20, 40, 60, 80, 100, 118)),
    "ions":     ("Z", (18, 36, 54, 72, 86, 100, 108)),
    "madrule":  ("Z", (36, 54, 72, 86, 100, 103, 108)),
    "nucshell": ("subshells", (8, 11, 14, 16, 18, 20, 22)),
    "madelung": ("electrons", (12, 20, 38, 56, 88, 120, 170)),
    # DOCKET 29.  A PARTICLE TABLE'S OWN REACH IS MASS: it grew by reaching
    # higher mass, the way the element tables grew by reaching higher Z, and
    # every one of the 292 baryons carries a mass so the cut is total.  The
    # cuts span the tabled range 938..6046 MeV.  `fundamental` is swept by
    # GENERATION instead -- six of its thirty carry no mass at all, so a mass
    # cut there would not be total, and generation is the axis that table
    # actually grew along.
    "baryons":  ("MeV", (1200, 1600, 2000, 2500, 3000, 5000, 6100)),
    "fundamental": ("generations", (1, 2, 3)),
}

DIM_SWEEP = (5, 6, 7, 8, 9, 10, 11)


# --------------------------------------------------------------- the charts

def _mod(name):
    import importlib
    return importlib.import_module(name)


def parent_chart(parent):
    """The parent's own full cell set, ASKED of the registry.  Memoised."""
    if parent not in _PARENT:
        for nm, mod, _acc, _me, _w, _q in registry.rows():
            if mod == parent and mod != SELF:
                _PARENT[parent] = registry.index_of(nm)
                break
        else:
            raise KeyError(parent)
    return _PARENT[parent]


_PROJ = {}
_PARENT = {}


def project(parent, cols, chart=None):
    """The sub-chart of `parent` on `cols`, as a cell set.  Memoised."""
    key = (parent, tuple(cols))
    if chart is None and key in _PROJ:
        return _PROJ[key]
    idx = [coords(parent).index(c) for c in cols]
    X = parent_chart(parent) if chart is None else chart
    P = frozenset(tuple(x[i] for i in idx) for x in X)
    if chart is None:
        _PROJ[key] = P
    return P


def at_reach(parent, cols, r):
    """The same sub-chart, at one point of the parent's own data reach."""
    idx = [coords(parent).index(c) for c in cols]
    if parent == "gravity":
        rows = _mod("gravity").rows()
        return frozenset(tuple(c[i] for i in idx)
                         for m, c in rows if m[0] <= r)
    if parent == "ions":
        return _mod("ions").subchart(tuple(cols), r)
    if parent in ("baryons", "mesons"):
        mod = _mod(parent)
        by = {int(x["pdgid"]): x["mass_MeV"]
              for x in _mod("pdgcapture").read()}
        keep = []
        for t in mod.rows():
            m = by[t[1]]
            if m != "?" and float(m) <= r:
                keep.append(t[2:])
        return frozenset(tuple(c[i] for i in idx) for c in keep)
    if parent == "fundamental":
        mod = _mod("fundamental")
        keep = [t[2:] for t in mod.rows() if t[5] <= r]
        return frozenset(tuple(c[i] for i in idx) for c in keep)
    if parent == "madrule":
        full = _mod("madrule").index(r)
    elif parent == "madelung":
        full = _mod("madelung").janet(r)
    elif parent == "nucshell":
        full = sorted(_mod("nucshell").index())[:r]
    else:
        raise KeyError(parent)
    return frozenset(tuple(x[i] for i in idx) for x in full)


# ------------------------------------------------------------- the grounds

SELF = "overlaprule"     # this file's own rows, once the ruling has seated them

# The channels occupied when this ruling was HANDED its index.  Historical, and
# kept so the file can say what moved rather than quietly re-measuring: DOCKET
# 34 seated spin4 at K4 and took a channel that was empty at the ruling.
RULED_CHANNELS = (0, 2, 3, 7)


def seated_channels():
    """The channels occupied BEFORE this ruling.  ASKED of the registry.

    THE RULING'S OWN ROWS ARE EXCLUDED, AND THEY HAVE TO BE.  `novel channel`
    asks whether a chart reaches somewhere the index does not already reach; the
    index it means is the one the ruling was handed.  Count the ruling's own
    seatings and the test eats itself the moment it succeeds -- K1 is occupied
    by gravity (B/F/X), so gravity (B/F/X) no longer has a novel channel, so it
    should not have been seated.  That is not a subtlety of implementation, it
    is what `novel` means, and the exclusion is the whole of it.

    IT ALSO MEANS THIS RULE CANNOT BE RUN TWICE TO GET MORE.  A second pass over
    the sub-charts sees the same four empty channels and the same six
    candidates.  Nothing compounds.
    """
    return frozenset(c[0] for nm, c in registry.cells().items()
                     if c != "UNMEASURED" and not nm.startswith(SELF + "."))


def ground_novel_channel(parent, cols):
    """R4: is this chart's channel occupied by no seated index?"""
    return mi.K(project(parent, cols)) not in seated_channels()


def ground_not_relabelling(parent, cols):
    """DOCKET 2's bijection ground: fewer cells than the parent separates."""
    return len(project(parent, cols)) < len(parent_chart(parent))


_SWEEP = {}


def reach_sweep(parent, cols):
    """[(label, cells, K)] over the parent's own data reach.  Memoised: pure,
    and the gate asks for it once per ground per candidate."""
    key = (parent, tuple(cols))
    if key not in _SWEEP:
        unit, pts = SWEEPS[parent]
        out = []
        for r in pts:
            X = at_reach(parent, cols, r)
            out.append(("%s <= %d" % (unit, r) if unit == "Z"
                        else "%d %s" % (r, unit), len(X), mi.K(X)))
        _SWEEP[key] = out
    return _SWEEP[key]


def dense_reach(parent):
    """Every reach the parent's own data holds INSIDE the span `SWEEPS`
    declares, at full resolution.  Section 3f.

    NOT A NEW SCHEDULE.  The endpoints are `SWEEPS`'s own first and last point
    and are never moved -- this reads the declared span at full resolution and
    nothing outside it, which is why it cannot be a fitted choice of where to
    look.
    """
    pts = SWEEPS[parent][1]
    lo, hi = pts[0], pts[-1]
    if parent == "gravity":
        vals = {m[0] for m, _c in _mod("gravity").rows()}
    elif parent in ("ions", "madrule", "madelung", "nucshell"):
        vals = set(range(lo, hi + 1))
    elif parent in ("baryons", "mesons"):
        by = {int(x["pdgid"]): x["mass_MeV"] for x in _mod("pdgcapture").read()}
        vals = {float(by[t[1]]) for t in _mod(parent).rows()
                if by[t[1]] != "?"}
    elif parent == "fundamental":
        vals = {t[5] for t in _mod("fundamental").rows()}
    else:
        raise KeyError(parent)
    return tuple(sorted(v for v in vals if lo <= v <= hi))


def dense_off_channel(parent, cols):
    """The reaches inside the declared span where the chart is NOT in its own
    channel.  A FINDING, AND DELIBERATELY NOT A GROUND -- section 3f.

    `grounds()` does not call this and must not.  Measured over all seven
    candidates, densifying the oscillation condition would fire on `madelung
    (n+l, k)` at 54 of its 159 dense reaches, and that chart is SEATED: section
    3 already withdrew the reading of an alphabet-growing chart's prefixes as
    evidence.  What it is for is saying whether a lapsed refusal lapsed about
    the chart or only about the sample.  Gravity's answer is the latter.
    """
    want = mi.K(project(parent, cols))
    return tuple(r for r in dense_reach(parent)
                 if mi.K(at_reach(parent, cols, r)) != want)


def seating_divergence():
    """[(row, what SEATED_ROWS holds, what the gate admits)] -- section 3f.

    EMPTY IS THE HEALTHY ANSWER and it is not empty.  The fixture
    "SEATED_ROWS agrees with what the gate admits" fails and is left failing;
    this pins the disagreement to its exact extent so that a second divergence
    cannot hide behind the first.
    """
    seats = {p: tuple(c) for p, c, _k, _n in admissible()}
    out = []
    for acc, (parent, cols) in sorted(SEATED_ROWS.items()):
        got = seats.get(parent)
        if got != tuple(cols):
            out.append((acc, tuple(cols), got))
    return out


def ground_reach_stable(parent, cols, want=None):
    """(passes, hits, total, late, oscillates, majority, the sweep).

    (a) no late arrival  (b) no oscillation  (c) majority -- section 3.
    """
    if want is None:
        want = mi.K(project(parent, cols))
    sweep = reach_sweep(parent, cols)
    hit = [i for i, (_l, _n, k) in enumerate(sweep) if k == want]
    late = (len(hit) <= 1) or (hit == [len(sweep) - 1])
    osc = (any(sweep[i][2] != want for i in range(min(hit), len(sweep)))
           if hit else True)
    maj = len(hit) * 2 > len(sweep)
    return ((not late) and (not osc) and maj,
            len(hit), len(sweep), late, osc, maj, sweep)


_SOUND = []


def sound():
    """The candidates that clear the three grounds of sections 1-3.

    SOUNDNESS ONLY.  Maximality is applied AFTER this and never before -- see
    section 3b: run the other way round the pair (B,F,X)/(B,F,X,E) resolves to
    the oscillating chart and K1 comes out empty.
    """
    if not _SOUND:
        for parent, cols, _k in CANDIDATES:
            if all(grounds(parent, cols).values()):
                _SOUND.append((parent, tuple(cols)))
        _SOUND.append(None)              # marks the cache as filled
    return [x for x in _SOUND if x is not None]


def ground_maximal(parent, cols, among=None):
    """Is no SOUND chart of this parent, in this channel, a super-chart of it?

    Section 3b.  Same parent, same channel, strictly more coordinates means the
    smaller chart repeats the larger one's language set and adds nothing: same
    information, and the smaller is the one to drop.
    """
    k = mi.K(project(parent, cols))
    pool = sound() if among is None else among
    here = set(cols)
    for p2, c2 in pool:
        if p2 != parent or set(c2) == here:
            continue
        if here < set(c2) and mi.K(project(p2, c2)) == k:
            return False
    return True


# Alternative FAITHFUL addresses of a parent's members: quantities the parent
# already banks, from which a re-coordinatisation can be built.  Section 3e.
ALT_COORDS = {
    "nucshell": ("nr", "l", "sigma", "2j"),
    "madelung": ("n", "l", "k", "S", "n-l", "2n", "l+k", "S+k"),
    "gravity":  ("D", "B", "F", "X", "Y", "L", "E"),
}


def _alt_rows(parent):
    """[{quantity: value}] over the parent's members, in the ALT_COORDS basis."""
    if parent == "nucshell":
        import nucshell
        return [{"nr": nr, "l": l, "sigma": int(2 * (j - l)), "2j": int(2 * j)}
                for nr, l, j in nucshell.order_a()]
    if parent == "madelung":
        import fibred
        return [{"n": n, "l": l, "k": k, "S": n + l, "n-l": n - l, "2n": 2 * n,
                 "l+k": l + k, "S+k": n + l + k}
                for n, l, k in fibred.addresses().values()]
    if parent == "gravity":
        import gravity
        NB = {"D": 0, "B": 1, "F": 2, "X": 3, "Y": 4, "L": 5, "E": 6}
        return [{k: c[i] for k, i in NB.items()} for _m, c in gravity.rows()]
    raise KeyError(parent)


def _partition(rows, ks):
    d = {}
    for i, r in enumerate(rows):
        d.setdefault(tuple(r[k] for k in ks), []).append(i)
    return (frozenset(frozenset(v) for v in d.values()),
            frozenset(tuple(r[k] for k in ks) for r in rows))


def recoordinatisations(parent, cols):
    """[(cols, cells, K)] for every alternative address inducing the SAME fibres.

    Section 3e.  The seated chart is included; anything else here partitions the
    parent's members exactly as it does, by other names.
    """
    if parent not in ALT_COORDS:
        return None
    rows = _alt_rows(parent)
    base, _X = _partition(rows, [{"n+l": "S"}.get(c, c) for c in cols])
    out = []
    for combo in itertools.combinations(ALT_COORDS[parent], len(cols)):
        pt, X = _partition(rows, combo)
        if pt == base:
            out.append((combo, len(X), mi.K(X)))
    return out


def ground_coordinate_forced(parent, cols):
    """Does the novel channel survive a faithful RE-COORDINATISATION?

    Section 3e, and it is the ground DOCKET 22 found by unseating a row this
    file had already seated.  Two addresses that induce the IDENTICAL partition
    of the identical members are the same chart written twice; if one reaches an
    empty channel and the other an occupied one, the channel is a fact about
    which name was written down.
    """
    alts = recoordinatisations(parent, cols)
    if alts is None:
        return True                       # no alternative basis banked: untested
    return len({k for _c, _n, k in alts}) == 1


def grounds(parent, cols):
    """{ground: bool} for the SOUNDNESS grounds.  Maximality is not one."""
    return {
        "novel channel": ground_novel_channel(parent, cols),
        "not a relabelling": ground_not_relabelling(parent, cols),
        "reach stable": ground_reach_stable(parent, cols)[0],
        "coordinate forced": ground_coordinate_forced(parent, cols),
    }


def adjudicate(parent, cols):
    """(seat, {ground: bool}) for one candidate, every ground measured."""
    g = grounds(parent, cols)
    pool = sound()
    g["maximal"] = ground_maximal(parent, cols, pool)
    return all(g.values()), g


def order_matters():
    """(K reached gate-first, K reached maximality-first) -- section 3b.

    THE TWO ORDERS GIVE DIFFERENT ANSWERS and this measures it rather than
    asserting it.  Maximality-first is computed over ALL candidates, sound or
    not, which is what running that test first means.
    """
    gate_first = sorted(k for _p, _c, k, _n in admissible())
    allc = [(p, tuple(c)) for p, c, _k in CANDIDATES]
    max_first = []
    for parent, cols, _k in CANDIDATES:
        if not ground_maximal(parent, cols, allc):
            continue
        if all(grounds(parent, cols).values()):
            max_first.append(mi.K(project(parent, cols)))
    return gate_first, sorted(max_first)


def admissible():
    """[(parent, cols, K, cells)] -- the coarsenings the ruling seats."""
    pool = sound()
    out = []
    for parent, cols in pool:
        if ground_maximal(parent, cols, pool):
            X = project(parent, cols)
            out.append((parent, tuple(cols), mi.K(X), len(X)))
    return out


def refused():
    """[(parent, cols, the ground that failed)] -- recorded, re-adjudicable."""
    out = []
    for parent, cols, _k in CANDIDATES:
        ok, g = adjudicate(parent, cols)
        if not ok:
            out.append((parent, tuple(cols),
                        sorted(n for n, v in g.items() if not v)))
    return out


# ------------------------------------------------- the seated three, as rows

# The rows this ruling seats, each naming the parent it coarsens.  ONE PLACE:
# the accessors read it and so does anyone asking whose members a row holds --
# `nucshell.py` asks, because its "no other seated index has a nuclear member"
# fixture has to exclude a coarsening of nucshell without excluding anything
# else, and the row's MODULE no longer says whose members it holds.
SEATED_ROWS = {
    "gravity_bound":   ("gravity",  ("B", "F", "X")),
    "madelung_slot":   ("madelung", ("n+l", "k")),
    # DOCKET 29.  THE TREE'S ONLY K5, and the first since DOCKET 22 retracted
    # the other one.  See `baryon_isomultiplet()`.
    "baryon_isomultiplet": ("baryons", ("2I", "Q3")),
}

# UNSEATED BY DOCKET 22, and kept here so the accessor still resolves for
# anyone re-adjudicating it.  Section 3e is the ground.
UNSEATED_ROWS = {
    "nucshell_lsigma": ("nucshell", ("l", "sigma")),
}


def parent_of(accessor):
    """Whose members does this ruling's row hold?  None if not one of ours.

    Answers for UNSEATED rows too -- the question is whose members a chart
    holds, which does not change when it stops being seated.
    """
    r = SEATED_ROWS.get(accessor) or UNSEATED_ROWS.get(accessor)
    return r[0] if r else None


def holds_members_of(name, parent):
    """Is the registry row `name` over `parent`'s own members?

    True for the parent's own row, and for any coarsening of it this ruling
    seated.  This is the question "same object?", which the module name stopped
    answering when three rows landed in one module.
    """
    mod, _, acc = name.partition(".")
    return mod == parent or (mod == SELF and parent_of(acc) == parent)


def gravity_bound():
    """gravity (B, F, X) -- the bound structure with D dropped.  K1.

    NOT "dimension-blind", which an earlier docstring claimed: B is a function
    of (D, q, F, Jzero) and its profile differs at D = 4, at D = 5 and at
    D >= 6.  Dropping D pools those, it does not make the chart independent of
    them.  DOCKET 22, correction G.
    """
    return project(*SEATED_ROWS["gravity_bound"])


def baryon_isomultiplet():
    """baryons (2I, Q3) -- isospin against charge, flavour dropped.  K5.

    DOCKET 29.  THE TREE'S ONLY K5.  The one DOCKET 22 retracted was
    `nucshell (l, sigma)`, and this is not that mistake repeated: that chart's
    K5 was a fact about writing the second coordinate as sigma, and an
    identical partition under (l, 2j) landed at K7.  This one is measured, its
    channel holds at every reach point of the parent's own data, and the bit
    that puts it at K5 rather than K2 is EARNED.

    WHY THE ARITY-2 FREE PASS DOES NOT REACH IT.  Section 3c: `statistics`
    closes for every arity-2 chart whatever it contains -- measured again for
    this docket at 105 of 105 across the tree -- so an arity-2 K4 shows only
    join-closure wearing a free bit.  K5 is protected from exactly that: the
    law forces statistics FROM geometry (Clause G.3), so the free pass changes
    nothing and the seating stands on geometry, which no arity buys.  And
    geometry is not free either -- 74 of 105 arity-2 charts close it, so 31 do
    not.  `arity2_freeness()` is that measurement.

    WHAT IT SAYS ABOUT BARYONS.  The cells are four isospins against the
    charges each reaches: 2I = 0 and 1 span Q3 in {-3, 0, 3}, 2I = 2 and 3
    span {-6, -3, 0, 3, 6}.  Geometry is hull-completeness on coordinate
    pairs, and the four box points the chart does not hold -- the corners
    (0, +-6) and (1, +-6) -- fall OUTSIDE the hull of the sixteen it does.
    That is the isospin multiplet structure: A MULTIPLET'S CHARGE SPAN WIDENS
    WITH ITS ISOSPIN, and widens steeply enough that the corners are cut off.
    The chart is that widening, and nothing else.
    """
    return project(*SEATED_ROWS["baryon_isomultiplet"])


def arity2_freeness():
    """{language: (closes, charts)} over every arity-2 sub-chart in the tree.

    SECTION 3c's CLAIM, RE-MEASURED FOR DOCKET 29 rather than quoted.  If
    geometry were free at arity 2 the way statistics is, the K5 seated above
    would be an artefact of coordinate count and nothing else.
    """
    import itertools
    out = {L: [0, 0] for L in hlaw.LANGS}
    for nm, mod, _a, _me, _w, _q in registry.rows():
        if mod == SELF:
            continue
        cols = coords(mod)
        X = registry.index_of(nm)
        for pair in itertools.combinations(range(len(cols)), 2):
            P = frozenset(tuple(c[i] for i in pair) for c in X)
            cl, _b = hlaw.closures(P)
            for L in hlaw.LANGS:
                out[L][1] += 1
                if len(cl[L]) == len(P):
                    out[L][0] += 1
    return {L: tuple(v) for L, v in out.items()}


def nucshell_lsigma():
    """nucshell (l, sigma) -- 12 cells, K5.  UNSEATED, DOCKET 22, section 3e.

    Kept callable because the finding is about it and a refusal that cannot be
    re-measured is not a record.  It is NOT in the registry.
    """
    return project(*UNSEATED_ROWS["nucshell_lsigma"])


def madelung_slot():
    """madelung (n+l, k) -- the Janet collapse, subshell-blind.  K6.

    CALLS madelung's OWN NAMED ACCESSOR rather than re-deriving the projection.
    `madelung.k6_chart()` already existed -- section 3 of that file measured
    this collapse and section 4 declined to seat it pending a ruling -- and the
    two are identical, which a fixture asserts.  An instrument imports a seated
    member; it never copies one, and re-projecting when the parent exposes the
    chart under its own name is a copy by another route.
    """
    import madelung
    return frozenset(madelung.k6_chart())


# ------------------------------------------------------------ the census

def census():
    """Re-derive the candidates from every proper sub-chart.  Slow.

    "272" WAS THE ELEVEN-INDEX FIGURE and this function has not swept 272 for a
    long time; it sweeps whatever the registry seats.  MEASURED at this pass:
    446 proper sub-charts over 24 modules, 440 over 22 before phonondex and
    kpointdex declared their NAMES.  The 272 in sections 1, 3b and 3c is left
    as written because it is scoped there to the eleven and is historical.
    """
    seated = seated_channels()
    out = []
    for nm, mod, _acc, _me, _w, _q in registry.rows():
        if mod == SELF:
            continue                      # a coarsening is not re-coarsened
        names = coords(mod)
        X = parent_chart(mod)
        for r in range(2, len(names)):
            for combo in itertools.combinations(names, r):
                P = project(mod, combo, X)
                k = mi.K(P)
                if k not in seated:
                    out.append((mod, combo, k))
    return tuple(sorted(out, key=lambda t: (t[2], t[0], len(t[1]))))


def reading_counts():
    """{reading: how many of the 272 it admits} -- section 1, re-measured."""
    seated_cells = frozenset(c for nm, c in registry.cells().items()
                             if c != "UNMEASURED"
                             and not nm.startswith(SELF + "."))
    seated_K = frozenset(c[0] for c in seated_cells)
    n = dict.fromkeys(("R1", "R2", "R3", "R4", "R3b", "R4b"), 0)
    for nm, mod, _acc, _me, _w, _q in registry.rows():
        if mod == SELF:
            continue
        names = coords(mod)
        X = parent_chart(mod)
        pcell = mi.cell(X)
        for r in range(2, len(names)):
            for combo in itertools.combinations(names, r):
                P = project(mod, combo, X)
                c = mi.cell(P)
                rel = len(P) == len(X)
                n["R1"] += c[0] != pcell[0]
                n["R2"] += c != pcell
                n["R3"] += c not in seated_cells
                n["R4"] += c[0] not in seated_K
                n["R3b"] += (c not in seated_cells) and not rel
                n["R4b"] += (c[0] not in seated_K) and not rel
    return n


def subchart_total():
    """How many PROPER sub-charts the readings are measured over.

    Pure combinatorics -- sum over the non-coarsening seated indexes of
    C(arity, r) for r = 2 .. arity-1 -- so it needs no projection and states
    the population the four readings in section 7 are counted against.
    """
    t = 0
    for nm, mod, _a, _me, _w, _q in registry.rows():
        if mod == SELF:
            continue
        d = len(coords(mod))
        for r in range(2, d):
            t += math.comb(d, r)
    return t


def reading_share():
    """(index, count) -- the largest single-index share of reading R3.

    The paper says "the third admits N coarsenings of a single index", and N
    was TYPED: no function computed it, so it survived the register growing
    from eleven indexes to twenty-four and the substitution guard could not
    see it, the figure being on a hand-kept exemption list.
    """
    seated_cells = frozenset(c for nm, c in registry.cells().items()
                             if c != "UNMEASURED"
                             and not nm.startswith(SELF + "."))
    per = {}
    for nm, mod, _acc, _me, _w, _q in registry.rows():
        if mod == SELF:
            continue
        names = coords(mod)
        X = parent_chart(mod)
        for r in range(2, len(names)):
            for combo in itertools.combinations(names, r):
                if mi.cell(project(mod, combo, X)) not in seated_cells:
                    per[registry.short(nm)] = per.get(registry.short(nm), 0) + 1
    return max(per.items(), key=lambda kv: (kv[1], kv[0])) if per else ("", 0)


def dimension_finding():
    """[(cols, [(D ceiling, cells, K)])] -- section 6.  A finding, not a gate."""
    rows = _mod("gravity").rows()
    out = []
    for cols in (("B", "F", "X"), ("B", "F", "X", "E")):
        idx = [COORDS["gravity"].index(c) for c in cols]
        seq = []
        for Dm in DIM_SWEEP:
            X = frozenset(tuple(c[i] for i in idx) for m, c in rows
                          if m[7] <= Dm)
            seq.append((Dm, len(X), mi.K(X)))
        out.append((cols, seq))
    return out


def statistics_is_free(d=2, k=2):
    """Does `statistics` close for free at arity d?  Section 3c.

    THE WITNESS IS THE CUBE MINUS ONE CORNER, {0,1}^d less the all-ones point.
    Every 2-projection of it is the whole of {0,1}^2, so reconstructing from
    the 2-projections gives the FULL cube -- one point more than the set.  It
    is the canonical not-2-determined set at every d >= 3.

    AT d = 2 THE SAME SET IS ALSO NOT 2-DETERMINED BY THAT ARGUMENT, and kdet
    returns True anyway, because of its opening `if k >= d: return True`.  That
    is the demonstration: not a set chosen to pass, but the very set that
    fails at every higher arity, passing at this one.
    """
    import decomposable as D
    full = [tuple(x) for x in itertools.product((0, 1), repeat=d)]
    X = frozenset(x for x in full if x != tuple([1] * d))
    return D.kdet(X, D.box_of(X, d), k)


def k4_analysis():
    """(the K4 candidates' arities, whether statistics is law-forced per channel).

    Section 3c.  K4 is the only channel above K1 whose extra bit over K1 is
    neither forced by the law nor earned at the arity its occupants have.
    """
    LAW = set(hlaw.LAWFUL)
    ch = mi.channels()
    forced = {}
    for i, S in enumerate(ch):
        forced[i] = ("statistics" in S and
                     any((("statistics", b) in LAW) for b in S))
    ar = {(p, tuple(c)): len(c) for p, c, k in CANDIDATES if k == 4}
    return ar, forced


def madrule_arity3():
    """Section 3d: every arity-3 chart of what madrule MEASURES, by channel.

    Ten quantities come out of `madrule.table()` -- the chart seats three of
    them.  This returns {K: [chart, ...]} over all 120 arity-3 combinations.

    REPORTED SO THE SEARCH IS ON THE RECORD.  Three of the 120 reach K4 with
    statistics earned, and none may be seated: a chart chosen because it lands
    in a channel is fitted, and this function is the evidence that they were
    chosen that way.
    """
    import madrule
    rows = []
    for _Z, _sym, (na, la), (nd, ld), cell in madrule.table():
        rows.append({"S_a": na + la, "l_d": ld, "occ": cell[2], "n_a": na,
                     "l_a": la, "n_d": nd, "S_d": nd + ld,
                     "dS": (na + la) - (nd + ld), "dn": na - nd, "dl": la - ld})
    keys = ("S_a", "l_d", "occ", "n_a", "l_a", "n_d", "S_d", "dS", "dn", "dl")
    out = {}
    for combo in itertools.combinations(keys, 3):
        X = frozenset(tuple(r[k] for k in combo) for r in rows)
        out.setdefault(mi.K(X), []).append("/".join(combo))
    return {k: sorted(v) for k, v in sorted(out.items())}


def semilattice(parent, cols):
    """(join counterexamples, meet counterexamples, pairs) for a sub-chart."""
    X = sorted(project(parent, cols))
    jn = mt = pr = 0
    S = set(X)
    for a, b in itertools.combinations(X, 2):
        pr += 1
        if tuple(max(x, y) for x, y in zip(a, b)) not in S:
            jn += 1
        if tuple(min(x, y) for x, y in zip(a, b)) not in S:
            mt += 1
    return jn, mt, pr


# ---------------------------------------------------------------------------

def report(do_census=False):
    print("=" * 74)
    print("THE OVERLAP RULING -- which overlapping charts may be seated")
    print("=" * 74)
    print()
    print("M: \"They can be seated with overlaps so long as it is not an")
    print("   overlap of same information ... its relative position in this")
    print("   index is information about an object.\"")
    print()
    print("1. THE CHANNELS THE ELEVEN OCCUPY.")
    sc = sorted(seated_channels())
    print("   occupied  %s" % ", ".join("K%d" % k for k in sc))
    print("   empty     %s" % ", ".join("K%d" % k for k in range(8)
                                        if k not in sc))
    print()
    print("2. THE CANDIDATES, AND EVERY GROUND MEASURED.")
    print("   %-10s %-14s %-3s %6s  %-6s %-6s %-6s %-6s %s"
          % ("parent", "sub-chart", "K", "cells", "novel", "not-rl", "reach",
             "maxml", "verdict"))
    for parent, cols, _k in CANDIDATES:
        ok, g = adjudicate(parent, cols)
        X = project(parent, cols)
        print("   %-10s %-14s K%-2d %6d  %-6s %-6s %-6s %-6s %s"
              % (parent, "/".join(cols), mi.K(X), len(X),
                 "yes" if g["novel channel"] else "NO",
                 "yes" if g["not a relabelling"] else "NO",
                 "yes" if g["reach stable"] else "NO",
                 "yes" if g["maximal"] else "NO",
                 "SEAT" if ok else "refuse"))
    gf, mf = order_matters()
    print()
    print("   THE ORDER OF THE TWO TESTS.  gate then maximality -> channels %s"
          % (["K%d" % k for k in gf],))
    print("   maximality then gate -> channels %s.  Section 3b."
          % (["K%d" % k for k in mf],))
    print()
    print("3. THE REACH SWEEPS.")
    for parent, cols, _k in CANDIDATES:
        ok, hits, tot, late, osc, maj, sweep = ground_reach_stable(parent, cols)
        print("   %-10s %-14s K%d at %d/%d   late %-5s osc %-5s maj %s"
              % (parent, "/".join(cols), mi.K(project(parent, cols)),
                 hits, tot, late, osc, maj))
        print("      " + "  ".join("%s K%d(%d)" % (l, k, n)
                                   for l, n, k in sweep))
    print()
    print("4. SEATED BY THE RULING.")
    for parent, cols, k, n in admissible():
        print("   %-10s %-14s K%d   %d cells" % (parent, "/".join(cols), k, n))
    print()
    print("5. REFUSED, AND ON WHICH GROUND.")
    for parent, cols, why in refused():
        print("   %-10s %-14s %s" % (parent, "/".join(cols), ", ".join(why)))
    print()
    print("6. THE DIMENSION FINDING -- gravity's D is a variable, not a reach.")
    for cols, seq in dimension_finding():
        print("   (%s)  %s" % ("/".join(cols),
                               "  ".join("D<=%d K%d(%d)" % (d, k, n)
                                         for d, n, k in seq)))
    print("   D = 6 is where singly-rotating Myers-Perry loses its horizon")
    print("   bound.  The closure algebra sees it without being told.")
    print()
    jn, mt, pr = semilattice("gravity", ("B", "F", "X"))
    print("7. THE K1 SHAPE.  gravity (B/F/X): %d join counterexamples, %d meet,"
          % (jn, mt))
    print("   in %d unordered pairs -- a join-semilattice, not a lattice." % pr)
    if do_census:
        print()
        print("8. THE CENSUS, re-derived over every proper sub-chart "
              "(446 over 24 modules at this pass; 272 was the eleven).")
        got = census()
        print("   candidates found  %d" % len(got))
        for mod, combo, k in got:
            print("      K%d  %-10s %s" % (k, mod, "/".join(combo)))
        print("   matches the pinned six: %s"
              % (got == tuple((p, tuple(c), k) for p, c, k in CANDIDATES) or
                 sorted(got) == sorted((p, tuple(c), k)
                                       for p, c, k in CANDIDATES)))
        print()
        print("   the six readings, re-counted:")
        for r, v in sorted(reading_counts().items()):
            print("      %-4s %4d" % (r, v))
    return 0


def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-56s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # the ruling's reading, and that it is the bounded one
    # DOCKET 34 MOVED THIS, AND THE MOVE IS THE FINDING.  When the ruling was
    # handed its index the seated rows occupied [0, 2, 3, 7] and K4 was empty,
    # which is why two candidates at K4 counted as novel.  spin4 then took K4,
    # so measured LIVE the occupied set is [0, 2, 3, 4, 7] and those two are
    # no longer novel.  Nothing is unseated by that -- neither was ever seated,
    # both having failed the reach gate -- but the ruling's own candidate list
    # is smaller today than the day it was ruled, and this file says so rather
    # than freezing the old number.  (DOCKET 35's nucbands lands at K2, which
    # was already occupied, and changes nothing here.)
    chk("LIVE, five channels are occupied -- DOCKET 34 added K4",
        sorted(seated_channels()), [0, 2, 3, 4, 7])
    chk("and at the ruling it was four: K4 is the one that arrived",
        sorted(set(seated_channels()) - set(RULED_CHANNELS)), [4])
    chk("seated_channels EXCLUDES this ruling's own rows -- it must",
        sorted({nm.split(".")[0] for nm in registry.cells()}
               & {SELF}) == [SELF]
        and sorted(seated_channels()) == [0, 2, 3, 4, 7],
        True)
    chk("a second pass finds the same five -- nothing compounds",
        len([c for c in CANDIDATES
             if ground_novel_channel(c[0], c[1])]), 5)
    chk("three channels are empty now, four at the ruling",
        ([k for k in range(8) if k not in seated_channels()],
         [k for k in range(8) if k not in RULED_CHANNELS]),
        ([1, 5, 6], [1, 4, 5, 6]))
    chk("seven candidates -- six, and DOCKET 29's from the particle sweep",
        len(CANDIDATES), 7)
    chk("and TWO of the seven lost their novel channel to DOCKET 34",
        sorted((c[0], c[1]) for c in CANDIDATES
               if not ground_novel_channel(c[0], c[1])),
        [("ions", ("sl", "tl")), ("madrule", ("S_a", "l_d"))])
    chk("both of those were at K4, and neither was ever seated",
        sorted({mi.K(project(c[0], c[1])) for c in CANDIDATES
                if not ground_novel_channel(c[0], c[1])}), [4])
    chk("NONE is a relabelling -- DOCKET 2's bijection ground",
        [c for c in CANDIDATES if not ground_not_relabelling(c[0], c[1])], [])

    # the gate, and that it REFUSES -- a rule that admits everything is none
    # THE SWEEPS MUST REACH EVERY SEATED INDEX.  They did not: COORDS stopped
    # at the eleven-index era and every consumer skipped a miss silently, so
    # nine of 24 were dropped from the paper's section 6 -- spin4, the K4
    # occupant, among them.  A miss is now a failure, not a shrug.
    chk("every seated index is reachable by the sub-chart sweeps",
        coords_reach(), [])

    chk("FOUR of the six are refused, after DOCKET 22", len(refused()), 4)
    # RE-PINNED True -> False, AND THE REASON IS SECTION 3f.  DOCKET 49b
    # widened gravity's reader (3,394 -> 3,663 member rows, 118 -> 126 species)
    # and the Z <= 40 reach went 48 cells at K0 to 50 cells at K1, so the six
    # declared points no longer sample the dip.  The two fixtures under it are
    # why this is a re-pin and not a retraction: the chart is STILL off-channel
    # at Z <= 35 and Z <= 36, so the refusal lapsed about the SAMPLE, not about
    # the chart.  3f records why densifying the gate is refused -- it would
    # unseat madelung_slot, which is off-channel at 54 of its 159.
    chk("the oscillation refusal of gravity (B/F/X/E) has LAPSED",
        ground_reach_stable("gravity", ("B", "F", "X", "E"))[4], False)
    chk("but densely, inside the span the sweep declares, it has not",
        dense_off_channel("gravity", ("B", "F", "X", "E")), (35, 36))
    chk("while gravity (B/F/X) is unmoved at every one of its 39 dense reaches",
        (dense_off_channel("gravity", ("B", "F", "X")),
         len(dense_reach("gravity"))), ((), 39))
    chk("it refuses ions (sl/tl) for late arrival",
        ground_reach_stable("ions", ("sl", "tl"))[3], True)
    chk("it refuses madrule (S_a/l_d) for want of a majority",
        ground_reach_stable("madrule", ("S_a", "l_d"))[5], False)
    # THE OPEN UPPER BOUND.  M: "until we can prove that no more elements are
    # left to discover or synthesize, the upper bound of the periodic table is
    # open."  A verdict holding at every available reach survives one more; a
    # verdict arriving at the last available reach does not.  Section 3.
    chk("every SEATED chart holds its channel at its widest TWO reaches",
        [(p, c) for p, c in sound()
         if [k for _l, _n, k in reach_sweep(p, c)][-2:]
         != [mi.K(project(p, c))] * 2], [])
    chk("of the refused, only ions fails that too -- madrule holds K4 at its "
        "widest two and is refused on the majority alone",
        sorted(p for p, c, _w in refused()
               if [k for _l, _n, k in reach_sweep(p, c)][-2:]
               != [mi.K(project(p, c))] * 2), ["ions"])
    chk("gravity (B/F/X) passes at every one of its six reaches",
        ground_reach_stable("gravity", ("B", "F", "X"))[1:3], (6, 6))
    chk("nucshell (l/sigma) passes at six of seven",
        ground_reach_stable("nucshell", ("l", "sigma"))[1:3], (6, 7))
    chk("madelung (n+l/k) passes at all seven",
        ground_reach_stable("madelung", ("n+l", "k"))[1:3], (7, 7))

    # maximality, and the ordering that makes it inert here -- section 3b
    # RE-PINNED [] -> [gravity (B/F/X)], SECTION 3f.  It was [] because
    # (B,F,X,E) failed the gate and so was not in the SOUND pool to contain
    # anything; it now passes, and maximality drops the arity-3 chart it
    # contains.  NOT LOOSENED TO "at most one": the one row is named.
    chk("maximality now drops gravity (B/F/X) among the SOUND ones",
        [c[:2] for c in CANDIDATES
         if not ground_maximal(c[0], c[1], sound())],
        [("gravity", ("B", "F", "X"))])
    chk("but (B/F/X) does NOT clear it among ALL candidates",
        ground_maximal("gravity", ("B", "F", "X"),
                       [(p, tuple(c)) for p, c, _k in CANDIDATES]), False)
    # RE-PINNED ([1,5,6],[5,6]) -> ([1,5,6],[1,5,6]), SECTION 3f.  The order
    # stopped deciding when (B,F,X,E) became sound: maximality-first now picks
    # it and the gate no longer kills it, so both orders reach the same three
    # channels.  Section 3b's PRINCIPLE stands; its only demonstration does not.
    chk("the order no longer decides -- both routes reach K1/K5/K6",
        order_matters(), ([1, 5, 6], [1, 5, 6]))

    # what seats, and where
    seats = admissible()
    chk("three seat", len(seats), 3)
    # LEFT FAILING ON PURPOSE, AND NOT LOOSENED -- SECTION 3f.  The gate admits
    # gravity (B,F,X,E); SEATED_ROWS seats (B,F,X).  Re-seating K1 is a RULING,
    # not a repair: it moves registry.py's pin of 26 cells, figure.py's width
    # and a figure the published paper prints, and the coordinate it would add
    # is `E`, gravity's "mass evidence (0 measured, 1 estimated)".  The fixture
    # below pins the divergence to exactly one row so it cannot widen unseen.
    chk("SEATED_ROWS agrees with what the gate admits",
        sorted((p, c) for p, c, _k, _n in seats),
        sorted(SEATED_ROWS.values()))
    chk("and the disagreement is exactly one row, and it is gravity's",
        seating_divergence(),
        [("gravity_bound", ("B", "F", "X"), ("B", "F", "X", "E"))])
    chk("every seated row names the parent whose members it holds",
        [a for a in SEATED_ROWS
         if not holds_members_of("%s.%s" % (SELF, a), parent_of(a))], [])
    chk("and holds_members_of does NOT claim a row of another parent",
        holds_members_of("overlaprule.nucshell_lsigma", "gravity"), False)
    chk("they occupy K1, K5 and K6",
        sorted(k for _p, _c, k, _n in seats), [1, 5, 6])
    # K5's HISTORY IN ONE FIXTURE.  The ruling first seated `nucshell
    # (l, sigma)` there; DOCKET 22 unseated it, because an identical partition
    # written (l, 2j) landed at K7 and the K5 was a fact about the spelling.
    # DOCKET 29 refilled K5 with a DIFFERENT chart over a different parent,
    # both of whose coordinates the PDG table prints, so there is no
    # alternative spelling for it to fall to.
    chk("K5 is occupied again, and by a different chart than the one DOCKET "
        "22 unseated",
        (sorted((p, c) for p, c, k, _n in seats if k == 5),
         UNSEATED_ROWS["nucshell_lsigma"] in
         [(p, c) for p, c, _k, _n in seats]),
        ([("baryons", ("2I", "Q3"))], False))
    chk("K4 is reached by two candidates and seated by neither",
        sorted(c[2] for c in CANDIDATES if c[2] == 4), [4, 4])
    chk("K4 stays empty", 4 in {k for _p, _c, k, _n in seats}, False)
    chk("gravity (B/F/X) is 26 cells", len(gravity_bound()), 26)
    chk("the UNSEATED nucshell (l/sigma) is still 12 cells and still K5",
        (len(nucshell_lsigma()), mi.K(nucshell_lsigma())), (12, 5))
    chk("madelung (n+l/k) is 82 cells", len(madelung_slot()), 82)
    chk("and it IS madelung.k6_chart, not a re-derivation of it",
        madelung_slot() == project(*SEATED_ROWS["madelung_slot"]), True)
    chk("its sibling madelung.k3_chart is the complementary collapse",
        (len(frozenset(__import__("madelung").k3_chart())),
         mi.K(frozenset(__import__("madelung").k3_chart()))), (82, 3))
    chk("K6 and K3 union to all five and meet at statistics alone",
        (sorted(set(mi.channels()[6]) | set(mi.channels()[3])),
         sorted(set(mi.channels()[6]) & set(mi.channels()[3]))),
        (sorted(hlaw.LANGS), ["statistics"]))
    chk("gravity (B/F/X) lands at K1", mi.K(gravity_bound()), 1)
    # SECTION 3e.  The ground that unseated it, and that the other two pass.
    chk("nucshell (l/sigma) FAILS coordinate-forced -- the identical partition "
        "under (l, 2j) is K7", ground_coordinate_forced("nucshell",
                                                        ("l", "sigma")), False)
    chk("and the channels its re-coordinatisations reach are K5 AND K7",
        sorted({k for _c, _n, k in recoordinatisations("nucshell",
                                                       ("l", "sigma"))}),
        [5, 7])
    chk("madelung (n+l/k) passes it -- every same-partition address is K6",
        sorted({k for _c, _n, k in recoordinatisations("madelung",
                                                       ("n+l", "k"))}), [6])
    chk("gravity (B/F/X) passes it", ground_coordinate_forced(
        "gravity", ("B", "F", "X")), True)
    chk("the parent is untouched: (nr,l,sigma) and (nr,l,2j) are both K3",
        sorted({mi.K(project("nucshell", ("nr", "l", "sigma")))}), [3])
    chk("madelung (n+l/k) lands at K6", mi.K(madelung_slot()), 6)

    # the K1 shape, which is the recipe section 5 names
    jn, mt, pr = semilattice("gravity", ("B", "F", "X"))
    chk("gravity (B/F/X) has NO join counterexample", jn, 0)
    chk("gravity (B/F/X) has 32 meet counterexamples, unordered", mt, 32)
    chk("325 pairs", pr, 325)

    # the dimension finding
    dim = dict((tuple(c), s) for c, s in dimension_finding())
    chk("(B/F/X) closes all five at D <= 5",
        dim[("B", "F", "X")][0][2], 7)
    chk("(B/F/X) drops to information alone at D <= 6",
        dim[("B", "F", "X")][1][2], 1)
    chk("and never moves again through D = 11",
        sorted({k for _d, _n, k in dim[("B", "F", "X")][1:]}), [1])

    # SECTION 3c.  statistics is free at arity 2, and K4 is the one channel
    # that has neither that protection nor the law's.
    chk("the cube-minus-a-corner is NOT 2-determined at arity 3",
        statistics_is_free(3), False)
    chk("nor at arity 4", statistics_is_free(4), False)
    chk("AND THE SAME SET PASSES AT ARITY 2 -- statistics is free there",
        statistics_is_free(2), True)
    ar, forced = k4_analysis()
    chk("both K4 candidates are arity 2", sorted(ar.values()), [2, 2])
    chk("statistics is LAW-FORCED at K5, K6 and K7",
        [k for k in (5, 6, 7) if not forced[k]], [])
    chk("and is NOT law-forced at K2 or K4 -- K4 is the exposed one",
        [k for k in (2, 4) if forced[k]], [])

    # SECTION 3d.  DOCKET 23: K4 IS reachable at arity 3, and the three that
    # reach it were found by searching for K4, which is what fitted means.
    m3 = madrule_arity3()
    chk("120 arity-3 charts of what madrule measures",
        sum(len(v) for v in m3.values()), 120)
    chk("three of them reach K4, with statistics EARNED at arity 3",
        m3.get(4, []),
        ["S_a/l_d/S_d", "S_a/l_d/dn", "l_d/S_d/dn"])
    chk("madrule's own full chart is K2, not K4 -- adding occ loses information",
        mi.K(project("madrule", ("S_a", "l_d", "occ"))), 2)
    chk("so the arity-2 pair is the only K4 route madrule already charts",
        mi.K(project("madrule", ("S_a", "l_d"))), 4)
    chk("and NONE of the three is seated -- they were found by searching",
        [c for c in m3.get(4, [])
         if tuple(c.split("/")) in {tuple(x[1]) for x in sound()}], [])

    # THE VACUITY GUARD.  A gate that passes everything measures nothing, and a
    # gate that fails everything measures nothing either.
    chk("the gate is not vacuous: it both admits and refuses",
        (len(admissible()) > 0, len(refused()) > 0), (True, True))

    print("overlaprule selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report("--census" in sys.argv))
