#!/usr/bin/env python3
r"""
mcheck_mi.py -- MACHINE-CHECKED foundations of the six-index classification.

Two claims the classification rests on are not facts about the seated indexes at
all -- they are claims about EVERY finite index -- and until now both were only
measured.  Z3 discharges them over every subset of a named box.

    python3 mcheck_mi.py            run the obligations
    python3 mcheck_mi.py --guards   the two soundness guards only

WHAT IS AND IS NOT ESTABLISHED HERE.  A `unsat` on the negation is a proof that
no counterexample exists IN THE NAMED BOX.  Nothing here is a claim about
unbounded boxes or higher arity, and PROOF-ASSISTANT.md's ceiling applies
unchanged: what is machine-checked is named, and nowhere else.

===============================================================================
THE OBLIGATIONS
===============================================================================

O1  CLOSERS IS A DOWN-SET.  The set of languages that close X is always a
    down-set of the language poset.  This is what makes "eight lawful channels
    out of thirty-two subsets" a theorem rather than a census: the eight are the
    down-sets, and no index can occupy any other subset.

O2  K0 IS UNIVERSAL.  Every non-empty index has a cell that no language refuses.
    Measured as 9 of 9 across the seated inventory; here it is proved for every
    subset of the box, which is a different and stronger statement.

O3  K7 IS NOT UNIVERSAL.  A witness exists -- an index with no cell that every
    language refuses.  This is a REFUTATION, and it matters because the seated
    nine all have such a cell and the plates say so.  That is a fact about the
    nine, not a law, and O3 is why the distinction is drawn.

O4  A MONOTONE REDUNDANT COORDINATE PRESERVES THE CHANNEL.  Append g(x) = x_0 to
    every cell of X.  The resulting index closes in exactly the same languages.
    This is the engine of the chart criterion -- it is what makes "invariant
    under a monotone redundant coordinate" a well-posed admissibility test --
    and it was measured on nine indexes.  Here it is proved over every subset of
    a 3 x 3 box.

===============================================================================
THE SPANNING HYPOTHESIS, AND WHY O1 AND O4 CARRY IT
===============================================================================

hlaw.closures takes the box to be the OBSERVED alphabet -- box_of(X) is, on each
axis, the sorted set of values X actually uses.  This harness quantifies over
subsets of a DECLARED box.  For a subset that uses every value on every axis the
two agree; for one that does not, they are operators on different boxes, and the
verdicts genuinely differ.

    X = [(0,1,0),(0,1,1),(0,1,2),(0,2,1),(0,2,2),(2,2,1),(2,2,2)]

closes all five under the observed box, and under the declared (3,3,3) box it
closes algebra, information and statistics but NOT order -- and order <= algebra
in the poset, so the closer-set is not a down-set.  The first run of this file
reported that as a refutation of O1.  It is not.  It is a measurement of the
convention: order's closure is the staircase WITHIN THE BOX, so a declared box
wider than the observed alphabet hands it cells X was never asked about, while
algebra's sublattice closure only ever takes mins and maxes of members and
cannot leave the observed alphabet.  The same mechanism drives the O4 case.

O1, O3 and O4 therefore carry `spans`, which is exactly hlaw's convention
restated inside the solver.  O1b and O4b run the SAME formulas WITHOUT it and
report what fails, because the convention is load-bearing and saying so is the
finding.  O2 needs no hypothesis: it is proved over every subset either way,
which is the stronger statement, and it is left that way deliberately.

    THE GUARD COULD NOT HAVE CAUGHT THIS.  guard_encoding skips every trial
    whose observed box is not the declared shape -- it has to, or it would be
    comparing two different operators -- so the region O1b and O4b live in is
    precisely the region it never sampled.  guard_encoding now reports its own
    skip count, and guard_encoding_nonspanning covers that region by handing
    hlaw the declared box instead of letting it observe one.

===============================================================================
THE ENCODINGS, AND THE ONE THAT NEEDED CARE
===============================================================================

order, algebra and information come from prover.py unchanged.  Two are new:

    STATISTICS.  St(X) = { x : (x_i, x_j) realised by some member, all i < j }.
    A direct disjunction; nothing subtle.

    GEOMETRY.  G(X) = { x : (x_i, x_j) in conv(pi_ij X), all i < j }.  Convexity
    is not first-order over the integers, so the hull is PRECOMPUTED EXACTLY:
    by Caratheodory in the plane, a point of the hull of P lies in the hull of at
    most three points of P, so membership is the finite disjunction over every
    Q subset of the projection grid with |Q| <= 3 whose hull contains the point.
    The hulls are computed in exact rational arithmetic, never floating point.

    AT A 2 x 2 PROJECTION GRID GEOMETRY AND STATISTICS COINCIDE, because the
    hull of a set of unit-square corners contains no corner it did not already
    contain.  Every obligation below therefore runs at a 3-valued coordinate or
    wider, and `--guards` checks that the two operators actually differ there.
"""

