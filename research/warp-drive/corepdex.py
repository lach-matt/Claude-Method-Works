#!/usr/bin/env python3
r"""
corepdex.py -- THE TIME-REVERSAL EXTENSION.  The corepresentations at every
isolated high-symmetry k-star: the LEVELS, where kpointdex seats the STARS.

    python3 corepdex.py             the reading
    python3 corepdex.py --selftest  fixtures, stdlib against the banked capture
    python3 corepdex.py --derive    rebuild the capture (needs numpy + spglib)

M: "Now seat the time-reversal extension for the antiunitary obstruction."

===============================================================================
0. THE OBSTRUCTION THIS SEATS, AND WHY DISCHARGING THE OTHER ONE WAS NOT ENOUGH
===============================================================================

`phonondex.py` refused k != 0 because the little group's representations are
PROJECTIVE for non-symmorphic groups.  `kpointdex.py` discharged that and seated
870 isolated high-symmetry k-stars.  Its own derivation recorded, and did not
repair, the reason that is not the end of it:

    "Discharging the projective refusal is NECESSARY AND NOT SUFFICIENT.  A
    second, independent obstruction -- TIME REVERSAL, via Herring's criterion --
    degenerates levels at 126 space groups' TRIMs against the projective
    mechanism's 108, and 56 space groups are touched by the antiunitary
    obstruction ALONE.  An implementation that discharges only the projective
    refusal is wrong at those 56 and ITS INTEGRALITY CHECKS DO NOT NOTICE."

THAT LAST CLAUSE IS THE WHOLE DIFFICULTY.  The unitary answer is internally
consistent: sum d^2 = |G_k| holds, the character table is orthogonal, every
dimension is an integer.  It is simply INCOMPLETE, and nothing inside it says
so.  Time reversal is ANTIUNITARY; it is not an element of the little group and
no amount of care with the little group will find it.

    THE MEMBER IS A LEVEL, NOT A STAR.  A corepresentation is the physically
    irreducible object -- what a spectrum actually shows as one degenerate
    multiplet.  At 309 of them the degeneracy is NOT the small-rep dimension.

===============================================================================
1. HERRING'S CRITERION, AND THE CONVENTION IT IS REPORTED IN
===============================================================================

With D^k({R|t}) = exp(-2 pi i k.t) Gamma(R) and Q = { q : q.k == -k mod G },

    W_r = (1/|G_k|) sum over q in Q of chi^k( {R_q|T_q}^2 )

|Q| = |G_k| whenever Q is non-empty, because Q is a coset of the little
co-group, so dividing by one or the other is the same number.

    W = +1   case (a)   corep = D          no doubling
    W = -1   case (b)   corep = D + D      DOUBLED, two copies of one irrep
    W =  0   case (c)   corep = D + D*     DOUBLED, two conjugate irreps fuse
    Q empty  type (x)   -k is not in the star of k

THE CONVENTION IS PART OF THE NUMBER.  W here is the NORMALISED indicator of
Bilbao's *Representations DSG* (Elcoro et al., J. Appl. Cryst. 50, 1457 (2017),
eq. 13), which returns +1/-1/0.  It is NOT Bradley & Cracknell eq. (7.3.48) or
Magnetic TQC's J_sigma: those are the same sum UNNORMALISED, returning
+-|G_k|, and MTQC additionally folds the spin sign sgn[chi(T^2)] inside.  A
number without its convention is not a measurement, and for double-valued
irreps the two spellings disagree in print on the (a)/(b) label -- see section 6.

TYPE (x) IS NOT A CASE (c), AND THE NORMALISED FORM HAS A DEFECT THERE.  With
Q empty the criterion reads 0/0 -- UNDEFINED, not zero -- while the
unnormalised form returns 0 and collides with case (c).  This file divides
nothing in that branch and records the status instead.  The literature names it:
MSGCorep (arXiv:2211.10740, eq. 9, Table 1) calls it TYPE (x), SpaceGroupIrep
(arXiv:2012.08871) gives it the reality code `x`, and the distinction is
physical:

    type (c)   doubled AT k: YES    doubled in the BZ: NO
    type (x)   doubled AT k: NO     doubled in the BZ: YES

===============================================================================
2. WHAT IS SEATED
===============================================================================

    3,529 COREPRESENTATIONS over kpointdex's own 870 isolated k-stars,
    over the 162 space groups that seat any.

    3,908 small representations                 the unitary answer
    3,529 corepresentations                     the physical answer
      594 case-(c) small reps fuse into 297     two irreps, one level, one k
      164 type-(x) small reps fuse into 82      two irreps at CONJUGATE k
      309 levels DOUBLED at k by time reversal  8.8 % of the member set
       86 space groups carry such a level
       42 stars are type (x), in 21 pairs       -k outside its own star

BY CASE:  3,138 case (a) | 12 case (b) | 297 case (c) | 82 type (x)

    3,908 - 297 - 82 = 3,529, and that is the whole accounting.

CASE (b) IS RARE AND IT IS NOT REDUNDANT.  Twelve levels in the whole
crystallographic catalogue double by pairing an irrep WITH ITSELF rather than
with a conjugate.  Case (c) cannot produce that, and an index that merged
(b) into (c) would lose a distinction the spectrum shows: under a
time-reversal-breaking perturbation a case-(b) level splits into two copies of
the same character, a case-(c) level into two conjugate ones.

===============================================================================
2b. A TYPE-(x) MEMBER IS SEATED ONCE, AND A FIRST VERSION SEATED IT TWICE
===============================================================================

WITHDRAWN: an earlier count of 3,611 and a by-case figure of 164 type (x).

A type-(x) corepresentation is D^{*k} + (D^{*-k})^*.  That is ONE object
spanning the star of k AND the star of -k -- and both of those stars are seated
here, because both are isolated high-symmetry stars of the same space group.  A
table with one row per (star, level) therefore names each such member TWICE,
once at each arm.  THAT IS OVER-REPRESENTATION, and it is the same fault
`phonondex` refused when it seated P-1 with TWO members rather than ITA's eight
identically contributing sites.

MEASURED, not assumed, and the derivation ASSERTS both conditions rather than
trusting them: the 42 type-(x) stars form exactly 21 CONJUGATE PAIRS, none
self-conjugate, none with an unseated partner.  So 164 rows named 82 objects.
The member is now emitted once, at the lexicographically smaller star, and the
partner is carried in the `k2` column.  849 stars appear in `k`, 21 more in
`k2`, and the union is kpointdex's 870.

AND n_small FOR TYPE (x) IS 2, NOT 1.  It contains two inequivalent small
representations, exactly as a case (c) does; the difference is only that case
(c)'s pair sits at one k and this one's at conjugate k.  The first version
counted 1, and that error had a visible cost -- it put (a) and (x) in the same
chart cell, which then had to be explained away as "a property of the star".
Counted right, the three dimension facts separate all four cases with nothing
left over and no exception to state.

===============================================================================
3. THE MEMBER SET IS kpointdex's OWN, PROVED SET-WISE
===============================================================================

This is not a new enumeration and it is not a re-seating.  The stars here are
the stars kpointdex seats, and that is MEASURED rather than assumed: the 1/12
mesh this file's derivation sweeps and `kpoint_derive.candidates`'s grid-free
Hermite-normal-form enumeration are compared AS SETS OF FRACTIONAL k-VECTORS in
the shared primitive basis, and they are IDENTICAL ON 230 OF 230 SPACE GROUPS.
Not equal in count -- equal as sets.

    A SIDE EFFECT WORTH RECORDING.  `phonon_kpoints_derive` said of its own
    mesh that it is "converged -- 1/12 and 1/24 give the same stars -- but
    converged is not proved".  Against the grid-free argument it is now PROVED,
    on every space group.  That is more than either file claimed before.

SO THE TWO INDEXES ARE AT DIFFERENT GRANULARITY OVER THE SAME GEOMETRY.
kpointdex's member is a k-star and its coordinates describe the star's whole
mode content; this file's member is one level at one star.  870 stars carry
3,529 levels.  Nothing is seated twice: `little_order`, `n_smallreps` and
`max_dim` are properties OF A STAR and stay there; `corep_dim` and the reality
type are properties OF A LEVEL and are here.

    AND ONE OF kpointdex's IS NOW WRONG AS GLOSSED.  It documents `max_dim` as
    "the largest small-rep dimension, i.e. the maximum DEGENERACY symmetry
    forces at that k".  The second clause is FALSE wherever time reversal
    doubles: measured, at 118 of its (space group, |G_k|, star) groups over 93
    space groups the true maximum degeneracy EXCEEDS `max_dim`.  The coordinate
    is right; the gloss is struck in that file.  THIS IS NOT A WARRANT FOR
    SEATING THIS INDEX -- an index justified by another file's error would
    dissolve when the error is fixed -- it is a repair the measurement forced.

===============================================================================
4. WHAT IS PROVED ABOUT THE TABLE, AND HOW
===============================================================================

FOUR INDEPENDENT VALIDATIONS.  None of them is the code checking itself.

(i) THE SIGNED SUM RULE, DERIVED RATHER THAN QUOTED.  The textbook twisted
    Frobenius-Schur rule sum_r d_r nu_r = #{a in A : a^2 = e} IS FALSE HERE,
    and that was found by measuring, not by reading: the unsigned count gives
    4 where the truth is -2 at the R point of space group 19, and 10 against 4
    at P in space group 230.  The reason is that summing the central
    extension's own twisted indicator over a central-character-zeta sector
    brings in sum_c zeta^(2c), which VANISHES for n > 2.  Derived directly from
    the omega-twisted regular character instead:

        sum_r d_r W_r  ==  sum over q in Q with R_q^2 = I of
                               exp(-2 pi i k.(R_q T_q + T_q))

    THE RIGHT-HAND SIDE TOUCHES NO CHARACTER TABLE -- it is pure space-group
    arithmetic -- which is what makes it a check and not a restatement.
    Measured: HOLDS ON ALL 828 STARS that have an antiunitary coset.

(ii) THE CASE-(c) PAIRING IS FIXED-POINT-FREE.  If a case-(c) irrep paired with
    itself the corepresentation would not exist and the member count would be
    wrong.  Every case-(c) rep has exactly one partner and never itself; every
    case-(a) and case-(b) rep is its own.  0 failures on all 828.

(iii) AGAINST AN IMPLEMENTATION SHARING NO CONVENTION.  `phonon_kpoint_derive`
    computes the same indicator in the ROW convention (k -> k R), on a
    primitive cell built by spglib's `standardize_cell` rather than by
    `hnf_basis`, through Herring's Ghat rather than through a central
    extension.  Compared over the 7 non-Gamma TRIMs of all 230 space groups --
    as MULTISETS per space group, because individual TRIM labels are
    basis-dependent while the 8 half-lattice points of the reciprocal torus are
    its 2-torsion subgroup and that set is not -- THE TWO AGREE ON 230 OF 230.

(iv) AGAINST THE PUBLISHED LITERATURE, INCLUDING ONE MEASURED SPECTRUM.

    sg 19   R          case (b), 2 -> 4    Yu et al., Sci. Bull. 67, 375 (2022),
                                           SM p.52: {R5,R5}, a charge-2 Dirac
                                           point.  X, Y, Z carry the SAME 2-dim
                                           irrep at case (a) and do not double,
                                           and U, S, T pair four 1-dim reps.
                                           One group, three verdicts.
    sg 230  P          (2,c) + (4,a)       Cai et al., Light Sci. Appl. 9, 38
                                           (2020): a 3D-printed phononic
                                           crystal, Dirac point OBSERVED at
                                           15.3 kHz.  Verbatim: "two
                                           inequivalent two-dimensional
                                           irreducible representations stuck
                                           with time-reversal symmetry", beside
                                           "a four-dimensional irreducible
                                           representation" that needs none.
                                           BOTH ROUTES GIVE FOUR-FOLD AT ONE k.
    sg 227  X          four x (2,a)        DIAMOND, and the discriminator: a
                                           16-element little group where time
                                           reversal adds NOTHING.  No level
                                           anywhere in diamond is doubled by it.
                                           A check that always says "doubled"
                                           fails here.
    sg 144  Gamma      (1,a) + (1,c)       the classic 1E / 2E pair of
    sg 76   Gamma      2x(1,a) + (1,c)     vibrational spectroscopy.

===============================================================================
5. THE COORDINATES, AND WHY THESE THREE
===============================================================================

    corep_dim      THE DEGENERACY -- how many branches sit on top of each other
    small_dim      how much of that degeneracy the UNITARY group accounts for
    n_small        how many distinct symmetry species the level contains, 1 or 2

THREE INDEPENDENT FACTS ABOUT ONE LEVEL, and none follows from the others.
`corep_dim` is what a spectrum measures.  `small_dim` is what the unitary
calculation sees, so `corep_dim / small_dim` IS THE ANTIUNITARY OBSTRUCTION,
read straight off the chart.  `n_small` separates the two ways of doubling and
the two ways of not doubling.  A degeneracy of 4 can be (4,4,1) -- the group is
non-abelian and time reversal adds nothing -- or (4,2,1) -- one 2-dim species
doubled onto itself -- or (4,2,2) -- two 2-dim species fused.  Three different
levels, kept apart.

THE THREE DETERMINE THE CASE EXACTLY, all four of them, with no exception:

    (a)  (d,  d, 1)        (b)  (2d, d, 1)
    (c)  (2d, d, 2)        (x)  (d,  d, 2)

so the case letter is carried on the member as a reader's label and is not an
axis -- kpointdex's own ruling about `star`, applied again, and here it costs
nothing at all because the axes already say it.

WITHDRAWN: `little_order` WAS A FOURTH COORDINATE AND SHOULD NOT HAVE BEEN.
It is CONSTANT ON EVERY ONE OF THE 870 STARS -- measured, 0 stars carry two
values -- so it is the star's property, not the level's, and it is already
`kpointdex.index()`'s first coordinate.  Carrying it here seats one fact in two
indexes, which is exactly the ground on which this file excludes `factor_order`
and `n_smallreps`; the first version stated that principle and then broke it.
Dropping it takes the chart from 50 cells to 13 and the cell from (0, 12, 8) to
(0, 6, 3).

WHAT IS DELIBERATELY NOT A COORDINATE.  `little_order`, `factor_order` and
`n_smallreps` are properties OF THE STAR and are kpointdex's.  `star` and
`pg_order` are excluded for kpointdex's own stated reason -- their product is
fixed by orbit-stabiliser.

===============================================================================
6. WHAT THIS FILE REFUSES
===============================================================================

**TO EXTEND TO HALF-INTEGER SPIN.**  Everything here is T^2 = +1, which is what
a phonon has.  For a spinor T^2 = -1, the antiunitary element squares into the
double group's E-bar, chi(E-bar . g) = -chi(g), and THE WHOLE SUM CHANGES SIGN,
so (a) and (b) exchange their physical readings.  Two standard references put
that sign in different places and therefore DISAGREE IN PRINT for double-valued
irreps: MTQC / MSGCorep / Bradley & Cracknell fold sgn[chi(T^2)] into the
indicator; Bilbao's *Representations DSG* reports the mathematical reality and
states the flipped physical rule separately.  Bilbao's own worked pair pins it:
the double-valued P-bar-7 of Ia-3 (206) is REAL and DOUBLES, while the
double-valued P-bar-7 of I4_132 (214) is PSEUDOREAL and does NOT.  Nothing here
may be quoted for electrons with spin-orbit coupling.

**TO EXTEND TO MAGNETIC SPACE GROUPS.**  The group is the grey group G + theta G
of a NONMAGNETIC crystal.  A magnetically ordered crystal has a different
antiunitary coset and this table says nothing about it.

**TO CLAIM A DEGENERACY IS OBSERVED.**  The table states what symmetry FORCES.
An accidental degeneracy at the same k is not symmetry's and is not here.

**TO SEAT THE LINES AND PLANES.**  kpointdex's refusal, unchanged: a symmetry
line is a one-parameter family, not a member.

**TO NAME A FREQUENCY.**  `phonondex.py` section 5, unchanged.  Symmetry fixes
the degeneracy and says nothing about where the level sits.

===============================================================================
6b. WHAT THE PASS FOUND IN THE NEIGHBOURING IMPLEMENTATION -- RECORDED
===============================================================================

`captures/phonon_kpoint_derive.py` is where the antiunitary obstruction was
first measured, and it is the file this one cross-checks against.  Its
`herring()` IS CORRECT -- attacked four independent ways and not broken, most
sharply by the spectrum route in validation (v).  FOUR FAULTS AROUND IT ARE
NOT, and none is repaired here.

  (A) `sectors()` SELECTS THE WRONG SECTOR FOR N > 2.  It keeps the rows with
      chi(z)/dim = -1, which is the physical sector only when N = 2; for N >= 3
      the sector is a PRIMITIVE N-th root.  The failure is SILENT, because
      omega = -1 is a legitimate sector whenever N is even and every sector
      satisfies sum d^2 = |P_k| -- a guard that is a genuine invariant of the
      WRONG OBJECT, which is exactly the shape of the 2-cocycle bug this tree
      already hit once.  Measured at the diamond W point, N = 4: it returns
      dims [1,1,1,1,2] where the physical sector is [2,2].  UNREACHABLE FROM
      `main()`, which calls it only at TRIMs where N = 2, so neither capture is
      wrong.  A latent trap for the next caller.

  (B) NO INTEGRALITY GUARD ON W ANYWHERE.  Both callers do
      `int(round(complex(W[i]).real))` -- discarding the imaginary part and
      rounding without checking.  Today the values are clean (|Im| <= 1.3e-14).
      It is the guard that would catch tomorrow's convention error, and it is
      the one absent, in a file emphatic about guards for multiplicities.
      THIS FILE HAS IT: a non-integral indicator raises in `one_star`.

  (C) THE CAPTURE HEADER CLAIMS A CROSS-VALIDATION THE FILE DOES NOT PERFORM.
      `PHONON-KGROUND.tsv` says "every row cross-validated against spgrep
      0.7.0" directly above columns `herring_W` and `antiunitary`; what
      `sweep()` compares is DIMENSIONS AND LITTLE-GROUP ORDER ONLY.  The
      antiunitary columns are cross-validated by nothing in the file, and the
      sentence is written unconditionally -- a machine without spgrep produces
      a capture asserting the check and a log reading "agree 0 disagree 0".
      The CLAIM is true (the missing comparison has since been made externally,
      1610 of 1610 on spgrep's own reality indicator); the FILE does not
      establish it.

  (D) `W is None` IS FLATTENED TO W = +1 BY BOTH CALLERS.  `herring()` is
      careful and returns None when Q is empty; `crystal_rows` renders it as
      case (a) and `main` records antiunitary = 0.  Two different states --
      "the criterion applies and gives +1" and "the criterion does not apply" --
      print identically, and it is live in the capture at alpha-quartz (sg 152,
      chiral) at K and at H.  A STATUS IS NEVER FLATTENED; this file seats the
      42 such stars as TYPE (x) with `in-bz` against case (a)'s `none`.

AND ONE GAP THAT IS NOT THIS INDEX'S EITHER.  `overlaprule.coords()` resolves a
seated module's axes through a COORDS table or a module-level NAMES, and RAISES
when it finds neither, "so a future index cannot go missing quietly".
`phonondex` and `kpointdex` declare neither.  So `overlaprule --selftest` fails
that fixture and `particlesweep --selftest` CRASHES OUTRIGHT with a KeyError on
`phonondex`.  MEASURED AS PRE-EXISTING, not inferred: both were run against
HEAD in a detached worktree and fail identically there, and `overlaprule`'s
five failing fixtures are the same five before and after this pass.  THIS INDEX
DECLARES `NAMES` so it does not join them.  Repairing the other two means
giving them coordinate names and re-measuring what the sub-chart sweeps then
reach, which moves other indexes' figures -- a separate pass, not this one.

===============================================================================
7. SEATED.  THE 27th REGISTERED INDEX
===============================================================================
"""
import os
import sys
import collections

