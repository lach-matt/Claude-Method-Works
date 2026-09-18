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

    AND THE REACH GATE SAYS THE ARITY-4 ONE IS NOT SOUND -- it oscillates, K1
    then K0 then K1 across the Z sweep.

    SO THE ORDER DECIDES THE ANSWER.  Maximality first picks (B,F,X,E), the gate
    then kills it, and K1 ENDS UP EMPTY.  Gate first kills (B,F,X,E), leaving
    (B,F,X) the only surviving K1 chart of that parent -- maximal among what
    survived -- and K1 ENDS UP OCCUPIED.

    THE GATE RUNS FIRST, AND NOT BECAUSE IT GIVES THE FULLER ANSWER.  The gate
    asks whether a channel verdict is a fact about the object; maximality asks
    which of two facts to keep.  A chart that fails the gate has no channel
    verdict to be maximal about.  Soundness before redundancy -- otherwise the
    redundancy test is choosing between one real reading and one artefact.

    HERE THE CLAUSE IS INERT.  The three that pass the gate have three different
    parents, so none contains another.  It is implemented and fixtured anyway,
    because it is inert by measurement and not by construction.

===============================================================================
4. THE VERDICTS
===============================================================================

    SEATED, three:

    madelung (n+l, k)     K6    82 cells    gate 7/7    parent K7 at (n+l,l,k)
    nucshell (l, sigma)   K5    12 cells    gate 6/7    parent K3 at (nr,l,sigma)
    gravity  (B, F, X)    K1    26 cells    gate 6/6    parent K0 at seven

    REFUSED, three, each recorded so it can be re-adjudicated:

    gravity (B,F,X,E)  K1   OSCILLATES.  K1, K0, K1, K1, K1, K1 across
                       Z <= 20/40/60/80/100/118.  The arity-4 extension of a
                       chart that passes; the gate refuses the extension and
                       keeps the arity-3 chart, which is the gate working.
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
                       here to be re-adjudicated.

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
    five languages -- a complete rectangle, which closes everything for free.
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
        the answer is that the fill-order base carries the order and algebra
        block and does NOT carry geometry.  The parent cannot say that, because
        the parent says yes to everything.  So the second part of the definition
        is not a language gained -- it is WHICH OF THE PARENT'S FIVE WERE REAL,
        and that is information about the electrons, not about the chart.

        WHAT THE ANSWER LEANS ON, STATED SO IT CAN BE ATTACKED.  It is
        strengthened by the sibling (n, k), which collapses the same 170 from the
        shell base to K3 and is exactly complementary.  But (n, k) sits in an
        OCCUPIED channel and this rule will not seat it, so the complementary
        pair is an argument available to a reader, not a vertex in the figure.
        The seating stands on the K7-probe argument alone.

    NUCSHELL.  Part A: the 22 nuclear single-particle subshells, addressed by
    (radial nodes, orbital angular momentum, spin-orbit sign), close geometry
    and statistics.  Part B: forget the radial node count.  The realised
    (l, sigma) pairs close geometry, statistics AND information -- join-closure
    is GAINED by forgetting nr.  Physically: any two realised
    orbital-angular-momentum/spin-orbit-alignment combinations have a realised
    combination above both, while the full three-coordinate address does not.
    The radial node count is what breaks join-closure in the nuclear shell
    sequence, and neither chart alone says that.

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
    chart lives in D, Y, L and E, and NOT in the bound structure, which is the
    part a warp-metric reading would need.  Neither chart alone locates it.

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

import itertools
import sys

import mi
import registry

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
}