import itertools
import sys
from fractions import Fraction

import hlaw
import prover
from prover import cells_of, closed, contains, in_J, in_R, subset_vars

if not prover.HAVE_Z3:
    prover.require_z3()

import z3


# ---------------------------------------------------------------------------
# the two encodings prover.py does not carry
# ---------------------------------------------------------------------------

def _in_hull_2d(pts, p):
    """Exact: is grid point p in the convex hull of the point set pts?"""
    if p in pts:
        return True
    P = sorted(pts)
    if len(P) < 2:
        return False
    # p is in conv(P) iff it is in the hull of at most three points (Caratheodory)
    for r in (2, 3):
        for Q in itertools.combinations(P, r):
            if _in_simplex(Q, p):
                return True
    return False


def _in_simplex(Q, p):
    """p in conv(Q) for |Q| = 2 (a segment) or 3 (a triangle), exactly."""
    px, py = Fraction(p[0]), Fraction(p[1])
    if len(Q) == 2:
        (ax, ay), (bx, by) = Q
        if (bx - ax) * (py - ay) != (by - ay) * (px - ax):
            return False
        return (min(ax, bx) <= px <= max(ax, bx)
                and min(ay, by) <= py <= max(ay, by))
    (ax, ay), (bx, by), (cx, cy) = Q
    det = Fraction((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))
    if det == 0:                       # degenerate triangle: try its edges
        return any(_in_simplex(E, p) for E in itertools.combinations(Q, 2))
    l1 = Fraction((px - ax) * (cy - ay) - (py - ay) * (cx - ax), det)
    l2 = Fraction((bx - ax) * (py - ay) - (by - ay) * (px - ax), det)
    return l1 >= 0 and l2 >= 0 and l1 + l2 <= 1


def _hull_witnesses(shape, i, j):
    """{grid point: [tuples of grid points whose hull contains it]} for pair i,j."""
    grid = [(a, b) for a in range(shape[i]) for b in range(shape[j])]
    out = {}
    for p in grid:
        ws = [(p,)]
        for r in (2, 3):
            for Q in itertools.combinations(grid, r):
                if p not in Q and _in_simplex(Q, p):
                    ws.append(Q)
        out[p] = ws
    return out


_HULL = {}


def in_geometry(X, x, cells, d, shape):
    """x in G(X): every 2-D projection of x lies in the hull of X's."""
    conj = []
    for i, j in itertools.combinations(range(d), 2):
        key = (shape, i, j)
        if key not in _HULL:
            _HULL[key] = _hull_witnesses(shape, i, j)
        p = (x[i], x[j])
        opts = []
        for Q in _HULL[key][p]:
            opts.append(z3.And([z3.Or([X[y] for y in cells
                                       if (y[i], y[j]) == q]) for q in Q]))
        conj.append(z3.Or(opts) if opts else z3.BoolVal(False))
    return z3.And(conj)


def in_statistics(X, x, cells, d):
    """x in St(X): every 2-D projection of x is realised by some member."""
    return z3.And([z3.Or([X[y] for y in cells
                          if y[i] == x[i] and y[j] == x[j]])
                   for i, j in itertools.combinations(range(d), 2)])


