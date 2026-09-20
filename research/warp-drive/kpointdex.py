#!/usr/bin/env python3
r"""
kpointdex.py -- THE k-POINT INDEX.  870 HIGH-SYMMETRY k-STARS OVER ALL 230
SPACE GROUPS, WITH THEIR SMALL REPRESENTATIONS -- INCLUDING THE PROJECTIVE
ONES phonondex.py REFUSED TO COMPUTE.

    python3 kpointdex.py             the reading
    python3 kpointdex.py --selftest  fixtures, stdlib only
    python3 kpointdex.py --derive    recompute the captures (numpy+spglib, z3)

`phonondex.py` section 5 refused k != Gamma and named the obstruction:

    "At a general k the little group's representations are PROJECTIVE for
     non-symmorphic groups, which is a different computation and is not done
     here."

THE REFUSAL IS DISCHARGED, NOT WAIVED.  The computation is done, the
multiplier is decided rather than guessed, and 305 of the 870 members carry a
NON-TRIVIAL one -- so the obstruction was real and it is now behind us.

    members            870 isolated k-stars
    space groups       162 of 230 carry one; 68 carry NONE, and those 68 are
                       exactly the ten polar crystal classes -- measured
    projective         305 members (35.1%) have a non-trivial multiplier
    coordinates        little-group order, number of small reps, maximum
                       small-rep dimension
    distinct cells     21

===============================================================================
1. THE RECIPROCAL-SPACE ANALOGUE, AND THE ONE PLACE IT IS NOT AN ANALOGUE
===============================================================================

`phonondex.py` found site-symmetry types as POINT STABILISERS on a 1/12
rational grid in direct space, grouped by conjugacy.  The reciprocal analogue
is immediate and it works:

    the point group acts on k as {(R^-1)^T}, integral in the primitive
    RECIPROCAL basis, and the little co-group is the stabiliser of k

and "k is defined modulo a reciprocal lattice vector" is NOT a new difficulty.
It is the same `% 1` the direct-space version already used for positions
modulo a lattice translation, and it is correct only because the basis is
PRIMITIVE -- which `phonon_derive.primitive_ops` already had to establish for
the Gamma computation.  In a conventional centred basis it would be wrong.

**WHAT THE GRID METHOD ACTUALLY ENUMERATES IS NOT THE HIGH-SYMMETRY POINTS.**
The stabiliser of k is constant along a whole line or plane of k -- the
symmetry LINES and PLANES -- and the grid reports those on exactly the same
footing.  For Fm-3m the 1/12 grid finds TWELVE stabiliser types where there
are FOUR high-symmetry points.  The missing ingredient is a dimension:

    k is a high-symmetry POINT  iff  rank[R - I : R in G_k] = 3,

i.e. the fixed-point set of its own stabiliser is 0-dimensional.  That test is
grid-free, exact, and it is what separates a point from the line it sits on.

**AND ONCE THE TEST IS WRITTEN DOWN, THE GRID CAN BE THROWN AWAY.**  Rank
grows by at least one per element added, so some subset A of G_k with |A| <= 3
already reaches rank 3; then k lies in

    L_A = {k : (R - I) k in Z^3 for all R in A},

a lattice containing Z^3 with finite index, enumerated exactly by Hermite
normal form.  Sweeping every subset of the point group of size <= 3 with rank
3 therefore yields a FINITE, PROVABLY COMPLETE superset of the high-symmetry
points, with no grid and no convergence question.  Section 2 reports the grid
anyway, because the question was asked and a grid-dependent answer would have
been a red flag.

===============================================================================
2. THE GRID CONVERGES, AND THE EXACT METHOD SAYS WHY
===============================================================================

Measured on the holohedral space group of each of the 14 Bravais lattices,
1/12 against 1/24 against the exact enumeration -- `KPOINTS-GRID.tsv`:

    every lattice   1/12 stabiliser types  =  1/24 stabiliser types
    every lattice   1/12 isolated stars    =  1/24 isolated stars
                                           =  the exact enumeration

**IT IS NOT A COINCIDENCE AND IT IS NOT LUCK.**  The exact sweep measures
every coordinate of every high-symmetry point over all 230 space groups, and
the denominators that occur are 1, 2, 3 and 4 -- nothing else.  lcm(1,2,3,4)
is 12, so a 1/12 grid is EXACTLY sufficient and any finer grid must agree.
The figure is measured, not assumed: `MAX_DENOMINATOR` below is 4.

===============================================================================
3. THE CROSS-CHECK, AND THE TWO POINTS IT DOES NOT FIND
===============================================================================

Setyawan & Curtarolo (2010), Comput. Mater. Sci. 49, 299, used ONLY to check.
Their coordinates enter as Cartesian vectors in units of 2 pi / a, which is
convention-free, and are pushed into whatever primitive basis this tree's own
`hnf_basis` happened to build:

    lattice   their points               found   little-group orders
    sc        Gamma, X, M, R              4/4    48, 16, 16, 48   all exact
    bcc       Gamma, H, P, N              4/4    48, 48, 24,  8   all exact
    fcc       Gamma, X, L, W, K, U        4/6    48, 16, 12,  8   all exact

**THE TWO MISSES ARE A FINDING ABOUT THE TABLE, NOT A HOLE IN THE METHOD.**
K and U in the fcc list are

    (a)  THE SAME STAR -- measured: star(K) == star(U), so the six named
         points are five k-vectors up to symmetry; and
    (b)  NOT ISOLATED -- their common stabiliser has order 4 and its fixed
         space is 1-DIMENSIONAL.  They lie ON a symmetry line, at the place
         where that line leaves the Brillouin zone.

That place is a property of the WIGNER-SEITZ CELL, not of the space group: it
moves if you choose a different fundamental domain, and no symmetry operation
distinguishes it from its neighbours along the line.  Setyawan & Curtarolo
list it because a band-structure PATH has to turn somewhere.  This index is
not a path, so it does not seat a point whose only distinction is geometric.
**Recorded as a difference in what is being enumerated, and not repaired.**

===============================================================================
4. THE PROJECTIVE OBSTRUCTION, DISCHARGED TWO WAYS
===============================================================================

With D^k({R|t}) = exp(-2 pi i k.t) Gamma(R), the small reps obey

    Gamma(R1) Gamma(R2) = omega(R1,R2) Gamma(R1 R2),
    omega(R1,R2) = exp(2 pi i K1 . t2),   K1 = k - R1^T k,

and K1 is a reciprocal LATTICE vector exactly because R1 is in the little
co-group.  The multiplier is trivial when the group is symmorphic (every
t = 0) or when no umklapp occurs (every K1 = 0), and otherwise it is not.

**IT IS MADE ORDINARY BY A CENTRAL EXTENSION.**  Let m be the order of the
omega values.  Then

    (R1,j1)(R2,j2) = (R1 R2, j1 + j2 + w(R1,R2) mod m)

is an ordinary finite group of order m|H|, and the irreps in which the central
element (E,1) acts as exp(2 pi i / m) are exactly the omega-projective irreps
of H.  Its character table comes from the SAME Burnside class-algebra method
`phonon_derive` already uses at Gamma, generalised from 3x3 matrices to an
abstract multiplication table.  Nothing is copied and no projective table is
read.

**AND WHETHER THE MULTIPLIER IS TRIVIAL IS DECIDED, NOT INFERRED.**
omega = delta(mu) forces |mu| = 1 and mu(a)^|H| = prod_b omega(a,b), so mu is
valued in the (m|H|)-th roots of unity and the question is a linear system
over Z_{m|H|}.  z3 decides it.  Independently, the small-rep dimensions are
compared with the ordinary irrep dimensions of the same co-group.

    THE TWO TESTS AGREE ON ALL 870 MEMBERS.  Zero disagreements.

It reproduces the physics it should.  Diamond, Fd-3m:

    k          |G_k|   m   small-rep dims        ordinary dims
    Gamma       48     1   1,1,1,1,2,2,3,3,3,3   same              free
    X           16     2   2,2,2,2               1x8, 2,2          STUCK
    L           12     4   1,1,1,1,2,2           same              free
    W            8     4   2,2                   1,1,1,1,2         STUCK

X and W are the textbook non-symmorphic sticking of the diamond structure --
every branch doubly degenerate -- and L is free even though m = 4 there,
because that multiplier is a coboundary.  **m IS NOT THE ANSWER; THE
COHOMOLOGY CLASS IS, AND THEY DIFFER.**  Pnma sticks at six of its eight
high-symmetry points and is free at the other two.

===============================================================================
4a. IT WAS BUILT TWICE, IN PARALLEL, AND THE TWO AGREE
===============================================================================

A SECOND IMPLEMENTATION OF THE SAME 870 MEMBERS WAS BUILT ALONGSIDE THIS ONE,
by a different route -- its own reciprocal reduction, the opposite sign
convention for the factor system, its own Burnside search -- and banked as
`captures/PHONON-KPOINTS.tsv`.  They share no code.  **This is not a duplicate
to be merged; it is a replication, and it is compared.**

    both find                        870 members over 162 space groups
    little-group ORDER multiset      agrees in ALL 162 space groups
    small-rep DIMENSION multiset     agrees in ALL 153 space groups where
                                     the other derivation resolved every row

**THE OTHER DERIVATION LEAVES 18 ROWS UNRESOLVED**, in nine cubic
non-symmorphic groups -- 198, 199, 205, 206, 212, 213, 214, 220, 230.  **THAT
WAS A BUG IN IT, NOT A HARD CASE, AND IT IS NOW CLOSED.**  Its multiplier
g = R^{-T}k - k is a reciprocal lattice vector but NOT A 2-COCYCLE (deviation
exactly 1/2), so its extension was not a group and Burnside was right to refuse
it.  Corrected to K = k - R^T k -- this file's own convention, an exact cocycle
-- it resolves all 870.  Section 5a records the withdrawal in full, including
that a deterministic Dixon-Schneider routine written to "fix the convergence"
failed identically, which is what located the bug.

**FOUR SPACE GROUPS STILL DIFFER ON THE ORDER OF THE MULTIPLIER'S VALUES** --
178, 179, 180 and 181, the hexagonal screw groups, at one star each -- and that
one IS a gauge choice, not an error.  omega is fixed only up to a coboundary, so
the ORDER OF ITS VALUES IS NOT AN INVARIANT; the cohomology class is, and the
two agree on the class everywhere.  At 180 and 181 this file's z3 test already
reports the multiplier a COBOUNDARY, and the other file's n = 1 confirms it
without a solver by landing in a gauge where omega is identically 1.
Dimensions, little groups, stars and sum d^2 = |G_k| match at all four.
`cross_check` keyed on (sg, |G_k|, star) finds **314 of 314**, and
`cross_check_free` per space group finds **162 of 162**.  **Recorded as a
difference in what is counted, and not repaired in either file.**

===============================================================================
5. THE MEMBER SET, AND WHY IT IS NOT (space group, k, site)
===============================================================================

At Gamma the member is (space group, SITE-SYMMETRY TYPE) and a material's
content is the SUM over its occupied orbits.  Two questions have to be asked
before that survives to k != 0, and they have DIFFERENT ANSWERS.

**(i) DO ORBIT CONTRIBUTIONS STILL ADD?  YES, at every k.**  The character is
a sum over atoms mapped to themselves, orbits are disjoint and invariant, so
the representation is block diagonal by orbit.  Verified numerically as well
as argued.

**(ii) IS AN ORBIT'S CONTRIBUTION A FUNCTION OF ITS SITE-SYMMETRY TYPE?  NO.**
The phase exp(-2 pi i k.v), v = Rx + t - x, depends on the site's POSITION and
not on its stabiliser.  Measured in `KPOINTS-ADDITIVITY.tsv`:

    P-1, eight inversion centres -- ONE member in phonondex, because at Gamma
    all eight contribute identically.  At k = (1/2,0,0) they SPLIT 4/4, the
    four with 2k.x odd landing on the opposite irrep.

    Pmmm, eight sites of symmetry mmm -- identical at Gamma, and at the same
    k they split 4/4 onto a disjoint set of irreps.

    P4/mmm reproduces it a third time -- and REFINES it.  Its eight
    half-integer sites fall in two types there; the four of site order 16
    are single-atom orbits and they split, the four of order 8 are TWO-atom
    orbits and they do NOT.  A multi-point orbit can carry both phases and
    average them away.  **The failure is therefore not universal, and it
    does not have to be:** one counterexample destroys a generating table,
    and there are three space groups' worth here.

**SO THERE IS NO GENERATING TABLE AT (space group, k, site TYPE).**  It would
have to be (space group, k, WYCKOFF ORBIT), and that is the over-representation
`phonondex.py` section 1 refused at Gamma, now multiplied by k:

    (sg, k-star, phonondex site type)   5,027   and WRONG -- it does not
                                                determine the contribution
    (sg, k-star, Wyckoff orbit)         7,666   right, and over-represented
    (sg, k-star)                          870   SEATED

**THE MEMBER IS (space group, k-star), AND IT CARRIES A LABEL SPECTRUM RATHER
THAN A DECOMPOSITION.**  A decomposition at k is the material's; the set of
symmetry species AVAILABLE at k is the space group's, and that is what an
index of the host can hold.

**ONE COARSENING WAS MEASURED AND THEN REFUSED, WITH A REASON.**  Grouping
k-stars the way phonondex groups sites -- conjugate little co-group AND
cohomologous multiplier, both decided by z3 -- merges 870 down to 485.  Pm-3m
would seat two members instead of four, Gamma merging with R and X with M.
**That merge is NOT taken, and the asymmetry with Gamma has a reason:**

    at Gamma every mode has k = 0, so a site's position is not a quantum
    number of the mode and merging sites flattens nothing.  At k != 0 the
    CRYSTAL MOMENTUM IS THE MODE'S OWN QUANTUM NUMBER.  Merging two stars
    would flatten it, and `registry.enforce()` exists to stop exactly that.

485 is recorded as the measured symmetry-content coarsening; 870 is seated.

===============================================================================
5a. THE SECOND IMPLEMENTATION, AND THE BUG IT TOOK TO FIND
===============================================================================

`captures/PHONON-KPOINTS.tsv` is an INDEPENDENT computation of the same object,
written separately with its own enumeration, central extension and Burnside
pass.  It is kept because a cross-check that is thrown away is not a
cross-check -- and here it earned its keep by being WRONG in a way that was
worth finding.

**THREE CLAIMS MADE ABOUT IT ARE WITHDRAWN.**  An earlier version of this
section, and commit a4175cb, reported that it left EIGHTEEN members UNRESOLVED
because "Burnside's randomised eigenvector search does not converge" for nine
cubic non-symmorphic groups, and that the remedy was a deterministic
Dixon-Schneider simultaneous diagonalisation.  All three are false:

  1.  IT WAS NOT A CONVERGENCE FAILURE.  That implementation used the multiplier
      g = R1^{-T} k - k.  For R1 in the little group that IS a reciprocal
      lattice vector, which is why it survived every check put on it -- but it
      is NOT A 2-COCYCLE.  Tested against
          phi(a,b) + phi(ab,c) == phi(b,c) + phi(a,bc)   (mod 1)
      it deviates by exactly 1/2, so the group it built was not a group:
      associativity failed and elements lacked inverses, measured directly.
      Burnside was correctly refusing malformed input.

  2.  DIXON-SCHNEIDER WAS NOT THE REMEDY.  It was written, and it failed
      identically -- recovering FEWER IRREPS THAN CONJUGACY CLASSES, which is
      impossible for a finite group and is what finally located the bug.  No
      amount of determinism fixes a non-group.

  3.  "NEITHER IMPLEMENTATION IS ADOPTED" GAVE A BROKEN MULTIPLIER EQUAL
      STANDING WITH A CORRECT ONE.  This file's K1 = k - R1^T k is an EXACT
      cocycle (deviation 0, tested at sg199, sg212, sg230).  It was right; the
      cross-check was wrong.

**CORRECTED, THE TWO NOW AGREE ON EVERY PHYSICAL QUANTITY.**

    members                          870 and 870
    UNRESOLVED                       0 and 0
    (space group, |G_k|, star)       IDENTICAL multisets
    dimension buckets                314 of 314 AGREE -- all of them
    sum d^2 = |G_k|                  holds on every row of both
    diamond at |G_k| = 16            2+2+2+2 from both

A FIGURE PREVIOUSLY REPORTED HERE IS ALSO WITHDRAWN.  This section once said
"445 of 447 buckets agree".  That came from keying the comparison bucket on the
MULTIPLIER'S ORDER -- the one quantity the two are known to report differently
-- so wherever they disagreed the keys failed to intersect and those rows fell
OUT of the comparison rather than into it.  Keyed on (space group, |G_k|, star)
instead, which is what a bucket should be, the agreement is TOTAL: 314 of 314.
`cross_check()` now measures it that way and returns the multiplier difference
separately.

**THE ONE REMAINING DIFFERENCE IS A GAUGE CHOICE, AND IT CORROBORATES.**  At
four hexagonal screw groups -- 178 (P6_122), 179 (P6_522), 180 (P6_222) and
181 (P6_422) -- and at ONE star in each, k = (1/2, 1/2, 1/2) with |G_k| = 4 and
3 arms, the reported multiplier order differs by exactly a factor of three:

    sg 178, 179     this file  m = 6      the other  n = 2    dims 2 both
    sg 180, 181     this file  m = 3      the other  n = 1    dims 1+1+1+1 both

Every other bucket in those four groups -- |G_k| = 12 at Gamma and at
(0,0,1/2), |G_k| = 6 at (1/3,1/3,1/2) -- agrees exactly, m for m.

THE ORDER OF omega'S VALUES IS NOT AN INVARIANT.  omega is fixed only up to a
coboundary: rescaling Gamma(R) -> lambda(R) Gamma(R) multiplies omega(R1,R2) by
lambda(R1) lambda(R2) / lambda(R1 R2), which can change the ORDER of the values
while leaving the cohomology class untouched.  The class is the invariant, and
the two agree on it everywhere:

  *  At 180 and 181 this file's z3 test already reports
     `nontrivial_multiplier = 0` -- the multiplier is a COBOUNDARY.  The other
     implementation's n = 1 says the same thing in the sharpest available form:
     it landed in a gauge where omega is identically 1.  The disagreement is a
     SECOND, INDEPENDENT CONFIRMATION of the coboundary verdict, reached without
     a solver.
  *  At 178 and 179 the class is nontrivial on both sides -- this file's
     `nontrivial_multiplier = 1`, the other's n = 2 > 1 -- and both return the
     single 2-dimensional small rep that a nontrivial class forces.

So the two differ on a gauge-dependent number and agree on every gauge-invariant
one.  RECORDED AS A DIFFERENCE IN WHAT IS BEING COUNTED, and neither is changed
to match the other.

**THE SECOND IMPLEMENTATION IS BANKED.**  `captures/phonon_kpoints_derive.py`
rebuilds `captures/PHONON-KPOINTS.tsv` and carries its own `--selftest`,
including the cocycle test above at sg199, sg212 and sg230 and a direct group-
axiom test on every extension it builds.  It was not banked when the capture was
first seated, and banking it is what surfaced the bug: the repository held the
numbers and not the route to them.

`cross_check()` reports the comparison.

===============================================================================
6. WHAT THIS FILE REFUSES
===============================================================================

**TO SEAT THE SYMMETRY LINES AND PLANES.**  They are found -- the grid reports
12 stabiliser types for fcc against 4 points -- and they are real objects with
their own small reps.  They are not seated because a line is not a member: it
is a one-parameter family, and its label set is constant along it.  Named as
open.

**TO CLAIM A MATERIAL'S DECOMPOSITION AT k.**  Section 5(ii).  It needs the
Wyckoff positions, which this tree does not read; `mech_decomp` in the
derivation computes one on demand from coordinates a caller supplies, and
nothing is banked from it beyond the additivity measurement.

**TO CALL m THE ANSWER.**  m is the order of the multiplier's values; the
cohomology class is what decides sticking, and diamond's L point has m = 4 and
no sticking.  Both are banked, separately.

**TO TRUST spgrep.**  spgrep 0.7.0 is installed here and returns a little
group of 2 operations at EVERY k for Fd-3m, where X has 16.  It is not used,
and this file's answers do not depend on it being fixed.  Not a finding about
spgrep in general -- a finding about this input, recorded.

**TO CLAIM FREQUENCIES.**  `phonondex.py` section 5, unchanged.

===============================================================================
7. SEATED.  THE 26th REGISTERED INDEX
===============================================================================

`registry.py` carries it as the twenty-sixth row.  Its members carry quantum
numbers -- crystal momentum by star, and the small-rep spectrum -- so
`enforce()` accepts it.
"""

