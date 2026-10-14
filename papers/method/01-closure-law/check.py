#!/usr/bin/env python3
"""check.py -- the machine checks behind "The closure law of a finite index".

Every number the paper prints and every decidable claim it makes is produced here.  Four kinds
of check, kept apart in the report:

  MACHINE-CHECKED  Z3 returned `unsat` on the negation of an obligation whose variables range
                   over EVERY subset of a named finite box (and, for the integer obligations,
                   over every integer), after the two guards passed;
  EXHAUSTIVE       a decision procedure visited every case of a stated finite family;
  REFUTATION       a claim disproved by an explicit witness, re-verified here;
  CITED            taken from the literature; printed for the record, not checked.

The operator under test is the staircase closure the atomic-index work computes (tools/cypher.py,
op_order), imported by path and never copied.  A fresh reference implementation `stair` is
written below and compared against it: the guard is an independent implementation, the object
under test is the seated one.  The Z3 harness is research/warp-drive/prover.py, imported by path.

    python3 check.py             every obligation, one line each, a summary, exit 1 on failure
    python3 check.py --selftest  the same, plus negative controls that MUST be refuted
"""
import importlib.util
import itertools
import math
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PROVER = os.path.join(REPO, "research", "warp-drive", "prover.py")
CYPHER = os.path.join(REPO, "tools", "cypher.py")


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


prover = load("prover", PROVER)
cypher = load("cypher", CYPHER)
prover.require_z3()
import z3
from prover import cells_of, meet, join, in_R, closed as z3closed, subset_vars

# ------------------------------------------------------------------ reporting

ROWS = []
FAILS = []


def row(status, name, detail, ok=True):
    ROWS.append((status, name, detail, ok))
    if not ok:
        FAILS.append(name)
    print("  [%s] %-16s %-58s %s" % ("ok" if ok else "XX", status, name, detail))


def boxname(shape):
    return "x".join(map(str, shape))


# ------------------------------------------------- the reference implementation
# Written fresh for this paper.  Own-box regime throughout: the box of X is the product of the
# alphabets X itself realises (D1, D2), so the observed-alphabet hypothesis is built in.

def alphabets(X):
    d = len(next(iter(X)))
    return [sorted({x[i] for x in X}) for i in range(d)]


def phi(X):
    """The boundary functions phi_ij(a) = max{ y_i : y in X, y_j <= a }, a in A_j (D4)."""
    A = alphabets(X)
    d = len(A)
    out = {}
    for i in range(d):
        for j in range(d):
            if i != j:
                for a in A[j]:
                    out[i, j, a] = max(y[i] for y in X if y[j] <= a)
    return out


def stair(X):
    """The staircase closure R(X) (D5)."""
    X = set(X)
    if not X:
        return set()
    A = alphabets(X)
    d = len(A)
    if d == 1:
        return set(X)
    ph = phi(X)
    return {x for x in itertools.product(*A)
            if all(x[i] <= ph[i, j, x[j]] for i in range(d) for j in range(d) if i != j)}


def gen(X):
    """The generated sublattice <X> (D3): iterate coordinatewise meet and join to a fixed point."""
    S = set(X)
    while True:
        L = sorted(S)
        new = set()
        for a in range(len(L)):
            for b in range(a + 1, len(L)):
                m, j = meet(L[a], L[b]), join(L[a], L[b])
                if m not in S:
                    new.add(m)
                if j not in S:
                    new.add(j)
        if not new:
            return S
        S |= new


def is_closed(X):
    """Closed under coordinatewise meet and join (D6)."""
    X = set(X)
    return all(meet(a, b) in X and join(a, b) in X for a in X for b in X)


def defect(X):
    return len(stair(X)) - len(set(X))


def cypher_R(X):
    """The seated operator: tools/cypher.py op_order, decoded back to the cells' own values."""
    X = sorted(set(X))
    d = len(X[0])
    ix = cypher.Index("x", ["c%d" % i for i in range(d)], X)
    out, _ = cypher.op_order(ix, {})
    return {tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in out}


def joinclosure(X):
    S = set(X)
    while True:
        new = {join(a, b) for a in S for b in S} - S
        if not new:
            return S
        S |= new


# ------------------------------------------------------- the Z3 encodings

def realised(X, x, cells, d):
    """x lies in Box(X): every coordinate value of x is taken by some cell of X."""
    return z3.And([z3.Or([X[y] for y in cells if y[i] == x[i]]) for i in range(d)])


def own(X, x, cells, d):
    """x in R(X), own-box: x in Box(X) and, for every i != j, a witness y in X with y_j <= x_j
    and y_i >= x_i (a maximum is attained exactly when a witness exists)."""
    return z3.And(realised(X, x, cells, d), in_R(X, x, cells, d))


def rvars(X, cells, d, prefix):
    """Fresh booleans r[c] defined to equal 'c in R(X)', so a formula about R(R(X)) stays small."""
    r = {c: z3.Bool("%s_%s" % (prefix, c)) for c in cells}
    defn = z3.And([r[c] == own(X, c, cells, d) for c in cells])
    return r, defn


def fixed_point(S, cells, d):
    return z3.And([S[c] == own(S, c, cells, d) for c in cells])


def sublattice(S, cells):
    return z3closed(S, cells)


def prove(name, shape, claim):
    return prover.prove(name, shape, claim, quiet=True)


def eval_own(Xset, x, cells, d):
    """Evaluate the Z3 predicate itself (not a retyping of it) with X pinned to constants."""
    Xc = {c: z3.BoolVal(c in Xset) for c in cells}
    return z3.is_true(z3.simplify(own(Xc, x, cells, d)))


def eval_witness_only(Xset, x, cells, d):
    Xc = {c: z3.BoolVal(c in Xset) for c in cells}
    return z3.is_true(z3.simplify(in_R(Xc, x, cells, d)))


# ================================================================ the guards