def in_algebra(X, S, x, cells):
    """x in <X>, via the closed-superset pattern: true if every closed S
    containing X contains x.  Used under an implication on S, as prover does."""
    return z3.Implies(z3.And(contains(X, S, cells), closed(S, cells)), S[x])


# ---------------------------------------------------------------------------
# closure verdicts as formulas
# ---------------------------------------------------------------------------

def closes_order(X, cells, d):
    return z3.And([z3.Implies(in_R(X, c, cells, d), X[c]) for c in cells])


def closes_information(X, cells):
    return z3.And([z3.Implies(in_J(X, c, cells), X[c]) for c in cells])


def closes_algebra(X, S, cells):
    """X is closed under meet and join -- the direct form, no fixed point."""
    return closed(X, cells)


def closes_geometry(X, cells, d, shape):
    return z3.And([z3.Implies(in_geometry(X, c, cells, d, shape), X[c])
                   for c in cells])


def closes_statistics(X, cells, d):
    return z3.And([z3.Implies(in_statistics(X, c, cells, d), X[c])
                   for c in cells])


def verdicts(X, S, cells, d, shape):
    """{language: a formula saying that language closes X}."""
    return {
        "order": closes_order(X, cells, d),
        "algebra": closes_algebra(X, S, cells),
        "geometry": closes_geometry(X, cells, d, shape),
        "information": closes_information(X, cells),
        "statistics": closes_statistics(X, cells, d),
    }


# ---------------------------------------------------------------------------
# the obligations
# ---------------------------------------------------------------------------

def spans(X, cells, shape):
    """X uses every value on every axis -- i.e. hlaw's observed box IS `shape`.

    This is not a convenience restriction.  It is hlaw's own convention written
    as a formula; without it the obligations below are about operators on a box
    the index does not occupy.  See the module docstring.

    prover.observed IS THIS FORMULA AND IT WAS ALREADY SEATED.  This file first
    rewrote it, which is the copy-a-member fault; it is imported here and the
    name `spans` kept only because that is what the obligations read as.  What
    is added is the reason: prover.py needs the observed alphabet to make the
    staircase's maxima attained, and this file needs it to be talking about
    hlaw's operators at all.
    """
    return prover.observed(X, cells, shape)



def O1_downset(X, S, cells, d, shape):
    """O1: the set of closers is a down-set of the language poset.

    If b closes and a <= b in the poset, a closes.  hlaw.LAWFUL is the poset's
    cover data, read here rather than restated.  Carries `spans`: see the module
    docstring.  O1b_downset_nospan is the same body without it.
    """
    v = verdicts(X, S, cells, d, shape)
    body = z3.And([z3.Implies(v[b], v[a]) for a, b in hlaw.LAWFUL])
    return z3.Implies(spans(X, cells, shape), body)


def O1b_downset_nospan(X, S, cells, d, shape):
    """O1 WITHOUT the spanning hypothesis -- expected to FAIL, and that is the
    finding.  The counterexample is a non-spanning index, so it is a statement
    about the declared-box convention and not about the down-set law.
    """
    v = verdicts(X, S, cells, d, shape)
    return z3.And([z3.Implies(v[b], v[a]) for a, b in hlaw.LAWFUL])


def O2_K0_universal(X, S, cells, d, shape):
    """O2: some cell is refused by nothing -- i.e. lies in all five closures.

    Every operator is extensive, so any member of X will do; the obligation is
    stated over the box so that the proof is of the general fact and not of the
    extensiveness of one operator.
    """
    inall = [z3.And(in_R(X, c, cells, d),
                    in_J(X, c, cells),
                    X[c],                       # in <X> trivially when in X
                    in_geometry(X, c, cells, d, shape),
                    in_statistics(X, c, cells, d)) for c in cells]
    nonempty = z3.Or([X[c] for c in cells])
    return z3.Implies(nonempty, z3.Or(inall))


def O4_monotone_redundant(X, S, cells, d, shape):
    """O4: appending g(x) = x_0 changes no language's verdict.

    Built in the LIFTED box: cells of the (shape + (shape[0],)) box, with X'
    the image of X under x -> (x, x_0).  A lifted cell is in X' exactly when its
    last coordinate equals its first and the projection is in X.
    """
    raise NotImplementedError("stated directly in O4_run, which builds two boxes")


