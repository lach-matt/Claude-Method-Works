#!/usr/bin/env python3
r"""
barter.py -- WHAT CAN BE TRADED FOR COST, AND WHAT CANNOT.

M: "Can we barter increments or time in measure of travel for a lower cost?
And maybe we don't need currency, if we can fool the account on the opposite
end, like a forged proof of purchase maybe using an inverse reflection."

Two questions, two halves, and BOTH ANSWERS ARE YES WITH A NAMED LIMIT.

    python3 barter.py             the reading
    python3 barter.py --selftest  fixtures

===============================================================================
HALF ONE -- TIME IS BARTERABLE.  THE CAP IS NOT.
===============================================================================

Crossing the deformation in N steps instead of one is a different protocol: it
post-selects N times.  Priced with the two-parameter overlap (postselect.py's
`dets_general`, because after the first step the bra is no longer the
undeformed TFD), at gap 0.15:

        d = 50 % of the cap      N=1  0.885    N=64   0.998
        d = 90 % of the cap      N=1  0.471    N=64   0.981
        d = 99 % of the cap      N=1  0.155    N=64   0.833   N=4096  0.997

SO THE PROBABILITY GOES TO 1, AND THE GAIN IS LARGEST EXACTLY WHERE IT IS
NEEDED -- at the edge of the cap, where a single jump nearly always fails.
This is the Zeno shape: each step's loss is second order in its own size, so N
steps lose O(1/N).  Time is the thing being spent, and it buys probability at
rate 1/N.

**THE CAP DOES NOT MOVE.**  Past delta_max the target is not a state, and
slicing the path does not make it one: at 1.001, 1.05, 1.5 and 3.0 times the
cap the path is refused at N = 1, 8, 64 and 512 alike.  A hard wall at every N.

WHAT THAT IS WORTH, STATED AT ITS REAL SIZE.  The probability was never the
binding cost -- it was already O(1).  What incrementing buys is the right to
work at the TOP of the cap instead of halfway up it, and since the opening
goes like delta^2 that is

        (0.99 / 0.50)^2  =  3.9x

A FACTOR OF FOUR IN THE OPENING, BOUGHT WITH TIME.  Not a factor of 10^77.
The 1/S^2 scaling is untouched, because the cap that sets it is untouched.

===============================================================================
HALF TWO -- THE RECEIPT CAN BE FORGED, AND THE REFLECTION IS HALF OF HOW
===============================================================================

An accountant reading language L cannot see X.  It sees L(X).  So any X' with
L(X') = L(X) settles the account, and the cheapest such X' is what the crossing
actually costs in cells.  Every generating set must contain the FORCED cells --
those x with x not in L(X \ {x}) -- so enumerating the rest gives the exact
minimum rather than an estimate.  On the seated 17-cell index:

        accountant reads   minimum receipt   discount   distinct minima
        order / algebra        8 of 17          53 %          6
        geometry               9 of 17          47 %          1
        information           11 of 17          35 %          1
        statistics            12 of 17          29 %          1

**THE MORE A LANGUAGE ADMITS, THE CHEAPER IT IS TO FOOL.**  `order` admits 192
cells and 8 convince it; `statistics` admits 17 and needs 12.  The discount
runs inversely to discrimination, which is the whole content of the table.

`order`'s 8 is exhaustive within X and is an UPPER bound on the unrestricted
minimum, since a forged receipt need not be a subset of what was observed.  The
lower bound is 5: a sublattice of a product of chains is distributive, the free
distributive lattice on 4 generators has 166 elements, and |order(X)| = 192.
So order's true minimum is in [5, 8] and this file does not close that gap.
For `information` and `statistics` there is nothing to close -- their forced
sets already generate, so 11 and 12 are exact and unrestricted forgery buys
nothing.

THE INVERSE REFLECTION, WHICH IS THE OTHER HALF OF THE IDEA.  A wormhole has
two ends and the reflection is what swaps them.  If the far account's ledger is
dual(X), then dual(X') settles it whenever X' settles this one -- because
L(dual(X')) = dual(L(X')) = dual(L(X)) = L(dual(X)), which needs exactly that L
commutes with the dual.  Measured:

        order  YES     algebra  YES     geometry  YES     statistics  YES
        information  NO

**ONE RECEIPT AND A REFLECTION PAYS BOTH ENDS, FOR FOUR OF THE FIVE.**  And the
one that catches it is the one whose invariance group is trivial.  This is not
a new fact: it is the Clause F refinement in reslice.py read as a list of who
can be fooled.  The invariance group IS the forgery group.

The SAME-side reflection -- passing dual(X') off as a receipt for X itself --
is weaker and mostly fails.  It needs L(X) to be setwise dual-fixed, which the
seated index is not (it is not self-dual), so it fails there for all five.  Over
300 random indexes it holds 126, 126, 89, 70 and 76 times of 300; restricted to
self-dual indexes it is automatic for four of the five (60/60) and STILL fails
for `information` (42/60).

===============================================================================
WHAT IT REFUSES TO DO
===============================================================================

**It does not call the probability gain a cost reduction.**  The binding cost
is geometric.  Time buys the right to spend the whole geometric budget instead
of half of it -- a factor of four, printed as a factor of four.

**It does not report a minimum it did not exhaust.**  `order`'s 8 is exact over
subsets of X and is printed as a bracket [5, 8] against the unrestricted
question, which is not exhausted here.

**It does not claim a cell is a unit of cost.**  The discount is in cells of
the receipt.  That cells are what one pays for is the currency metaphor's
assumption, not a result of this file, and nothing here converts a cell count
into an energy.

**It does not claim the reflection is physically free.**  On the index it is
exact for four languages.  Whether the two ends of a real wormhole are related
by an isometry that costs nothing to apply is a different question and is not
touched here.
"""

