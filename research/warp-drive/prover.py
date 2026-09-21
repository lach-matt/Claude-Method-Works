#!/usr/bin/env python3
r"""
prover.py -- a reusable machine-checking harness for finite claims about
lattices, orders and closure operators.  Point it at a claim; it returns PROVED
or a counterexample.

WHY THIS EXISTS.  No proof assistant ships with this environment and the usual
ones cannot be fetched: elan (Lean) and opam (Coq) both need github, which the
egress proxy refuses.  But PYPI IS REACHABLE, so the Z3 SMT solver installs:

    pip install z3-solver

That one fact is the whole trick, and it was not obvious.  Any future session
wanting a machine-checked result should start here rather than rediscovering it.

WHAT IT PROVES, AND WHAT THAT MEANS.  A claim is stated as a formula whose
variables range over EVERY subset of a finite box.  The harness asserts the
NEGATION and asks Z3 for a model.  `unsat` means no counterexample exists --
a proof over that box, not a sample of it.  At d = 3 over a 3x3x3 box that is
2^27 = 134,217,728 subsets, well past what enumeration can reach.

TWO ENCODINGS THAT MAKE IT DECIDABLE.  Both are the difference between a claim
you can check and one you cannot:

  1. NO max, NO phi.  The staircase membership test
         x_i <= max{ y_i : y in X, y_j <= x_j }
     is equivalent to the existence of a witness:
         there is y in X with y_j <= x_j and y_i >= x_i
     which is first-order.  `in_R` below.

  2. NO FIXED POINT.  The generated sublattice <X> is a least fixed point,
     which SMT cannot express directly.  Instead use its other definition --
     the intersection of all closed supersets -- so "S subset <X>" becomes
     "for every closed T containing X, S subset T", which is first-order.
     `closed` below, and see machinecheck.py for the pattern.

ALWAYS RUN THE GUARDS.  A machine-check is worthless if the hypotheses are
unsatisfiable (the implication is then vacuously true and `unsat` proves
nothing) or if the encoding is not the operator you meant.  `non_vacuous` and
`encoding_matches` are provided for exactly this and should be called before
any result is reported.  machinecheck.py does so.

WORKED EXAMPLE -- run `python3 prover.py` to see it discharge two obligations.
"""

import itertools
import sys

try:
    import z3
    HAVE_Z3 = True
except ImportError:                                     # pragma: no cover
    HAVE_Z3 = False

INSTALL = "pip install z3-solver     # pypi is reachable here; github is not"


def require_z3():
    if not HAVE_Z3:
        print("prover.py needs the Z3 SMT solver.\n\n    %s\n" % INSTALL)
        sys.exit(2)


# ------------------------------------------------------------------ the box

def cells_of(shape):
    """Every cell of the box, e.g. cells_of((3,3)) -> the nine pairs."""
    return list(itertools.product(*[range(n) for n in shape]))


def meet(a, b):
    return tuple(map(min, a, b))


def join(a, b):
    return tuple(map(max, a, b))


def subset_vars(cells, prefix):
    """A boolean variable per cell: membership in an unknown subset."""
    return {c: z3.Bool("%s_%s" % (prefix, c)) for c in cells}


# ------------------------------------------------------- reusable predicates

def observed(X, cells, shape):
    """Every value of every coordinate is realised by some cell of X.
    (The 'observed alphabet' hypothesis; the only place it is ever needed is to
    make the staircase's maxima attained.)"""
    return z3.And([z3.Or([X[c] for c in cells if c[i] == v])
                   for i, n in enumerate(shape) for v in range(n)])


def in_R(X, x, cells, d):
    """Membership of x in the staircase closure of X -- witness form, no max."""
    return z3.And([z3.Or([X[y] for y in cells if y[j] <= x[j] and y[i] >= x[i]])
                   for i in range(d) for j in range(d) if i != j])


def in_J(X, x, cells):
    """Membership of x in the join-closure of X, one join deep or already in X.
    (Sufficient where X is small; for the full closure use the closed-superset
    pattern instead.)"""
    return z3.Or([X[x]] + [z3.And(X[a], X[b]) for a in cells for b in cells
                           if join(a, b) == x])


def closed(S, cells):
    """S is closed under coordinatewise meet and join."""
    return z3.And([z3.Implies(z3.And(S[a], S[b]), S[meet(a, b)])
                   for a in cells for b in cells] +
                  [z3.Implies(z3.And(S[a], S[b]), S[join(a, b)])
                   for a in cells for b in cells])