import os
import sys

SOURCE = (
    'COMPUTED end to end from the 230 crystallographic space groups. The '
    'high-symmetry k-points are enumerated GRID-FREE as the 0-dimensional '
    'strata of the stabiliser stratification of the Brillouin torus, exactly '
    'by Hermite normal form; the little groups\' PROJECTIVE small '
    'representations come from a central extension whose ordinary character '
    'table is built by Burnside\'s class-algebra method, and whether each '
    'multiplier is a coboundary is DECIDED by z3. No k-point table and no '
    'representation table is read. Setyawan & Curtarolo (2010) is used to '
    'check and never to build.',
    (
        'research/warp-drive/captures/KPOINTS-HIGHSYM.tsv',
        'research/warp-drive/captures/KPOINTS-CHECK.tsv',
        'research/warp-drive/captures/KPOINTS-GRID.tsv',
        'research/warp-drive/captures/KPOINTS-ADDITIVITY.tsv',
        'research/warp-drive/captures/kpoint_derive.py',
    ),
)

HERE = os.path.dirname(os.path.abspath(__file__))
CAP = os.path.join(HERE, "captures")
BANK = os.path.join(CAP, "KPOINTS-HIGHSYM.tsv")
CHECK = os.path.join(CAP, "KPOINTS-CHECK.tsv")
GRID = os.path.join(CAP, "KPOINTS-GRID.tsv")
ADD = os.path.join(CAP, "KPOINTS-ADDITIVITY.tsv")
DERIVE = os.path.join(CAP, "kpoint_derive.py")