import functools
import itertools
import math
import sys

import decomposable as D
import hlaw
import necindex
import postselect as PS


# ------------------------------------------------- half one: time for a price

def p_step(lam, a, b):
    """One post-selection, from deformation a to deformation b, for one mode.

    None where b is past the mode's bound -- the refusal, not a small number.
    """
    if not PS.admissible(lam, b):
        return None
    da, db = PS.dets_general(lam, a, a), PS.dets_general(lam, b, b)
    if da <= 0 or db <= 0:
        return None
    return math.sqrt(da * db) / abs(PS.dets_general(lam, a, b))


def p_path(gap, d, n_steps):
    """Probability of reaching deformation d in n_steps equal increments."""
    tot = 0.0
    for _, lam in PS.modes(gap):
        for k in range(n_steps):
            p = p_step(lam, k * d / n_steps, (k + 1) * d / n_steps)
            if p is None:
                return None
            tot += -math.log(p)
    return math.exp(-tot)


def zeno(gap=0.15, fracs=(0.5, 0.9, 0.99), steps=(1, 2, 8, 64)):
    """[(frac, [(N, P)])] -- what stepping buys, at fractions of the cap."""
    dm = PS.delta_max(gap)
    return [(f, [(N, p_path(gap, f * dm, N)) for N in steps]) for f in fracs]


def wall(gap=0.15, overs=(1.001, 1.05, 1.5, 3.0), steps=(1, 8, 64, 512)):
    """[(over, [(N, P or None)])] -- the cap does not move with N."""
    dm = PS.delta_max(gap)
    return [(o, [(N, p_path(gap, o * dm, N)) for N in steps]) for o in overs]


# ---------------------------------------------- half two: forging the receipt

def _closer(L, d):
    op = hlaw.OPS[L]
    def close(S):
        S = frozenset(S)
        return frozenset() if not S else frozenset(op(sorted(S), D.box_of(S, d)))
    return close