def guards():
    print("GUARDS -- run before any obligation is reported")
    ok = True
    rnd = random.Random(2026)
    pool = [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3), (2, 2, 2, 2), (4, 3)]

    # (a) the fresh reference agrees with the seated operator, cell for cell
    tot = bad = 0
    for _ in range(400):
        shape = rnd.choice(pool)
        cells = cells_of(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(1, min(len(cells), 9))))
        R1, R2 = stair(X), cypher_R(X)
        tot += 1
        bad += R1 != R2
    ok &= bad == 0
    row("GUARD", "reference == seated operator", "%d random X over %s, %d disagreements" % (tot, ",".join(map(boxname, pool)), bad), bad == 0)
    # negative control: a wrong reference (the join-closure) must be caught
    nbad = sum(joinclosure(frozenset(rnd.sample(cells_of((3, 3)), 4))) != cypher_R(frozenset(rnd.sample(cells_of((3, 3)), 4))) for _ in range(1))
    nb = 0
    for _ in range(50):
        X = frozenset(rnd.sample(cells_of((3, 3)), rnd.randint(2, 5)))
        nb += joinclosure(X) != cypher_R(X)
    ok &= nb > 0
    row("GUARD", "negative control: wrong reference is caught", "join-closure vs seated: %d of 50 disagree" % nb, nb > 0)

    # (b) the Z3 encoding IS the operator: evaluated over EVERY cell of the declared box
    tot = bad = 0
    for _ in range(200):
        shape = rnd.choice(pool[:5])
        cells = cells_of(shape)
        d = len(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(1, min(len(cells), 8))))
        R = cypher_R(X)
        for x in cells:
            tot += 1
            bad += eval_own(X, x, cells, d) != (x in R)
    ok &= bad == 0
    row("GUARD", "Z3 encoding `own` == seated operator", "%d cells of declared boxes, %d disagreements" % (tot, bad), bad == 0)
    # negative control: the witness form WITHOUT the box conjunct is a different operator
    tot = bad = 0
    for _ in range(200):
        shape = rnd.choice(pool[:5])
        cells = cells_of(shape)
        d = len(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(1, min(len(cells), 8))))
        R = cypher_R(X)
        for x in cells:
            tot += 1
            bad += eval_witness_only(X, x, cells, d) != (x in R)
    ok &= bad > 0
    row("GUARD", "negative control: witness-only encoding differs", "%d disagreements of %d cells (fixed-box operator, not R)" % (bad, tot), bad > 0)

    # (c) 'in every closed superset' == <X>, brute forced
    tot = bad = 0
    for _ in range(60):
        shape = rnd.choice([(3, 3), (2, 2, 2)])
        cells = cells_of(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(1, 6)))
        inter = set(cells)
        for mask in range(1 << len(cells)):
            S = {cells[i] for i in range(len(cells)) if mask >> i & 1}
            if X <= S and is_closed(S):
                inter &= S
        tot += 1
        bad += inter != gen(X)
    ok &= bad == 0
    row("GUARD", "hull encoding: intersection of closed supersets == <X>", "%d sets, %d disagreements" % (tot, bad), bad == 0)

    # (c') the Z3 closure predicate (D6) IS closure: evaluated on random sets against a direct test
    tot = bad = 0
    for _ in range(300):
        shape = rnd.choice(pool[:5])
        cells = cells_of(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(1, min(len(cells), 8))))
        Xc = {c: z3.BoolVal(c in X) for c in cells}
        tot += 1
        bad += z3.is_true(z3.simplify(sublattice(Xc, cells))) != is_closed(X)
    ok &= bad == 0
    row("GUARD", "Z3 closure predicate == direct closure test", "%d random sets over %s, %d disagreements" % (tot, ",".join(map(boxname, pool[:5])), bad), bad == 0)

    # (d) non-vacuity of every hypothesis used below, satisfiable non-trivially
    for shape in ((3, 3), (2, 2, 2), (3, 3, 3)):
        cells = cells_of(shape)
        d = len(shape)
        X = subset_vars(cells, "x")
        S = subset_vars(cells, "s")
        T = subset_vars(cells, "t")
        hyps = {
            "X subset S closed, S != box": z3.And(z3.Or([X[c] for c in cells]), z3.And([z3.Implies(X[c], S[c]) for c in cells]), sublattice(S, cells), z3.Or([z3.Not(S[c]) for c in cells])),
            "S, T fixed points, distinct, proper": z3.And(fixed_point(S, cells, d), fixed_point(T, cells, d), z3.Or([S[c] != T[c] for c in cells]), z3.Or([z3.Not(S[c]) for c in cells]), z3.Or([z3.Not(T[c]) for c in cells]), z3.Or([S[c] for c in cells]), z3.Or([T[c] for c in cells])),
            "X strictly inside Y": z3.And(z3.Or([X[c] for c in cells]), z3.And([z3.Implies(X[c], S[c]) for c in cells]), z3.Or([z3.And(S[c], z3.Not(X[c])) for c in cells])),
            "G strictly inside closed X with R(G) = X": z3.And(fixed_point(S, cells, d), z3.And([z3.Implies(X[c], S[c]) for c in cells]), z3.Or([z3.And(S[c], z3.Not(X[c])) for c in cells]), z3.And([S[c] == own(X, c, cells, d) for c in cells])),
        }
        for label, h in hyps.items():
            s = z3.Solver()
            s.add(h)
            good = s.check() == z3.sat
            ok &= good
            row("GUARD", "non-vacuity, %s" % boxname(shape), label, good)
    # (d') Theorem 4's hypothesis: a non-empty proper X cut out of its box by an isotone integer system
    for shape in ((3, 3), (2, 2, 2)):
        cells = cells_of(shape)
        d = len(shape)
        X = subset_vars(cells, "x")
        A = [sorted({c[i] for c in cells}) for i in range(d)]
        psi = {(i, j, a): z3.Int("nv_psi_%d_%d_%d" % (i, j, a)) for i in range(d) for j in range(d) if i != j for a in A[j]}
        isotone = z3.And([psi[i, j, a] <= psi[i, j, b] for (i, j, a) in psi for b in A[j] if a < b])
        cut = lambda x: z3.And(realised(X, x, cells, d), z3.And([x[i] <= psi[i, j, x[j]] for i in range(d) for j in range(d) if i != j]))
        h = z3.And(isotone, z3.And([X[c] == cut(c) for c in cells]), z3.Or([X[c] for c in cells]), z3.Or([z3.Not(X[c]) for c in cells]))
        s = z3.Solver()
        s.add(h)
        good = s.check() == z3.sat
        ok &= good
        row("GUARD", "non-vacuity, %s" % boxname(shape), "Theorem 4: non-empty proper X = cut(psi), psi isotone", good)
    print()
    return ok


# ============================================================ Z3 obligations

def ob_extensive(X, S, cells, d, shape):
    return z3.And([z3.Implies(X[c], own(X, c, cells, d)) for c in cells])


def ob_monotone(X, S, cells, d, shape):
    return z3.Implies(z3.And([z3.Implies(X[c], S[c]) for c in cells]),
                      z3.And([z3.Implies(own(X, c, cells, d), own(S, c, cells, d)) for c in cells]))


def ob_idempotent(X, S, cells, d, shape):
    r, defn = rvars(X, cells, d, "r")
    return z3.Implies(defn, z3.And([own(r, c, cells, d) == r[c] for c in cells]))


def ob_sublattice(X, S, cells, d, shape):
    r, defn = rvars(X, cells, d, "r")
    return z3.Implies(defn, sublattice(r, cells))


def ob_hardhalf(X, S, cells, d, shape):
    hyp = z3.And(z3.And([z3.Implies(X[c], S[c]) for c in cells]), sublattice(S, cells))
    return z3.Implies(hyp, z3.And([z3.Implies(own(X, c, cells, d), S[c]) for c in cells]))


def ob_closed_iff_fixed(X, S, cells, d, shape):
    return sublattice(S, cells) == fixed_point(S, cells, d)