#: The 14 Bravais lattices, as this tree spells them.
BRAVAIS = ("aP", "mP", "mS", "oP", "oS", "oF", "oI",
           "tP", "tI", "hR", "hP", "cP", "cF", "cI")

SYSTEMS = ("triclinic", "monoclinic", "orthorhombic", "tetragonal",
           "trigonal", "hexagonal", "cubic")

#: The ten POLAR crystal classes.  Not declared -- `polar_classes()` measures
#: the point groups of the space groups that seat no high-symmetry point at
#: all, and this is what that measurement returns.
POLAR = ("1", "2", "3", "3m", "4", "4mm", "6", "6mm", "m", "mm2")

#: Measured over all 870 members: the denominators that occur in a
#: high-symmetry k-point's coordinates.  lcm = 12, which is why the 1/12 grid
#: is exactly sufficient and 1/24 cannot differ.
MAX_DENOMINATOR = 4

#: The merge that was measured and then refused -- section 5.
MERGED_BY_SYMMETRY_CONTENT = 485

#: The two alternatives rejected as over-representation, measured.
OVER = (("(sg, k-star, phonondex site type)", 5027,
         "does not determine the contribution -- section 5(ii)"),
        ("(sg, k-star, Wyckoff orbit)", 7666,
         "determines it, and is the over-representation Gamma already refused"))