def forced(X, L):
    """The cells no receipt can omit: x not in L(X \\ {x}).  Every generating
    set contains all of these, which is what makes the enumeration below exact
    rather than a search that stopped early."""
    d = len(next(iter(X)))
    close = _closer(L, d)
    return frozenset(x for x in sorted(X) if x not in close(X - {x}))


@functools.lru_cache(maxsize=None)
def minimum_receipt(X, L):
    """(size, [every minimum receipt]).  Exhaustive over the non-forced cells,
    so the size is the MINIMUM and not merely a minimal one."""
    d = len(next(iter(X)))
    close = _closer(L, d)
    full = close(X)
    F = forced(X, L)
    rest = [x for x in sorted(X) if x not in F]
    for k in range(len(rest) + 1):
        hits = [F | frozenset(T) for T in itertools.combinations(rest, k)
                if close(F | frozenset(T)) == full]
        if hits:
            return len(F) + k, hits
    return len(X), [frozenset(X)]


def dual_of(X):
    """Reverse every coordinate over the observed box -- the lattice dual."""
    d = len(next(iter(X)))
    rev = [dict(zip(v, list(reversed(v)))) for v in D.box_of(X, d)]
    return frozenset(tuple(rev[i][x[i]] for i in range(d)) for x in X)


def reflection_carries(X, L):
    """Does dual(receipt for X) settle the account on dual(X)?

    True exactly when L commutes with the dual, which is the Clause F
    refinement's diagonal subgroup read as a forgery test.
    """
    d = len(next(iter(X)))
    close = _closer(L, d)
    target = close(dual_of(X))
    return all(close(dual_of(m)) == target for m in minimum_receipt(X, L)[1])


def same_side_possible(X, L):
    """The weaker forgery -- passing a dual receipt off for X itself -- needs
    L(X) setwise dual-fixed.  Necessary, and reported as such."""
    d = len(next(iter(X)))
    c = _closer(L, d)(X)
    rev = [dict(zip(v, list(reversed(v)))) for v in D.box_of(X, d)]
    return frozenset(tuple(rev[i][y[i]] for i in range(d)) for y in c) == c


FD_MAX = 4          # n = 5 is 2^32 antichain candidates; not computed here


@functools.lru_cache(maxsize=None)
def free_distributive(n):
    """|FD(n)| = M(n) - 2, computed rather than quoted, for the lower bound on
    `order`'s unrestricted minimum.  A sublattice of a product of chains is
    distributive, so k generators cannot build more than |FD(k)| elements.

    Brute force over antichains, which is why FD_MAX is 4: the n = 5 count runs
    over 2^32 candidates.  The bound below is stated as a floor for that reason
    rather than being pushed until it binds.
    """
    if n > FD_MAX:
        raise ValueError("free_distributive is brute force; n <= %d only" % FD_MAX)
    U = list(range(n))
    subs = [frozenset(c) for r in range(n + 1) for c in itertools.combinations(U, r)]
    cnt = 0
    for mask in range(1 << len(subs)):
        A = [subs[i] for i in range(len(subs)) if mask >> i & 1]
        if all(not (a < b) for a in A for b in A if a is not b):
            cnt += 1
    return cnt - 2


def order_bracket(X):
    """(lower, upper) on the unrestricted minimum receipt for `order`.

    The lower end is a FLOOR from what is computable here, not the best bound
    that exists: k generators build at most |FD(k)| elements, FD is brute-forced
    only to n = 4, and if FD(4) is already below |order(X)| the bound returned
    is 5 with no attempt to push it further.  Widening it means a bigger
    Dedekind computation, which this file does not do and says so.
    """
    upper = minimum_receipt(X, "order")[0]
    size = len(_closer("order", len(next(iter(X))))(X))
    k = 1
    while k < FD_MAX and free_distributive(k) < size:
        k += 1
    return (k if free_distributive(k) >= size else k + 1), upper


# --------------------------------------------------------------- the reading