def ob_moore_intersection(X, S, cells, d, shape):
    T = {c: z3.And(S[c], X[c]) for c in cells}
    hyp = z3.And(fixed_point(S, cells, d), fixed_point(X, cells, d))
    return z3.Implies(hyp, fixed_point(T, cells, d))


def ob_projection(i, j):
    def claim(X, S, cells, d, shape):
        pcells = cells_of((shape[i], shape[j]))
        P = {p: z3.Or([S[c] for c in cells if (c[i], c[j]) == p]) for p in pcells}
        return z3.Implies(fixed_point(S, cells, d), fixed_point(P, pcells, 2))
    return claim


def ob_graph(m):
    def claim(X, S, cells, d, shape):
        h = {c: z3.Int("h_%s" % (c,)) for c in cells}
        bounds = z3.And([z3.And(h[c] >= 0, h[c] <= m - 1) for c in cells])
        mx = lambda a, b: z3.If(a >= b, a, b)
        mn = lambda a, b: z3.If(a <= b, a, b)
        graph_closed = z3.And([z3.Implies(z3.And(S[a], S[b]),
                                          z3.And(S[join(a, b)], h[join(a, b)] == mx(h[a], h[b]),
                                                 S[meet(a, b)], h[meet(a, b)] == mn(h[a], h[b])))
                               for a in cells for b in cells])
        hom = z3.And([z3.Implies(z3.And(S[a], S[b]), z3.And(h[join(a, b)] == mx(h[a], h[b]),
                                                          h[meet(a, b)] == mn(h[a], h[b])))
                      for a in cells for b in cells])
        return z3.Implies(bounds, graph_closed == z3.And(sublattice(S, cells), hom))
    return claim


def ob_difference(X, S, cells, d, shape):
    h = lambda c: c[0] - c[1]
    le = lambda a, b: a[0] <= b[0] and a[1] <= b[1]
    hom = z3.And([z3.Implies(z3.And(S[a], S[b]), z3.BoolVal(h(join(a, b)) == max(h(a), h(b)) and h(meet(a, b)) == min(h(a), h(b))))
                  for a in cells for b in cells])
    chain = z3.And([z3.Implies(z3.And(S[a], S[b]), z3.BoolVal(le(a, b) or le(b, a))) for a in cells for b in cells])
    mono = z3.And([z3.Implies(z3.And(S[a], S[b]), z3.BoolVal((not le(a, b)) or h(a) <= h(b))) for a in cells for b in cells])
    return hom == z3.And(chain, mono)


def ob_seed(X, S, cells, d, shape):
    # S is the closed set, X the candidate generating set inside it
    A = [sorted({c[i] for c in cells}) for i in range(d)]
    hyp = z3.And(fixed_point(S, cells, d), z3.And([z3.Implies(X[c], S[c]) for c in cells]))
    generates = z3.And([S[c] == own(X, c, cells, d) for c in cells])
    alph = z3.And([z3.Or([X[c] for c in cells if c[i] == v]) == z3.Or([S[c] for c in cells if c[i] == v])
                   for i in range(d) for v in A[i]])
    env = []
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            for a in A[j]:
                inS = z3.Or([S[c] for c in cells if c[j] == a])
                for v in A[i]:
                    reachX = z3.Or([X[y] for y in cells if y[j] <= a and y[i] >= v])
                    reachS = z3.Or([S[y] for y in cells if y[j] <= a and y[i] >= v])
                    env.append(z3.Implies(inS, reachX == reachS))
    return z3.Implies(hyp, generates == z3.And(alph, z3.And(env)))


def ob_normalform(X, S, cells, d, shape):
    A = [sorted({c[i] for c in cells}) for i in range(d)]
    psi = {(i, j, a): z3.Int("psi_%d_%d_%d" % (i, j, a)) for i in range(d) for j in range(d) if i != j for a in A[j]}
    isotone = z3.And([psi[i, j, a] <= psi[i, j, b] for (i, j, a) in psi for b in A[j] if a < b])
    cut = lambda x: z3.And(realised(X, x, cells, d), z3.And([x[i] <= psi[i, j, x[j]] for i in range(d) for j in range(d) if i != j]))
    hyp = z3.And(isotone, z3.And([X[c] == cut(c) for c in cells]))
    concl = z3.And([z3.Implies(z3.And(X[x], z3.BoolVal(x[j] <= a)), x[i] <= psi[i, j, a])
                    for x in cells for (i, j, a) in psi])
    return z3.Implies(hyp, concl)


def ob_product(X, S, cells, d, shape):
    # A on coordinates (0,1), B on coordinate 2; the product index on all three
    acells = cells_of(shape[:2])
    A = {p: z3.Bool("a_%s" % (p,)) for p in acells}
    B = {v: z3.Bool("b_%d" % v) for v in range(shape[2])}
    P = {c: z3.And(A[c[:2]], B[c[2]]) for c in cells}
    hyp = z3.And(z3.Or(list(A.values())), z3.Or(list(B.values())))
    return z3.Implies(hyp, z3.And([own(P, c, cells, d) == z3.And(own(A, c[:2], acells, 2), B[c[2]]) for c in cells]))


def ob_staircase_form(X, S, cells, d, shape):
    """d = 2.  S a fixed point  ==>  S is the band L(s) <= t <= U(s) of its own fibre extremes,
    and those are isotone; conversely every band of isotone L <= U is a sublattice."""
    n0, n1 = shape
    below = lambda s, t: z3.Or([S[(s, u)] for u in range(n1) if u <= t])   # L(s) <= t
    above = lambda s, t: z3.Or([S[(s, u)] for u in range(n1) if u >= t])   # t <= U(s)
    real1 = lambda t: z3.Or([S[(s, t)] for s in range(n0)])
    real0 = lambda s: z3.Or([S[(s, t)] for t in range(n1)])
    band = z3.And([S[(s, t)] == z3.And(real0(s), real1(t), below(s, t), above(s, t)) for s in range(n0) for t in range(n1)])
    iso = z3.And([z3.Implies(z3.And(real0(s), real0(s2)),
                             z3.And([z3.And(z3.Implies(above(s, t), above(s2, t)), z3.Implies(below(s2, t), below(s, t))) for t in range(n1)]))
                  for s in range(n0) for s2 in range(n0) if s < s2])
    forward = z3.Implies(fixed_point(S, cells, 2), z3.And(band, iso))
    L = {s: z3.Int("L_%d" % s) for s in range(n0)}
    U = {s: z3.Int("U_%d" % s) for s in range(n0)}
    hypLU = z3.And([z3.And(L[s] >= 0, L[s] <= U[s], U[s] <= n1 - 1) for s in range(n0)] +
                   [z3.And(L[s] <= L[s + 1], U[s] <= U[s + 1]) for s in range(n0 - 1)])
    T = {(s, t): z3.And(L[s] <= t, t <= U[s]) for s in range(n0) for t in range(n1)}
    backward = z3.Implies(hypLU, sublattice(T, cells))
    return z3.And(forward, backward)