# ---------------------------------------------------------------------------

def run_O4(base=(3, 3), quiet=False, span=True, label=None):
    """O4 over every subset of the base box, comparing verdicts before/after.

    Two boxes are needed, so this does not fit prover.prove's single-box shape
    and is stated here.  X ranges over subsets of `base`; X' is its image in
    base + (base[0],) under x -> (x, x_0).

    `span` adds the spanning hypothesis (hlaw's observed-box convention).  With
    span=False this is O4b, which FAILS, and the failure is the measurement of
    the convention rather than a refutation of the chart criterion -- see the
    module docstring.  Note the lift of a spanning X spans its own box
    automatically, since the appended coordinate is a copy of the first.
    """
    prover.require_z3()
    d = len(base)
    cells = cells_of(base)
    lift = base + (base[0],)
    lcells = cells_of(lift)
    X = subset_vars(cells, "x")
    S = subset_vars(cells, "s")
    LS = subset_vars(lcells, "ls")

    # X' as a formula per lifted cell: present iff last == first and base in X
    Xl = {c: (X[c[:d]] if c[d] == c[0] else z3.BoolVal(False)) for c in lcells}

    v0 = verdicts(X, S, cells, d, base)
    v1 = verdicts(Xl, LS, lcells, d + 1, lift)
    same = z3.And([v0[L] == v1[L] for L in sorted(hlaw.LANGS)])
    nonempty = z3.Or([X[c] for c in cells])

    hyp = z3.And(nonempty, spans(X, cells, base)) if span else nonempty
    s = z3.Solver()
    s.add(z3.Not(z3.Implies(hyp, same)))
    r = s.check()
    ok = r == z3.unsat
    if not quiet:
        print("  [%s] %-52s %-6s (2^%d subsets)"
              % ("PROVED" if ok else "  XX  ",
                 label or "O4  monotone redundant coordinate keeps the channel",
                 r, len(cells)))
        if r == z3.sat:
            m = s.model()
            print("        counterexample X = %s"
                  % sorted(c for c in cells if z3.is_true(m.eval(X[c], True))))
    return ok


def run_O3(shape=(3, 3, 3), quiet=False):
    """O3: K7 is NOT universal -- find an X with no cell every language refuses.

    A REFUTATION, so `sat` is the result wanted and the model is the witness.
    The witness is required to SPAN the box, so that it is a witness under
    hlaw's own convention and not an artefact of the declared box.
    """
    prover.require_z3()
    d = len(shape)
    cells = cells_of(shape)
    X = subset_vars(cells, "x")
    refused_by_all = [z3.And(z3.Not(in_R(X, c, cells, d)),
                             z3.Not(in_J(X, c, cells)),
                             z3.Not(X[c]),
                             z3.Not(in_geometry(X, c, cells, d, shape)),
                             z3.Not(in_statistics(X, c, cells, d)))
                      for c in cells]
    s = z3.Solver()
    s.add(spans(X, cells, shape))                 # hlaw's convention; see docstring
    s.add(z3.Not(z3.Or(refused_by_all)))          # NO cell that all five refuse
    r = s.check()
    ok = r == z3.sat
    wit = None
    if ok:
        m = s.model()
        wit = sorted(c for c in cells if z3.is_true(m.eval(X[c], True)))
    if not quiet:
        print("  [%s] %-52s %-6s"
              % ("REFUTED" if ok else "  XX  ",
                 "O3  K7 is NOT universal -- a witness exists", r))
        if wit is not None:
            print("        witness X = %s" % (wit if len(wit) < 12
                                              else "%d cells" % len(wit)))
    return ok, wit


# ---------------------------------------------------------------------------
# the two guards PROOF-ASSISTANT.md requires
# ---------------------------------------------------------------------------