SOURCE = (
    'COMPUTED end to end from the 230 crystallographic space groups. Herring\'s '
    'criterion is evaluated on the SMALL REPRESENTATIONS of each isolated '
    'high-symmetry k-star, whose projective character tables come from a '
    'central extension built by Burnside\'s class-algebra method; the k-stars '
    'are kpointdex\'s own, proved identical as SETS to its grid-free '
    'Hermite-normal-form enumeration on 230 of 230 space groups. No '
    'representation table, no corepresentation table and no k-point table is '
    'read. Bradley & Cracknell, Bilbao and the published phonon literature are '
    'used to CHECK and never to build.',
    (
        'research/warp-drive/captures/COREPS-HIGHSYM.tsv',
        'research/warp-drive/captures/corep_derive.py',
    ),
)

HERE = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(HERE, "captures")
BANK = os.path.join(CAP, "COREPS-HIGHSYM.tsv")
DERIVE = os.path.join(CAP, "corep_derive.py")
KBANK = os.path.join(CAP, "KPOINTS-HIGHSYM.tsv")

#: The coordinate names, in `index()`'s order.  `overlaprule` resolves a seated
#: module's axes through its COORDS table first and a module-level NAMES second,
#: and RAISES rather than skipping when it finds neither -- "so a future index
#: cannot go missing quietly".  phonondex and kpointdex declare neither and are
#: already caught by that fixture; this one declares NAMES so it does not join
#: them.  See section 6 for the pre-existing failure, which is recorded, not
#: repaired here.
NAMES = ("corep_dim", "small_dim", "n_small")