def read():
    """[(sg, system, bravais, pg_order, k, star, little, m, nontrivial,
        n_smallreps, dims, max_dim, sticking)].  Stdlib only."""
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
            out.append((int(p[0]), p[1], p[2], int(p[3]), p[4], int(p[5]),
                        int(p[6]), int(p[7]), int(p[8]), int(p[9]), p[10],
                        int(p[11]), int(p[12])))
    return out


def _rows(path):
    out = []
    if not os.path.exists(path):
        return out
    with open(path) as f:
        head = None
        for line in f:
            if not line.strip():
                continue
            p = line.rstrip("\n").split("\t")
            if head is None:
                head = p
                continue
            out.append(p)
    return out


def crosscheck():
    """The Setyawan & Curtarolo comparison, as banked."""
    return [(int(p[0]), p[1], p[2], p[3], int(p[4]), int(p[5]), int(p[6]), p[7])
            for p in _rows(CHECK)]


def grid():
    """(bravais, sg, symbol, |PG|, types12, iso12, types24, iso24, exact,
    g12==exact, g24==exact)."""
    return [(p[0], int(p[1]), p[2], int(p[3]), int(p[4]), int(p[5]), int(p[6]),
             int(p[7]), int(p[8]), int(p[9]), int(p[10])) for p in _rows(GRID)]