# The six candidates R4 admits.  PINNED so the default report runs in a second;
# `--census` re-derives them from all 272 proper sub-charts and asserts this
# tuple, and the selftest runs that assertion.
CANDIDATES = (
    ("gravity",  ("B", "F", "X"),           1),
    ("gravity",  ("B", "F", "X", "E"),      1),
    ("ions",     ("sl", "tl"),              4),
    ("madrule",  ("S_a", "l_d"),            4),
    ("nucshell", ("l", "sigma"),            5),
    ("madelung", ("n+l", "k"),              6),
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
    idx = [COORDS[parent].index(c) for c in cols]
    X = parent_chart(parent) if chart is None else chart
    P = frozenset(tuple(x[i] for i in idx) for x in X)
    if chart is None:
        _PROJ[key] = P
    return P


def at_reach(parent, cols, r):
    """The same sub-chart, at one point of the parent's own data reach."""
    idx = [COORDS[parent].index(c) for c in cols]
    if parent == "gravity":
        rows = _mod("gravity").rows()
        return frozenset(tuple(c[i] for i in idx)
                         for m, c in rows if m[0] <= r)
    if parent == "ions":
        return _mod("ions").subchart(tuple(cols), r)
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


def grounds(parent, cols):
    """{ground: bool} for the three SOUNDNESS grounds.  Maximality is not one."""
    return {
        "novel channel": ground_novel_channel(parent, cols),
        "not a relabelling": ground_not_relabelling(parent, cols),
        "reach stable": ground_reach_stable(parent, cols)[0],
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

def gravity_bound():
    """gravity (B, F, X) -- the bound structure, dimension-blind.  K1."""
    return project("gravity", ("B", "F", "X"))


def nucshell_lsigma():
    """nucshell (l, sigma) -- the nuclear subshells, radially blind.  K5."""
    return project("nucshell", ("l", "sigma"))


def madelung_slot():
    """madelung (n+l, k) -- the Janet collapse, subshell-blind.  K6."""
    return project("madelung", ("n+l", "k"))


# ------------------------------------------------------------ the census

def census():
    """Re-derive the candidates from all 272 proper sub-charts.  Slow."""
    seated = seated_channels()
    out = []
    for nm, mod, _acc, _me, _w, _q in registry.rows():
        if mod == SELF:
            continue                      # a coarsening is not re-coarsened
        names = COORDS[mod]
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
        names = COORDS[mod]
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
        print("8. THE CENSUS, re-derived over all 272 proper sub-charts.")
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
    chk("the eleven occupy four channels", sorted(seated_channels()),
        [0, 2, 3, 7])
    chk("seated_channels EXCLUDES this ruling's own rows -- it must",
        sorted({nm.split(".")[0] for nm in registry.cells()}
               & {SELF}) == [SELF]
        and sorted(seated_channels()) == [0, 2, 3, 7],
        True)
    chk("a second pass finds the same six -- nothing compounds",
        len([c for c in CANDIDATES
             if ground_novel_channel(c[0], c[1])]), 6)
    chk("four channels are empty",
        [k for k in range(8) if k not in seated_channels()], [1, 4, 5, 6])
    chk("six candidates", len(CANDIDATES), 6)
    chk("every candidate has a novel channel",
        [c for c in CANDIDATES if not ground_novel_channel(c[0], c[1])], [])
    chk("NONE is a relabelling -- DOCKET 2's bijection ground",
        [c for c in CANDIDATES if not ground_not_relabelling(c[0], c[1])], [])

    # the gate, and that it REFUSES -- a rule that admits everything is none
    chk("the reach gate refuses three of six", len(refused()), 3)
    chk("it refuses gravity (B/F/X/E) for oscillation",
        ground_reach_stable("gravity", ("B", "F", "X", "E"))[4], True)
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
    chk("all six clear maximality among the SOUND ones",
        [c[:2] for c in CANDIDATES
         if not ground_maximal(c[0], c[1], sound())], [])
    chk("but (B/F/X) does NOT clear it among ALL candidates",
        ground_maximal("gravity", ("B", "F", "X"),
                       [(p, tuple(c)) for p, c, _k in CANDIDATES]), False)
    chk("so the order decides: gate-first K1/K5/K6, maximality-first K5/K6",
        order_matters(), ([1, 5, 6], [5, 6]))

    # what seats, and where
    seats = admissible()
    chk("three seat", len(seats), 3)
    chk("they occupy K1, K5 and K6", sorted(k for _p, _c, k, _n in seats),
        [1, 5, 6])
    chk("K4 is reached by two candidates and seated by neither",
        sorted(c[2] for c in CANDIDATES if c[2] == 4), [4, 4])
    chk("K4 stays empty", 4 in {k for _p, _c, k, _n in seats}, False)
    chk("gravity (B/F/X) is 26 cells", len(gravity_bound()), 26)
    chk("nucshell (l/sigma) is 12 cells", len(nucshell_lsigma()), 12)
    chk("madelung (n+l/k) is 82 cells", len(madelung_slot()), 82)
    chk("gravity (B/F/X) lands at K1", mi.K(gravity_bound()), 1)
    chk("nucshell (l/sigma) lands at K5", mi.K(nucshell_lsigma()), 5)
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