#: The four reality types, and where each one's doubling lives.
#: MSGCorep (arXiv:2211.10740) Table 1.  Not declared -- `doubling_table()`
#: measures it off the capture and this is what it returns.
CASES = ("a", "b", "c", "x")
DOUBLING = {"a": "none", "b": "at-k", "c": "at-k", "x": "in-bz"}


def read():
    """[(sg, system, k, k2, little_order, star, factor_order, small_dim,
        n_small, case, corep_dim, doubling)].  Stdlib only.

    `k2` is "-" except on a type-(x) member, where it names the CONJUGATE STAR
    the same corepresentation also occupies.  Section 2b."""
    out = []
    if not os.path.exists(BANK):
        return out
    with open(BANK) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if p[0] == "sg":
                continue
            out.append((int(p[0]), p[1], p[2], p[3], int(p[4]), int(p[5]),
                        int(p[6]), int(p[7]), int(p[8]), p[9], int(p[10]),
                        p[11]))
    return out


def index():
    """The seated member set, as cells.  Section 5.

    COORDINATES, and each is a quantum number of the LEVEL:

        corep_dim      the DEGENERACY -- what a spectrum measures
        small_dim      how much of it the UNITARY group accounts for, so that
                       corep_dim / small_dim IS the antiunitary obstruction
        n_small        how many distinct species fuse, 1 or 2 -- which
                       separates two copies of one character from a
                       conjugate pair

    THE CASE LETTER IS NOT A COORDINATE because the three determine it:
    (a) (d,d,1), (b) (2d,d,1), (c) (2d,d,2), (x) (d,d,2).  `little_order`,
    `n_smallreps`, `factor_order`, `star` and `pg_order` are excluded as
    properties of the STAR, which are kpointdex's."""
    return frozenset((r[10], r[7], r[8]) for r in read())