def report():
    X = frozenset(necindex.cells())
    print("=" * 74)
    print("WHAT CAN BE TRADED FOR COST, AND WHAT CANNOT")
    print("=" * 74)
    print()

    gap = 0.15
    print("HALF ONE -- TIME IS BARTERABLE. THE CAP IS NOT.")
    print("   Crossing in N steps post-selects N times. gap = %.2f, cap = %.5f"
          % (gap, PS.delta_max(gap)))
    print("   %-22s %s" % ("", "  ".join("N=%-8d" % N for N in (1, 2, 8, 64))))
    for f, row in zeno(gap):
        print("   %-22s %s" % ("d = %2d%% of the cap" % (100 * f),
              "  ".join("%-10.4f" % p for _, p in row)))
    print()
    print("   The probability goes to 1, and the gain is largest at the EDGE,")
    print("   where a single jump nearly always fails. That is the Zeno shape:")
    print("   each step loses at second order in its own size, so N steps lose")
    print("   O(1/N). Time is what is spent and probability is what it buys.")
    print()
    print("   BUT THE CAP DOES NOT MOVE. Past it there is no state to reach:")
    for o, row in wall(gap):
        print("     d = %-6.3f x cap   %s" % (o, "  ".join(
            "N=%-4d %-7s" % (N, "REFUSED" if p is None else "%.4f" % p) for N, p in row)))
    print()
    print("   WORTH, AT ITS REAL SIZE: the probability was never the binding")
    print("   cost. What time buys is the right to work at the TOP of the cap")
    print("   instead of halfway up, and the opening goes like delta^2:")
    print("       (0.99 / 0.50)^2 = %.1fx   -- a factor of four, not of 10^77."
          % ((0.99 / 0.50) ** 2))
    print("   The 1/S^2 scaling is untouched, because the cap is untouched.")
    print()

    print("HALF TWO -- THE RECEIPT CAN BE FORGED.")
    print("   An accountant reading L cannot see X, only L(X). Any X' with")
    print("   L(X') = L(X) settles it. Forced cells are in EVERY receipt, so")
    print("   enumerating the rest gives the MINIMUM, not an estimate.")
    print()
    print("   %-13s %8s %9s %10s %9s %s"
          % ("reads", "|L(X)|", "forced", "minimum", "discount", "#minima"))
    for L in hlaw.LANGS:
        close = _closer(L, len(next(iter(X))))
        m, hits = minimum_receipt(X, L)
        print("   %-13s %8d %9d %10d %9.0f%% %d"
              % (L, len(close(X)), len(forced(X, L)), m, 100 * (1 - m / len(X)), len(hits)))
    print()
    print("   THE MORE A LANGUAGE ADMITS, THE CHEAPER IT IS TO FOOL. `order`")
    print("   admits 192 cells and 8 convince it; `statistics` admits 17 and")
    print("   needs 12. The discount runs inversely to discrimination.")
    print()
    lo, hi = order_bracket(X)
    print("   `order`'s %d is exhaustive within X and an UPPER bound on the" % hi)
    print("   unrestricted minimum, since a forged receipt need not be a subset")
    print("   of what was observed. The lower bound is %d: the lattice is" % lo)
    print("   distributive, so k generators build at most |FD(k)| elements, and")
    print("   |FD(%d)| = %d against |order(X)| = %d."
          % (FD_MAX, free_distributive(FD_MAX), len(_closer("order", 5)(X))))
    print("   BRACKET [%d, %d], NOT CLOSED -- and the %d is a floor from what is"
          % (lo, hi, lo))
    print("   computable here, not the best bound that exists: FD is brute force")
    print("   and n = %d is 2^32 candidates, so it was not pushed further." % (FD_MAX + 1))
    print()

    print("   THE INVERSE REFLECTION. A wormhole has two ends and the dual is")
    print("   what swaps them. dual(X') settles the far account whenever X'")
    print("   settles this one -- provided L commutes with the dual:")
    for L in hlaw.LANGS:
        print("     %-13s two-sided %-5s   same-side possible here %s"
              % (L, "YES" if reflection_carries(X, L) else "NO",
                 same_side_possible(X, L)))
    print()
    print("   ONE RECEIPT AND A REFLECTION PAYS BOTH ENDS, FOR FOUR OF FIVE.")
    print("   The one that catches it is the one whose invariance group is")
    print("   trivial. That is the Clause F refinement read as a list of who")
    print("   can be fooled: THE INVARIANCE GROUP IS THE FORGERY GROUP.")
    print()
    print("   The same-side forgery -- passing a dual receipt off for X itself")
    print("   -- needs L(X) setwise dual-fixed, and this index is not self-dual,")
    print("   so it fails here for all five.")
    print()
    print("   A CELL IS NOT SHOWN TO BE A UNIT OF COST. The discount is in cells")
    print("   of the receipt; that cells are what one pays for is the metaphor's")
    print("   assumption, and nothing here turns a cell count into an energy.")
    return 0