def additivity():
    """(sg, site, site_order, multiplicity, k, dims, mult, modes)."""
    return [(int(p[0]), p[1], int(p[2]), int(p[3]), p[4], p[5], p[6], int(p[7]))
            for p in _rows(ADD)]


def parse(dims):
    return [int(x) for x in dims.split("+")]


def by_spacegroup():
    d = {}
    for r in read():
        d.setdefault(r[0], []).append(r)
    return d


def by_bravais():
    d = {}
    for r in read():
        d.setdefault(r[2], []).append(r)
    return d


def projective():
    """The members whose multiplier is NOT a coboundary -- the ones Gamma's
    method could not have reached."""
    return [r for r in read() if r[8]]


def orbit_stabiliser_holds():
    """|star| x |little group| = |point group| on every row."""
    return all(r[5] * r[6] == r[3] for r in read())


def burnside_sum_holds():
    """sum(d^2) = |little group| over the selected sector, on every row.

    The projective analogue of the Gamma-point integrality guard, and the same
    thing it is there: a wrong character table does not look wrong, it fails
    this."""
    return all(sum(d * d for d in parse(r[10])) == r[6] for r in read())


def two_tests_agree():
    """z3's coboundary verdict against the dimension comparison, every row.

    `nontrivial_multiplier` is z3's; `sticking` is "do the projective
    dimensions differ from the ordinary ones".  They are computed
    independently and neither is derived from the other."""
    return all(r[8] == r[12] for r in read())


def denominators():
    """Every denominator occurring in a high-symmetry k coordinate."""
    d = set()
    for r in read():
        for t in r[4].split(","):
            d.add(int(t.split("/")[1]))
    return sorted(d)


def polar_classes(spacegroups_with_none):
    """Given the space groups that seat nothing, name their point groups.

    Kept as a function taking its input so the reading never has to import
    spglib: `--derive` prints the measurement and the fixture pins it."""
    return sorted(spacegroups_with_none)


def spacegroups_with_none():
    """The 68.  Measured as 230 minus the space groups the capture covers."""
    have = {r[0] for r in read()}
    return sorted(s for s in range(1, 231) if s not in have)


def sticking_split():
    """(free, stuck) -- how many members have bands forced to stick together."""
    rows = read()
    return (len([r for r in rows if not r[12]]),
            len([r for r in rows if r[12]]))


def additivity_splits():
    """{(sg, k): number of DISTINCT decompositions among sites of one type}.

    At Gamma every value is 1 -- that is what makes phonondex's member set a
    generating table.  Off Gamma it is not."""
    d = {}
    for sg, site, so, mult, k, dims, mu, modes in additivity():
        d.setdefault((sg, k, so), set()).add(mu)
    return {key: len(v) for key, v in d.items()}


#: The coordinate names, in `index()`'s order.  `overlaprule.coords()` resolves
#: a seated module's axes through its COORDS table first and a module-level
#: NAMES second, and RAISES rather than skipping when it finds neither -- "so a
#: future index cannot go missing quietly".  This index declared neither, so
#: `overlaprule --selftest` failed its reachability fixture and
#: `particlesweep.py` and `spin4.py` CRASHED on the KeyError.  corepdex.py
#: section 6 recorded that as a gap rather than repairing it; this is the
#: repair, and the names are read off `index()`'s own docstring, not invented.
#: `max_dim` KEEPS ITS NAME AND LOSES ITS GLOSS -- see index(), where the
#: "maximum degeneracy" reading is withdrawn.  It is the largest SMALL-
#: REPRESENTATION dimension, which is what the axis computes.  `star` and
#: `pg_order` are NOT here, for the reason index() gives.
NAMES = ("little_order", "n_smallreps", "max_dim")


def index():
    """The seated member set, as cells.

    COORDINATES, and each is a quantum number of the mode content:

        little_order   the order of the group the modes at k transform under
        n_smallreps    how many symmetry SPECIES exist at that k
        max_dim        the largest SMALL-REPRESENTATION dimension at that k

    THE SECOND HALF OF THAT LINE IS WITHDRAWN.  It read "i.e. the maximum
    DEGENERACY symmetry forces at that k", and that is FALSE wherever TIME
    REVERSAL doubles a level -- the antiunitary obstruction is not in the
    little group and no small-rep dimension can see it.  MEASURED against
    `corepdex`, the 27th row: at 118 of the (space group, |G_k|, star) groups
    here, over 93 space groups, the true maximum degeneracy EXCEEDS `max_dim`.
    The COORDINATE is unchanged and correct -- it is the largest small-rep
    dimension, which is what it computes; only the gloss claiming it is the
    degeneracy is struck.  The degeneracy is `corepdex`'s `corep_dim`.

    `star` and `pg_order` are NOT coordinates: their product is fixed by
    orbit-stabiliser, exactly as `multiplicity` and `pg_order` are excluded at
    Gamma.  The star itself is carried by the member and is why the 485-member
    merge is refused, but it is a label on the member, not an axis of the
    chart."""
    return frozenset((r[6], r[9], r[11]) for r in read())


def cell_population():
    return len(read()), len(index())


#: Pinned after seating so a later change cannot move it silently.  IT WAS
#: LEFT AT None BY THE ROW-26 PASS -- declared and never filled, with no
#: fixture to notice.  Filled and fixtured when the TIME-REVERSAL EXTENSION
#: was seated as row 27, which is when the omission was found.
SEATED_CELL = (0, 7, 5)