def cell_population():
    return len(read()), len(index())


#: Pinned at seating so a later change cannot move it silently.  MEASURED, and
#: measured AFTER seating: figure.py records that a resolution read against a
#: candidate that was not the one seated is not a reading of the index at all.
SEATED_CELL = (0, 6, 3)


# ------------------------------------------------------------ the measurements
def by_case():
    """{case: count of corepresentations}."""
    return dict(collections.Counter(r[9] for r in read()))


def _by_star():
    """{(sg, k): {little_order}} -- it is one value on every star.  Section 5."""
    out = collections.defaultdict(set)
    for r in read():
        out[(r[0], r[2])].add(r[4])
    return dict(out)


def _cells_by_case():
    """{cell: {case}} -- which reality types share a cell.  Section 5."""
    out = collections.defaultdict(set)
    for r in read():
        out[(r[10], r[7], r[8])].add(r[9])
    return dict(out)


def doubling_table():
    """{case: {doubling}} -- MEASURED off the capture, never declared."""
    out = collections.defaultdict(set)
    for r in read():
        out[r[9]].add(r[11])
    return {k: sorted(v) for k, v in sorted(out.items())}


def doubled():
    """The levels time reversal doubles AT k.  Invisible to the unitary pass."""
    return [r for r in read() if r[11] == "at-k"]