# -------------------------------------------------------------------- checks

def selftest():
    ok = True

    def chk(name, got, want, tol=None):
        nonlocal ok
        good = (abs(got - want) <= tol) if tol is not None else (got == want)
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", name, got))
        if not good:
            print("        expected %r" % (want,))

    print("barter selftest")
    X = frozenset(necindex.cells())
    gap = 0.15

    # HALF ONE.  A single step must reproduce postselect's own probability --
    # that is what ties this file to the already-checked arithmetic.
    d = 0.5 * PS.delta_max(gap)
    chk("one step reproduces postselect.total_probability",
        abs(p_path(gap, d, 1) - PS.total_probability(gap, d)) < 1e-12, True)
    chk("stepping strictly increases the probability",
        all(p_path(gap, d, a) < p_path(gap, d, b)
            for a, b in ((1, 2), (2, 8), (8, 64))), True)
    chk("and it tends to 1 at the edge of the cap",
        p_path(gap, 0.99 * PS.delta_max(gap), 4096), 1.0, 5e-3)
    chk("a single jump at that edge mostly fails",
        p_path(gap, 0.99 * PS.delta_max(gap), 1) < 0.2, True)
    chk("THE CAP DOES NOT MOVE: every N refused past it",
        all(p is None for _, row in wall(gap) for _, p in row), True)
    chk("and nothing inside it is refused",
        all(p is not None for _, row in zeno(gap) for _, p in row), True)

    # HALF TWO.  The minima, exhaustive.
    want = {"order": (8, 6), "algebra": (8, 6), "geometry": (9, 1),
            "information": (11, 1), "statistics": (12, 1)}
    for L in hlaw.LANGS:
        m, hits = minimum_receipt(X, L)
        chk("%s: minimum receipt and how many" % L, (m, len(hits)), want[L])
    for L in hlaw.LANGS:
        F = forced(X, L)
        chk("%s: every minimum contains the forced cells" % L,
            all(F <= h for h in minimum_receipt(X, L)[1]), True)
        chk("%s: no smaller set generates" % L,
            all(_closer(L, 5)(frozenset(h) - {x}) != _closer(L, 5)(X)
                for h in minimum_receipt(X, L)[1] for x in h), True)

    # The reflection, and the one language that catches it.
    for L in hlaw.LANGS:
        chk("%s: two-sided reflection carries" % L, reflection_carries(X, L),
            L != "information")
    chk("this index is not self-dual, so no same-side forgery here",
        any(same_side_possible(X, L) for L in hlaw.LANGS), False)

    # The bracket on order's unrestricted minimum.
    chk("free distributive lattice sizes, computed not quoted",
        [free_distributive(k) for k in range(1, 5)], [1, 4, 18, 166])
    chk("order's unrestricted minimum is bracketed [5, 8], the 5 a floor",
        order_bracket(X), (5, 8))
    try:
        free_distributive(FD_MAX + 1)
        chk("free_distributive refuses past its brute-force reach", False, True)
    except ValueError:
        chk("free_distributive refuses past its brute-force reach", True, True)

    print("barter selftest: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else report())