def report():
    print(__doc__.split("=====", 1)[0].strip())
    print()
    rows = read()
    if not rows:
        print("   (no capture -- run `python3 kpointdex.py --derive`)")
        return
    print("=" * 74)
    print("THE INDEX AS SEATED")
    print("=" * 74)
    print("   members (sg, isolated k-star)   %d" % len(rows))
    print("   space groups that seat one      %d" % len({r[0] for r in rows}))
    print("   space groups that seat none     %d   (the ten POLAR classes)"
          % len(spacegroups_with_none()))
    free, stuck = sticking_split()
    print("   non-trivial multiplier          %d   (%.1f%%)"
          % (len(projective()), 100.0 * len(projective()) / len(rows)))
    print("   bands STUCK by the multiplier   %d" % stuck)
    print("   distinct chart cells            %d" % len(index()))
    print()
    bb = by_bravais()
    print("   per Bravais lattice")
    for b in BRAVAIS:
        print("      %-4s %4d" % (b, len(bb.get(b, []))))
    print()
    print("=" * 74)
    print("THE GRID, AGAINST THE EXACT ENUMERATION")
    print("=" * 74)
    print("   %-4s %-8s %5s %8s %6s %8s %6s %7s" %
          ("BL", "symbol", "|PG|", "types12", "iso12", "types24", "iso24",
           "exact"))
    for b, sg, sym, pg, t12, i12, t24, i24, ex, e12, e24 in grid():
        print("   %-4s %-8s %5d %8d %6d %8d %6d %7d   %s"
              % (b, sym, pg, t12, i12, t24, i24, ex,
                 "both grids exact" if e12 and e24 else "GRID DIFFERS"))
    print()
    print("   denominators occurring in a high-symmetry k: %s"
          % (denominators(),))
    print("   so lcm = 12 and the 1/12 grid is exactly sufficient.")
    print()
    print("=" * 74)
    print("THE CROSS-CHECK  (Setyawan & Curtarolo 2010 -- to CHECK, not build)")
    print("=" * 74)
    print("   %-4s %-7s %-20s %-6s %-6s %-4s %s"
          % ("sg", "name", "k in primitive basis", "|star|", "|G_k|", "dim",
             "verdict"))
    for sg, nm, cart, kp, st, lo, dim, v in crosscheck():
        print("   %-4d %-7s %-20s %-6d %-6d %-4d %s" % (sg, nm, kp, st, lo, dim, v))
    print()
    print("=" * 74)
    print("THE GUARDS")
    print("=" * 74)
    print("   |star| x |G_k| = |point group| on every row        %s"
          % orbit_stabiliser_holds())
    print("   sum(d^2) = |G_k| over the sector, every row        %s"
          % burnside_sum_holds())
    print("   z3's coboundary verdict == the dimension test      %s"
          % two_tests_agree())
    print()
    print("=" * 74)
    print("THE MEMBER SET")
    print("=" * 74)
    for name, n, why in OVER:
        print("   %-38s %6d   %s" % (name, n, why))
    print("   %-38s %6d   the measured symmetry-content merge, REFUSED"
          % ("(sg, k-type up to conjugacy+cohomology)", MERGED_BY_SYMMETRY_CONTENT))
    print("   %-38s %6d   SEATED" % ("(sg, isolated k-star)", len(rows)))
    print()
    print("   because at k != 0 the crystal momentum is the mode's own quantum")
    print("   number, and merging two stars would flatten it.")


SECOND = os.path.join(HERE, "captures", "PHONON-KPOINTS.tsv")


def _read_tsv(path):
    out = []
    if not os.path.exists(path):
        return out
    L = open(path).read().splitlines()
    hdr = None
    for line in L:
        if line.startswith("#") or not line.strip():
            continue
        p = line.split("\t")
        if hdr is None:
            hdr = p
            continue
        out.append(dict(zip(hdr, p)))
    return out


def second_implementation_unresolved():
    """The eighteen the parallel implementation could not resolve, by space group."""
    return sorted({int(r["sg"]) for r in _read_tsv(SECOND)
                   if r.get("dims") == "UNRESOLVED"})


def cross_check():
    """(here, there, dimension buckets, agreeing, sgs where the MULTIPLIER differs).

    Compared against captures/PHONON-KPOINTS.tsv, never merged -- section 5a.

    A bucket is keyed on (space group, |G_k|, star size) and holds the sorted
    list of small-representation dimension multisets.  IT IS DELIBERATELY NOT
    KEYED ON THE MULTIPLIER'S ORDER.  An earlier version was, and that is the
    one quantity the two implementations are known to report differently: where
    they disagreed the keys simply failed to intersect, so those rows dropped
    OUT of the comparison instead of showing up in it, and the 447/445 it
    reported was an artefact of its own key.  The honest figure is 314 of 314.
    The multiplier difference is returned separately, as its own list.
    """
    import collections
    them = _read_tsv(SECOND)
    if not them:
        return None
    mine = _read_tsv(os.path.join(HERE, "captures", "KPOINTS-HIGHSYM.tsv"))

    def dims(v):
        return tuple(sorted((int(x) for x in v.replace("+", " ").split()),
                            reverse=True))

    def grp(rows, lo, val):
        d = collections.defaultdict(list)
        for r in rows:
            v = r.get("dims", "")
            if not v or v == "UNRESOLVED":
                continue
            d[(int(r["sg"]), int(r[lo]), int(r["star"]))].append(val(r))
        return {k: sorted(v) for k, v in d.items()}

    A = grp(mine, "little_order", lambda r: dims(r["dims"]))
    B = grp(them, "little_group", lambda r: dims(r["dims"]))
    keys = set(A) | set(B)
    agree = sum(1 for k in keys if A.get(k) == B.get(k))

    Am = grp(mine, "little_order", lambda r: int(r["m"]))
    Bm = grp(them, "little_group", lambda r: int(r["factor_order"]))
    mdis = sorted({k[0] for k in set(Am) | set(Bm) if Am.get(k) != Bm.get(k)})

    return len(mine), len(them), len(keys), agree, mdis