def type_x():
    """The levels whose star does not contain -k: doubled in the BZ, not at k."""
    return [r for r in read() if r[9] == "x"]


def stars():
    """{(sg, k)} -- the member set this index sits on."""
    return ({(r[0], r[2]) for r in read()}
            | {(r[0], r[3]) for r in read() if r[3] != "-"})


def small_rep_total():
    """How many SMALL representations the 3,529 corepresentations were built
    from.  Cases (c) and (x) each fuse two, so this is strictly larger."""
    return sum(r[8] for r in read())


def spacegroups_touched():
    """[sg] carrying at least one level doubled at k by time reversal."""
    return sorted({r[0] for r in doubled()})


def mechanism_split():
    """(antiunitary only, projective only, both, neither) over the SEATED STARS.

    THIS IS NOT THE 126/108/56 FIGURE and must not be quoted as it.  That one
    is over the 7 non-Gamma TRIMs of ALL 230 space groups, seated or not, and
    lives in `captures/PHONON-KGROUND.tsv`.  This one is over the 870 ISOLATED
    HIGH-SYMMETRY STARS, which is a different population -- most TRIMs are not
    isolated, and most isolated stars are not TRIMs.  Two measurements of two
    things, kept apart.
    """
    A = {r[0] for r in doubled()}
    P = set()
    for r in _kread():
        if r[1] > 1:
            P.add(r[0])
    S = {r[0] for r in read()}
    return (len(A - P), len(P - A), len(A & P), len(S - A - P))


