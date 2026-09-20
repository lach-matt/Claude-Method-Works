#!/usr/bin/env python3
r"""ghosts.py -- THE ADJUDICATION OF E.  DOCKET 39.

    python3 ghosts.py             the reading
    python3 ghosts.py --selftest  fixtures

M: "Do the bound per index and separate UNPLACED from OPEN.  Derive all you
can, including proofs, theorems, and laws."

`predict.py` measured E for every seated index -- 4,759 cells the register's own
closure demands and no member occupies -- named three bins for them, and left
both halves of the adjudication undone.  This file does both, and in doing the
first half it finds that most of it CANNOT BE DONE, for a reason that is a
theorem rather than a shortage of physics.

===============================================================================
1. SEVEN LAWS, AND THE FIRST FOUR DECIDE THE WHOLE PROGRAMME
===============================================================================

Write X for a seated index, a set of cells in a product of totally ordered
coordinate sets.  The join is COMPONENTWISE MAX (`decomposable.joinclose`), J(X)
the join-closure, D = J(X) \ X the demand, E = |D|.  A BOUND is a set B of cells
a physical law admits; it FORBIDS a demanded cell c when c is in D and not in B.
Every law below is proved, and then measured on the live tree.

    LAW 1 -- PROJECTION.  pi_i(J(X)) = pi_i(X) for every coordinate i.

        PROOF.  X is contained in J(X).  For the converse, J(X) is generated
        from X by repeated componentwise max, and max(a, b) is a or b, so each
        coordinate of each generated cell is a coordinate value already present
        in X.  Induction on the generation. []

        COROLLARY -- NO SINGLE-COORDINATE BOUND CAN FORBID ANYTHING.  The demand
        never invents a coordinate value, so "2J must be odd" or "Q3 must be a
        multiple of three" rule out nothing that the closure asked for.  This is
        measured below: of 1,012 demanded baryon cells, ZERO carry an even 2J.

    LAW 2 -- MAX-STABILITY.  If X is contained in B and B is closed under
    componentwise max, then J(X) is contained in B: B forbids nothing.

        PROOF.  J(X) is the least max-closed set containing X. []

    LAW 3 -- MONOTONE VACUITY.  A bound of the form x_i <= f(x_j1, ..., x_jm),
    with i not among the j and f non-decreasing in each argument, is max-closed
    and therefore forbids nothing.

        PROOF.  Let a, b be in B and c = a v b.  Then c_i = max(a_i, b_i); say
        it is a_i.  Then c_i = a_i <= f(a_j1, ..., a_jm) <= f(c_j1, ..., c_jm),
        since a_j <= c_j for every j and f is non-decreasing. []

        THIS IS THE FINDING OF THIS FILE.  Every bound the atomic and nuclear
        indexes admit is of exactly that shape:

            l <= n - 1          the radial node count n - l - 1 is >= 0
            k <= 2(2l + 1)      PAULI: a subshell holds 2(2l+1) spin-orbitals
            q <= k              you cannot ionise more electrons than are there
            l = 0 => sigma = +1  j = l +- 1/2 and j >= 0, so l = 0 forces j = 1/2
            occ <= 2(2 floor((S_a-1)/2) + 1)     Pauli through a hidden l_a

        All five are real theorems of quantum mechanics, all five hold on every
        seated member without exception, AND ALL FIVE FORBID NOTHING.  Not
        "nothing was found": nothing CAN be found, by Law 3.

    LAW 4 -- WHAT CAN FORBID.  A bound forbids only if its admissible set is not
    max-closed -- it must be antitone in some coordinate, or carry a congruence,
    or be a non-monotone function of several coordinates.

        THE ONE BOUND IN THIS TREE THAT QUALIFIES acts on the baryons, and it
        qualifies twice over: an absolute value and a mod-2 congruence.  It is
        the THREE-QUARK FLAVOUR BOUND, and it forbids 894 of the 1,012 demanded
        baryon cells -- 88.3% of them, emptied by theorem.  Gell-Mann--Nishijima
        is its corollary and forbids 593, a strict subset: an audit found the
        weaker one seated here and the 301 cells between them wrongly OPEN.

    LAW 5 -- COORDINATE EXPRESSIBILITY.  If the bound is a predicate B(c, v) on a
    cell and a variable v the index does not carry, then c is forbidden iff
    there is NO v with B(c, v).  A hidden variable free to range forbids
    nothing; a hidden variable whose range the coordinates bound may forbid.

        INSTANCE THAT FORBIDS NOTHING -- THE QUARK MODEL ON THE MESONS.  For a
        q-qbar state P = (-1)^(L+1), C = (-1)^(L+S), S in {0,1} and
        |L - S| <= J <= L + S.  L and S are hidden: `mesons.py` charts
        (2J, P, 2I, Q3).

            THEOREM.  Every (J, P) with J a non-negative integer and P = +-1 is
            realised by some q-qbar (L, S).

            PROOF, four cases.
              P = -1 needs L even.  J even: take L = J, S = 0; then
                P = (-1)^(J+1) = -1 and J = L is in [|L-S|, L+S].  J odd: take
                L = J-1 (even, and >= 0), S = 1; then P = (-1)^J = -1 and
                L+S = J.  J = 0 forces L = S, and L = S = 0 gives 0-.
              P = +1 needs L odd.  J odd: take L = J, S = 0.  J even and >= 2:
                take L = J-1 (odd), S = 1; then P = (-1)^J = +1 and L+S = J.
                J = 0 forces L = S, and L = S = 1 gives 0+. []

            SO THE QUARK MODEL FORBIDS NO CELL OF THE MESON INDEX.  The famous
            exotics -- 0--, 0+-, 1-+, 2+- -- are forbidden in J^PC, and C IS NOT
            A COORDINATE HERE.  `mesons.py` refused it for TOTALITY: 168 of 250
            mesons carry no C at all.  The refusal was right and it has a price,
            and this is the first time the price is measured.  A COORDINATE
            REFUSED FOR TOTALITY IS ADJUDICATION POWER GIVEN UP.

        INSTANCE THAT BINDS THE HIDDEN VARIABLE -- `madrule`.  The acceptor's
        l_a is hidden; only its Madelung group S_a = n_a + l_a is charted.  But
        l <= n-1 gives 2 l_a <= S_a - 1, so the Pauli capacity IS a function of
        S_a.  The bound exists.  It is monotone, so Law 3 still empties it.

    LAW 6 -- ADJUDICATION IS RELATIVE TO THE CLOSURE OPERATOR.  E is a deficit
    against an operator, and which cells a bound forbids depends on which.

        MEASURED ON ONE SET OF CELLS, the 90-position period x group periodic
        table: the JOIN deficit is 0 and the ORDER deficit (`decomposable.stair`)
        is 36, and l <= n-1 forbids 25 of the 36 order ghosts and -- necessarily,
        by Law 3 -- none of the join ghosts, of which there are none to forbid.

        THIS CORRECTS DOCKET 38.  `predict.py` section 2 cites the element
        layer's "E = 36, split 25 forbidden and 11 deferred" as the precedent for
        adjudicating the seated indexes' E, without saying that the 36 is an
        ORDER deficit and the 4,759 are JOIN deficits.  `tools/cypher.py`'s own
        fixture says so -- ("periodic table 2-D", {"order": 36}).  The three bins
        survive the correction intact; the precedent is re-attributed, and Law 3
        explains why it could never have transferred.

    LAW 7 -- FORBIDDING POWER IS A PROPERTY OF THE CHART, NOT OF THE BOUND.

        The same bound, l <= n-1, forbids 25 cells on (period, group), 0 on
        (n, l, k) and 0 on (n+l, l, k).  The physics did not move.

        AND THE CAUTION IS SHARPER THAN THE LAW.  DOCKET 2 WITHDREW the 2-D
        periodic layout from the master index as over-representation, and it is
        exactly the chart on which the bound has teeth.  A chart that can forbid
        is not thereby a better chart.  Do not read forbidding power as evidence.

===============================================================================
2. THE BOUND PER INDEX
===============================================================================

Every bound below was DERIVED from a stated physical law, CHECKED against every
seated member of its index (zero violations anywhere), and then applied to the
demand.  A bound was never fitted to the demand.

    index              bound                            monotone  FORBIDDEN
    baryons     1012   three-quark flavour content          NO        894
    ions         296   l<=n-1 (both ends), Pauli, q<=k     yes          0
    fibred       140   l<=n-1, Pauli                       yes          0
    terms         98   mult = 1 => not SHORT               yes          0
    observed      56   l<=n-1, Pauli                       yes          0
    madrule       18   Pauli through S_a                   yes          0
    nucshell      14   l = 0 => sigma = +1                 yes          0
    mesons        15   NONE -- and the absence is a THEOREM   -         0
    (nine others)     none derived                          -          0

SEVEN BOUNDS DERIVED, SIX OF THEM MONOTONE, AND THE SEVENTH DOES ALL THE WORK.
The Russell-Saunders row is in the table to answer "did you look?" at the
largest of the undecided indexes: a bound WAS found for `terms`, and Law 3
empties it like the rest.

===============================================================================
3. GELL-MANN--NISHIJIMA IS NOT ASSUMED HERE.  IT IS MEASURED OFF THE QUARKS
===============================================================================

Q = I3 + Y/2 with Y = B + S + C + B' + T is an identity, not a fit, and the
derivation is four lines from the quark charges.  Writing n_a for (quarks minus
antiquarks) of flavour a:

    Q  = (2/3)(n_u + n_c + n_t) - (1/3)(n_d + n_s + n_b)
    I3 = (n_u - n_d)/2,   S = -n_s,  C = n_c,  B' = -n_b,  T = n_t
    B  = (n_u + n_d + n_s + n_c + n_b + n_t)/3

    Q - I3 = n_u/6 + n_d/6 + (2/3)(n_c + n_t) - (1/3)(n_s + n_b) = Y/2   []

`gmn_from_quarks()` re-derives all three legs from the capture's OWN quark
strings, with no textbook value imported:

    baryons  292 rows, 292 parse, charge from quarks 292/292, isospin weight
             292/292, the identity 292/292.  No exception.
    mesons   250 rows, 191 parse (59 are flavour mixtures -- which is exactly
             why `mesons.py` could not chart S, C and B, and therefore why the
             bound is inexpressible there), charge 191/191, identity 191/191,
             AND THE ISOSPIN WEIGHT FAILS TWICE.

    THE TWO FAILURES ARE A FAULT IN THE CAPTURE AND THEY ARE RECORDED, NOT
    REPAIRED.  B(s2)*(5840)0 and its antiparticle carry quark content `sB` and
    I2 = 1, i.e. I = 1/2, while the very same content on B(s)0 and B(s)*0 carries
    I2 = 0 in the same file (`captures/PDG-2026.tsv` lines 370, 371, 372, 452,
    453, 454).  An s-bbar pair contains no u or d, so I3 = 0 and I = 1/2 has no
    weight to sit on.  The capture contradicts itself, and the contradiction was
    found by a consistency leg of a bound, not by re-reading the source.

    AND IT CHANGES NOTHING, WHICH IS ALSO MEASURED.  `bs2_consequence()` rebuilds
    the meson index with I2 = 0 on both rows: 66 cells before and after, E = 15
    before and after, cell (0, 10, 14) before and after, no cell gained or lost,
    because both (4, 1, 1, 0) and (4, 1, 0, 0) are occupied by other members.
    The fault is real, the fault is inconsequential HERE, and neither half of
    that is asserted without the number.

===============================================================================
4. UNPLACED SEPARATED FROM OPEN, AND THE SEPARATOR IS A RULE
===============================================================================

    A demanded cell c is UNPLACED iff the index's OWN SOURCE holds a row the
    module declined to chart which supplies arity - 1 of the coordinates and
    agrees with c on every one of them.

THE STRENGTH CONDITION IS THE WHOLE RULE.  A row missing one coordinate names a
line of cells and pins each of them up to that coordinate's value; a row missing
two names a plane and pins nothing.  Counting the second kind as UNPLACED would
let four thousand unparsed term labels "explain" every empty cell in `terms`.
Rows below the strength are counted apart and never used.

    index         E    FORBIDDEN  UNPLACED  OPEN   the source rows that pin
    gravity     1550     1080         0      470   source gapless
    baryons     1012      894         8      110   14 with no P (Xi, Omega)
    readrezayi   678        0         0      678   source gapless
    channels     367        0        23      344   25 with a non-integer B
    ions         296        0         0      296   source gapless
    laws         254        0         0      254   13 dropped, none pins a cell
    fibred       140        0         0      140   source gapless
    probability  112        0         0      112   source gapless
    terms         98        0         ?        ?   NOT DECIDED -- see below
    fqh           71        0         0       71   source gapless
    observed      56        0         0       56   source gapless
    fundamental   46        0         0       46   source gapless
    inversion     24        0         0       24   source gapless
    madrule       18        0         0       18   source gapless
    mesons        15        0         3       12   8 with no P (D, D_s)
    nucshell      14        0         0       14   source gapless
    nucbands       5        0         2        3   93 levels with no parity
    deformedbnds   3        0         0        3   56 levels with no parity

    TOTAL      4,759    1,974        36    2,651   and 98 UNDECIDED

    TERMS IS THE ONE REFUSAL AND ITS REASON IS EXACT.  4,033 of 16,624 NIST rows
    carry a bracketed jK, jj or Racah label, which supplies neither `mult` nor
    `L` -- two of four coordinates -- so no refused row can pin a cell at the
    required strength.  But `terms._load()` DISCARDS a refused row without
    recording its term key, so the tree cannot ask the one question that would
    settle it: is there a term ALL of whose level rows were refused?  Such a term
    would supply mult, L and parity and lack only `completeness`, which is
    exactly strength arity - 1.  WHAT WOULD SETTLE IT: have the loader bank the
    refused rows' keys.  Until then 98 cells are UNDECIDED between UNPLACED and
    OPEN, and are not counted as either.

    A NOTE ON DOUBLE COVER.  Three meson cells are UNPLACED against two objects,
    not three: D(s2)*(2573)+ lacks only P, so it pins BOTH (4,-1,0,3) and
    (4,1,0,3), and it will fill exactly one of them.  `unplaced_objects()` counts
    objects beside cells so the two numbers are never confused.

===============================================================================
5. WHAT THIS FILE REFUSES
===============================================================================

    TO CALL 2,651 A COUNT OF UNDISCOVERED OBJECTS.  It is the count of demanded
    cells that no bound derivable here forbids and no source row explains.  For
    the seven indexes with a derived bound the OPEN figure is FINAL AGAINST
    EVERY MONOTONE BOUND, by Law 3 -- that is a proof, not a survey.  For the
    nine with none derived it is open against nothing at all, and a bound found
    tomorrow may empty any of them.  The two situations are different and are not summed
    into one adjective.

    TO REPAIR THE B(s2)*(5840) ROWS.  Section 3 measures the fault and its
    consequence.  The chat-67 full hold governs a capture exactly as it governs
    a section read.

    TO CALL THE MESONS' ZERO A WEAK RESULT.  It is the strongest kind available:
    not "no forbidding bound was found" but "the quark model, fully stated,
    forbids no cell of this chart", with the theorem in section 1 and the reason
    -- the coordinate C was refused for totality -- in `mesons.py`.

    TO READ LAW 7 AS AN ARGUMENT FOR THE 2-D LAYOUT.  It is not.  DOCKET 2's
    withdrawal stands.  Law 7 says only that forbidding power and chart quality
    are independent, which cuts both ways and is a caution in both directions.
"""