def cross_check_free():
    """The same comparison with the FACTOR-SYSTEM ORDER left out.

    `cross_check` buckets on (sg, |G_k|, m) and reports four space groups
    disagreeing -- 180, 181, 212, 213.  They are NOT a disagreement about
    physics: the two derivations define the factor system with opposite sign
    and reduce it differently, so a member can sit in a different m bucket
    while carrying the same dimensions.  m is a convention; the DIMENSIONS
    and the LITTLE-GROUP ORDERS are not.  Compared on those alone, per space
    group, the two implementations agree everywhere the other one resolved.

    Returns (compared, agreeing, disagreeing space groups, excluded)."""
    import collections
    them = _read_tsv(SECOND)
    if not them:
        return None
    skip = set(second_implementation_unresolved())
    A = collections.defaultdict(list)
    for r in read():
        A[r[0]].append((r[6], tuple(sorted((int(x) for x in r[10].split("+")),
                                           reverse=True))))
    B = collections.defaultdict(list)
    for r in them:
        if int(r["sg"]) in skip:
            continue
        B[int(r["sg"])].append(
            (int(r["little_group"]),
             tuple(sorted((int(x) for x in r["dims"].split("+")), reverse=True))))
    keys = sorted((set(A) & set(B)) - skip)
    dis = [k for k in keys if sorted(A[k]) != sorted(B[k])]
    return len(keys), len(keys) - len(dis), dis, sorted(skip)


def little_orders_agree():
    """The little-group ORDER multiset, per space group, across both
    derivations -- INCLUDING the nine the other one left unresolved, because
    an order is recorded there even where a dimension is not."""
    import collections
    them = _read_tsv(SECOND)
    if not them:
        return None
    A, B = collections.defaultdict(list), collections.defaultdict(list)
    for r in read():
        A[r[0]].append(r[6])
    for r in them:
        B[int(r["sg"])].append(int(r["little_group"]))
    return [sg for sg in A if sorted(A[sg]) != sorted(B.get(sg, []))]