def _kread():
    """[(sg, m, little_order, k)] from kpointdex's capture.  Stdlib only."""
    out = []
    if not os.path.exists(KBANK):
        return out
    with open(KBANK) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if p[0] == "sg":
                continue
            out.append((int(p[0]), int(p[7]), int(p[6]), p[4]))
    return out


def against_kpointdex():
    """(stars here, stars there, space groups whose (|G_k|, star) multisets
    agree, space groups compared, levels, small reps).

    THE TWO INDEXES SIT ON THE SAME STARS, AND THE JOIN IS NOT ON THE LABEL.
    See `label_disagreement`: a star is labelled by one of its own arms and the
    two derivations do not always pick the same arm.  What is compared here is
    label-free -- the multiset of (little-group order, star size) per space
    group, one entry per STAR on both sides, which is stdlib-visible.  The
    set-wise identity of the stars themselves needs the point group to expand
    them and so is proved in the derivation, which has numpy: `corep_derive`
    reports 230 of 230.
    """
    import collections as _c
    MA, MB = _c.defaultdict(list), _c.defaultdict(list)
    seen = set()
    for r in read():
        # both arms of a type-(x) member are stars; the conjugate carries the
        # same little-group order and star size, being the image of it under -1
        for lab in (r[2], r[3]):
            if lab == "-" or (r[0], lab) in seen:
                continue
            seen.add((r[0], lab))
            MA[r[0]].append((r[4], r[5]))
    for sg, lo, st in _kpairs():
        MB[sg].append((lo, st))
    keys = set(MA) | set(MB)
    agree = sum(1 for kk in keys
                if sorted(MA.get(kk, [])) == sorted(MB.get(kk, [])))
    return (len(stars()), len(_kpairs()), agree, len(keys), len(read()),
            small_rep_total())


def _kpairs():
    """[(sg, little_order, star)] -- one row per kpointdex star."""
    out = []
    if not os.path.exists(KBANK):
        return out
    with open(KBANK) as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if p[0] == "sg":
                continue
            out.append((int(p[0]), int(p[6]), int(p[5])))
    return out