def guard_vacuity(shape=(3, 3, 3)):
    """An obligation over a hypothesis nothing satisfies is vacuously true.

    Checks the hypotheses actually have models: a non-empty X exists, and both
    an X that closes statistics and one that does not.
    """
    prover.require_z3()
    d = len(shape)
    cells = cells_of(shape)
    X = subset_vars(cells, "x")
    out = {}
    for lab, f in (("a non-empty index exists", z3.Or([X[c] for c in cells])),
                   ("one that closes statistics",
                    z3.And(z3.Or([X[c] for c in cells]),
                           closes_statistics(X, cells, d))),
                   ("one that does NOT",
                    z3.And(z3.Or([X[c] for c in cells]),
                           z3.Not(closes_statistics(X, cells, d))))):
        s = z3.Solver()
        s.add(f)
        out[lab] = s.check() == z3.sat
    return out


def guard_encoding(trials=400, seed=11, shape=(3, 3, 3)):
    """The new encodings must agree with hlaw's own operators on real sets.

    ENCODING DRIFT IS THE FAILURE MODE THAT MATTERS.  A Z3 proof about a formula
    that is not the operator proves nothing about the operator.  Random subsets
    of the box are put to both, and the verdicts compared.
    """
    import random
    rnd = random.Random(seed)
    cells = cells_of(shape)
    d = len(shape)
    bad = []
    skipped = 0
    for _ in range(trials):
        k = rnd.randint(1, len(cells))
        Xs = frozenset(rnd.sample(cells, k))
        cl, box = hlaw.closures(Xs)
        want = {L: len(cl[L]) == len(Xs) for L in hlaw.LANGS}
        # only comparable when hlaw's own box is the full box, since hlaw takes
        # the OBSERVED alphabet and this encoding takes the declared shape.
        # THE SKIP IS A BLIND SPOT, not a detail: every counterexample O1b and
        # O4b report is non-spanning, so it lives exactly here.  The count is
        # returned so the blind spot is visible in the report, and
        # guard_encoding_nonspanning covers it.
        if [len(b) for b in box] != list(shape):
            skipped += 1
            continue
        lit = {c: z3.BoolVal(c in Xs) for c in cells}
        S = subset_vars(cells, "g")
        got = {}
        for L, f in (("order", closes_order(lit, cells, d)),
                     ("information", closes_information(lit, cells)),
                     ("algebra", closes_algebra(lit, S, cells)),
                     ("geometry", closes_geometry(lit, cells, d, shape)),
                     ("statistics", closes_statistics(lit, cells, d))):
            s = z3.Solver()
            s.add(z3.Not(f))
            got[L] = s.check() == z3.unsat
        for L in want:
            if want[L] != got[L]:
                bad.append((sorted(Xs), L, want[L], got[L]))
    return bad, skipped


def guard_encoding_nonspanning(trials=200, seed=13, shape=(3, 3, 3)):
    """The encoding must match hlaw on NON-spanning sets too -- the region
    guard_encoding is structurally unable to sample.

    hlaw observes its box, so it cannot be asked about a declared one through
    hlaw.closures.  It CAN be asked through hlaw.OPS, which takes the box as an
    argument; that is the comparison made here.  A pass means the O1b and O4b
    counterexamples are real properties of the declared-box convention and not
    artefacts of this file's formulas.
    """
    import random
    rnd = random.Random(seed)
    cells = cells_of(shape)
    d = len(shape)
    box = [list(range(n)) for n in shape]
    bad = []
    seen = 0
    for _ in range(trials):
        k = rnd.randint(1, len(cells))
        Xs = frozenset(rnd.sample(cells, k))
        if [len(sorted({x[i] for x in Xs})) for i in range(d)] == list(shape):
            continue                              # spanning: the other guard's
        seen += 1
        want = {L: frozenset(hlaw.OPS[L](sorted(Xs), box)) <= Xs
                for L in hlaw.LANGS}
        lit = {c: z3.BoolVal(c in Xs) for c in cells}
        S = subset_vars(cells, "h")
        for L, f in (("order", closes_order(lit, cells, d)),
                     ("information", closes_information(lit, cells)),
                     ("algebra", closes_algebra(lit, S, cells)),
                     ("geometry", closes_geometry(lit, cells, d, shape)),
                     ("statistics", closes_statistics(lit, cells, d))):
            s = z3.Solver()
            s.add(z3.Not(f))
            if want[L] != (s.check() == z3.unsat):
                bad.append((sorted(Xs), L))
    return bad, seen