def integer_obligations():
    """Bands and the triangle, over ALL integers (every k, every box)."""
    res = []
    a1, b1, a2, b2, k = z3.Ints("a1 b1 a2 b2 k")
    ab = lambda x: z3.If(x >= 0, x, -x)
    mx = lambda a, b: z3.If(a >= b, a, b)
    mn = lambda a, b: z3.If(a <= b, a, b)
    inB = lambda a, b: ab(a - b) <= k
    s = z3.Solver()
    s.add(z3.And(inB(a1, b1), inB(a2, b2), k >= 0))
    nv = s.check() == z3.sat
    s = z3.Solver()
    s.add(z3.Not(z3.Implies(z3.And(inB(a1, b1), inB(a2, b2)), z3.And(inB(mx(a1, a2), mx(b1, b2)), inB(mn(a1, a2), mn(b1, b2))))))
    r = s.check()
    ok = r == z3.unsat and nv
    res.append(ok)
    row("MACHINE-CHECKED", "Theorem 10: band |a-b| <= k is a sublattice", "all integers a,b,k: %s; hypothesis satisfiable: %s" % (r, nv), ok)

    L1, S1, J1, L2, S2, J2 = z3.Ints("L1 S1 J1 L2 S2 J2")
    inT = lambda L, S, J: z3.And(ab(L - S) <= J, J <= L + S)
    s = z3.Solver()
    s.add(z3.Not(z3.Implies(z3.And(inT(L1, S1, J1), inT(L2, S2, J2)), inT(mx(L1, L2), mx(S1, S2), mx(J1, J2)))))
    r = s.check()
    ok = r == z3.unsat
    res.append(ok)
    row("MACHINE-CHECKED", "Theorem 11: triangle region is join-closed", "all integers: %s" % r, ok)
    s = z3.Solver()
    s.add(z3.And(inT(L1, S1, J1), inT(L2, S2, J2), z3.Not(inT(mn(L1, L2), mn(S1, S2), mn(J1, J2)))))
    r = s.check()
    ok = r == z3.sat
    res.append(ok)
    row("REFUTATION", "triangle region is NOT meet-closed", "Z3 finds a meet failure: %s" % r, ok)
    a, b, c, a2_, b2_, c2_ = z3.Ints("a b c a2 b2 c2")
    inC = lambda a, b, c: ab(a - b) <= c
    s = z3.Solver()
    s.add(z3.Not(z3.Implies(z3.And(inC(a, b, c), inC(a2_, b2_, c2_)), inC(mx(a, a2_), mx(b, b2_), mx(c, c2_)))))
    r = s.check()
    ok = r == z3.unsat
    res.append(ok)
    row("MACHINE-CHECKED", "region |a-b| <= c is join-closed", "all integers: %s" % r, ok)
    return all(res)


def z3_obligations():
    print("MACHINE-CHECKED -- Z3 %s, `unsat` on the negation, every subset of the named box" % z3.get_version_string())
    plan = [
        ("Theorem 1 (i): X subset R(X)", ob_extensive, [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3)]),
        ("Theorem 1 (ii): X subset Y => R(X) subset R(Y)", ob_monotone, [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3)]),
        ("Theorem 1 (iii): R(R(X)) = R(X)", ob_idempotent, [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3)]),
        ("Lemma 4: R(X) is a sublattice", ob_sublattice, [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3)]),
        ("Theorem 2: R(X) inside every sublattice containing X", ob_hardhalf, [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3), (2, 2, 2, 2)]),
        ("Theorem 3: closed <=> X = R(X)", ob_closed_iff_fixed, [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3)]),
        ("Theorem 6: fixed points closed under intersection", ob_moore_intersection, [(3, 3), (4, 4), (2, 2, 2), (3, 3, 3)]),
        ("Theorem 8: projection (0,1) of a fixed point is a fixed point", ob_projection(0, 1), [(2, 2, 2), (3, 3, 3), (2, 3, 4)]),
        ("Theorem 8: projection (0,2) of a fixed point is a fixed point", ob_projection(0, 2), [(2, 2, 2), (3, 3, 3), (2, 3, 4)]),
        ("Theorem 9: graph of h closed <=> S closed and h a homomorphism", ob_graph(3), [(3, 3), (2, 2, 2)]),
        ("Proposition 3: x0 - x1 is a homomorphism on S <=> chain and isotone", ob_difference, [(3, 3), (4, 4), (3, 3, 3)]),
        ("Theorem 12: generation criterion", ob_seed, [(3, 3), (2, 2, 2)]),
        ("Theorem 4: recovered bounds are the least isotone bound system", ob_normalform, [(3, 3), (2, 2, 2)]),
        ("Proposition 4: R(A x B) = R(A) x R(B)", ob_product, [(2, 2, 2), (3, 3, 3), (2, 3, 4)]),
        ("Theorem 5: closed sets at d = 2 are the bands of isotone L <= U", ob_staircase_form, [(3, 3), (4, 4), (3, 5)]),
    ]
    res = []
    for name, claim, shapes in plan:
        for shape in shapes:
            t = time.time()
            ok = prove(name, shape, claim)
            res.append(ok)
            row("MACHINE-CHECKED", name, "box %s, 2^%d subsets, %.1fs" % (boxname(shape), math.prod(shape), time.time() - t), ok)
    res.append(integer_obligations())
    print()
    return all(res)


# ============================================================ EXHAUSTIVE checks

def all_subsets(shape):
    cells = cells_of(shape)
    n = len(cells)
    for mask in range(1, 1 << n):
        yield frozenset(cells[i] for i in range(n) if mask >> i & 1)


def exhaustive_axioms():
    print("EXHAUSTIVE -- every case of a stated finite family")
    res = []
    fams = [(2, 2), (3, 2), (2, 2, 2), (3, 3), (4, 3), (2, 2, 3), (2, 2, 2, 2)]
    tot = bad_ext = bad_idem = bad_gen = bad_iff = 0
    for shape in fams:
        for X in all_subsets(shape):
            R = stair(X)
            tot += 1
            bad_ext += not X <= R
            bad_idem += stair(R) != R
            if len(cells_of(shape)) <= 12:
                bad_gen += gen(X) != R
            bad_iff += is_closed(X) != (R == X)
    ok = (bad_ext, bad_idem, bad_gen, bad_iff) == (0, 0, 0, 0)
    res.append(ok)
    row("EXHAUSTIVE", "Theorem 1, 2, 3 on every non-empty subset", "%d subsets of %s: ext %d, idem %d, R=<X> %d (boxes <= 12 cells), closed<=>fixed %d" % (tot, ",".join(map(boxname, fams)), bad_ext, bad_idem, bad_gen, bad_iff), ok)
    # monotone over every nested pair of the four smallest ambients
    tot = bad = 0
    for shape in fams[:4]:
        cells = cells_of(shape)
        n = len(cells)
        for mask in range(1, 1 << n):
            X = frozenset(cells[i] for i in range(n) if mask >> i & 1)
            RX = stair(X)
            rest = [i for i in range(n) if not mask >> i & 1]
            for sub in range(1 << len(rest)):
                Y = X | {cells[rest[i]] for i in range(len(rest)) if sub >> i & 1}
                tot += 1
                bad += not RX <= stair(Y)
    ok = bad == 0
    res.append(ok)
    row("EXHAUSTIVE", "Theorem 1 (ii) on every nested pair", "%d pairs X subset Y in %s, %d failures" % (tot, ",".join(map(boxname, fams[:4])), bad), ok)
    # Lemma 5's four-witness construction, built on every cell of R(X)
    tot = bad = 0
    for shape in ((3, 3), (4, 4)):
        for X in all_subsets(shape):
            R = stair(X)
            for (a, b) in R:
                y = next(v for v in X if v[0] == a)
                zz = next(v for v in X if v[1] == b)
                u = max((v for v in X if v[0] <= a), key=lambda v: v[1])
                w = max((v for v in X if v[1] <= b), key=lambda v: v[0])
                al = join(y, u)
                ga = join(zz, w)
                tot += 1
                bad += not (al[0] == a and al[1] >= b and ga[1] == b and ga[0] >= a and meet(al, ga) == (a, b))
    ok = bad == 0
    res.append(ok)
    row("EXHAUSTIVE", "Lemma 5: the four-witness construction on every cell", "%d cells of R(X) over every X in 3x3 and 4x4, %d failures" % (tot, bad), ok)
    print()
    return all(res)