def label_disagreement():
    """(labels in common, stars here, stars there).

    A RECORDED FINDING, NOT A FAULT IN EITHER FILE.  Both captures label a star
    by one of its own arms, and they do not always pick the same arm: this file
    takes the LEXICOGRAPHIC MINIMUM of the star, which is canonical and
    reproducible by construction, while `kpoint_derive` keeps whichever
    representative its candidate set yielded first, which is an iteration order.
    703 of the 870 labels coincide; the other 167 name the same star by a
    different arm.  Joining the two captures on (sg, k) therefore UNDERCOUNTS,
    and nothing downstream should do it -- join on (sg, |G_k|, star) instead,
    or expand the star.  Recorded rather than repaired: canonicalising
    kpointdex's column would rewrite a seated capture.
    """
    mine = stars()
    theirs = {(r[0], r[3]) for r in _kread()}
    return (len(mine & theirs), len(mine), len(theirs))


def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    rows = read()
    if not rows:
        print("   (no capture -- run `python3 corepdex.py --derive`)")
        return
    print("=" * 74)
    print("THE INDEX AS SEATED")
    print("=" * 74)
    print("   members (corepresentations)     %d" % len(rows))
    print("   the stars they sit on           %d" % len(stars()))
    print("   space groups                    %d" % len({r[0] for r in rows}))
    print("   small representations behind    %d" % small_rep_total())
    print("   distinct chart cells            %d" % len(index()))
    print()
    bc = by_case()
    print("   by reality type")
    for c in CASES:
        print("      (%s)  %-34s %5d" % (
            c, {"a": "real, no doubling",
                "b": "pseudoreal, DOUBLED at k",
                "c": "complex pair, DOUBLED at k",
                "x": "-k outside the star, doubled in BZ"}[c], bc.get(c, 0)))
    print()
    d = doubled()
    print("   LEVELS DOUBLED AT k BY TIME REVERSAL   %d   (%.1f%%)"
          % (len(d), 100.0 * len(d) / len(rows)))
    print("   space groups carrying one              %d"
          % len(spacegroups_touched()))
    print("   type (x) levels                        %d  in %d stars"
          % (len(type_x()), len({(r[0], r[2]) for r in type_x()})))
    print()
    print("   degeneracy spectrum")
    for dim, n in sorted(collections.Counter(r[9] for r in rows).items()):
        print("      %2d-fold  %5d" % (dim, n))
    print()
    print("=" * 74)
    print("AGAINST kpointdex -- THE SAME STARS, A FINER MEMBER")
    print("=" * 74)
    a = against_kpointdex()
    print("   stars here / there              %d / %d" % a[:2])
    print("   space groups whose (|G_k|, star) multisets agree   %d of %d"
          % a[2:4])
    print("   levels on them                  %d" % a[4])
    print("   small representations           %d" % a[5])
    print("   fused by time reversal          %d small reps -> %d levels"
          % (2 * len([r for r in rows if r[7] == 2]),
             len([r for r in rows if r[7] == 2])))
    lc, lm, lt = label_disagreement()
    print()
    print("   star LABELS in common           %d of %d   -- see "
          "label_disagreement" % (lc, lm))
    print()
    ao, po, both, none = mechanism_split()
    print("   over the SEATED STARS, by which obstruction bites")
    print("      antiunitary only   %3d space groups" % ao)
    print("      projective only    %3d" % po)
    print("      both               %3d" % both)
    print("      neither            %3d" % none)
    print()
    print("   (the 126 / 108 / 56 figure is a DIFFERENT population -- the 7")
    print("    non-Gamma TRIMs of all 230 groups.  See mechanism_split.)")