def guard_geometry_differs(shape=(3, 3, 3), trials=300, seed=7):
    """Geometry and statistics must actually differ at this shape.

    At a 2 x 2 projection grid they coincide, and an obligation run there would
    be silently weaker than it looks.
    """
    import random
    rnd = random.Random(seed)
    cells = cells_of(shape)
    for _ in range(trials):
        Xs = frozenset(rnd.sample(cells, rnd.randint(2, len(cells))))
        cl, box = hlaw.closures(Xs)
        if [len(b) for b in box] != list(shape):
            continue
        if cl["geometry"] != cl["statistics"]:
            return True, sorted(Xs)
    return False, None


# ---------------------------------------------------------------------------

def main(argv):
    print("=" * 74)
    print("MACHINE-CHECKED FOUNDATIONS OF THE SIX-INDEX CLASSIFICATION")
    print("=" * 74)
    print()
    print("GUARDS FIRST -- an obligation is worth nothing until these pass.")
    diff, wit = guard_geometry_differs()
    print("  [%s] geometry and statistics differ at this shape   %s"
          % ("ok" if diff else "XX", "witness %d cells" % len(wit) if wit else ""))
    vac = guard_vacuity()
    for lab, sat in vac.items():
        print("  [%s] non-vacuous: %s" % ("ok" if sat else "XX", lab))
    bad, skipped = guard_encoding()
    print("  [%s] encoding matches hlaw on spanning sets   %s"
          % ("ok" if not bad else "XX",
             "no drift" if not bad else "%d disagreements" % len(bad)))
    print("  [--] that guard SKIPPED %d of 400 trials as non-spanning -- its"
          % skipped)
    print("       blind spot, and where O1b and O4b below live.")
    bad2, seen = guard_encoding_nonspanning()
    print("  [%s] encoding matches hlaw on %d NON-spanning sets   %s"
          % ("ok" if not bad2 else "XX", seen,
             "no drift" if not bad2 else "%d disagreements" % len(bad2)))
    if bad or bad2:
        for b in (bad + bad2)[:3]:
            print("        %s" % (b,))
        print("  ENCODING DRIFT -- the obligations below are NOT trustworthy.")
        return 1
    if "--guards" in argv:
        return 0
    print()

    print("THE OBLIGATIONS -- all four carry hlaw's observed-box convention as")
    print("the hypothesis `spans`, except O2, which needs none.")
    ok = True
    ok &= prover.prove("O1  closers is always a DOWN-SET", (3, 3, 3), O1_downset)
    ok &= prover.prove("O2  K0 is universal", (3, 3, 3), O2_K0_universal)
    r3, _w = run_O3()
    ok &= r3
    ok &= run_O4()
    print()
    print("THE CONVENTION IS LOAD-BEARING, AND THIS IS THE MEASUREMENT OF IT.")
    print("The same two formulas without `spans`.  Both FAIL, and the failures")
    print("are findings about the declared-box convention, not refutations of")
    print("the down-set law or of the chart criterion.  A `PROVED` on either")
    print("line below would be the surprise.")
    b1 = prover.prove("O1b closers is a DOWN-SET  (no spanning hypothesis)",
                      (3, 3, 3), O1b_downset_nospan)
    b4 = run_O4(span=False,
                label="O4b monotone redundant coordinate  (no spanning hyp.)")
    print("  [%s] both O1b and O4b fail, as the docstring states"
          % ("ok" if not b1 and not b4 else "XX"))
    ok &= (not b1 and not b4)
    print()
    print("A `unsat` on the negation is a proof that no counterexample exists")
    print("IN THE NAMED BOX, UNDER THE NAMED CONVENTION.  Nothing here reaches")
    print("unbounded boxes or higher arity; PROOF-ASSISTANT.md's ceiling")
    print("applies unchanged.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