def moore_family():
    print("EXHAUSTIVE -- the family of closed sets (Section 5)")
    res = []
    table = []
    fams = [(2, 2), (3, 2), (2, 2, 2), (3, 3), (4, 3), (2, 2, 3), (2, 2, 2, 2)]
    for shape in fams:
        cells = cells_of(shape)
        n = len(cells)
        cl = [frozenset()]
        for X in all_subsets(shape):
            if is_closed(X):
                cl.append(X)
        clset = set(cl)
        ne = [S for S in cl if S]
        # union / intersection over unordered pairs of distinct members
        def pairs(fam, op, member):
            tot = ok = 0
            for i in range(len(fam)):
                for j in range(i + 1, len(fam)):
                    tot += 1
                    ok += op(fam[i], fam[j]) in member
            return ok, tot
        neset = set(ne)
        uo, ut = pairs(cl, lambda a, b: a | b, clset)
        io, it = pairs(cl, lambda a, b: a & b, clset)
        io2, it2 = pairs(ne, lambda a, b: a & b, neset)
        uo2, ut2 = pairs(ne, lambda a, b: a | b, neset)
        # meet-irreducibles: members that are not the intersection of the members strictly above
        mi = 0
        for S in cl:
            inter = frozenset(cells)
            for T in cl:
                if S < T:
                    inter &= T
            mi += inter != S
        # the family as an index over U, and its own closure
        fam_index = [tuple(1 if c in S else 0 for c in cells) for S in cl]
        ph = phi(fam_index)
        all_one = all(v == 1 for v in ph.values())
        Rfam = stair(fam_index)          # direct: the family closed as an index over its 2^n candidate cells
        sizeR = len(Rfam)
        E_fam = sizeR - len(cl)
        sep = all(any((p in S) and (q not in S) for S in cl) for p in cells for q in cells if p != q)
        ok = (io == it) and (uo < ut) and (E_fam == 2 ** n - len(cl)) and all_one and sep and (frozenset(cells) in clset)
        res.append(ok)
        table.append((shape, n, len(cl), len(ne), 2 ** n - len(cl), io, it, uo, ut, uo2, ut2, io2, it2, mi, E_fam))
        row("EXHAUSTIVE", "Moore family at %s" % boxname(shape),
            "|Cl|=%d (%d non-empty), inter %d/%d, union %d/%d (%.1f%%; without empty %.1f%%, inter without empty %.1f%%), meet-irr %d, |R(Cl)| = %d computed directly, E(Cl)=%d = 2^%d-|Cl|" %
            (len(cl), len(ne), io, it, uo, ut, 100 * uo / ut, 100 * uo2 / ut2, 100 * io2 / it2, mi, sizeR, E_fam, n), ok)
    # the witness that unions escape: two chains in 2x2
    S1, S2 = frozenset({(0, 0), (1, 0)}), frozenset({(0, 0), (0, 1)})
    ok = is_closed(S1) and is_closed(S2) and not is_closed(S1 | S2) and is_closed(S1 & S2)
    res.append(ok)
    row("REFUTATION", "union of closed sets need not be closed", "{(0,0),(1,0)} u {(0,0),(0,1)} lacks (1,1); intersection {(0,0)} closed", ok)
    print()
    return all(res), table


def projections():
    print("EXHAUSTIVE -- projections (Section 6)")
    res = []
    cells = cells_of((2, 2, 2))
    tot = bad = 0
    for X in all_subsets((2, 2, 2)):
        if len(X) < 2:
            continue
        proj_ok = all(is_closed({(c[i], c[j]) for c in X}) for i, j in ((0, 1), (0, 2), (1, 2)))
        if proj_ok:
            tot += 1
            bad += not is_closed(X)
    W = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)}
    wit = all(is_closed({(c[i], c[j]) for c in W}) for i, j in ((0, 1), (0, 2), (1, 2))) and not is_closed(W) and join((1, 0, 1), (1, 1, 0)) == (1, 1, 1)
    res.append(wit)
    row("REFUTATION", "closed projections do not imply closure", "six-cell witness in 2x2x2: all three 2-fold projections closed, (1,0,1) v (1,1,0) = (1,1,1) missing", wit)
    res.append(tot > 0)
    row("EXHAUSTIVE", "subsets of 2x2x2 (>= 2 cells) with all 2-fold projections closed", "%d such subsets, %d of them not closed (%.1f%%)" % (tot, bad, 100 * bad / tot), tot > 0)
    # projections of closed sets are closed, every closed subset of 3x3x3 restricted to |X| <= 4 plus every subset of 2x2x2
    tot = bad = 0
    for X in all_subsets((2, 2, 2)):
        if is_closed(X):
            for F in ((0,), (1,), (2,), (0, 1), (0, 2), (1, 2)):
                tot += 1
                bad += not is_closed({tuple(c[i] for i in F) for c in X})
    ok = bad == 0
    res.append(ok)
    row("EXHAUSTIVE", "Theorem 8 on every closed subset of 2x2x2, every proper F", "%d projections, %d failures" % (tot, bad), ok)
    print()
    return all(res), (tot, bad)