def selftest():
    fails = []

    def chk(name, got, want):
        ok = got == want
        if not ok:
            fails.append(name)
        print("   %-64s %s" % (name, "ok" if ok else
                               "FAIL got %r want %r" % (got, want)))

    rows = read()
    chk("the capture is present", bool(rows), True)
    if not rows:
        print("\n%d failure(s)" % len(fails) if fails else "")
        return 1

    # -- the member set
    chk("3,529 corepresentations are seated", len(rows), 3529)
    chk("on 870 stars -- kpointdex's own", len(stars()), 870)
    chk("849 of them named in k, 21 more only in k2",
        (len({(r[0], r[2]) for r in rows}),
         len({(r[0], r[3]) for r in rows if r[3] != "-"})), (849, 21))
    chk("over the 162 space groups that seat a star",
        len({r[0] for r in rows}), 162)
    chk("built from 3,908 small representations", small_rep_total(), 3908)

    # -- the obstruction
    bc = by_case()
    chk("by reality type: 3,138 (a), 12 (b), 297 (c), 82 (x)",
        (bc["a"], bc["b"], bc["c"], bc["x"]), (3138, 12, 297, 82))
    chk("309 LEVELS ARE DOUBLED AT k BY TIME REVERSAL", len(doubled()), 309)
    chk("and 309 = 12 case (b) + 297 case (c)",
        len(doubled()), bc["b"] + bc["c"])
    chk("86 space groups carry one", len(spacegroups_touched()), 86)
    chk("the whole accounting: 3,908 - 297 - 82 = 3,529",
        small_rep_total() - bc["c"] - bc["x"], len(rows))

    # -- type (x) is seated ONCE, and is not a case (c).  Section 2b.
    chk("82 type-(x) members over 21 conjugate star pairs",
        (len(type_x()), len({(r[0], r[2]) for r in type_x()}),
         len({(r[0], r[3]) for r in type_x()})), (82, 21, 21))
    chk("only type (x) carries a second star label",
        sorted({r[9] for r in rows if r[3] != "-"}), ["x"])
    chk("no type-(x) member names its own star twice",
        [r for r in type_x() if r[2] == r[3]], [])
    chk("no type (x) level is doubled AT k",
        sorted({r[11] for r in type_x()}), ["in-bz"])
    chk("and none of them has corep_dim above its small_dim",
        [r for r in type_x() if r[10] != r[7]], [])

    # -- MSGCorep Table 1, measured off the capture rather than declared
    chk("each case doubles in exactly one place -- MSGCorep Table 1",
        doubling_table(),
        {"a": ["none"], "b": ["at-k"], "c": ["at-k"], "x": ["in-bz"]})
    chk("and the table the module states agrees with the capture",
        {c: DOUBLING[c] for c in CASES},
        {c: v[0] for c, v in doubling_table().items()})

    # -- the arithmetic of a corep
    chk("every level's degeneracy is its small_dim or twice it",
        sorted({r[10] // r[7] for r in rows}), [1, 2])
    chk("doubled at k is exactly where they differ",
        all((r[11] == "at-k") == (r[10] != r[7]) for r in rows), True)
    chk("(c) and (x) contain two small reps, (a) and (b) one",
        sorted({(r[9], r[8]) for r in rows}),
        [("a", 1), ("b", 1), ("c", 2), ("x", 2)])

    # -- the published rows.  Not self-consistency: someone else's numbers.
    def at(sg, order=None, case=None):
        return sorted((r[7], r[9], r[10]) for r in rows
                      if r[0] == sg and (order is None or r[4] == order)
                      and (case is None or r[9] == case))
    chk("sg19 carries case (b) exactly once -- the charge-2 Dirac point at R",
        at(19, 4, "b"), [(2, "b", 4)])
    chk("while X, Y and Z carry the SAME 2-dim irrep undoubled",
        [x for x in at(19, 4, "a") if x[0] == 2],
        [(2, "a", 2), (2, "a", 2), (2, "a", 2)])
    chk("sg230 at |G_k| = 24 is the MEASURED Dirac point: a case-(c) pair and "
        "a 4-dim case (a), both 4-fold", at(230, 24),
        [(2, "c", 4), (4, "a", 4)])
    chk("diamond at |G_k| = 16 (X) is four 2-fold levels, none doubled",
        at(227, 16), [(2, "a", 2)] * 4)
    chk("NO level anywhere in diamond is doubled by time reversal",
        sorted({r[11] for r in rows if r[0] == 227}), ["none"])

    # -- the chart
    import mi
    chk("its own cell is the one pinned at seating", mi.cell(index()),
        SEATED_CELL)
    chk("13 distinct cells", len(index()), 13)
    chk("and every cell is a 3-tuple", {len(c) for c in index()}, {3})
    chk("the chart reads the obstruction off directly -- corep_dim/small_dim",
        sorted({c[0] // c[1] for c in index()}), [1, 2])
    chk("THE THREE COORDINATES DETERMINE THE CASE, all four, no exception",
        len({(r[10], r[7], r[8], r[9]) for r in rows}), len(index()))
    chk("little-group orders divide the crystallographic orders",
        [r for r in rows if r[4] not in
         (1, 2, 3, 4, 6, 8, 12, 16, 24, 48)], [])
    chk("little_order is CONSTANT on every star, which is why it is not an "
        "axis -- section 5",
        sum(1 for v in _by_star().values() if len(v) > 1), 0)

    # -- it sits on kpointdex, it does not re-seat it
    a = against_kpointdex()
    chk("870 stars here and 870 there", (a[0], a[1]), (870, 870))
    chk("and their (|G_k|, star) multisets agree in EVERY space group",
        (a[2], a[3]), (162, 162))
    chk("this index has MORE members, because a star is not a level",
        a[4] > a[1], True)

    # -- the derivation travels with the capture
    chk("it declares its coordinate NAMES, so overlaprule can resolve it",
        (NAMES, len(NAMES)),
        (("corep_dim", "small_dim", "n_small"), len(next(iter(index())))))
    chk("the derivation is banked beside the capture",
        os.path.exists(DERIVE), True)
    chk("it IMPORTS rather than copies",
        all(s in open(DERIVE, encoding="utf-8").read()
            for s in ("from phonon_derive import",
                      "import phonon_kpoints_derive")), True)

    print("\n%d failure(s)" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--derive" in sys.argv:
        sys.path.insert(0, CAP)
        import corep_derive
        corep_derive.main()
        sys.exit(0)
    report()