def contains(A, B, cells):
    """A subset B, for two membership dictionaries or predicates."""
    av = (lambda c: A[c]) if isinstance(A, dict) else A
    bv = (lambda c: B[c]) if isinstance(B, dict) else B
    return z3.And([z3.Implies(av(c), bv(c)) for c in cells])


# ------------------------------------------------------------------- prove

def prove(name, shape, claim, quiet=False):
    """claim(X, S, cells, d, shape) -> a z3 formula that should hold for ALL X
    (and all S).  Returns True if Z3 proves it; prints a counterexample if not."""
    require_z3()
    cells = cells_of(shape)
    d = len(shape)
    X = subset_vars(cells, "x")
    S = subset_vars(cells, "s")
    s = z3.Solver()
    s.add(z3.Not(claim(X, S, cells, d, shape)))
    r = s.check()
    ok = r == z3.unsat
    if not quiet:
        print("  [%s] %-52s %-6s (2^%d subsets)" %
              ("PROVED" if ok else "  XX  ", name, r, len(cells)))
    if r == z3.sat and not quiet:
        m = s.model()
        print("        counterexample X = %s" %
              sorted(c for c in cells if z3.is_true(m.eval(X[c], True))))
        print("                       S = %s" %
              sorted(c for c in cells if z3.is_true(m.eval(S[c], True))))
    return ok


# ------------------------------------------------------------------- guards

def non_vacuous(shape, hypothesis, extra=None):
    """The hypothesis must be SATISFIABLE, else the implication is empty and
    `unsat` proves nothing.  `extra` adds a non-triviality demand."""
    require_z3()
    cells = cells_of(shape)
    X = subset_vars(cells, "x")
    S = subset_vars(cells, "s")
    s = z3.Solver()
    s.add(hypothesis(X, S, cells, len(shape), shape))
    if extra is not None:
        s.add(extra(X, S, cells, len(shape), shape))
    return s.check() == z3.sat


def encoding_matches(reference, shape_pool, trials=200, seed=5):
    """The encoded predicate must BE the operator you meant.  `reference` takes
    (X, box, d) and returns the true closure as a set of cells; this compares it
    against in_R evaluated concretely.  Returns (compared, disagreements)."""
    import random
    rnd = random.Random(seed)
    bad = tot = 0
    for _ in range(trials):
        shape = rnd.choice(shape_pool)
        d = len(shape)
        cells = cells_of(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 8))))
        box = [sorted({x[i] for x in X}) for i in range(d)]
        R = reference(X, box, d)
        for x in itertools.product(*box):
            tot += 1
            enc = all(any(y[j] <= x[j] and y[i] >= x[i] for y in X)
                      for i in range(d) for j in range(d) if i != j)
            bad += enc != (x in R)
    return tot, bad


# --------------------------------------------------------- worked example

def _example_extensive(X, S, cells, d, shape):
    """X subset R(X): every cell of X survives its own staircase."""
    return z3.And([z3.Implies(X[c], in_R(X, c, cells, d)) for c in cells])


def _example_monotone(X, S, cells, d, shape):
    """X subset S implies R(X) subset R(S) -- the staircase is monotone in X."""
    return z3.Implies(contains(X, S, cells),
                      z3.And([z3.Implies(in_R(X, c, cells, d),
                                         in_R(S, c, cells, d)) for c in cells]))


def main():
    require_z3()
    print(__doc__)
    print("=" * 79)
    print("WORKED EXAMPLE -- Z3 %s" % z3.get_version_string())
    print("=" * 79)
    print()
    print("  extensivity of the staircase")
    a = [prove("d=%d, box %s" % (len(s), "x".join(map(str, s))), s,
               _example_extensive) for s in ((3, 3), (3, 3, 3))]
    print()
    print("  monotonicity of the staircase in X")
    b = [prove("d=%d, box %s" % (len(s), "x".join(map(str, s))), s,
               _example_monotone) for s in ((3, 3), (3, 3, 3))]
    print()
    print("  guards")
    nv = non_vacuous((3, 3), lambda X, S, c, d, sh: observed(X, c, sh))
    print("  [%s] the 'observed' hypothesis is satisfiable" % ("ok" if nv else "XX"))
    print()
    n = len(a + b)
    print("%d of %d example obligations discharged; guards %s"
          % (sum(a + b), n, "passed" if nv else "FAILED"))
    print()
    print("To machine-check your own claim: write a function")
    print("    claim(X, S, cells, d, shape) -> z3 formula")
    print("and call  prove('name', shape, claim).  See machinecheck.py for the")
    print("full set of obligations behind THE-HIERARCHY-LAW.md.")
    return 0 if (all(a + b) and nv) else 1


if __name__ == "__main__":
    sys.exit(main())