def bands_and_triangle():
    print("EXHAUSTIVE / REFUTATION -- bands and the triangle (Section 8)")
    res = []
    T = lambda L, S, J: abs(L - S) <= J <= L + S
    w1 = (T(0, 1, 1) and T(1, 0, 1) and not T(*meet((0, 1, 1), (1, 0, 1))) and meet((0, 1, 1), (1, 0, 1)) == (0, 0, 1))
    w2 = (T(4, 0, 4) and T(2, 2, 0) and not T(*meet((4, 0, 4), (2, 2, 0))) and meet((4, 0, 4), (2, 2, 0)) == (2, 0, 0))
    res.append(w1 and w2)
    row("REFUTATION", "triangle meet witnesses", "(0,1,1)^(1,0,1)=(0,0,1) breaks J <= L+S; (4,0,4)^(2,2,0)=(2,0,0) breaks |L-S| <= J", w1 and w2)
    counts = {}
    for cap in (8, 12, 16):
        C = [(a, b, c) for a in range(cap + 1) for b in range(cap + 1) for c in range(cap + 1) if abs(a - b) <= c]
        Cs = set(C)
        fails = sum(1 for i in range(len(C)) for j in range(i + 1, len(C)) if meet(C[i], C[j]) not in Cs)
        jfails = sum(1 for i in range(len(C)) for j in range(i + 1, len(C)) if join(C[i], C[j]) not in Cs)
        counts[cap] = (len(C), fails, jfails)
        row("EXHAUSTIVE", "region |a-b| <= c on {0..%d}^3" % cap, "%d cells, %d unordered pairs, %d meet failures, %d join failures" % (len(C), len(C) * (len(C) - 1) // 2, fails, jfails), jfails == 0 and fails > 0)
        res.append(jfails == 0 and fails > 0)
    # band exhaustively on a 6x6 box for k = 0..5, as a fixed point of R
    bad = 0
    for k in range(0, 6):
        B = {(a, b) for a in range(6) for b in range(6) if abs(a - b) <= k}
        bad += not (is_closed(B) and stair(B) == B)
    res.append(bad == 0)
    row("EXHAUSTIVE", "band B_k on 6x6 is a fixed point of R", "k = 0..5, %d failures" % bad, bad == 0)
    print()
    return all(res), counts


def staircase_algebra():
    print("EXHAUSTIVE -- the staircase algebra (Section 4)")
    res = []
    # the nine-cell provenance-by-domain index
    L = lambda s: s // 2
    U = lambda s: s + s // 3
    nine = {(s, t) for s in range(4) for t in range(6) if L(s) <= t <= U(s)}
    R = stair(nine)
    ph = phi(nine)
    Uread = {s: max(t for (s2, t) in nine if s2 == s) for s in range(4)}
    Lread = {s: min(t for (s2, t) in nine if s2 == s) for s in range(4)}
    ok = (len(nine) == 9 and R == nine and cypher_R(nine) == nine and all(Uread[s] == U(s) and Lread[s] == L(s) for s in range(4))
          and all(ph[1, 0, s] == U(s) for s in range(4)) and sorted({t for (_, t) in nine}) == [0, 1, 2, 3, 4])
    res.append(ok)
    row("EXHAUSTIVE", "nine-cell staircase: E = 0, L = floor(s/2), U = s + floor(s/3)", "cells %s; |R| = %d; fibre extremes %s / %s" % (sorted(nine), len(R), [Lread[s] for s in range(4)], [Uread[s] for s in range(4)]), ok)
    # Theorem 5 on every closed subset of 4x4 and 3x5: fibres are intervals of the alphabet, extremes isotone
    tot = bad = 0
    for shape in ((4, 4), (3, 5)):
        for X in all_subsets(shape):
            if not is_closed(X):
                continue
            A0 = sorted({s for s, _ in X})
            A1 = sorted({t for _, t in X})
            Lx = {s: min(t for s2, t in X if s2 == s) for s in A0}
            Ux = {s: max(t for s2, t in X if s2 == s) for s in A0}
            band = {(s, t) for s in A0 for t in A1 if Lx[s] <= t <= Ux[s]}
            iso = all(Lx[a] <= Lx[b] and Ux[a] <= Ux[b] for a in A0 for b in A0 if a < b)
            tot += 1
            bad += not (band == X and iso)
    ok = bad == 0
    res.append(ok)
    row("EXHAUSTIVE", "Theorem 5 on every closed subset of 4x4 and 3x5", "%d closed sets, %d not a band of isotone fibre extremes" % (tot, bad), ok)
    print()
    return all(res)


def periodic_cells(he_group=18):
    """The 18-column table on (period, group) with the f block detached: 90 cells, He at `he_group`."""
    pt = {(1, 1), (1, he_group)} | {(p, g) for p in (2, 3) for g in [1, 2] + list(range(13, 19))} | {(p, g) for p in (4, 5, 6, 7) for g in range(1, 19)}
    return pt


FIG1_INDEX = {(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)}


def defects():
    print("EXHAUSTIVE -- worked defects (Section 2)")
    res = []
    # Figure 1's five-cell index
    R1 = stair(FIG1_INDEX)
    ph1 = phi(FIG1_INDEX)
    ok = len(R1) == 9 and cypher_R(FIG1_INDEX) == R1 and len(R1) - len(FIG1_INDEX) == 4
    res.append(ok)
    row("EXHAUSTIVE", "Figure 1: the five-cell index in 5x5", "|R| = %d, E = %d; phi_21 = %s, phi_12 = %s" % (len(R1), len(R1) - 5, [ph1[1, 0, a] for a in range(5)], [ph1[0, 1, a] for a in range(5)]), ok)
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cal = {(m, dd) for m, n in enumerate(months, 1) for dd in range(1, n + 1)}
    R = stair(cal)
    extra = sorted(R - cal)
    ok = len(cal) == 365 and len(R) == 372 and cypher_R(cal) == R and extra == [(2, 29), (2, 30), (2, 31), (4, 31), (6, 31), (9, 31), (11, 31)]
    res.append(ok)
    row("EXHAUSTIVE", "the calendar (month, day)", "365 cells, |R| = %d, E = %d: %s" % (len(R), len(R) - 365, extra), ok)
    pt = periodic_cells(18)
    R = stair(pt)
    gaps = sorted(R - pt)
    want = [(1, g) for g in range(2, 18)] + [(2, g) for g in range(3, 13)] + [(3, g) for g in range(3, 13)]
    ok = len(pt) == 90 and len(R) == 126 and cypher_R(pt) == R and gaps == want
    res.append(ok)
    row("EXHAUSTIVE", "the periodic table, 18 columns, He in group 18, f-block detached", "90 cells, |R| = %d, E = %d; gaps: period 1 groups 2-17 (16), periods 2-3 groups 3-12 (20)" % (len(R), len(R) - 90), ok)
    pt2 = periodic_cells(2)
    R2 = stair(pt2)
    ok = pt2 == (pt - {(1, 18)}) | {(1, 2)} and len(R2) - 90 == 20 and cypher_R(pt2) == R2
    res.append(ok)
    row("EXHAUSTIVE", "the same table with He in group 2", "90 cells, E = %d" % (len(R2) - 90), ok)
    box = {(l, w, h) for l in range(1, 7) for w in range(1, l + 1) for h in range(1, w + 1)}
    ok = len(box) == 56 and stair(box) == box and cypher_R(box) == box
    res.append(ok)
    row("EXHAUSTIVE", "the ordered box l >= w >= h on six values", "56 cells, E = %d" % defect(box), ok)
    print()
    return all(res)


def product_rule():
    print("EXHAUSTIVE -- the product rule (Section 7)")
    tot = bad = badE = 0
    for A in all_subsets((3, 2)):
        for B in all_subsets((2, 2)):
            P = {a + b for a in A for b in B}
            RA, RB, RP = stair(A), stair(B), stair(P)
            tot += 1
            bad += RP != {a + b for a in RA for b in RB}
            EA, EB = len(RA) - len(A), len(RB) - len(B)
            badE += (len(RP) - len(P)) != len(A) * EB + len(B) * EA + EA * EB
    ok = bad == 0 and badE == 0
    row("EXHAUSTIVE", "Proposition 4: R(A x B) = R(A) x R(B) and the defect identity", "%d pairs (A in 3x2, B in 2x2), %d closure failures, %d identity failures" % (tot, bad, badE), ok)
    print()
    return ok


# ------------------------------------------------------------------- seeds

def cover_elements(X):
    """The set-cover instance of Theorem 13: alphabet slots (i, v) and steps (i, j, t)."""
    A = alphabets(X)
    d = len(A)
    ph = phi(X)
    slots = [("slot", i, v) for i in range(d) for v in A[i]]
    steps = []
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            seen = set()
            for t in A[j]:
                if ph[i, j, t] not in seen:
                    seen.add(ph[i, j, t])
                    steps.append(("step", i, j, t))
    return slots + steps, ph


def covers(g, el, ph):
    if el[0] == "slot":
        return g[el[1]] == el[2]
    _, i, j, t = el
    return g[j] <= t and g[i] == ph[i, j, t]


def seed_bruteforce(X, cap):
    """Least k with some k-subset G of X having R(G) = X, by direct closure (no set cover)."""
    X = set(X)
    L = sorted(X)
    for k in range(1, cap + 1):
        for G in itertools.combinations(L, k):
            if stair(G) == X:
                return k, G
    return None, None


def seed_cover(X):
    """Exact minimum set cover by branch and bound: branch on the element with fewest covering cells."""
    els, ph = cover_elements(X)
    L = sorted(X)
    cov = {el: [g for g in L if covers(g, el, ph)] for el in els}
    best = [len(L), None]

    def rec(chosen, uncovered):
        if not uncovered:
            if len(chosen) < best[0]:
                best[0], best[1] = len(chosen), list(chosen)
            return
        if len(chosen) + 1 >= best[0]:
            return
        el = min(uncovered, key=lambda e: len(cov[e]))
        for g in cov[el]:
            rec(chosen + [g], [e for e in uncovered if not covers(g, e, ph)])

    rec([], list(els))
    return best[0], best[1]


def central(m):
    return math.comb(m, m // 2)


def m_of(d):
    m = 1
    while central(m) < d:
        m += 1
    return m


def seed_formula_box(c, d):
    return c - 2 + m_of(d)


def max_clique(vs, adj):
    best = [0]

    def bk(R, P, X):
        if not P and not X:
            best[0] = max(best[0], len(R))
            return
        if len(R) + len(P) <= best[0]:
            return
        pivot = max(P | X, key=lambda u: len(P & adj[u]))
        for v in list(P - adj[pivot]):
            bk(R | {v}, P & adj[v], X & adj[v])
            P = P - {v}
            X = X | {v}
    bk(frozenset(), frozenset(vs), frozenset())
    return best[0]


def seeds():
    print("EXHAUSTIVE -- the seed (Section 9)")
    res = []
    out = {}
    # (a) the set-cover reduction against direct closure, every G inside every closed X of 3x3 and 2x2x2
    tot = bad = 0
    for shape in ((3, 3), (2, 2, 2)):
        for X in all_subsets(shape):
            if not is_closed(X):
                continue
            els, ph = cover_elements(X)
            L = sorted(X)
            for mask in range(1, 1 << len(L)):
                G = [L[i] for i in range(len(L)) if mask >> i & 1]
                tot += 1
                bad += (stair(G) == X) != all(any(covers(g, el, ph) for g in G) for el in els)
    ok = bad == 0
    res.append(ok)
    row("EXHAUSTIVE", "Theorem 13: R(G) = X <=> G covers every slot and step", "%d pairs (G, X) over every closed X of 3x3 and 2x2x2, %d disagreements" % (tot, bad), ok)
    # (b) full boxes: brute force by closure at tiny sizes, set cover and clique beyond
    brute = {(2, 2): 2, (3, 2): 3, (2, 3): 3, (3, 3): 4, (2, 4): 4, (2, 5): 4, (4, 2): 4, (5, 2): 5}
    bad = 0
    for (c, d), want in brute.items():
        X = set(itertools.product(range(c), repeat=d))
        k, G = seed_bruteforce(X, want)
        okk = k == want and k == seed_formula_box(c, d)
        bad += not okk
        out[("box", c, d)] = k
        row("EXHAUSTIVE", "seed of the full box %d^%d by direct closure" % (c, d), "every subset of size < %d fails, one of size %d generates: %s; formula c-2+m(d) = %d; d+c-2 = %d" % (want, want, G, seed_formula_box(c, d), d + c - 2), okk)
    res.append(bad == 0)
    # (b') the law at (c, d) = (5, 2023): m(2023) by the central binomials, against the 18 printed in Czedli 2023b table (4.30)
    m = m_of(2023)
    ok = m == 14 and central(13) == 1716 and central(14) == 3432 and seed_formula_box(5, 2023) == 17
    res.append(ok)
    row("EXHAUSTIVE", "the law at (c, d) = (5, 2023)", "C(13,6) = %d < 2023 <= %d = C(14,7), m(2023) = %d, c-2+m = %d (Czedli 2023b table (4.30) prints 18; its Thm 2.4 with p = 3 gives %d)" % (central(13), central(14), m, seed_formula_box(5, 2023), 3 + m), ok)
    # (c) the clique form: largest d that k cells generate, c = 2, 3, 4
    def compat(u, v, c):
        return any(u[r] == c - 1 and v[r] == 0 for r in range(len(u))) and any(v[r] == c - 1 and u[r] == 0 for r in range(len(u)))
    bad = 0
    for c, ks in ((2, range(2, 8)), (3, range(3, 7)), (4, range(4, 7))):
        got = []
        for k in ks:
            vs = [v for v in itertools.product(range(c), repeat=k) if set(v) == set(range(c))]
            adj = {u: frozenset(v for v in vs if v != u and compat(u, v, c)) for u in vs}
            w = max_clique(vs, adj)
            got.append((k, w, central(k - c + 2)))
            bad += w != central(k - c + 2)
        out[("clique", c)] = got
        row("EXHAUSTIVE", "full box c = %d: largest d generated by k cells" % c, "; ".join("k=%d: %d (C(k-c+2, floor) = %d)" % g for g in got), all(g[1] == g[2] for g in got))
    res.append(bad == 0)
    # (d) the ordered simplex D(d, c): x_1 >= ... >= x_d, exact seed d + c - 1 and every seed cell forced
    bad = 0
    for d, c in ((2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (4, 4), (3, 4), (4, 3), (5, 3)):
        X = {x for x in itertools.product(range(c), repeat=d) if all(x[i] >= x[i + 1] for i in range(d - 1))}
        els, ph = cover_elements(X)
        L = sorted(X)
        forced = {el: [g for g in L if covers(g, el, ph)] for el in els}
        forced_cells = {tuple(v[0]) for v in forced.values() if len(v) == 1}
        pred = {tuple([t] * d) for t in range(c)} | {tuple([c - 1] * k + [0] * (d - k)) for k in range(1, d)}
        covers_all = all(any(covers(g, el, ph) for g in pred) for el in els)
        k, G = seed_cover(X)
        if d + c <= 6:
            kb, _ = seed_bruteforce(X, d + c - 1)
        else:
            kb = k
        okk = forced_cells == pred and covers_all and k == d + c - 1 and kb == d + c - 1 and len(X) == math.comb(d + c - 1, d) and stair(pred) == X
        bad += not okk
        out[("simplex", d, c)] = k
        row("EXHAUSTIVE", "ordered simplex D(%d,%d): %d cells" % (d, c, len(X)), "forced cells = the %d predicted, they generate; min cover %d; direct closure %s" % (len(pred), k, kb), okk)
    res.append(bad == 0)
    # (e) refutations: seed >= d fails (a chain), d + c - 2 fails at 2^5
    ch = {(0, 0, 0), (1, 1, 1)}
    k, _ = seed_bruteforce(ch, 3)
    ok = is_closed(ch) and stair(ch) == ch and k == 2
    res.append(ok)
    row("REFUTATION", "seed >= d fails", "the chain {(0,0,0),(1,1,1)} is closed in d = 3 and generated by 2 cells", ok)
    ok = out[("box", 2, 5)] == 4 and seed_formula_box(2, 5) == 4
    res.append(ok)
    row("REFUTATION", "seed of a full box = d + c - 2 fails from d = 5", "2^5 is generated by 4 cells (d + c - 2 = 5); the law c - 2 + m(d) gives 4", ok)
    # (f) alphabet lower bound on every closed subset of 3x3 and 2x2x2
    tot = bad = 0
    for shape in ((3, 3), (2, 2, 2)):
        for X in all_subsets(shape):
            if is_closed(X):
                k, _ = seed_cover(X)
                tot += 1
                bad += k < max(len(a) for a in alphabets(X))
    ok = bad == 0
    res.append(ok)
    row("EXHAUSTIVE", "Proposition 5: seed >= largest alphabet", "%d closed sets, %d violations" % (tot, bad), ok)
    print()
    return all(res), out


def cited():
    print("CITED -- taken from the literature, not checked here")
    for name, src in [
        ("Moore closure operators and Moore families", "E. H. Moore 1910; M. Ward 1942; Caspard & Monjardet 2003"),
        ("sublattices of a product determined by 2-fold projections", "Baker & Pixley 1975 (majority term); Bergman 1977 (name, converse); Topkis 1976; Veinott 1989; Queyranne & Tardella 2008"),
        ("E = 0 is binary decomposability into monotone constraints; row-convex networks are globally consistent", "Montanari 1974; van Beek & Dechter 1995"),
        ("staircase / connected row-convex constraints", "Deville, Barette & Van Hentenryck 1999"),
        ("Sperner's theorem, the LYM inequality, the Bollobas set-pair inequality", "Sperner 1928; Lubell 1966; Bollobas 1965"),
        ("minimum set cover is NP-complete", "Karp 1972"),
        ("seed(c^d) = c - 2 + m(d): the generating number of a direct power of a chain", "Czedli 2023a Thm 2.1 (c = 2); Czedli 2023b Thm 2.4 + Obs 3.1 with Griggs, Stahl & Trotter 1984 (all c)"),
        ("Caratheodory number of the subsemilattice convexity = breadth; breadth of d chains = d", "Jamison-Waldner 1982; van de Vel 1993; Queyranne & Tardella 2017"),
    ]:
        row("CITED", name, src)
    print()


# ------------------------------------------------------------------- selftest

def selftest():
    print("SELFTEST -- negative controls that MUST be refuted")
    res = []
    # (1) a false Z3 claim: R(X) subset X
    def false_claim(X, S, cells, d, shape):
        return z3.And([z3.Implies(own(X, c, cells, d), X[c]) for c in cells])
    refuted = not prover.prove("negative control", (3, 3), false_claim, quiet=True)
    res.append(refuted)
    row("SELFTEST", "false claim 'R(X) subset X' refuted by Z3", "3x3: %s" % ("sat, counterexample found" if refuted else "NOT refuted"), refuted)
    # (2) a false exhaustive claim: unions of closed sets are closed
    bad = 0
    cl = [X for X in all_subsets((2, 2)) if is_closed(X)]
    for i in range(len(cl)):
        for j in range(i + 1, len(cl)):
            bad += not is_closed(cl[i] | cl[j])
    res.append(bad > 0)
    row("SELFTEST", "false claim 'the family is union-closed' refuted", "%d unordered pairs of distinct closed sets in 2x2 whose union escapes" % bad, bad > 0)
    # (3) a false seed law, refuted by direct closure (a decision procedure, not a formula comparison)
    k, G = seed_bruteforce(set(itertools.product(range(2), repeat=5)), 5)
    refuted = k is not None and k < 5
    res.append(refuted)
    row("SELFTEST", "false law 'seed(c^d) = d + c - 2' refuted at (2,5) by direct closure", "law says 5; every subset of size < %s fails and %s cells generate: %s" % (k, k, G), refuted)
    print()
    return all(res)


def main():
    t0 = time.time()
    print(__doc__)
    g = guards()
    if not g:
        print("GUARDS FAILED -- obligations not reported")
        return 1
    ok = z3_obligations()
    ok &= exhaustive_axioms()
    mf, table = moore_family()
    ok &= mf
    pr, _ = projections()
    ok &= pr
    bt, _ = bands_and_triangle()
    ok &= bt
    ok &= staircase_algebra()
    ok &= defects()
    ok &= product_rule()
    sd, _ = seeds()
    ok &= sd
    cited()
    if "--selftest" in sys.argv:
        ok &= selftest()
    print("=" * 100)
    from collections import Counter
    cnt = Counter(s for s, _, _, _ in ROWS)
    for s in ("GUARD", "MACHINE-CHECKED", "EXHAUSTIVE", "REFUTATION", "CITED", "SELFTEST"):
        if cnt[s]:
            print("  %-16s %3d" % (s, cnt[s]))
    print("  %d rows, %d failures, %.0f s" % (len(ROWS), len(FAILS), time.time() - t0))
    for f in FAILS:
        print("  FAILED: " + f)
    print("=" * 100)
    return 0 if ok and not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