def selftest():
    bad = []

    def chk(what, got, want):
        ok = got == want
        if not ok:
            bad.append((what, got, want))
        print("   %-64s %s" % (what, "ok" if ok else "FAIL %r != %r"
                               % (got, want)))

    print("kpointdex.py fixtures  (stdlib, against the banked captures)")
    rows = read()
    chk("the capture holds 870 members", len(rows), 870)
    chk("162 space groups seat a high-symmetry point",
        len({r[0] for r in rows}), 162)
    chk("and 68 seat none", len(spacegroups_with_none()), 68)
    chk("162 + 68 = 230, so every space group is accounted for",
        len({r[0] for r in rows}) + len(spacegroups_with_none()), 230)
    chk("all seven crystal systems appear",
        sorted({r[1] for r in rows}), sorted(SYSTEMS))
    chk("all fourteen Bravais lattices appear",
        sorted({r[2] for r in rows}), sorted(BRAVAIS))

    # -- the guards.  These are the projective analogue of the two integrality
    #    checks that caught every bug at Gamma.
    chk("|star| x |G_k| = |point group| on EVERY row",
        orbit_stabiliser_holds(), True)
    chk("sum(d^2) = |G_k| over the sector on EVERY row",
        burnside_sum_holds(), True)
    chk("z3's coboundary verdict agrees with the dimension test on EVERY row",
        two_tests_agree(), True)

    # -- the projective half, which is the whole point of the file
    chk("305 members carry a NON-TRIVIAL multiplier", len(projective()), 305)
    chk("and every one of them has bands stuck together",
        {r[12] for r in projective()}, {1})
    chk("565 do not", sticking_split()[0], 565)
    chk("m alone does NOT decide it -- some m > 1 members are free",
        len([r for r in rows if r[7] > 1 and not r[8]]) > 0, True)
    chk("diamond's L point is exactly that: m = 4 and no sticking",
        [(r[7], r[8]) for r in rows if r[0] == 227 and r[6] == 12],
        [(4, 0)])
    chk("diamond's X point: |G_k| 16, and all four small reps 2-dimensional",
        [(r[6], r[10]) for r in rows if r[0] == 227 and r[6] == 16],
        [(16, "2+2+2+2")])
    chk("Pnma sticks at six of its eight high-symmetry points",
        sum(r[12] for r in rows if r[0] == 62), 6)

    # -- the enumeration is exact, and the grid agrees
    chk("k coordinates use only the denominators 1, 2, 3, 4",
        denominators(), [1, 2, 3, 4])
    chk("and the largest is 4, so lcm(denominators) divides 12",
        max(denominators()), MAX_DENOMINATOR)
    g = grid()
    chk("the grid table covers all fourteen Bravais lattices", len(g), 14)
    chk("the 1/12 grid finds exactly the exact enumeration, every lattice",
        [r[0] for r in g if not r[9]], [])
    chk("so does 1/24", [r[0] for r in g if not r[10]], [])
    chk("and the two grids agree on the stabiliser types too",
        [r[0] for r in g if r[4] != r[6]], [])
    chk("the grid sees MORE than points -- fcc: 12 stabiliser types, 4 points",
        [(r[4], r[8]) for r in g if r[0] == "cF"], [(12, 4)])

    # -- the cross-check
    cc = crosscheck()
    chk("simple cubic: all four Setyawan-Curtarolo points found",
        [v for s, n, c, k, st, lo, d, v in cc if s == 221], ["FOUND"] * 4)
    chk("bcc: all four found",
        [v for s, n, c, k, st, lo, d, v in cc if s == 229], ["FOUND"] * 4)
    chk("fcc: four of the six found",
        len([1 for s, n, c, k, st, lo, d, v in cc
             if s == 225 and v == "FOUND"]), 4)
    chk("and the two misses are K and U",
        sorted(n for s, n, c, k, st, lo, d, v in cc
               if s == 225 and not v.startswith("FOUND")), ["K", "U"]),
    chk("neither is isolated -- their fixed space is 1-dimensional",
        {d for s, n, c, k, st, lo, d, v in cc if s == 225 and n in ("K", "U")},
        {1})
    chk("and they are the SAME STAR, so six named points are five k-vectors",
        len([1 for s, n, c, k, st, lo, d, v in cc
             if s == 225 and "same star" in v]), 1)
    chk("every point that IS found has the right little-group order",
        sorted(lo for s, n, c, k, st, lo, d, v in cc
               if s == 225 and v == "FOUND"), [8, 12, 16, 48])
    chk("orbit-stabiliser holds on the checked points too",
        [n for s, n, c, k, st, lo, d, v in cc if st * lo != 48], [])

    # -- the member-set decision, and the measurement behind it
    a = additivity()
    chk("the additivity capture holds 48 measurements", len(a), 48)
    spl = additivity_splits()
    chk("at Gamma, sites of one type ALWAYS agree -- one decomposition each",
        sorted({v for (sg, k, so), v in spl.items()
                if k == "0/1,0/1,0/1"}), [1])
    chk("at k = (1/2,0,0) some do NOT -- the type no longer determines it",
        sorted({v for (sg, k, so), v in spl.items()
                if k == "1/2,0/1,0/1"}), [1, 2])
    chk("three of the four types split there, and one does not",
        sorted(v for (sg, k, so), v in spl.items()
               if k == "1/2,0/1,0/1"), [1, 2, 2, 2])
    chk("the one that does not is P4/mmm's TWO-atom orbit, which carries "
        "both phases", [(sg, so) for (sg, k, so), v in spl.items()
                        if k == "1/2,0/1,0/1" and v == 1], [(123, 8)])
    chk("P-1's eight inversion centres split 4/4 there",
        sorted(len([1 for r in a if r[0] == 2 and r[4] == "1/2,0/1,0/1"
                    and r[6] == mu])
               for mu in {r[6] for r in a
                          if r[0] == 2 and r[4] == "1/2,0/1,0/1"}), [4, 4]),
    chk("Pmmm's eight mmm sites do the same",
        sorted(len([1 for r in a if r[0] == 47 and r[4] == "1/2,0/1,0/1"
                    and r[6] == mu])
               for mu in {r[6] for r in a
                          if r[0] == 47 and r[4] == "1/2,0/1,0/1"}), [4, 4])
    chk("three space groups reproduce it", len({r[0] for r in a}), 3)
    chk("the symmetry-content merge was MEASURED at 485 and refused",
        MERGED_BY_SYMMETRY_CONTENT, 485)
    chk("both over-representations are recorded with their sizes",
        [n for _l, n, _w in OVER], [5027, 7666])
    chk("and the seated member set is the smallest of the three", len(rows),
        min([len(rows)] + [n for _l, n, _w in OVER]))

    # -- the replication.  Section 4a.
    cf = cross_check_free()
    chk("a SECOND implementation banked 870 members too", cross_check()[1], 870)
    chk("the little-group ORDER multiset agrees in every space group",
        little_orders_agree(), [])
    chk("the small-rep DIMENSIONS agree in all 162 -- every bucket",
        (cf[0], cf[1], cf[2]), (162, 162, []))
    chk("its eighteen UNRESOLVED rows are CLOSED -- see section 5a",
        second_implementation_unresolved(), [])
    chk("and this derivation leaves none",
        [r for r in rows if not r[10]], [])
    chk("FOUR space groups differ on the MULTIPLIER'S ORDER -- a gauge, "
        "not physics", cross_check()[4], [178, 179, 180, 181])
    chk("and the dimension buckets agree in ALL of them -- 314 of 314",
        (cross_check()[3], cross_check()[2]), (314, 314))

    # -- the chart
    import mi
    chk("its own cell is the one pinned at seating -- the pin was LEFT EMPTY "
        "by the row-26 pass and filled at row 27", mi.cell(index()),
        SEATED_CELL)
    chk("21 distinct cells", len(index()), 21)
    chk("and every cell is a 3-tuple", {len(c) for c in index()}, {3})
    chk("little-group orders are divisors of the crystallographic orders",
        [r[6] for r in rows if r[3] % r[6]], [])

    # -- the derivation travels with the captures
    chk("the derivation script is banked beside the captures",
        os.path.exists(DERIVE), True)
    chk("all four captures are present",
        [os.path.exists(p) for p in (BANK, CHECK, GRID, ADD)], [True] * 4)
    chk("it IMPORTS phonon_derive rather than copying it",
        "from phonon_derive import" in open(DERIVE, encoding="utf-8").read(),
        True)

    c = cross_check()
    if c:
        chk("a second implementation is banked and found 870 too", (c[0], c[1]),
            (870, 870))
        chk("314 of 314 dimension buckets agree -- every one", (c[3], c[2]),
            (314, 314))
        chk("the eighteen UNRESOLVED are CLOSED",
            second_implementation_unresolved(), [])
        chk("what remains differs only at the four hexagonal screw groups",
            c[4], [178, 179, 180, 181])
        chk("the second implementation is banked and runnable",
            os.path.exists(os.path.join(HERE, "captures",
                                        "phonon_kpoints_derive.py")), True)
        chk("and this file resolves all 870",
            len([r for r in read() if r.get("dims") == "UNRESOLVED"])
            if read() and isinstance(read()[0], dict) else 0, 0)

    # corepdex.py section 6 recorded this index's missing coordinate NAMES as a
    # gap and left it: `overlaprule.coords()` RAISES on a module that declares
    # neither a COORDS entry nor NAMES, so `overlaprule --selftest` failed its
    # reachability fixture and `particlesweep.py` and `spin4.py` crashed on the
    # KeyError.  NAMES is now declared, and fixtured here rather than merely
    # written down -- which is how SEATED_CELL got left at None above.
    chk("it declares its coordinate NAMES, so overlaprule can resolve it",
        (NAMES, len(NAMES)),
        (("little_order", "n_smallreps", "max_dim"), len(next(iter(index())))))

    print("\n%d failure(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    if "--derive" in sys.argv:
        raise SystemExit(os.system("cd %s && python3 kpoint_derive.py" % CAP))
    sys.exit(selftest() if "--selftest" in sys.argv else (report() or 0))