import itertools
import sys

import decomposable as D
import demand
import mesons
import mi
import pdgcapture
import registry

CAP = lambda l: 2 * (2 * l + 1)                # Pauli: spin-orbitals in (n, l)


# --------------------------------------------------------------- the bounds
#
# Each is (label, the physical law it comes from, monotone?, predicate).
# MONOTONE means "max-closed", which `max_closed()` verifies by exhaustion over
# the index's own product box rather than by reading the shape off the source.

def _b_observed(c):
    """(n, l, k) with k the PRIOR occupancy of the subshell that gained."""
    n, l, k = c
    return l <= n - 1 and 0 <= k <= CAP(l) - 1


def _b_ions(c):
    """(sn, sl, k, q, tn, tl, g) -- a Lambda_8 ionisation transition."""
    sn, sl, k, q, tn, tl, g = c
    return (sl <= sn - 1 and tl <= tn - 1
            and 0 <= k <= CAP(sl) and 0 <= g <= CAP(tl) and 0 <= q <= k)


def _b_nucshell(c):
    """(nr, l, sigma).  j = l +- 1/2 and j >= 0, so l = 0 admits only j = 1/2."""
    _nr, l, s = c
    return not (l == 0 and s == -1)


def _b_madrule(c):
    """(S_a, l_d, occ).  l_a is hidden; l <= n-1 gives 2 l_a <= S_a - 1."""
    Sa, _ld, occ = c
    return 0 <= occ <= CAP((Sa - 1) // 2)


def _b_terms(c):
    """(mult, L, parity, completeness).  mult = 1 => the term is not SHORT.

    A singlet has S = 0, so Russell-Saunders gives it the single level J = L.
    SHORT means the observed J set is a PROPER SUBSET of the predicted one, and
    a proper non-empty subset of a singleton does not exist -- while a term with
    no observed level at all is not in the table.  `terms.COMPLETENESS` indexes
    SHORT at 1.
    """
    mult, _L, _p, comp = c
    return not (mult == 1 and comp == 1)


def _b_baryons(c):
    """(2J, P, 2I, Q3, S, C, B) -- GELL-MANN--NISHIJIMA.

    2 I3 = 2Q - Y = 2Q3/3 - (B_n + S + C + B), and I3 must be a weight of the
    isospin-I representation: |2 I3| <= 2I and 2I - 2 I3 even.  Baryon number
    is NOT a coordinate -- `baryons.py` refused it as the sign of the pdgid --
    so it is the hidden variable of Law 5, and its range is {+1, -1}.  The
    congruence is insensitive to the choice; the inequality is not.
    """
    _j, _P, i2, q3, S, C, B = c
    for Bn in (1, -1):
        t2 = 2 * q3 // 3 - (Bn + S + C + B)
        if abs(t2) <= i2 and (i2 - t2) % 2 == 0:
            return True
    return False


# ---------------------------------------------------- DOCKET 43, the stronger
# bound.  GELL-MANN--NISHIJIMA IS A COROLLARY, AND IT UNDER-FORBIDS BY 301.
# `_b_baryons` quantifies over a hidden baryon number Bn in {+1, -1} and asks
# only that SOME Bn make the weight condition close.  That is weaker than the
# quark model the capture already carries: it never asks whether the flavour
# numbers are SIMULTANEOUSLY realisable by three quarks, or by three
# antiquarks, at all.  The demanded cell (2J,P,2I,Q3,S,C,B) = (1,-1,0,3,1,1,1)
# needs an anti-strange, a charm AND an anti-bottom quark in one baryon -- a
# mixed state, not a baryon -- and GMN passes it because at Bn = -1 the
# arithmetic happens to close.
#
# Measured: the three-quark bound forbids 894 of the 1012 demanded baryon
# cells against GMN's 593, holds on all 184 seated members without exception,
# and every one of GMN's 593 is among the 894 -- a strict containment, so
# nothing GMN forbade is released.
_QUARKS = {"u": (2, 0, 0, 0), "d": (-1, 0, 0, 0), "s": (-1, -1, 0, 0),
           "c": (2, 0, 1, 0), "b": (-1, 0, 0, -1)}       # (Q3, S, C, B)
_REACH = None


def quark_reachable():
    """{(2I, Q3, S, C, B)} realisable by three quarks OR three antiquarks.

    Flavour fixes five of the seven coordinates and says nothing about 2J or
    P, which orbital and radial excitation reach freely -- so this is a bound
    on a five-coordinate projection and is silent on the other two.

    2I is bounded BOTH WAYS.  Above by the light-quark count n_ud, with the
    same parity; below by |n_u - n_d|, because I3 must be a weight of the
    isospin-I representation.  THE LOWER BOUND IS NOT DECORATION: without it
    uuu is admitted at I = 1/2, which is not a state -- Delta++ is I = 3/2
    only -- and the count comes out 890 instead of 894.
    """
    global _REACH
    if _REACH is None:
        out = set()
        for combo in itertools.combinations_with_replacement("udscb", 3):
            q3 = sum(_QUARKS[q][0] for q in combo)
            S = sum(_QUARKS[q][1] for q in combo)
            C = sum(_QUARKS[q][2] for q in combo)
            B = sum(_QUARKS[q][3] for q in combo)
            nu = combo.count("u")
            nd = combo.count("d")
            nud = nu + nd
            for i2 in range(max(abs(nu - nd), nud % 2), nud + 1, 2):
                out.add((i2, q3, S, C, B))
                out.add((i2, -q3, -S, -C, -B))
        _REACH = frozenset(out)
    return _REACH


# ------------------------------------------------------- DOCKET 49, GRAVITY.
# gravity held 1,550 demanded cells -- the largest demand in the register --
# against NO derived bound, so every one was OPEN against nothing at all.  Two
# bounds are derivable from the chart's own coordinates.
#
# BOUND 1, THE HORIZON BOUND.  B is not free: gravity.bound_class(D, q, F,
# Jzero) is a TOTAL FUNCTION, and two of its inputs are coordinates already --
# q > 0 iff Y > 0, since the charge decade rank is 0 exactly when Qtilde is --
# while F is charted outright.  The third, Jzero, is HIDDEN, and this is Law 5's
# may-forbid case rather than its forbids-nothing case because the coordinates
# BOUND ITS RANGE two ways: X > 0 means chi > 0 means 2Je != 0, and F == 1 means
# the total angular momentum cannot vanish.  bound_class is ANTITONE IN D -- a
# bound at five, none above it, singly-rotating Myers-Perry -- so Law 4 permits
# it to forbid, and it forbids 1,100.
#
# BOUND 2, THE DECADE BOUND.  chi and Qtilde are not independent:
#
#     chi      = Je / alpha_G            alpha_G = G M^2 / (hbar c)
#     Qtilde^2 = q^2 alpha / alpha_G     alpha   = e^2 / (4 pi eps0 hbar c)
#     =>  chi / Qtilde^2 = Je / (q^2 alpha)
#
# THE GRAVITATIONAL COUPLING CANCELS, so the ratio is MASS-FREE.  Verified on
# all 1,589 member rows at zero failures.  This is not new physics and is not
# claimed as any: alpha_G is the standard gravitational coupling constant and
# alpha/alpha_G is Dirac's large number (Dirac 1937).  What is new is only the
# use made of it -- the join pairs a spin decade with a charge decade freely,
# and the identity says most pairings are unphysical.  Je and q are hidden and
# their ranges are READ FROM THE MEMBER SET, which is what Law 5 licenses; the
# bound is then exact given those ranges.  It forbids 128 more.
#
# A FITTED VERSION OF BOUND 2 FORBADE 192 AND IS REFUSED.  Taking the OBSERVED
# band of floor(log chi) - 2 floor(log Qtilde) over the members, rather than
# deriving the interval from the hidden ranges, gains 64 cells -- and a band
# measured on the members and then used to forbid demanded cells is fitting.
# The derived 128 is the figure this file reports.
# EVERY PHYSICAL INPUT TO THE GRAVITY BOUND, CITED.  Nothing below is claimed
# as new physics: the bound's content is the USE, not the results it rests on.
GRAVITY_SOURCES = (
    "Kerr-Newman horizon condition chi^2 + Qtilde^2 <= 1 -- Newman, Couch, "
    "Chinnapared, Exton, Prakash and Torrence, J. Math. Phys. 6, 918 (1965)",
    "Myers-Perry solutions in D dimensions, and the absence of any extremality "
    "bound on a SINGLE angular momentum for D >= 6 -- Myers and Perry, Ann. "
    "Phys. 172, 304 (1986); reviewed in Emparan and Reall, 'Black Holes in "
    "Higher Dimensions', Living Rev. Rel. 11, 6 (2008)",
    "the gravitational coupling constant alpha_G = G M^2 / (hbar c), and "
    "alpha / alpha_G as Dirac's large number -- Dirac, Nature 139, 323 (1937)",
    "the fine-structure constant alpha = e^2 / (4 pi eps0 hbar c), CODATA",
)

_GRAV_RATIO = None


def gravity_source_gap():
    """(species named by a level capture, species charted) -- and they agree.

    AN EARLIER VERSION OF THIS COUNTED FILES AND CALLED THEM SPECIES.
    `captures()` is keyed by SPECIES and records the one file that won, so every
    other file for the same species looked declined.  That gave a "gap" of 31
    species "with no readable J" -- and their J columns parse perfectly; they
    are duplicate captures of species already charted from another file.  The
    real figure is zero: every species any level table names is charted, so
    gravity is GAPLESS and its UNPLACED zero needs no strength-rule argument.
    """
    import os
    import gravity as g
    named = set()
    for fn in sorted(os.listdir(g.ASD)):
        if not fn.endswith(".tsv"):
            continue
        with open(os.path.join(g.ASD, fn), encoding="utf-8",
                  errors="replace") as fh:
            txt = fh.read()
        lines = txt.split("\n")
        # THE SAME COLUMN TEST captures() USES.  An earlier version of this
        # asked the narrow question ("level_cm1" in txt) while captures() had
        # been widened to accept `Level_cm-1` and the rest, so it reported 118
        # named against 126 charted -- more charted than named, which is not a
        # gap in either direction but two readers disagreeing.
        if not any(g._columns(l) for l in lines[:40]):
            continue                      # a mass table, not a level table
        sp = g._species_of(lines) or g._species_of_filename(fn)
        if sp is not None:
            named.add(sp)
    return len(named), len(g.captures())


def gravity_ratio_range():
    """[lo, hi] for chi/Qtilde^2 = Je/(q^2 alpha), from the hidden ranges."""
    global _GRAV_RATIO
    if _GRAV_RATIO is None:
        import gravity as g
        alpha = 7.2973525693e-3
        Je = {m[5] / 2.0 for m in g.members() if m[5] > 0}
        qs = {m[3] for m in g.members() if m[3] > 0}
        _GRAV_RATIO = (min(Je) / (max(qs) ** 2) / alpha,
                       max(Je) / (min(qs) ** 2) / alpha)
    return _GRAV_RATIO


_GIMAGE = None
GRAVITY_JCUT = 32          # saturation is reached by 16; see gravity_image_saturates()


def gravity_image(jcut=None):
    """Every cell the chart's COORDINATE MAP can produce, exhausted.

    THIS REPLACES TWO SEPARATE BOUNDS WITH ONE, AND REMOVES THEIR ASSUMPTIONS.
    The horizon bound and the decade bound each asked "does physics permit this
    cell"; both needed a range for a hidden variable, and the decade bound took
    Je's range from the OBSERVED members -- which forbade 148 cells the
    parameter space actually reaches, Zr-113 at q = 1 and 2Je = 15 among them.

    The question this asks instead is exact and needs no range: B, F, X and Y
    are all FUNCTIONS of (nuclide, q, 2Je), so the map has an IMAGE, and a
    demanded cell outside it cannot be occupied by construction -- not because
    physics forbids it, but because no parameter point maps there.  The only
    free parameter, the cutoff on 2Je, is removed by SATURATION: the image stops
    growing at 2Je = 16 and is identical at 32 and 64.

    It also disposes of an objection to the old horizon bound, that it leaned on
    `bound_class` returning "undetermined" -- 980 of its 1,228.  Here there is
    no epistemic step at all: whatever B the map assigns, it assigns, and a cell
    carrying a different B is simply not in the image.
    """
    global _GIMAGE
    if jcut is None and _GIMAGE is not None:
        return _GIMAGE
    import math
    import gravity as g
    cut = GRAVITY_JCUT if jcut is None else jcut
    alpha = 7.2973525693e-3
    hbar, c_, gn = 1.054571817e-34, g.C_SI, 6.67430e-11
    sp, ch = g._ranks()
    spi = {d: i + 1 for i, d in enumerate(sp)}
    chi = {d: i + 1 for i, d in enumerate(ch)}
    seeds = set()
    for Z, N, A, _sym, dm, _qual in g.nuclides():
        base = A * g.U_KG + dm * g.KEV_J / c_ ** 2
        for q in range(0, Z + 1):
            M = base - q * g.M_E
            if M <= 0:
                continue
            aG = gn * M * M / (hbar * c_)
            Y = 0
            if q > 0:
                Y = chi.get(math.floor(math.log10(math.sqrt(q * q * alpha / aG))))
                if Y is None:
                    continue
            F = (A + (Z - q)) % 2
            for tj in range(0, cut + 1):
                if tj == 0:
                    X = 0
                else:
                    X = spi.get(math.floor(math.log10((tj / 2.0) / aG)))
                    if X is None:
                        continue
                seeds.add((F, X, Y, (Z % 2 == 0 and N % 2 == 0 and tj == 0),
                           1 if q > 0 else 0))
    out = {(D, g.bound_class(D, qp, F, Jz), F, X, Y, L, E)
           for (F, X, Y, Jz, qp) in seeds
           for D in range(4, 12) for L in (0, 1) for E in (0, 1)}
    if jcut is None:
        _GIMAGE = out
    return out


def gravity_image_saturates():
    """[(cutoff, image size)] -- the cutoff is not a free parameter."""
    return [(k, len(gravity_image(k))) for k in (8, 16, 32, 64)]


def gravity_superseded():
    """(what the old pair forbade, how many of those the image REACHES).

    The first pass derived two bounds -- a horizon bound from the exact
    solutions, and a decade bound whose range for Je was taken from the
    OBSERVED members.  They are kept here, not in prose, so the comparison the
    paper draws is reproducible: the second was too strong, and these are the
    cells it forbade that the parameter space actually reaches.
    """
    import math
    import gravity as g
    import registry
    sp, ch = g._ranks()
    alpha = 7.2973525693e-3
    Je = {m[5] / 2.0 for m in g.members() if m[5] > 0}
    qs = {m[3] for m in g.members() if m[3] > 0}
    lo = min(Je) / (max(qs) ** 2) / alpha
    hi = max(Je) / (min(qs) ** 2) / alpha

    def old(c):
        D, B, F, X, Y, _L, _E = c
        q = 1 if Y > 0 else 0
        ok = set()
        for Jz in (True, False):
            if Jz and (X > 0 or F == 1):
                continue
            ok.add(g.bound_class(D, q, F, Jz))
        if B not in ok:
            return False
        if X == 0 or Y == 0:
            return True
        d = sp[X - 1] - 2 * ch[Y - 1]
        return (10.0 ** (d - 2) < hi) and (10.0 ** (d + 1) > lo)

    dm = frozenset(demand.demand(frozenset(registry.index_of("gravity.index"))))
    img = gravity_image()
    forb = [c for c in dm if not old(c)]
    return len(forb), len([c for c in forb if c in img])


def gravity_superseded_witness():
    """(symbol, A, q, 2Je) -- one cell the withdrawn bound forbade and the
    parameter space reaches, with the nuclide that reaches it.

    The paper names this witness.  A NAMED NUCLIDE IS A CLAIM, so it is found
    rather than typed: an earlier draft wrote "Zr-113" into the prose and the
    substitution guard caught the bare 113, which is the guard working.
    """
    import math
    import gravity as g
    import registry
    sp, ch = g._ranks()
    alpha = 7.2973525693e-3
    hbar, c_, gn = 1.054571817e-34, g.C_SI, 6.67430e-11
    spi = {d: i + 1 for i, d in enumerate(sp)}
    chi = {d: i + 1 for i, d in enumerate(ch)}
    n_forb, _reach = gravity_superseded()
    dm = frozenset(demand.demand(frozenset(registry.index_of("gravity.index"))))
    img = gravity_image()
    Je = {m[5] / 2.0 for m in g.members() if m[5] > 0}
    qs = {m[3] for m in g.members() if m[3] > 0}
    lo = min(Je) / (max(qs) ** 2) / alpha
    hi = max(Je) / (min(qs) ** 2) / alpha

    def old_ok(c):
        D, B, F, X, Y, _L, _E = c
        q = 1 if Y > 0 else 0
        ok = set()
        for Jz in (True, False):
            if Jz and (X > 0 or F == 1):
                continue
            ok.add(g.bound_class(D, q, F, Jz))
        if B not in ok:
            return False
        if X == 0 or Y == 0:
            return True
        d = sp[X - 1] - 2 * ch[Y - 1]
        return (10.0 ** (d - 2) < hi) and (10.0 ** (d + 1) > lo)

    wrong = sorted(c for c in dm if not old_ok(c) and c in img)
    if not wrong:
        return None
    target = wrong[0]
    for Z, N, A, sym, dmx, _q in g.nuclides():
        base = A * g.U_KG + dmx * g.KEV_J / c_ ** 2
        for q in range(0, Z + 1):
            M = base - q * g.M_E
            if M <= 0:
                continue
            aG = gn * M * M / (hbar * c_)
            Y = 0
            if q > 0:
                Y = chi.get(math.floor(math.log10(math.sqrt(q * q * alpha / aG))))
                if Y is None:
                    continue
            if Y != target[4]:
                continue
            F = (A + (Z - q)) % 2
            if F != target[2]:
                continue
            for tj in range(0, GRAVITY_JCUT + 1):
                if tj == 0:
                    X = 0
                else:
                    X = spi.get(math.floor(math.log10((tj / 2.0) / aG)))
                    if X is None:
                        continue
                if X != target[3]:
                    continue
                Jz = (Z % 2 == 0 and N % 2 == 0 and tj == 0)
                if g.bound_class(target[0], 1 if q > 0 else 0, F, Jz) == target[1]:
                    return (sym, A, q, tj)
    return None


def _b_gravity(c):
    """(D, B, F, X, Y, L, E) -- is this cell in the coordinate map's image?"""
    return c in gravity_image()


# ------------------------------------- DOCKET 49b, THE OPEN BARYON CELLS, BUILT
# An OPEN cell says only that no bound forbids it.  These say more: each names a
# quark content, an orbital L and a quark spin that REALISES it, so the residue
# is constructively open rather than merely unforbidden.
#
# TWO ERRORS WERE MADE HERE AND BOTH WERE CAUGHT BY THE INDEX ITSELF.  A first
# version enumerated only baryons and not antibaryons -- the seated bound has
# both -- and reported 77 cells unreachable that are reached by an antibaryon.
# A second added a symmetry rule: three IDENTICAL quarks have symmetric flavour,
# so spin-cross-space must be symmetric, which was taken to mean Sq = 3/2 with L
# even, forbidding negative parity.  THE SEATED MEMBERS REFUTE IT: uuu-flavour
# states are charted at 2J = 1, 3 and 5 with P = -1, which is Delta(1620) 1/2-,
# Delta(1700) 3/2- and a 5/2-.  Three identical quarks reach odd L through mixed
# spatial x mixed spin symmetry, and no such rule is imposed.
_QFLAV = {"u": (2, 0, 0, 0), "d": (-1, 0, 0, 0), "s": (-1, -1, 0, 0),
          "c": (2, 0, 1, 0), "b": (-1, 0, 0, -1)}


def baryon_witness(cell, lmax=8):
    """(quarks, is antibaryon, L, 2Sq) realising this cell, or None.

    P = (-1)^L for three quarks, and J couples L to Sq in {1/2, 3/2}.
    """
    j2, P, i2, q3, S, C, B = cell
    for combo in itertools.combinations_with_replacement("udscb", 3):
        v = [sum(_QFLAV[x][k] for x in combo) for k in range(4)]
        nu, nd = combo.count("u"), combo.count("d")
        nud = nu + nd
        if i2 not in range(max(abs(nu - nd), nud % 2), nud + 1, 2):
            continue
        for anti in (False, True):
            sg = -1 if anti else 1
            if (sg * v[0], sg * v[1], sg * v[2], sg * v[3]) != (q3, S, C, B):
                continue
            for L in range(lmax + 1):
                if (-1) ** L != P:
                    continue
                for s2 in (1, 3):
                    if abs(2 * L - s2) <= j2 <= 2 * L + s2:
                        return (combo, anti, L, s2)
    return None


def baryon_open_built():
    """(open cells, how many carry a witness) -- and they are equal."""
    import baryons
    X = frozenset(baryons.index())
    d = frozenset(demand.demand(X))
    fn = BOUNDS["baryons.index"][3]
    gap = GAPS["baryons.index"]()
    op = [c for c in d if fn(c) and not any(_pins(g, c) for g in gap)]
    return len(op), sum(1 for c in op if baryon_witness(c) is not None)


def _b_baryons_quark(c):
    """(2J, P, 2I, Q3, S, C, B) -- THE THREE-QUARK FLAVOUR BOUND."""
    _j, _P, i2, q3, S, C, B = c
    return (i2, q3, S, C, B) in quark_reachable()


BOUNDS = {
    "gravity.index": ("the cell lies in the IMAGE of the coordinate map, "
                      "exhausted over every nuclide, every ionisation stage "
                      "and every 2Je to saturation",
                      "exact solutions of the D-dimensional field equations, "
                      "and chi = Je/alpha_G with Qtilde^2 = q^2 alpha/alpha_G",
                      False, _b_gravity),
    "baryons.index": ("three-quark flavour content: (2I, Q3, S, C, B) is "
                      "realisable by qqq or by anti-qqq, with "
                      "|n_u - n_d| <= 2I <= n_ud and 2I = n_ud (mod 2)",
                      "the quark model, on the capture's own quark strings",
                      False, _b_baryons_quark),
    "ions.index": ("l <= n-1 at both ends; Pauli on k and g; q <= k",
                   "radial node count; Pauli exclusion", True, _b_ions),
    "fibred.index": ("l <= n-1; k <= 2(2l+1) - 1",
                     "radial node count; Pauli exclusion", True, _b_observed),
    "observed.index": ("l <= n-1; k <= 2(2l+1) - 1",
                       "radial node count; Pauli exclusion", True, _b_observed),
    "madrule.index": ("occ <= 2(2 floor((S_a-1)/2) + 1)",
                      "Pauli exclusion through the hidden l_a", True,
                      _b_madrule),
    "nucshell.index": ("l = 0 => sigma = +1",
                       "j = l +- 1/2 and j >= 0", True, _b_nucshell),
    "terms.index": ("mult = 1 => the term is not SHORT",
                    "Russell-Saunders: a singlet has one level", True,
                    _b_terms),
}

# The mesons carry a bound that is PROVED to forbid nothing.  That is a
# different statement from "no bound was derived" and is kept apart from it.
NO_BOUND_BY_THEOREM = ("mesons.index",)

NO_BOUND_DERIVED = (
    "readrezayi.index", "channels.index", "laws.index", "probability.index",
    "fqh.index", "fundamental.index", "inversion.index", "nucbands.index",
    "deformedbands.index",
)


# ---------------------------------------------------------- the source gaps
#
# A gap accessor returns [(known-coordinate tuple with None in the missing
# slot)] for every source row the module declined to chart.  A row missing more
# than one coordinate is returned too, and `_pins` drops it: the strength
# condition of section 4 is applied in one place and only one.

def _gap_mesons():
    return [(r[2], None, r[4], r[5]) for r in mesons.all_rows() if r[3] is None]


def _gap_baryons():
    import baryons
    return [(t[2], None) + t[4:] for t in baryons.all_rows() if t[3] is None]


def _gap_nucbands():
    import nucbands
    out = [(int(r["2I"]), None) for r in nucbands.levels()
           if r["2I"] and not r["par"]]
    # 27 bandheads with no I^pi and 6 level rows with no I^pi at all supply
    # NEITHER coordinate.  Returned so `_pins` can drop them on the rule.
    out += [(None, None) for r in nucbands.bandrows()
            if r["status"] == "NO-SPIN"]
    out += [(None, None) for _r in nucbands.unplaced_rows()]
    return out


def _gap_deformed():
    """Levels of the deformed bands carrying a spin and no parity.

    DOCKET 36b.  Measured rather than left out: they pin nothing, because the
    spins they carry top out well below the three demanded cells.  A zero that
    was looked for is a different thing from a zero nobody measured.
    """
    import deformedbands
    return [(i2, None) for i2, _A, _Z, _N, _e in deformedbands.no_parity()]


def _gap_channels():
    import channels

    def i(v):
        try:
            return int(v)
        except (TypeError, ValueError):
            return None
    return [(i(r["l"]), None, i(r["mult"])) for r in channels.malformed()]


def _gap_laws():
    import laws
    out = []
    for r in laws.rows():
        res, n = laws.residuals(r), laws._range(r["n"])
        lv = laws._num(r["levels"])
        if res is None or n is None or lv is None:
            out.append((None if n is None else int(n[1] - n[0]),
                        None if lv is None else int(lv),
                        None if res is None else int(abs(res[1] - res[0]) * 10)))
        elif laws.is_reversed(r):
            out.append((int(n[1] - n[0]), int(lv),
                        int(abs(res[1] - res[0]) * 10)))
    return out


GAPS = {
    "mesons.index": _gap_mesons,
    "baryons.index": _gap_baryons,
    "nucbands.index": _gap_nucbands,
    "channels.index": _gap_channels,
    "laws.index": _gap_laws,
    "deformedbands.index": _gap_deformed,
}

# Sources with no gap at all: every source row is charted, so UNPLACED is zero
# by construction and not by a failure to look.  The count each name carries is
# (source rows, rows charted), re-measured by `gapless()`.
GAPLESS = ("gravity.index",
           "readrezayi.index", "ions.index", "fibred.index",
           "probability.index", "fqh.index", "observed.index",
           "fundamental.index", "inversion.index", "madrule.index",
           "nucshell.index")

# The one index where the separation cannot be run, with what would settle it.
UNDECIDED = {
    "terms.index": (
        "terms._load() discards a bracketed jK/jj/Racah row without banking its "
        "term key, so the tree cannot ask whether any term lost ALL of its "
        "levels.  Such a term would pin a cell at strength arity-1.  SETTLED BY: "
        "banking the refused rows' keys."),
}


def _pins(partial, cell):
    """Does this partial source row pin this cell?  Section 4's rule, once."""
    if sum(1 for v in partial if v is None) != 1:
        return False
    return all(v is None or v == w for v, w in zip(partial, cell))


# --------------------------------------------------------------- the proofs

def max_closed(nm):
    """Is the bound's admissible set closed under componentwise max?

    EXHAUSTIVE over the index's own product box, so Law 3's hypothesis is
    verified rather than read off the algebra.  Returns (closed, witness).
    """
    label = BOUNDS[nm]
    fn = label[3]
    X = sorted(registry.index_of(nm))
    box = [sorted({c[i] for c in X}) for i in range(len(X[0]))]
    adm = [c for c in itertools.product(*box) if fn(c)]
    for a, b in itertools.combinations(adm, 2):
        c = tuple(map(max, a, b))
        if not fn(c):
            return False, (a, b, c)
    return True, None


def members_obey(nm):
    """(members, violations) -- a bound is checked against the seated index."""
    fn = BOUNDS[nm][3]
    X = registry.index_of(nm)
    return len(X), [c for c in sorted(X) if not fn(c)]


def qqbar(jmax=12):
    """{(2J, P)} realised by some q-qbar (L, S) with L <= jmax + 1, S in {0,1}."""
    out = set()
    for S in (0, 1):
        for L in range(0, jmax + 2):
            for J in range(abs(L - S), L + S + 1):
                if J <= jmax:
                    out.add((2 * J, (-1) ** (L + 1)))
    return out


def qqbar_theorem(jmax=12):
    """Section 1's theorem, checked: every (2J, P) with J <= jmax is realised."""
    want = {(2 * J, P) for J in range(jmax + 1) for P in (1, -1)}
    return want == qqbar(jmax), sorted(want - qqbar(jmax))


def _nets(quarks):
    """{flavour letter: quarks - antiquarks}, or None if the string is a mixture.

    The case convention is `mesons.QUARK_LETTERS`' -- lowercase is the quark --
    and it is IMPORTED, never restated: `mesons.case_convention()` pins it.
    """
    if not quarks or any(ch not in mesons.QUARK_LETTERS for ch in quarks):
        return None
    return {a: sum(-1 if ch.isupper() else 1 for ch in quarks
                   if ch.upper() == a) for a in "UDSCBT"}


def gmn_from_quarks(family):
    """(rows, parsed, charge ok, isospin weight ok, identity ok, [faults]).

    Section 3, re-derived from the capture's own quark strings.  Nothing here
    reads a textbook value: the charge is built from the quark charges, the
    isospin projection from (n_u - n_d), and the identity Q - I3 = Y/2 is then
    checked cell by cell against the capture's Q3 and I2.
    """
    n = parsed = okq = oki = okid = 0
    faults = []
    for r in pdgcapture.read():
        if r["family"] != family:
            continue
        n += 1
        z = _nets(r["quarks"])
        if z is None:
            continue
        parsed += 1
        nu, nd, ns, nc, nb, nt = (z["U"], z["D"], z["S"], z["C"], z["B"], z["T"])
        if 2 * (nu + nc + nt) - (nd + ns + nb) == int(r["Q3"]):
            okq += 1
        i2, t2 = int(r["I2"]), nu - nd
        if abs(t2) <= i2 and (i2 - t2) % 2 == 0:
            oki += 1
        else:
            faults.append((r["name"], r["quarks"], i2, t2))
        tot = nu + nd + ns + nc + nb + nt
        if tot % 3 == 0:
            Bn, S, C, B = tot // 3, -ns, nc, -nb
            if 2 * int(r["Q3"]) // 3 - (Bn + S + C + B) == t2:
                okid += 1
    return n, parsed, okq, oki, okid, faults


def bs2_consequence():
    """((cells, E, cell) as captured, the same with I2 = 0 on pdgid +-535).

    Section 3's second half.  The counterfactual is MEASURED and the capture is
    not touched: the rebuilt set is local to this function.
    """
    X = frozenset(mesons.index())
    Y = frozenset((j, P, 0 if abs(p) == 535 else i, q)
                  for _n, p, j, P, i, q in mesons.rows())
    f = lambda Z: (len(Z), demand.E(Z), mi.cell(Z))
    return f(X), f(Y)


def periodic2d():
    """The 90 drawn positions of the period x group table, as cypher builds it."""
    occ = [(1, 1), (1, 18)]
    occ += [(p, g) for p in (2, 3) for g in (1, 2, 13, 14, 15, 16, 17, 18)]
    occ += [(p, g) for p in (4, 5, 6, 7) for g in range(1, 19)]
    return frozenset(occ)


def element_precedent():
    """(cells, E_join, E_order, order ghosts failing l<=n-1, join ghosts failing).

    Law 6, measured.  `l` is read off the group exactly as `Transitions.md`
    L368 reads it -- s at 1-2, d at 3-12, p at 13-18 -- and `n` is the period.
    """
    X = periodic2d()
    J = D.joinclose(X)
    box = [sorted({c[i] for c in X}) for i in range(2)]
    S = D.stair(X, box)
    l_of = lambda g: 0 if g <= 2 else (1 if g >= 13 else 2)
    bad = lambda G: len([c for c in G if l_of(c[1]) > c[0] - 1])
    return len(X), len(J) - len(X), len(S) - len(X), bad(set(S) - X), bad(set(J) - X)


# --------------------------------------------------------- the adjudication

def adjudicate(nm):
    """(E, FORBIDDEN, UNPLACED, OPEN, UNDECIDED) for one seated index."""
    X = frozenset(registry.index_of(nm))
    d = sorted(demand.demand(X))
    fn = BOUNDS[nm][3] if nm in BOUNDS else None
    forb = [c for c in d if fn and not fn(c)]
    rest = [c for c in d if c not in set(forb)]
    if nm in UNDECIDED:
        return len(d), len(forb), 0, 0, len(rest)
    gap = GAPS[nm]() if nm in GAPS else []
    unp = [c for c in rest if any(_pins(g, c) for g in gap)]
    return len(d), len(forb), len(unp), len(rest) - len(unp), 0


def unplaced_objects(nm):
    """(cells pinned, source rows that pin at least one) -- never confused.

    D(s2)*(2573)+ lacks only P and so pins two cells it can fill only one of.
    """
    X = frozenset(registry.index_of(nm))
    d = sorted(demand.demand(X))
    gap = GAPS[nm]() if nm in GAPS else []
    cells = {c for c in d for g in gap if _pins(g, c)}
    rows = [g for g in gap if any(_pins(g, c) for c in d)]
    return len(cells), len(rows)


# Recorded so the default report does not re-close twenty-two indexes; the
# selftest RE-MEASURES a sample rather than trusting the table.
TABLE = {
    # DOCKET 42.  gravity was excluded from the demand on a ground stated as a
    # computational limit and measured to be false: it closes in about 16
    # seconds.  It carries no bound and no source gap, so all 1,550 are OPEN --
    # the largest single demand in the register, and the honest answer.
    "gravity.index": (1550, 1080, 0, 470, 0),
    # DOCKET 43.  893 -> 894 forbidden under the three-quark bound, against
    # Gell-Mann--Nishijima's 593, which it strictly contains.
    "baryons.index": (1012, 894, 8, 110, 0),
    "readrezayi.index": (678, 0, 0, 678, 0),
    "channels.index": (367, 0, 23, 344, 0),
    "ions.index": (296, 0, 0, 296, 0),
    "laws.index": (254, 0, 0, 254, 0),
    "fibred.index": (140, 0, 0, 140, 0),
    "probability.index": (112, 0, 0, 112, 0),
    "terms.index": (98, 0, 0, 0, 98),
    "fqh.index": (71, 0, 0, 71, 0),
    "observed.index": (56, 0, 0, 56, 0),
    "fundamental.index": (46, 0, 0, 46, 0),
    "inversion.index": (24, 0, 0, 24, 0),
    "madrule.index": (18, 0, 0, 18, 0),
    "mesons.index": (15, 0, 3, 12, 0),
    "nucshell.index": (14, 0, 0, 14, 0),
    "nucbands.index": (5, 0, 2, 3, 0),
    "deformedbands.index": (3, 0, 0, 3, 0),
}

TOTALS = (4759, 1974, 36, 2651, 98)


def totals():
    z = [0, 0, 0, 0, 0]
    for v in TABLE.values():
        z = [a + b for a, b in zip(z, v)]
    return tuple(z)


def gapless():
    """[(index, source rows, rows charted)] -- the GAPLESS claim, re-measured."""
    import fibred
    import fqh
    import fundamental
    import inversion
    import ions
    import madrule
    import nucshell
    import observed
    import probability
    import readrezayi
    return [
        ("observed.index", len([Z for Z in observed._lw1().GROUND
                                if Z <= observed.REACH]),
         len(observed.addresses())),
        ("fibred.index", fibred.REACH, len(fibred.addresses())),
        ("fundamental.index", len([r for r in pdgcapture.read()
                                   if r["family"] in fundamental.FAMILIES]),
         len(fundamental.rows())),
        ("nucshell.index", len(nucshell.order_a()), len(nucshell.order_a())),
        ("ions.index", len(ions.stage_rows()), len(ions.stage_rows())),
        ("fqh.index", len(fqh.rows()), len(fqh.rows())),
        ("readrezayi.index", len(readrezayi.rows()), len(readrezayi.rows())),
        ("probability.index", len(probability.index()),
         len(probability.index())),
        ("inversion.index", len(inversion.inversions()),
         len(inversion.inversions())),
        ("madrule.index", len(madrule.index()), len(madrule.index())),
        ("gravity.index",) + gravity_source_gap(),
    ]


# -------------------------------------------------------------------- tests

def selftest():
    ok = True

    def chk(lab, got, want):
        nonlocal ok
        good = got == want
        ok = ok and good
        print("  [%s] %-60s %s" % ("ok" if good else "XX", lab,
                                   got if good else "%s != %s" % (got, want)))

    # -------- LAW 1: the demand invents no coordinate value.
    for nm in ("mesons.index", "nucshell.index", "observed.index"):
        X = frozenset(registry.index_of(nm))
        J = D.joinclose(X)
        same = all({c[i] for c in J} == {c[i] for c in X}
                   for i in range(len(next(iter(X)))))
        chk("LAW 1 projection holds on %s" % nm, same, True)
    X = frozenset(registry.index_of("baryons.index"))
    chk("LAW 1 corollary: no demanded baryon cell has an even 2J",
        sum(1 for c in demand.demand(X) if c[0] % 2 == 0), 0)

    # -------- LAW 3: every monotone bound is max-closed, by exhaustion.
    for nm, (_lab, _law, mono, _fn) in sorted(BOUNDS.items()):
        got, wit = max_closed(nm)
        chk("LAW 3 max-closure of %-16s (declared monotone=%s)" % (nm, mono),
            (got, wit is None), (mono, mono))

    # -------- a bound is checked against its members before it is applied.
    for nm in sorted(BOUNDS):
        n, bad = members_obey(nm)
        chk("bound on %-18s holds on all %3d members" % (nm, n), bad, [])

    # -------- LAW 5: the q-qbar theorem, and the exotics it does not reach.
    good, missing = qqbar_theorem(12)
    chk("LAW 5 theorem: every (2J, P) up to J = 12 is a q-qbar state",
        (good, missing), (True, []))
    chk("and no exotic is expressible: C is not a meson coordinate",
        [c for c in mesons.NAMES if c in ("C", "G")], [])

    # -------- LAW 6 / the DOCKET 38 correction.
    cells, ej, eo, fo, fj = element_precedent()
    chk("LAW 6 periodic 2-D: 90 cells, E_join = 0, E_order = 36",
        (cells, ej, eo), (90, 0, 36))
    chk("and l <= n-1 forbids 25 order ghosts and 0 join ghosts", (fo, fj),
        (25, 0))

    # -------- section 3: Gell-Mann--Nishijima off the quark strings.
    n, p, q, i, d_, f = gmn_from_quarks("baryon")
    chk("GMN on baryons: 292 rows, all parse, all three legs clean",
        (n, p, q, i, d_, f), (292, 292, 292, 292, 292, []))
    n, p, q, i, d_, f = gmn_from_quarks("meson")
    chk("GMN on mesons: 250 rows, 191 parse (59 are mixtures)", (n, p), (250, 191))
    chk("charge and the identity clean, the isospin weight fails twice",
        (q, d_, i), (191, 191, 189))
    chk("and the two are B(s2)*(5840) and its antiparticle",
        sorted(x[0] for x in f),
        ["B(s2)*(5840)0", "B(s2)*(5840)~0"])
    chk("both carry sb-bar with I2 = 1", sorted({(x[1].lower(), x[2], x[3])
                                                 for x in f}),
        [("sb", 1, 0)])
    a, b = bs2_consequence()
    chk("and correcting it moves nothing: cells, E and cell all unchanged",
        (a == b, a), (True, (66, 15, (0, 10, 14))))

    # -------- section 4: the separator.  THE WHOLE TABLE IS RE-MEASURED, not a
    # sample of it: the sixteen close in about eight seconds together, so there
    # is no reason to trust a recorded row.
    drift = [(nm, adjudicate(nm), v) for nm, v in sorted(TABLE.items())
             if adjudicate(nm) != v]
    chk("every recorded row re-measured from the tree", drift, [])
    chk("the strength rule drops a row missing two coordinates",
        _pins((None, None, 3), (1, 2, 3)), False)
    chk("and keeps one missing exactly one", _pins((1, None, 3), (1, 2, 3)), True)
    chk("three meson cells are pinned by two objects, not three",
        unplaced_objects("mesons.index"), (3, 2))

    # -------- the gapless claim is measured, not assumed.
    bad = [(nm, a, b) for nm, a, b in gapless() if a != b]
    chk("every GAPLESS source charts every row it holds", bad, [])
    chk("and the ten named are the ten measured",
        sorted(nm for nm, _a, _b in gapless()), sorted(GAPLESS))

    # -------- the books balance.
    chk("the table sums to the totals", totals(), TOTALS)
    chk("and its E column is predict.py's live total", totals()[0],
        __import__("predict").total())
    # THE LEDGER GUARD.  An audit pointed out that nothing tied this table to
    # the registry.  A seated index needs a row here only if it DEMANDS
    # something: an E = 0 index has nothing to adjudicate, and `gravity` is
    # named too large to close.  So the partition must be exact three ways.
    import predict as _pred
    _seated = {nm for nm, *_r in registry.rows()}
    _zero = {n for n, e in _pred.E_BY_INDEX.items() if e == 0}
    chk("every seated index is adjudicated, complete, or named too large",
        sorted(_seated - (set(TABLE) | _zero | set(_pred.TOO_LARGE))), [])
    chk("and the three groups do not overlap",
        sorted((set(TABLE) & _zero) | (set(TABLE) & set(_pred.TOO_LARGE))), [])
    chk("every index with E > 0 is adjudicated exactly once",
        sorted(TABLE), sorted(set(BOUNDS) | set(NO_BOUND_BY_THEOREM)
                              | set(NO_BOUND_DERIVED)))
    chk("and terms is the only UNDECIDED", sorted(UNDECIDED), ["terms.index"])

    # ------------------------------------------------- DOCKET 49, THE RESIDUES
    # Both large indexes are CLOSED: every demanded cell is FORBIDDEN, UNPLACED
    # or OPEN, and each zero is measured with a reason rather than left blank.
    chk("gravity closes: 1,080 forbidden + 0 unplaced + 470 open = 1,550",
        adjudicate("gravity.index"), (1550, 1080, 0, 470, 0))
    # THE CUTOFF IS NOT A FREE PARAMETER.  The image stops growing at 2Je = 16
    # and is identical at 32 and 64, so the figure does not depend on where the
    # sweep is stopped -- which is what removes the last fitted range from this
    # bound.  An earlier version capped Je at the OBSERVED maximum and forbade
    # 148 cells the parameter space reaches, Zr-113 at q = 1, 2Je = 15 among
    # them.  Saturation is checked, not assumed.
    chk("and the image SATURATES, so the 2Je cutoff is not a parameter",
        [n for _k, n in gravity_image_saturates()[1:]], [1416, 1416, 1416])
    # THE GAP WAS A COUNTING ERROR AND IS WITHDRAWN.  A first version reported
    # 31 declined species "with no readable J"; their J columns parse perfectly
    # and they are duplicate FILES for species already charted.  gravity's
    # source is gapless, so UNPLACED is zero because there is nothing to place,
    # not because declined rows are too weak to pin.
    _named, _charted = gravity_source_gap()
    chk("gravity's source is GAPLESS -- every species named is charted",
        _named == _charted and _named > 0, True)
    chk("so it is declared gapless rather than given a gap function",
        ("gravity.index" in GAPLESS, "gravity.index" in GAPS), (True, False))
    chk("baryons closes: 894 forbidden + 8 unplaced + 110 open = 1,012",
        adjudicate("baryons.index"), (1012, 894, 8, 110, 0))
    # EVERY open baryon cell carries an ODD doubled spin, as three spin-1/2
    # quarks require, and every (2J, P) it uses occurs in a seated member.  The
    # SU(6) constraint that would couple I to J further binds GROUND states
    # only; this index holds orbitally excited baryons, where L is hidden and
    # free, so by Law 5 it forbids nothing here.  That is why 110 is the floor.
    import baryons as _bar
    _Xb = frozenset(_bar.index())
    _Db = frozenset(demand.demand(_Xb))
    _fn = BOUNDS["baryons.index"][3]
    _gp = GAPS["baryons.index"]()
    _op = [c for c in _Db if _fn(c) and not any(_pins(g, c) for g in _gp)]
    chk("every OPEN baryon cell has an odd 2J", [c for c in _op if c[0] % 2 == 0], [])
    # DOCKET 49b.  Every open cell is CONSTRUCTIVELY realisable, not merely
    # unforbidden -- each names a quark content, an L and a quark spin.
    _nopen, _nbuilt = baryon_open_built()
    chk("and every OPEN baryon cell is BUILT by the quark model",
        (_nopen, _nbuilt), (110, 110))
    # The witness test must also pass on every SEATED member, or it is too
    # loose to mean anything.
    chk("and the same witness test reaches every seated member",
        [m for m in _Xb if baryon_witness(m) is None], [])
    # THE RULE THE INDEX REFUTED.  Three identical quarks DO reach negative
    # parity; a symmetry rule forbidding it would have declared these
    # impossible, and they are seated.
    chk("uuu-flavour states are seated at negative parity, so no such rule",
        sorted(c[0] for c in _Xb
               if (c[2], c[3], c[4], c[5], c[6]) == (3, 6, 0, 0, 0)
               and c[1] == -1), [1, 3, 5])
    chk("and every (2J, P) it uses is one a seated member exhibits",
        sorted({(c[0], c[1]) for c in _op} - {(m[0], m[1]) for m in _Xb}), [])

    # The gravity bound's physical inputs are cited, not proved here.
    chk("four physical inputs to the gravity bound, each cited",
        len(GRAVITY_SOURCES), 4)
    # And alpha_G cancels: the ratio is mass-free.  Checked, not asserted.
    import gravity as _g
    _al = 7.2973525693e-3
    _hb, _c, _G = 1.054571817e-34, 2.99792458e8, 6.67430e-11
    _bad = 0
    for _m in _g.members():
        _q, _tj, _M, _chi, _qt = _m[3], _m[5], _m[9], _m[10], _m[11]
        if _chi <= 0 or _qt <= 0:
            continue
        _aG = _G * _M * _M / (_hb * _c)
        if abs(_chi - (_tj / 2.0) / _aG) / _chi > 1e-9:
            _bad += 1
        if abs(_qt * _qt - _q * _q * _al / _aG) / (_qt * _qt) > 1e-9:
            _bad += 1
    chk("chi = Je/alpha_G and Qtilde^2 = q^2 alpha/alpha_G, so alpha_G cancels",
        _bad, 0)

    print("ghosts selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


def report():
    print("=" * 79)
    print("DOCKET 39 -- THE ADJUDICATION OF E")
    print("=" * 79)
    print()
    print("1. THE LAWS")
    print("   L1 PROJECTION      pi_i(J(X)) = pi_i(X).  The demand invents no")
    print("                      coordinate value, so NO SINGLE-COORDINATE BOUND")
    print("                      CAN FORBID ANYTHING.")
    print("   L2 MAX-STABILITY   X in B and B max-closed => J(X) in B.")
    print("   L3 MONOTONE        x_i <= f(x_j) with f non-decreasing is")
    print("      VACUITY         max-closed, hence forbids nothing.  Every")
    print("                      atomic and nuclear bound in this tree is of")
    print("                      that shape.")
    print("   L4 WHAT FORBIDS    only a bound that is antitone somewhere or")
    print("                      carries a congruence.  One qualifies here.")
    print("   L5 EXPRESSIBILITY  a hidden variable free to range forbids")
    print("                      nothing; the coordinates must bound its range.")
    print("   L6 OPERATOR        E is a deficit against an OPERATOR, and which")
    print("      RELATIVITY      cells a bound forbids depends on which.")
    print("   L7 CHART, NOT      forbidding power is a property of the chart.")
    print("      BOUND           It is not evidence that the chart is right.")
    print()
    print("2. THE BOUND PER INDEX")
    print("   %-20s %-44s %s" % ("index", "bound", "mono"))
    for nm, (lab, _law, mono, _fn) in sorted(BOUNDS.items()):
        print("   %-20s %-44s %s" % (nm, lab[:44], "yes" if mono else "NO"))
    for nm in NO_BOUND_BY_THEOREM:
        print("   %-20s %-44s %s" % (nm, "NONE -- and the absence is a THEOREM", "-"))
    print("   %-20s %-44s %s"
          % ("(%d others)" % len(NO_BOUND_DERIVED),
             "none derived -- see section 5's refusal", "-"))
    print()
    print("3. GELL-MANN--NISHIJIMA, RE-DERIVED FROM THE QUARK STRINGS")
    for fam in ("baryon", "meson"):
        n, p, q, i, d_, f = gmn_from_quarks(fam)
        print("   %-8s rows %3d  parse %3d  charge %3d  weight %3d  identity %3d"
              % (fam, n, p, q, i, d_))
        for nm, qk, i2, t2 in f:
            print("       FAULT  %-18s %-4s I2 = %d but 2I3 = %d"
                  % (nm, qk, i2, t2))
    a, b = bs2_consequence()
    print("   the fault's consequence for the index: %s -> %s  (%s)"
          % (a, b, "nothing moves" if a == b else "MOVES"))
    print()
    print("4. THE ADJUDICATION")
    print("   %-20s %6s %6s %6s %6s %6s"
          % ("index", "E", "FORB", "UNPL", "OPEN", "UNDEC"))
    for nm, v in sorted(TABLE.items(), key=lambda kv: -kv[1][0]):
        print("   %-20s %6d %6d %6d %6d %6d" % ((nm,) + v))
    print("   %-20s %6d %6d %6d %6d %6d" % (("TOTAL",) + totals()))
    print()
    E, F = TABLE["baryons.index"][0], TABLE["baryons.index"][1]
    print("   FORBIDDEN is %d cells and every one of them is a baryon cell"
          % totals()[1])
    print("   Gell-Mann--Nishijima empties -- %.1f%% of the largest prediction"
          % (100.0 * F / E))
    print("   set in the register, by theorem.  Everywhere else FORBIDDEN is")
    print("   zero AND LAW 3 SAYS IT HAD TO BE.")
    print()
    for nm, why in sorted(UNDECIDED.items()):
        print("   UNDECIDED  %s" % nm)
        for ln in why.split("  "):
            if ln.strip():
                print("      %s" % ln.strip())
    print()
    print("5. WHAT THIS FILE REFUSES")
    print("   To call %s a count of undiscovered objects.  For the %d"
          % (format(totals()[3], ","), len(BOUNDS)))
    print("   indexes with a derived bound it is FINAL AGAINST EVERY MONOTONE")
    print("   BOUND, by Law 3.  For the %d with none derived it is open"
          % len(NO_BOUND_DERIVED))
    print("   against nothing at all.  The two are not summed into one word.")
    print("   To repair the B(s2)*(5840) rows.  Measured, recorded, held.")
    print("   To read Law 7 as an argument for the withdrawn 2-D layout.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    sys.exit(report())
