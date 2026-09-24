#!/usr/bin/env python3
"""check.py -- every number and every decidable claim of PAPER.md (order recovery and the
arity law), recomputed.

    python3 check.py              one line per obligation, a summary, exit 1 on any failure
    python3 check.py --selftest   the same, plus the negative controls (a false claim must be
                                  reported REFUTED and a wrong encoding reference must be caught)

stdlib + z3 + numpy.  Python 3.12 (export PATH="$PWD/method/bin:$PATH").

Instruments are imported BY PATH and never copied:
  research/warp-drive/prover.py   the Z3 harness (cells_of, observed, closed, subset_vars)
  tools/cypher.py                 op_order, the reference staircase closure R, and the seated
                                  index fixtures (_lambda, _periodic, _janet)

Status words, exactly as the paper uses them:
  PROVED          a written proof in the paper; nothing to run (listed for the record)
  MACHINE-CHECKED Z3 returned unsat on the negation over EVERY subset of a named box and, where
                  an order is unknown, every total order on the named axis, both guards passed
  EXHAUSTIVE      a decision procedure visited every case of a stated finite family
  SAMPLED         a seeded pseudorandom sweep of a stated size
  REFUTATION      an explicit witness disproves the claim

Writes results.json beside this file; figures.py draws from it and from nothing else.
"""
import importlib.util
import itertools
import json
import math
import os
import random
import statistics
import sys
import time
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))


def _load(name, rel):
    path = os.path.join(ROOT, rel)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


prover = _load("prover", "research/warp-drive/prover.py")
cypher = _load("cypher", "tools/cypher.py")
prover.require_z3()
import z3  # noqa: E402

RESULTS = {}
LINES = []
FAILS = []


def report(status, name, ok, detail=""):
    tag = status if ok else "FAIL"
    line = "  [%-15s] %-58s %s" % (tag, name, detail)
    print(line)
    LINES.append(line)
    if not ok:
        FAILS.append(name)
    return ok


def put(key, value):
    RESULTS[key] = value
    return value


# ---------------------------------------------------------------- concrete reference code
# Independent implementations of the objects the obligations encode.  They are the guard's
# reference, written fresh; the reference CLOSURE of the paper is cypher.op_order.

def cells_of(shape):
    return prover.cells_of(shape)


def meet(a, b):
    return tuple(map(min, a, b))


def join(a, b):
    return tuple(map(max, a, b))


def leq(a, b):
    return all(x <= y for x, y in zip(a, b))


def alphabets(X, d):
    return [sorted({c[i] for c in X}) for i in range(d)]


def closed_under(X, ranks):
    """X closed under the ordering given by ranks[i]: value -> rank (a total order per axis)."""
    d = len(ranks)
    Y = {tuple(ranks[i][c[i]] for i in range(d)) for c in X}
    Yl = sorted(Y)
    for a in range(len(Yl)):
        for b in range(a + 1, len(Yl)):
            x, y = Yl[a], Yl[b]
            if meet(x, y) not in Y or join(x, y) not in Y:
                return False
    return True


def natural(X, d):
    return [{v: v for v in a} for a in alphabets(X, d)]


def P_relation(X, axis, ranks):
    """The 'may precede' relation on axis `axis`, the other axes ordered by ranks.
    u P v  iff  for all p in F(u), q in F(v): p ^ q in F(u) and p v q in F(v)."""
    d = len(ranks)
    others = [i for i in range(d) if i != axis]
    vals = sorted({c[axis] for c in X})
    fib = {u: {tuple(ranks[i][c[i]] for i in others) for c in X if c[axis] == u} for u in vals}
    P = {}
    for u in vals:
        for v in vals:
            P[(u, v)] = all(meet(p, q) in fib[u] and join(p, q) in fib[v]
                            for p in fib[u] for q in fib[v])
    return vals, P


def total_preorder(vals, P):
    return (all(P[(u, u)] for u in vals)
            and all(P[(u, v)] or P[(v, u)] for u in vals for v in vals))


def linear_extensions(vals, P):
    """Every linear extension of the total preorder P (ties in every order)."""
    def strict_pred(u):
        return sum(1 for v in vals if P[(v, u)] and not P[(u, v)])
    blocks = {}
    for u in vals:
        blocks.setdefault(strict_pred(u), []).append(u)
    for combo in itertools.product(*[list(itertools.permutations(blocks[k])) for k in sorted(blocks)]):
        yield tuple(u for blk in combo for u in blk)


def canonical_extension(vals, P):
    """The linear extension the existence theorem names: strict P first, ties by the raw label."""
    return tuple(sorted(vals, key=lambda u: (sum(1 for v in vals if P[(v, u)] and not P[(u, v)]), u)))


def reorderable_brute(X, d):
    A = alphabets(X, d)
    for perms in itertools.product(*[itertools.permutations(a) for a in A]):
        if closed_under(X, [{v: r for r, v in enumerate(p)} for p in perms]):
            return True
    return False


def R_index(X, names=None):
    """cypher.op_order on X (natural order on each observed alphabet): the reference closure."""
    d = len(next(iter(X)))
    ix = cypher.Index("X", names or ["c%d" % i for i in range(d)], [tuple(c) for c in X])
    adm, _ = cypher.op_order(ix, {})
    return {tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in adm}


# ---------------------------------------------------------------- the tree-propagation DP

def tree_recover(X, d, tree, root=0, all_solutions=False):
    """Order recovery on a constraint tree.  Returns (solutions, root_orders_tried).
    A solution maps each axis to a tuple (its recovered order).  With all_solutions=False the
    first solution is returned; with True, every solution, as a list."""
    A = alphabets(X, d)
    adj = {i: [] for i in range(d)}
    for (i, j) in tree:
        adj[i].append(j)
        adj[j].append(i)
    proj = {}
    for (i, j) in tree:
        proj[(i, j)] = {(c[i], c[j]) for c in X}
        proj[(j, i)] = {(c[j], c[i]) for c in X}
    parent = {root: None}
    stack = [root]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in parent:
                parent[v] = u
                stack.append(v)
    children = {i: [v for v in adj[i] if parent.get(v) == i] for i in range(d)}
    memo = {}

    def P_child(i, rank_i, c):
        pr = proj[(i, c)]
        vals = sorted({p[1] for p in pr})
        fib = {u: {rank_i[p[0]] for p in pr if p[1] == u} for u in vals}
        P = {(u, v): all(min(p, q) in fib[u] and max(p, q) in fib[v] for p in fib[u] for q in fib[v])
             for u in vals for v in vals}
        return vals, P

    def feasible(i, oi):
        """All (or the first) assignments of the subtree at i consistent with order oi at i."""
        key = (i, oi)
        if key in memo:
            return memo[key]
        rank = {v: r for r, v in enumerate(oi)}
        partial = [{i: oi}]
        for c in children[i]:
            vals, P = P_child(i, rank, c)
            if not total_preorder(vals, P):
                memo[key] = []
                return []
            subs = []
            for oc in linear_extensions(vals, P):
                s = feasible(c, oc)
                subs.extend(s)
                if s and not all_solutions:
                    break
            if not subs:
                memo[key] = []
                return []
            partial = [{**p, **s} for p in partial for s in subs]
            if not all_solutions:
                partial = partial[:1]
        memo[key] = partial
        return partial

    out = []
    tried = 0
    for orr in itertools.permutations(A[root]):
        tried += 1
        sol = feasible(root, orr)
        out.extend(sol)
        if sol and not all_solutions:
            break
    return out, tried


def tree_structured(X, d, tree):
    """X equals the intersection of the cylinders over its tree-edge projections."""
    A = alphabets(X, d)
    proj = {e: {(c[e[0]], c[e[1]]) for c in X} for e in tree}
    Xs = set(X)
    for x in itertools.product(*A):
        if all((x[i], x[j]) in proj[(i, j)] for (i, j) in tree) != (x in Xs):
            return False
    return True


# ---------------------------------------------------------------- Z3 encodings

def order_vars(A, tag):
    s = {(u, v): z3.Bool("%s_%s_%s" % (tag, u, v)) for u in A for v in A if u != v}
    total_antisym = z3.And([z3.Xor(s[(u, v)], s[(v, u)]) for u in A for v in A if u < v])
    trans = z3.And([z3.Implies(z3.And(s[(u, v)], s[(v, w)]), s[(u, w)])
                    for u in A for v in A for w in A if len({u, v, w}) == 3])
    return s, z3.And(total_antisym, trans)


def enc_closed_s(X, s, cells, axis):
    """X closed under: the order s on `axis`, the natural order elsewhere."""
    cons = []
    for x in cells:
        for y in cells:
            if x >= y:
                continue
            if x[axis] == y[axis]:
                cons.append(z3.Implies(z3.And(X[x], X[y]), z3.And(X[meet(x, y)], X[join(x, y)])))
            else:
                for (lo, hi) in ((x, y), (y, x)):
                    m, j = list(meet(x, y)), list(join(x, y))
                    m[axis], j[axis] = lo[axis], hi[axis]
                    cons.append(z3.Implies(z3.And(X[x], X[y], s[(lo[axis], hi[axis])]),
                                           z3.And(X[tuple(m)], X[tuple(j)])))
    return z3.And(cons)


def enc_P(X, cells, axis, A):
    """P[(u,v)] : u may precede v on `axis`, the other axes in natural order."""
    fib = {u: [c for c in cells if c[axis] == u] for u in A}
    P = {}
    for u in A:
        for v in A:
            cons = []
            for p in fib[u]:
                for q in fib[v]:
                    m, j = list(meet(p, q)), list(join(p, q))
                    m[axis], j[axis] = u, v
                    cons.append(z3.Implies(z3.And(X[p], X[q]), z3.And(X[tuple(m)], X[tuple(j)])))
            P[(u, v)] = z3.And(cons)
    return P


def enc_canonical(P, A, tag):
    """The canonical linear extension s*: u before v iff u has fewer strict predecessors, ties by
    label.  Encoded as a Bool per ordered pair, defined from P by counting."""
    def npred(u):
        return z3.Sum([z3.If(z3.And(P[(v, u)], z3.Not(P[(u, v)])), 1, 0) for v in A])
    s = {}
    for u in A:
        for v in A:
            if u != v:
                s[(u, v)] = z3.Or(npred(u) < npred(v), z3.And(npred(u) == npred(v), z3.BoolVal(u < v)))
    return s


def enc_interval(X, A, B):
    """Every fibre F(u), u in A, is an interval of the chain B."""
    return z3.And([z3.Implies(z3.And(X[(u, b1)], X[(u, b3)]), X[(u, b2)])
                   for u in A for b1 in B for b2 in B for b3 in B if b1 < b2 < b3])


def enc_lo_le(X, B, u, v):
    """lo(u) <= lo(v): every c in F(v) has some c2 <= c in F(u)."""
    return z3.And([z3.Implies(X[(v, c)], z3.Or([X[(u, c2)] for c2 in B if c2 <= c])) for c in B])


def enc_hi_le(X, B, u, v):
    """hi(u) <= hi(v): every c in F(u) has some c2 >= c in F(v)."""
    return z3.And([z3.Implies(X[(u, c)], z3.Or([X[(v, c2)] for c2 in B if c2 >= c])) for c in B])


def enc_mono(X, s, A, B):
    """Both endpoints non-decreasing along s."""
    return z3.And([z3.Implies(s[(u, v)], z3.And(enc_lo_le(X, B, u, v), enc_hi_le(X, B, u, v)))
                   for u in A for v in A if u != v])


def enc_remclosed(S, cells, a, b):
    """S minus the interval [a,b] is closed under meet and join."""
    def rem(c):
        return z3.And(S[c], z3.BoolVal(not (leq(a, c) and leq(c, b))))
    return z3.And([z3.Implies(z3.And(rem(x), rem(y)), z3.And(rem(meet(x, y)), rem(join(x, y))))
                   for x in cells for y in cells if x < y])


def enc_jp(S, cells, a):
    """a is join-prime in S."""
    return z3.And([z3.Implies(z3.And(S[x], S[y], z3.BoolVal(leq(a, join(x, y)))),
                              z3.BoolVal(leq(a, x) or leq(a, y))) for x in cells for y in cells])


def enc_mp(S, cells, b):
    """b is meet-prime in S."""
    return z3.And([z3.Implies(z3.And(S[x], S[y], z3.BoolVal(leq(meet(x, y), b))),
                              z3.BoolVal(leq(x, b) or leq(y, b))) for x in cells for y in cells])


def ev(f):
    """Evaluate a closed Z3 formula (every atom a BoolVal) to a Python bool."""
    return z3.is_true(z3.simplify(f))


# ---------------------------------------------------------------- concrete references for the guard
# Written fresh, from the paper's definitions, never from the encodings above.

def ref_fibre(Xs, u):
    return sorted(c[1] for c in Xs if c[0] == u)


def ref_interval(Xs, A):
    for u in A:
        F = ref_fibre(Xs, u)
        if F and F != list(range(F[0], F[-1] + 1)):
            return False
    return True


def ref_lo_le(Xs, u, v):
    Fu, Fv = ref_fibre(Xs, u), ref_fibre(Xs, v)
    if not Fv:
        return True
    if not Fu:
        return False
    return Fu[0] <= Fv[0]


def ref_hi_le(Xs, u, v):
    Fu, Fv = ref_fibre(Xs, u), ref_fibre(Xs, v)
    if not Fu:
        return True
    if not Fv:
        return False
    return Fu[-1] <= Fv[-1]


def ref_mono(Xs, rank0, A):
    return all((not rank0[u] < rank0[v]) or (ref_lo_le(Xs, u, v) and ref_hi_le(Xs, u, v))
               for u in A for v in A if u != v)


def ref_remclosed(Ss, a, b):
    rem = [c for c in Ss if not (leq(a, c) and leq(c, b))]
    R = set(rem)
    return all(meet(x, y) in R and join(x, y) in R for x in rem for y in rem)


def ref_jp(Ss, a):
    return all((not leq(a, join(x, y))) or leq(a, x) or leq(a, y) for x in Ss for y in Ss)


def ref_mp(Ss, b):
    return all((not leq(meet(x, y), b)) or leq(x, b) or leq(y, b) for x in Ss for y in Ss)


def ref_closed_natural(Ss):
    S = set(Ss)
    return all(meet(x, y) in S and join(x, y) in S for x in Ss for y in Ss)


def z3_prove(claim):
    sv = z3.Solver()
    sv.add(z3.Not(claim))
    r = sv.check()
    return r == z3.unsat, (sv.model() if r == z3.sat else None)


def z3_sat(formula):
    sv = z3.Solver()
    sv.add(formula)
    r = sv.check()
    return r == z3.sat, (sv.model() if r == z3.sat else None)


# ======================================================================= sections

def section_lambda():
    print("\nA. The atomic index Lambda: closure, totality, structure")
    t = time.time()
    ix = cypher._lambda()
    cells = [tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in ix.cells]
    d = 8
    L = set(cells)
    adm, _ = cypher.op_order(ix, {})
    put("lambda_cells", len(cells))
    put("lambda_box", ix.box)
    put("lambda_alphabets", [len(a) for a in ix.alphabets])
    put("lambda_E", len(adm) - len(ix.cells))
    report("EXHAUSTIVE", "Lambda: 976 cells in a box of 6,912, E = 0 under op_order",
           len(cells) == 976 and ix.box == 6912 and len(adm) == 976,
           "cells=%d box=%d E=%d" % (len(cells), ix.box, len(adm) - 976))
    A = alphabets(cells, d)

    # totality: the seven bounds decide every ambient point, and agree with membership
    def chi(x):
        n, l, k, q, e, f, g, S = x
        return l <= n - 1 and k <= 4 * l + 2 and q <= k and f <= e - 1 and g <= 4 * f + 2 and g <= q and S <= k
    amb = list(itertools.product(*A))
    agree = sum(1 for x in amb if chi(x) == (x in L))
    put("ambient", len(amb))
    put("chi_agree", agree)
    report("EXHAUSTIVE", "totality: chi decided on all 6,912 ambient points, = membership",
           len(amb) == 6912 and agree == 6912, "ambient=%d agree=%d" % (len(amb), agree))
    # Corollary 1's own predicate: the conjunction of the 56 envelope comparisons, evaluated at every
    # ambient point by the local envelope routine (guarded against op_order), equals membership
    env = R_local(cells, d)
    put("envelope_conjunction_agrees", env == L)
    report("EXHAUSTIVE", "Corollary 1: the envelope conjunction, evaluated at all 6,912 ambient points, = membership",
           env == L and len(amb) == 6912, "|envelope region|=%d cells=%d" % (len(env), len(L)))
    # the seventh bound 2S <= k admits spin labels of the wrong parity: Lambda is an index of
    # admissible labels under seven envelope bounds, not of realised configurations
    odd = sum(1 for c in cells if (c[7] - c[2]) % 2)
    put("lambda_wrong_parity_cells", odd)
    report("EXHAUSTIVE", "Lambda admits 2S of the wrong parity: (1,0,1,0,1,0,0,0) is a cell; cells with 2S - k odd counted",
           (1, 0, 1, 0, 1, 0, 0, 0) in L and odd > 0, "wrong-parity cells=%d of %d" % (odd, len(cells)))

    # the alphabet has closed size sum(|A_i| - 1) = 17 = join-irreducibles above the bottom
    C = np.array(cells)
    ji, mi = [], []
    for c in cells:
        cc = np.array(c)
        below = C[np.all(C <= cc, axis=1) & np.any(C != cc, axis=1)]
        above = C[np.all(C >= cc, axis=1) & np.any(C != cc, axis=1)]
        if len(below) == 0 or tuple(below.max(axis=0)) != c:
            ji.append(c)
        if len(above) == 0 or tuple(above.min(axis=0)) != c:
            mi.append(c)
    put("lambda_JI", len(ji))
    put("lambda_MI", len(mi))
    put("lambda_JI_cap_MI", len(set(ji) & set(mi)))
    put("lambda_sum_alph_minus1", sum(len(a) - 1 for a in A))
    report("EXHAUSTIVE", "Lambda: 18 join-irreducibles (17 + bottom), 18 meet-irreducibles, none both",
           len(ji) == 18 and len(mi) == 18 and not (set(ji) & set(mi)) and sum(len(a) - 1 for a in A) == 17,
           "JI=%d MI=%d both=%d sum(|A_i|-1)=%d" % (len(ji), len(mi), len(set(ji) & set(mi)), sum(len(a) - 1 for a in A)))

    # binding pairs and the constraint tree
    bind = [(i, j) for i in range(d) for j in range(i + 1, d)
            if len({(c[i], c[j]) for c in cells}) < len(A[i]) * len(A[j])]
    TREE = [(0, 1), (1, 2), (2, 3), (4, 5), (5, 6), (3, 6), (2, 7)]
    ts = tree_structured(cells, d, TREE)
    put("lambda_binding_pairs", len(bind))
    put("lambda_tree", TREE)
    put("lambda_tree_structured", ts)
    report("EXHAUSTIVE", "Lambda: 16 binding pairs; equals the cylinder intersection over the 7-edge tree",
           len(bind) == 16 and ts, "binding=%d tree-structured=%s" % (len(bind), ts))

    # pushback over all pairs; the floor is derived from JI cap MI = empty
    pb = {c: 0 for c in cells}
    cl = sorted(cells)
    pairs = 0
    for i in range(len(cl)):
        for j in range(i + 1, len(cl)):
            a, b = cl[i], cl[j]
            pairs += 1
            m, jn = meet(a, b), join(a, b)
            if m != a and m != b:
                pb[m] += 1
            if jn != a and jn != b:
                pb[jn] += 1
    v = sorted(pb.values())
    put("pushback", dict(pairs=pairs, min=v[0], median=float(statistics.median(v)), max=v[-1],
                         mean=round(sum(v) / len(v), 1), zero=v.count(0)))
    zero_iff = all((pb[c] == 0) == (c in set(ji) and c in set(mi)) for c in cells)
    report("EXHAUSTIVE", "pushback over 475,800 pairs: min 16, median 503.5, mean 739.0, max 5,091, none zero; zero iff JI and MI",
           pairs == 475800 and v[0] == 16 and v.count(0) == 0 and zero_iff and v[-1] == 5091
           and statistics.median(v) == 503.5 and round(sum(v) / len(v), 1) == 739.0,
           "pairs=%d min=%d median=%s max=%d mean=%.1f zero=%d" % (pairs, v[0], statistics.median(v), v[-1], sum(v) / len(v), v.count(0)))

    # the step: the smallest interval [a,b] with a join-prime (= JI, distributive) and b meet-prime
    best = None
    for a in ji:
        for b in mi:
            if leq(a, b):
                cnt = sum(1 for c in cells if leq(a, c) and leq(c, b))
                if best is None or cnt < best[0]:
                    best = (cnt, a, b)
    cnt, a, b = best
    rem = [c for c in cells if not (leq(a, c) and leq(c, b))]
    Rs = set(rem)
    bad = 0
    pr = 0
    for i in range(len(rem)):
        for j in range(i + 1, len(rem)):
            pr += 1
            if meet(rem[i], rem[j]) not in Rs or join(rem[i], rem[j]) not in Rs:
                bad += 1
    put("step_lambda", dict(step=cnt, a=list(a), b=list(b), remaining=len(rem), pairs=pr, failures=bad))
    report("EXHAUSTIVE", "step(Lambda) = 4, interval (2,1,3,3,2,1,3,0)..(3,1,3,3,3,1,3,0); 972 left, 0 failures",
           cnt == 4 and a == (2, 1, 3, 3, 2, 1, 3, 0) and b == (3, 1, 3, 3, 3, 1, 3, 0) and len(rem) == 972 and pr == 471906 and bad == 0,
           "step=%d remaining=%d pairs=%d failures=%d" % (cnt, len(rem), pr, bad))

    # the 216-cell cap setting, built from the seven bounds (independent), and the tree there
    def lam(N, E, LL, K, F):
        out = []
        for n, l, k, q, e, f, g, S in itertools.product(range(1, N + 1), range(0, LL + 1), range(1, K + 1), range(0, K + 1),
                                                       range(1, E + 1), range(0, F + 1), range(0, 4 * F + 3), range(0, K + 1)):
            if l <= n - 1 and k <= 4 * l + 2 and q <= k and f <= e - 1 and g <= 4 * f + 2 and g <= q and S <= k:
                out.append((n, l, k, q, e, f, g, S))
        return out
    L976 = lam(3, 3, 1, 3, 1)
    L216 = lam(2, 2, 1, 2, 1)
    put("lambda_216", len(L216))
    report("EXHAUSTIVE", "the seven bounds rebuild Lambda: 976 at caps (3,3,1,3,1), 216 at (2,2,1,2,1)",
           set(L976) == L and len(L216) == 216 and tree_structured(L216, d, TREE),
           "976=%s 216=%d" % (set(L976) == L, len(L216)))
    print("     (%.1f s)" % (time.time() - t))
    return cells, L216, TREE, A


def section_amplification(cells):
    print("\nM. The cost of one fabricated cell (paper 7.3), over every ambient non-cell (reference closure: op_order)")
    t = time.time()
    d = 8
    L = set(cells)
    A = alphabets(cells, d)
    names = ["n", "l", "k", "q", "e", "f", "g", "S"]
    non = [x for x in itertools.product(*A) if x not in L]
    amp = []
    for y in non:
        ix2 = cypher.Index("L+y", names, cells + [y])
        adm2, _ = cypher.op_order(ix2, {})
        amp.append(len(adm2) - len(cells) - 1)
    amp_sorted = sorted(amp)
    argmin = [non[i] for i, a in enumerate(amp) if a == amp_sorted[0]]
    put("amplification", dict(noncells=len(non), min=amp_sorted[0], median=float(statistics.median(amp)),
                              max=amp_sorted[-1], mean=round(sum(amp) / len(amp), 1),
                              zero=amp.count(0), argmin=[list(c) for c in argmin], values=amp))
    report("EXHAUSTIVE", "A(y) over all 5,936 non-cells: min 15, median 309, mean 380.9, max 1,795, none zero; the minimum at %d non-cells, first %s"
           % (len(argmin), argmin[0]),
           len(non) == 5936 and amp_sorted[0] == 15 and statistics.median(amp) == 309 and round(sum(amp) / len(amp), 1) == 380.9
           and amp_sorted[-1] == 1795 and amp.count(0) == 0 and len(argmin) == 32 and argmin[0] == (2, 1, 3, 2, 2, 1, 3, 0),
           "n=%d min=%d median=%s max=%d mean=%.1f zero=%d" % (len(non), amp_sorted[0], statistics.median(amp), amp_sorted[-1], sum(amp) / len(amp), amp.count(0)))
    print("     (%.1f s)" % (time.time() - t))


def R_local(X, d):
    """A fast local implementation of the staircase closure, used for the exhaustive sweeps.
    Guarded against cypher.op_order, which stays the reference; never a copy of it -- op_order
    builds an Index and encodes its alphabets, this evaluates the envelopes directly."""
    A = alphabets(X, d)
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            for v in A[j]:
                cand = [x[i] for x in X if x[j] <= v]
                phi[(i, j, v)] = max(cand) if cand else None
    out = set()
    for x in itertools.product(*A):
        good = True
        for i in range(d):
            for j in range(d):
                if i == j:
                    continue
                p = phi[(i, j, x[j])]
                if p is None or x[i] > p:
                    good = False
                    break
            if not good:
                break
        if good:
            out.add(x)
    return out


def BPC_local(X, d):
    """The binary-projection closure: every ambient point whose every pair-projection is in X's."""
    A = alphabets(X, d)
    pr = {(i, j): {(x[i], x[j]) for x in X} for i in range(d) for j in range(i + 1, d)}
    return {x for x in itertools.product(*A)
            if all((x[i], x[j]) in pr[(i, j)] for i in range(d) for j in range(i + 1, d))}


def median3(a, b, c):
    return tuple(max(min(p, q), min(q, r), min(p, r)) for p, q, r in zip(a, b, c))


def median_witness(X):
    """A triple of X whose coordinatewise median is not in X, or None."""
    Xs = set(X)
    for a in X:
        for b in X:
            for c in X:
                m = median3(a, b, c)
                if m not in Xs:
                    return (a, b, c, m)
    return None


def pair_fault(X, d):
    """A pair (i, j) whose projection of X is not a sublattice of A_i x A_j, or None."""
    for i in range(d):
        for j in range(i + 1, d):
            pr = sorted({(x[i], x[j]) for x in X})
            if not closed_under(pr, natural(pr, 2)):
                return (i, j)
    return None


def section_closure():
    """The closure theorem and the diagnostic split, over EVERY subset of each box."""
    print("\nB. Closure and its defect (Theorem 1, Theorem 6): R-fixed = sublattice, and the diagnostic split")
    rows = []
    for shape in [(3, 3), (2, 4), (2, 2, 2), (2, 2, 3), (2, 2, 2, 2)]:
        t = time.time()
        cells = cells_of(shape)
        N = len(cells)
        d = len(shape)
        tot = disagree = 0
        bpc_bad = 0
        defect = pfonly = mwonly = both = neither = 0
        for m in range(1, 1 << N):
            X = [cells[i] for i in range(N) if m >> i & 1]
            if len(X) < 2:
                continue
            tot += 1
            Xs = set(X)
            fixed = R_local(X, d) == Xs
            lat = closed_under(X, natural(X, d))
            disagree += fixed != lat
            if fixed:
                bpc_bad += BPC_local(X, d) != Xs
            else:
                defect += 1
                pf = pair_fault(X, d) is not None
                mw = median_witness(X) is not None
                both += pf and mw
                pfonly += pf and not mw
                mwonly += mw and not pf
                neither += not pf and not mw
        rows.append(dict(box=list(shape), subsets=tot, disagreements=disagree, bpc_failures=bpc_bad,
                         defective=defect, pair_fault_only=pfonly, median_only=mwonly, both=both,
                         neither=neither, seconds=round(time.time() - t, 1)))
        report("EXHAUSTIVE", "box %s: E(X) = 0 <=> X a sublattice, on all %d subsets; E = 0 => X = BPC(X)"
               % ("x".join(map(str, shape)), tot), disagree == 0 and bpc_bad == 0,
               "disagreements=%d bpc-failures=%d" % (disagree, bpc_bad))
        report("EXHAUSTIVE", "box %s: every defective subset has a pair fault or a median witness"
               % "x".join(map(str, shape)), neither == 0,
               "defective=%d pair-only=%d median-only=%d both=%d neither=%d" % (defect, pfonly, mwonly, both, neither))
    put("closure_equivalence", rows)


#  The worked example the figures draw: a 13-cell index in the box 5x4, scrambled and recovered.
EX_LO = [0, 0, 0, 1, 2]
EX_HI = [1, 2, 2, 3, 3]
EX_PERM0 = [3, 0, 4, 2, 1]        # new label of the old value v, axis 0
EX_PERM1 = [2, 0, 3, 1]           # ... and axis 1


def example_index():
    return sorted((u, b) for u in range(5) for b in range(EX_LO[u], EX_HI[u] + 1))


def section_example():
    """The worked example: built, scrambled, and recovered, with every count the figures print."""
    print("\nB2. The worked example in the box 5x4: built, scrambled, recovered")
    X = example_index()
    d = 2
    scr = sorted((EX_PERM0[u], EX_PERM1[b]) for (u, b) in X)
    # brute force: every ordering of both alphabets under which the SCRAMBLED set is closed
    adm = []
    for p0 in itertools.permutations(range(5)):
        for p1 in itertools.permutations(range(4)):
            ranks = [{v: r for r, v in enumerate(p0)}, {v: r for r, v in enumerate(p1)}]
            if closed_under(scr, ranks):
                adm.append((p0, p1))
    # the algorithm: enumerate orders of axis 1, decide axis 0 by Theorem 1
    found = None
    tried = 0
    for p1 in itertools.permutations(range(4)):
        tried += 1
        ranks1 = {v: r for r, v in enumerate(p1)}
        vals, P = P_relation(scr, 0, [{v: v for v in range(5)}, ranks1])
        if total_preorder(vals, P):
            found = (canonical_extension(vals, P), p1, vals, P)
            break
    ok = found is not None and closed_under(
        scr, [{v: r for r, v in enumerate(found[0])}, {v: r for r, v in enumerate(found[1])}])
    # the may-precede relation on axis 0 at the recovered order of axis 1, as the figure draws it
    vals, P = (found[2], found[3]) if found else ([], {})
    ties = sorted({tuple(sorted((u, v))) for u in vals for v in vals
                   if u != v and P[(u, v)] and P[(v, u)]})
    put("example", dict(lo=EX_LO, hi=EX_HI, perm0=EX_PERM0, perm1=EX_PERM1,
                        cells=[list(c) for c in X], scrambled=[list(c) for c in scr],
                        n_cells=len(X), box=20, admissible=len(adm),
                        recovered0=list(found[0]) if found else None,
                        recovered1=list(found[1]) if found else None,
                        axis1_orders_tried=tried,
                        P=[[int(P[(u, v)]) for v in vals] for u in vals], vals=list(vals),
                        ties=[list(t) for t in ties]))
    report("EXHAUSTIVE", "example: 13 cells of the box 5x4; 4 of the 2,880 orderings admit it; recovery returns one",
           len(X) == 13 and len(adm) == 4 and ok and len(ties) == 1,
           "cells=%d admissible=%d of %d; axis-1 orders tried=%d; ties on axis 0=%s"
           % (len(X), len(adm), 120 * 24, tried, ties))


def section_diagnostic():
    print("\nC. The diagnostic on two coordinatisations of the elements")
    per = cypher._periodic()
    jan = cypher._janet()
    adm_p, _ = cypher.op_order(per, {})
    adm_j, _ = cypher.op_order(jan, {})
    Ep = len(adm_p) - len(per.cells)
    Ej = len(adm_j) - len(jan.cells)
    box_p = math.prod(len(m) for m in per.code)
    put("periodic_E", Ep)
    put("periodic_cells", len(per.cells))
    put("periodic_box", box_p)
    put("janet_fixture_E", Ej)
    put("janet_fixture_cells", len(jan.cells))
    report("EXHAUSTIVE", "periodic table (period x group): 90 cells in a box of 126, E = 36; the capped left-step fixture (22 cells): E = 0",
           Ep == 36 and len(per.cells) == 90 and box_p == 126 and Ej == 0 and len(jan.cells) == 22,
           "periodic cells=%d box=%d E=%d; fixture cells=%d E=%d" % (len(per.cells), box_p, Ep, len(jan.cells), Ej))
    # The subshells actually occupied through Z = 118 -- 1s ... 7p, nineteen of them -- and the twenty
    # with 8s, each coordinatised by (n + l, l).  The fixture's 22 include 6f, 7d and 7f, which no
    # element through oganesson occupies; the paper prints the occupied count.
    SUB = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (4, 3),
           (5, 0), (5, 1), (5, 2), (5, 3), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1)]
    cells19 = sorted({(n + l, l) for n, l in SUB})
    cells20 = sorted(set(cells19) | {(8, 0)})
    out = {}
    for label, cs in (("19", cells19), ("20", cells20)):
        ix = cypher.Index("left-step, occupied", ["n+l", "l"], cs)
        adm, _ = cypher.op_order(ix, {})
        box = math.prod(len(m) for m in ix.code)
        E = len(adm) - len(cs)
        out[label] = dict(cells=len(cs), box=box, E=E)
        report("EXHAUSTIVE", "left-step (n+l, l): the %s subshells occupied through Z = 118%s, box %d, E = %d"
               % (label, "" if label == "19" else " plus 8s", box, E),
               len(cs) == int(label) and E == 0 and box == 32, "cells=%d box=%d E=%d" % (len(cs), box, E))
    put("janet_occupied", out)


def guards():
    """Both guards, before any Z3 obligation is reported: (a) non-vacuity of the hypothesis on EVERY box
    an obligation ranges over; (b) fidelity of EVERY Z3 encoding against a concrete reference written
    from the paper's definitions; (c) the reference closure; (d) a negative control on the guard."""
    print("\nGUARDS (run before the obligations)")
    ok = True
    rnd = random.Random(11)
    G = {}
    # (a) non-vacuity: Theorems 2 and 3 -- observed, s a total order, X closed under s, X a proper subset
    nv = []
    for shape in ((3, 3), (4, 4), (2, 2, 3), (3, 3, 3), (3, 5), (5, 4)):
        cells = cells_of(shape)
        X = prover.subset_vars(cells, "x")
        A0 = list(range(shape[0]))
        s, order = order_vars(A0, "s")
        hyp = z3.And(prover.observed(X, cells, shape), order, enc_closed_s(X, s, cells, 0),
                     z3.Or([z3.Not(X[c]) for c in cells]))
        sat, _ = z3_sat(hyp)
        ok &= sat
        nv.append(["x".join(map(str, shape)), "Theorems 2-3", sat])
        print("  [%s] hypothesis 'observed, s a total order, X closed under s, X != box' satisfiable, %s"
              % ("ok" if sat else "XX", "x".join(map(str, shape))))
    # (a) non-vacuity: Lemma 9 -- S closed, a and b in S, S a proper subset, the removal non-empty
    for shape in ((3, 3), (2, 2, 2), (2, 2, 3)):
        cells = cells_of(shape)
        S = prover.subset_vars(cells, "s")
        a, b = cells[0], cells[1]                      # the bottom cell and a cover of it
        hyp = z3.And(prover.closed(S, cells), S[a], S[b], z3.Or([z3.Not(S[c]) for c in cells]),
                     z3.Or([S[c] for c in cells if not leq(a, c) or not leq(c, b)] or [z3.BoolVal(False)]))
        sat, _ = z3_sat(hyp)
        ok &= sat
        nv.append(["x".join(map(str, shape)), "Lemma 9", sat])
        print("  [%s] hypothesis 'S closed, a, b in S, S != box' satisfiable, %s" % ("ok" if sat else "XX", "x".join(map(str, shape))))
    # (a) non-vacuity: Theorem 9 -- a proper non-empty sublattice of 2^d exists
    for d in range(2, 7):
        cells = cells_of((2,) * d)
        S = prover.subset_vars(cells, "s")
        hyp = z3.And(prover.closed(S, cells), z3.Or([z3.Not(S[c]) for c in cells]), z3.Or([S[c] for c in cells]))
        sat, _ = z3_sat(hyp)
        ok &= sat
        nv.append(["2^%d" % d, "Theorem 9", sat])
        print("  [%s] hypothesis 'S closed, S != box, S non-empty' satisfiable, 2^%d" % ("ok" if sat else "XX", d))
    G["non_vacuity"] = nv
    # (b) encoding fidelity, Theorem 2's encodings: closed-under-s, P, s*, and the harness's closed
    tot = bad = 0
    tot2 = bad2 = 0
    tot3 = bad3 = 0
    tot4 = bad4 = 0
    for _ in range(150):
        shape = rnd.choice([(3, 3), (4, 4), (2, 2, 3), (3, 3, 3)])
        cells = cells_of(shape)
        d = len(shape)
        while True:
            Xs = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 9))))
            if all(len({c[i] for c in Xs}) == shape[i] for i in range(d)):
                break
        A0 = list(range(shape[0]))
        perm = list(A0)
        rnd.shuffle(perm)
        rank0 = {v: r for r, v in enumerate(perm)}
        Xv = {c: z3.BoolVal(c in Xs) for c in cells}
        sv = {(u, v): z3.BoolVal(rank0[u] < rank0[v]) for u in A0 for v in A0 if u != v}
        ranks = [rank0] + [{v: v for v in range(shape[i])} for i in range(1, d)]
        tot += 1
        bad += ev(enc_closed_s(Xv, sv, cells, 0)) != closed_under(Xs, ranks)
        Pz = enc_P(Xv, cells, 0, A0)
        vals, Pr = P_relation(Xs, 0, [{v: v for v in range(shape[i])} for i in range(d)])
        for u in A0:
            for v in A0:
                tot2 += 1
                bad2 += ev(Pz[(u, v)]) != Pr[(u, v)]
        # s*: the canonical extension, from the Z3 P against the concrete rule of D7
        star = enc_canonical(Pz, A0, "c")
        canon = canonical_extension(vals, Pr)
        pos = {u: i for i, u in enumerate(canon)}
        for u in A0:
            for v in A0:
                if u != v:
                    tot3 += 1
                    bad3 += ev(star[(u, v)]) != (pos[u] < pos[v])
        # the harness's closure predicate (Theorem 9, Lemma 9) against a concrete closure test
        tot4 += 1
        bad4 += ev(prover.closed(Xv, cells)) != ref_closed_natural(sorted(Xs))
    ok &= bad == 0 and bad2 == 0 and bad3 == 0 and bad4 == 0
    print("  [%s] enc_closed_s EVALUATED == closed_under: %d instances, %d disagreements" % ("ok" if bad == 0 else "XX", tot, bad))
    print("  [%s] enc_P EVALUATED == P_relation: %d pairs, %d disagreements" % ("ok" if bad2 == 0 else "XX", tot2, bad2))
    print("  [%s] enc_canonical (s*) EVALUATED == canonical_extension: %d pairs, %d disagreements" % ("ok" if bad3 == 0 else "XX", tot3, bad3))
    print("  [%s] harness closed EVALUATED == concrete closure test: %d instances, %d disagreements" % ("ok" if bad4 == 0 else "XX", tot4, bad4))
    G.update(fidelity_instances=tot, fidelity_pairs=tot2, canonical_pairs=tot3, closed_instances=tot4)
    # (b) encoding fidelity, Theorem 3's encodings: interval, lo_le, hi_le, mono
    t5 = b5 = t6 = b6 = t7 = b7 = 0
    for _ in range(120):
        shape = rnd.choice([(3, 3), (4, 4), (3, 5), (5, 4)])
        cells = cells_of(shape)
        while True:
            Xs = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 9))))
            if all(len({c[i] for c in Xs}) == shape[i] for i in range(2)):
                break
        A, B = list(range(shape[0])), list(range(shape[1]))
        perm = list(A)
        rnd.shuffle(perm)
        rank0 = {v: r for r, v in enumerate(perm)}
        Xv = {c: z3.BoolVal(c in Xs) for c in cells}
        sv = {(u, v): z3.BoolVal(rank0[u] < rank0[v]) for u in A for v in A if u != v}
        t5 += 1
        b5 += ev(enc_interval(Xv, A, B)) != ref_interval(Xs, A)
        for u in A:
            for v in A:
                t6 += 2
                b6 += ev(enc_lo_le(Xv, B, u, v)) != ref_lo_le(Xs, u, v)
                b6 += ev(enc_hi_le(Xv, B, u, v)) != ref_hi_le(Xs, u, v)
        t7 += 1
        b7 += ev(enc_mono(Xv, sv, A, B)) != ref_mono(Xs, rank0, A)
    ok &= b5 == 0 and b6 == 0 and b7 == 0
    print("  [%s] enc_interval EVALUATED == fibres are intervals: %d instances, %d disagreements" % ("ok" if b5 == 0 else "XX", t5, b5))
    print("  [%s] enc_lo_le / enc_hi_le EVALUATED == endpoint comparisons: %d pairs, %d disagreements" % ("ok" if b6 == 0 else "XX", t6, b6))
    print("  [%s] enc_mono EVALUATED == endpoints monotone along s: %d instances, %d disagreements" % ("ok" if b7 == 0 else "XX", t7, b7))
    G.update(interval_instances=t5, endpoint_pairs=t6, mono_instances=t7)
    # (b) encoding fidelity, Lemma 9's encodings: remclosed, jp, mp, on arbitrary S and a <= b
    t8 = b8 = b9 = b10 = 0
    for _ in range(120):
        shape = rnd.choice([(3, 3), (2, 2, 2), (2, 2, 3)])
        cells = cells_of(shape)
        Ss = frozenset(rnd.sample(cells, rnd.randint(1, len(cells))))
        while True:
            a, b = rnd.choice(cells), rnd.choice(cells)
            if leq(a, b):
                break
        Sv = {c: z3.BoolVal(c in Ss) for c in cells}
        t8 += 1
        b8 += ev(enc_remclosed(Sv, cells, a, b)) != ref_remclosed(sorted(Ss), a, b)
        b9 += ev(enc_jp(Sv, cells, a)) != ref_jp(sorted(Ss), a)
        b10 += ev(enc_mp(Sv, cells, b)) != ref_mp(sorted(Ss), b)
    ok &= b8 == 0 and b9 == 0 and b10 == 0
    print("  [%s] enc_remclosed EVALUATED == concrete removal test: %d instances, %d disagreements" % ("ok" if b8 == 0 else "XX", t8, b8))
    print("  [%s] enc_jp / enc_mp EVALUATED == concrete primality tests: %d instances, %d / %d disagreements" % ("ok" if b9 + b10 == 0 else "XX", t8, b9, b10))
    G.update(removal_instances=t8)
    # (c) the reference closure: closed under the natural order iff E = 0 under cypher.op_order
    tc = bc = 0
    for _ in range(120):
        shape = rnd.choice([(3, 3), (2, 2, 3), (3, 3, 3), (2, 2, 2, 2)])
        cells = cells_of(shape)
        d = len(shape)
        while True:
            Xs = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 9))))
            if all(len({c[i] for c in Xs}) == shape[i] for i in range(d)):
                break
        tc += 1
        bc += closed_under(Xs, natural(Xs, d)) != (R_index(Xs) == set(Xs))
    ok &= bc == 0
    print("  [%s] closed_under(natural) == (op_order adds nothing): %d instances, %d disagreements" % ("ok" if bc == 0 else "XX", tc, bc))
    # (c2) the fast local closure used by the exhaustive sweeps, against the reference op_order
    tl = bl = 0
    for _ in range(120):
        shape = rnd.choice([(3, 3), (2, 4), (2, 2, 2), (2, 2, 3), (3, 3, 3), (2, 2, 2, 2)])
        cells = cells_of(shape)
        d = len(shape)
        Xs = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 10))))
        tl += 1
        bl += R_local(sorted(Xs), d) != R_index(Xs)
    ok &= bl == 0
    print("  [%s] R_local == cypher.op_order, cell for cell: %d instances, %d disagreements" % ("ok" if bl == 0 else "XX", tl, bl))
    # (d) negative control on the fidelity guard: a wrong reference must be caught
    wrong = 0
    for _ in range(20):
        shape = (3, 3)
        cells = cells_of(shape)
        Xs = frozenset(rnd.sample(cells, rnd.randint(2, 6)))
        Xv = {c: z3.BoolVal(c in Xs) for c in cells}
        sv = {(u, v): z3.BoolVal(u < v) for u in range(3) for v in range(3) if u != v}
        wrong += ev(enc_closed_s(Xv, sv, cells, 0)) != (len(Xs) % 2 == 0)      # a deliberately wrong 'reference'
    ok &= wrong > 0
    print("  [%s] negative control: the guard detects a wrong reference (%d disagreements)" % ("ok" if wrong > 0 else "XX", wrong))
    G.update(closure_instances=tc, local_instances=tl, negative_control=wrong, ok=ok)
    put("guards", G)
    return ok


def section_one_axis():
    print("\nD. One-axis order recovery (Theorem 2) -- Z3 over every X and every total order on axis 0")
    boxes = [(3, 3), (4, 4), (2, 2, 3), (3, 3, 3)]
    rows = []
    for shape in boxes:
        t = time.time()
        cells = cells_of(shape)
        d = len(shape)
        X = prover.subset_vars(cells, "x")
        A0 = list(range(shape[0]))
        s, order = order_vars(A0, "s")
        obs = prover.observed(X, cells, shape)
        cl = enc_closed_s(X, s, cells, 0)
        P = enc_P(X, cells, 0, A0)
        refl = z3.And([P[(u, u)] for u in A0])
        sub = z3.And([z3.Implies(s[(u, v)], P[(u, v)]) for u in A0 for v in A0 if u != v])
        total = z3.And([z3.Or(P[(u, v)], P[(v, u)]) for u in A0 for v in A0 if u < v])
        transP = z3.And([z3.Implies(z3.And(P[(u, v)], P[(v, w)]), P[(u, w)]) for u in A0 for v in A0 for w in A0])
        sstar = enc_canonical(P, A0, "c")
        star_order = z3.And([z3.Xor(sstar[(u, v)], sstar[(v, u)]) for u in A0 for v in A0 if u < v] +
                            [z3.Implies(z3.And(sstar[(u, v)], sstar[(v, w)]), sstar[(u, w)])
                             for u in A0 for v in A0 for w in A0 if len({u, v, w}) == 3])
        cl_star = enc_closed_s(X, sstar, cells, 0)
        obl = [
            ("2(a) P is transitive", z3.Implies(obs, transP)),
            ("2(b) closed under s  =>  P reflexive and s in P", z3.Implies(z3.And(obs, order, cl), z3.And(refl, sub))),
            ("2(b) P reflexive and s in P  =>  closed under s", z3.Implies(z3.And(obs, order, refl, sub), cl)),
            ("2(c) P total preorder  =>  s* is a total order and X closed under s*",
             z3.Implies(z3.And(obs, refl, total), z3.And(star_order, cl_star))),
        ]
        allok = True
        for name, claim in obl:
            ok, _ = z3_prove(claim)
            allok &= ok
            report("MACHINE-CHECKED", "%s, box %s" % (name, "x".join(map(str, shape))), ok,
                   "2^%d subsets x %d orders" % (len(cells), len(list(itertools.permutations(A0)))))
        # the refutation: closed under some order does NOT make P antisymmetric
        antis = z3.And([z3.Not(z3.And(P[(u, v)], P[(v, u)])) for u in A0 for v in A0 if u < v])
        sat, m = z3_sat(z3.And(obs, order, cl, z3.Not(antis)))
        wit = sorted(c for c in cells if z3.is_true(m.eval(X[c], True))) if sat else None
        report("REFUTATION", "'closed under some order => P antisymmetric', box %s" % "x".join(map(str, shape)),
               sat, "witness X = %s" % (wit,))
        rows.append(dict(box=list(shape), subsets=2 ** len(cells), orders=len(list(itertools.permutations(A0))),
                         ok=allok, refutation_witness=wit, seconds=round(time.time() - t, 1)))
    put("one_axis_z3", rows)


def section_interval_characterisation():
    print("\nE. The fibre characterisation at d = 2 (Theorem 3) -- Z3 over every X and every order on axis 0")
    rows = []
    for shape in [(3, 3), (4, 4), (3, 5), (5, 4)]:
        t = time.time()
        cells = cells_of(shape)
        A, B = list(range(shape[0])), list(range(shape[1]))
        X = prover.subset_vars(cells, "x")
        s, order = order_vars(A, "s")
        obs = prover.observed(X, cells, shape)
        cl = enc_closed_s(X, s, cells, 0)
        ok, _ = z3_prove(z3.Implies(z3.And(obs, order), cl == z3.And(enc_interval(X, A, B), enc_mono(X, s, A, B))))
        report("MACHINE-CHECKED", "closed under s  <=>  fibres are intervals with endpoints monotone along s, box %s"
               % "x".join(map(str, shape)), ok, "2^%d subsets x %d orders" % (len(cells), len(list(itertools.permutations(A)))))
        rows.append(dict(box=list(shape), ok=ok, seconds=round(time.time() - t, 1)))
    put("fibre_z3", rows)
    # The alphabet convention of D1 is load-bearing (paper 3.1): with A_1 DECLARED as {0,1,2} the set
    # {(0,0),(0,2),(1,0),(1,2)} is closed while its fibre over 0 is not an interval of {0,1,2}; under
    # D1 the alphabet is {0,2} and the fibre is an interval; adding (1,1) makes 1 used and breaks closure.
    Xd = [(0, 0), (0, 2), (1, 0), (1, 2)]
    declared = [{0: 0, 1: 1}, {0: 0, 1: 1, 2: 2}]
    closed_declared = closed_under(Xd, declared)
    F0 = sorted(b for (u, b) in Xd if u == 0)
    interval_declared = F0 == list(range(F0[0], F0[-1] + 1))
    A1 = sorted({b for (u, b) in Xd})
    interval_observed = all(b in F0 for b in A1 if F0[0] <= b <= F0[-1])
    Xe = Xd + [(1, 1)]
    closed_extended = closed_under(Xe, natural(Xe, 2))
    m = meet((0, 2), (1, 1))
    put("d1_exhibit", dict(X=[list(c) for c in Xd], closed_declared=closed_declared, fibre0=F0,
                           interval_in_declared=interval_declared, observed_A1=A1, interval_in_observed=interval_observed,
                           with_11_closed=closed_extended, breaking_meet=list(m)))
    report("REFUTATION", "'Theorem 3 holds for a declared alphabet': {(0,0),(0,2),(1,0),(1,2)} with A_1 = {0,1,2} is closed, fibre {0,2} no interval",
           closed_declared and not interval_declared and A1 == [0, 2] and interval_observed and not closed_extended and m == (0, 1),
           "closed=%s fibre(0)=%s; under D1 A_1=%s, interval=%s; with (1,1): closed=%s, meet (0,2)^(1,1)=%s"
           % (closed_declared, F0, A1, interval_observed, closed_extended, m))


def section_interval_lemma():
    print("\nF. The nesting lemma (Lemma 5), exhaustive over every set of 2..4 distinct intervals on 2..5 points")

    def intervals(n):
        return [(a, b) for a in range(n) for b in range(a, n)]

    def admits(S):
        for p in itertools.permutations(S):
            if all(p[i][0] <= p[i + 1][0] and p[i][1] <= p[i + 1][1] for i in range(len(p) - 1)):
                return True
        return False

    def strict_nest(S):
        return any(a[0] < b[0] and b[1] < a[1] for a in S for b in S)

    def weak_nest(S):
        return any(a != b and a[0] <= b[0] and b[1] <= a[1] for a in S for b in S)

    def sorted_test(S):
        S2 = sorted(S)
        return all(S2[i][1] <= S2[i + 1][1] for i in range(len(S2) - 1))
    tot = ok = okweak = oksort = 0
    for n in range(2, 6):
        for k in range(2, 5):
            for S in itertools.combinations(intervals(n), k):
                tot += 1
                adm = admits(S)
                ok += adm == (not strict_nest(S))
                okweak += adm == (not weak_nest(S))
                oksort += adm == sorted_test(S)
    put("interval_family", dict(size=tot, lemma_holds=ok, weak_reading_holds=okweak, weak_refuted=tot - okweak, sorted_test=oksort))
    report("EXHAUSTIVE", "2,354 interval sets: monotone order exists iff no strict nesting; sort test decides",
           tot == 2354 and ok == tot and oksort == tot, "family=%d holds=%d sort-test=%d" % (tot, ok, oksort))
    report("REFUTATION", "the reading 'no nesting at all' fails on 1,098 of the 2,354",
           tot - okweak == 1098, "refuted=%d" % (tot - okweak))
    # the lemma for MULTISETS of intervals (fibres may coincide -- that is a tie): repeats allowed
    totm = okm = oksm = 0
    for n in range(2, 6):
        for k in range(2, 5):
            for S in itertools.combinations_with_replacement(intervals(n), k):
                totm += 1
                adm = admits(S)
                okm += adm == (not strict_nest(S))
                oksm += adm == sorted_test(S)
    put("interval_multiset_family", dict(size=totm, lemma_holds=okm, sorted_test=oksm))
    report("EXHAUSTIVE", "%d interval multisets of 2..4 members on 2..5 points (repeats allowed): lemma and sort test hold on every one" % totm,
           okm == totm and oksm == totm, "family=%d holds=%d sort-test=%d" % (totm, okm, oksm))


CENSUS_PINS = {(2, 2): (16, 3), (2, 3): (64, 5), (2, 4): (256, 7), (3, 3): (506, 8), (3, 4): (3772, 11),
               (4, 4): (47416, 15), (2, 2, 2): (158, 6), (2, 2, 3): (1342, 10), (2, 3, 3): (20068, 16),
               (2, 2, 2, 2): (3290, 12)}


def section_census():
    """Every subset of each box: closed under the natural order, reorderable, the step, the largest
    proper reorderable subset of the full box.  Bitmask arrays, one bit per cell."""
    print("\nG. Reorderability census (Table 2, Figure 4), every subset of each box")
    boxes = [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4), (2, 2, 2), (2, 2, 3), (2, 3, 3), (2, 2, 2, 2)]
    rows = []
    CENSUS = {}
    for shape in boxes:
        t = time.time()
        cells = cells_of(shape)
        N = len(cells)
        idx = {c: i for i, c in enumerate(cells)}
        d = len(shape)
        masks = np.arange(1 << N, dtype=np.uint32)
        bit = lambda i: ((masks >> i) & 1).astype(bool)
        closed = np.ones(1 << N, dtype=bool)
        for i in range(N):
            for j in range(i + 1, N):
                a, b = cells[i], cells[j]
                m, jn = idx[meet(a, b)], idx[join(a, b)]
                if m in (i, j) and jn in (i, j):
                    continue
                closed &= (~(bit(i) & bit(j))) | (bit(m) & bit(jn))
        obs = np.ones(1 << N, dtype=bool)
        for i, n in enumerate(shape):
            for v in range(n):
                any_ = np.zeros(1 << N, dtype=bool)
                for c in cells:
                    if c[i] == v:
                        any_ |= bit(idx[c])
                obs &= any_
        reord = np.zeros(1 << N, dtype=bool)
        perms_list = list(itertools.product(*[list(itertools.permutations(range(n))) for n in shape]))
        permmaps = []
        for perms in perms_list:
            pm = np.zeros(1 << N, dtype=np.uint32)
            for c in cells:
                pm |= ((masks >> idx[c]) & 1) << idx[tuple(perms[k][c[k]] for k in range(d))]
            permmaps.append(pm)
            reord |= closed[pm]
        # the step: over reorderable Y with |Y| >= 2, the least k with a reorderable subset of size |Y|-k
        popc = np.array([bin(m).count("1") for m in range(1 << N)], dtype=np.int16)
        step = 0
        step_at = None
        rmasks = np.nonzero(reord & (popc >= 2))[0]
        for m in rmasks:
            bits = [i for i in range(N) if m >> i & 1]
            found = None
            for k in range(1, len(bits)):
                for drop in itertools.combinations(bits, k):
                    m2 = int(m)
                    for i in drop:
                        m2 &= ~(1 << i)
                    if reord[m2]:
                        found = k
                        break
                if found is not None:
                    break
            if found is None:
                found = len(bits) - 1
            if found > step:
                step, step_at = found, int(m)
        full = (1 << N) - 1
        proper = np.nonzero(reord & (masks != full))[0]
        maxproper = int(popc[proper].max())
        # doubly irreducible cells of the full box: exactly one coordinate above its minimum and
        # exactly one below its maximum (the two corners at d = 2, none at d >= 3)
        dbl = sum(1 for c in cells if sum(1 for v in c if v > 0) == 1 and sum(1 for v, n in zip(c, shape) if v < n - 1) == 1)
        exp_reord, exp_max = CENSUS_PINS[shape]
        row = dict(box=list(shape), subsets=1 << N, orderings=len(perms_list), closed_natural_observed=int((closed & obs).sum()),
                   reorderable_observed=int((reord & obs).sum()), reorderable_all=int(reord.sum()),
                   fraction_reorderable=round(int(reord.sum()) / (1 << N), 3), step=step,
                   step_attained_at_full_box=(N - maxproper == step), max_proper_reorderable=maxproper,
                   doubly_irreducible=dbl,
                   three_quarters=(maxproper == 3 * (1 << N) // 4) if all(n == 2 for n in shape) else None,
                   seconds=round(time.time() - t, 1))
        rows.append(row)
        CENSUS[shape] = dict(cells=cells, idx=idx, closed=closed, obs=obs, reord=reord, permmaps=permmaps, perms=perms_list, popc=popc)
        report("EXHAUSTIVE", "box %s: %d subsets, %d reorderable, step %d, largest proper reorderable %d, box - largest = step"
               % ("x".join(map(str, shape)), 1 << N, int(reord.sum()), step, maxproper),
               step == 2 ** (d - 2) and int(reord.sum()) == exp_reord and maxproper == exp_max
               and N - maxproper == step and (maxproper == N - 1) == (d == 2) and dbl == (2 if d == 2 else 0),
               "doubly irreducible cells of the box: %d; first subset attaining the step in mask order is the full box: %s"
               % (dbl, step_at == full))
    put("census", rows)
    return CENSUS


def section_projection_gap(CENSUS):
    """Pointwise is not enough: every PAIR PROJECTION reorderable, and X not.  Exhaustive over
    every observed subset of each box, with the smallest witness printed."""
    print("\nH2. Pointwise is not enough (paper 4.1): every pair projection reorderable does not make X reorderable")
    rows = []
    for shape in [(2, 2, 2), (2, 2, 3), (2, 2, 2, 2)]:
        t = time.time()
        C = CENSUS[shape]
        cells, reord, obs = C["cells"], C["reord"], C["obs"]
        N = len(cells)
        d = len(shape)
        n = gap = allpairs = 0
        wit = None
        for m in np.nonzero(obs)[0]:
            X = [cells[i] for i in range(N) if m >> i & 1]
            n += 1
            ok = all(reorderable_brute(sorted({(c[i], c[j]) for c in X}), 2)
                     for i in range(d) for j in range(i + 1, d))
            allpairs += ok
            if ok and not reord[m]:
                gap += 1
                if wit is None or len(X) < len(wit):
                    wit = X
        rows.append(dict(box=list(shape), observed=n, all_pairs_reorderable=allpairs,
                         reorderable=int((reord & obs).sum()), gap=gap,
                         witness=[list(c) for c in wit] if wit else None,
                         seconds=round(time.time() - t, 1)))
        exp_n, exp_gap = {(2, 2, 2): (193, 98), (2, 2, 3): (3271, 2460), (2, 2, 2, 2): (63775, 61462)}[shape]
        report("EXHAUSTIVE", "box %s: %d observed subsets, %d with every pair projection reorderable, %d of those not reorderable"
               % ("x".join(map(str, shape)), n, allpairs, gap), gap == exp_gap and n == exp_n and allpairs == n,
               "smallest witness (%d cells): %s" % (len(wit), wit) if wit else "no witness")
    put("projection_gap", rows)


def section_d2_algorithm(CENSUS):
    print("\nH. The d = 2 decision DECIDE2 by root enumeration + Theorem 2, against the brute-force census")
    rows = []
    for shape in [(2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]:
        t = time.time()
        C = CENSUS[shape]
        cells, reord, obs = C["cells"], C["reord"], C["obs"]
        N = len(cells)
        n = agree = 0
        for m in np.nonzero(obs)[0]:
            X = [cells[i] for i in range(N) if m >> i & 1]
            alg = False
            for p in itertools.permutations(range(shape[0])):
                ranks = [{v: r for r, v in enumerate(p)}, {v: v for v in range(shape[1])}]
                vals, P = P_relation(X, 1, ranks)
                if total_preorder(vals, P):
                    alg = True
                    break
            n += 1
            agree += alg == bool(reord[m])
        rows.append(dict(box=list(shape), instances=n, agree=agree, seconds=round(time.time() - t, 1)))
        report("EXHAUSTIVE", "box %s: DECIDE2 == brute force on every observed subset" % "x".join(map(str, shape)),
               agree == n and n == {(2, 3): 25, (2, 4): 79, (3, 3): 265, (3, 4): 2161, (4, 4): 41503}[shape], "%d of %d" % (agree, n))
    put("d2_algorithm", rows)


def section_tree(CENSUS, lam976, lam216, TREE):
    print("\nI. Tree propagation RECOVER (Theorem 5): every solution, against brute force, on every tree-structured subset")
    rows = []
    families = [((2, 2, 3), [(0, 1), (1, 2)], "path"), ((2, 3, 3), [(0, 1), (1, 2)], "path"),
                ((2, 2, 2, 2), [(0, 1), (1, 2), (2, 3)], "path"), ((2, 2, 2, 2), [(0, 1), (0, 2), (0, 3)], "star")]
    for shape, tree, kind in families:
        t = time.time()
        C = CENSUS[shape]
        cells, reord, obs, closed, permmaps, perms = C["cells"], C["reord"], C["obs"], C["closed"], C["permmaps"], C["perms"]
        N = len(cells)
        d = len(shape)
        n = agree = nclosed = scr = scr_ok = 0
        for m in np.nonzero(obs)[0]:
            X = [cells[i] for i in range(N) if m >> i & 1]
            if not tree_structured(X, d, tree):
                continue
            n += 1
            # brute force: every ordering under which X is closed
            truth = set()
            for k, pm in enumerate(permmaps):
                if closed[pm[m]]:
                    # perms[k][i] maps value v -> rank perms[k][i][v]?  perms are tuples p with p[v] = new label
                    truth.add(tuple(tuple(sorted(range(shape[i]), key=lambda v: perms[k][i][v])) for i in range(d)))
            sols, _ = tree_recover(X, d, tree, root=0, all_solutions=True)
            got = {tuple(s[i] for i in range(d)) for s in sols}
            agree += got == truth
            if truth:
                nclosed += 1
                # every relabelling of a closed set is recovered: the recovered order is admissible
                for k in range(len(perms)):
                    maps = [{v: perms[k][i][v] for v in range(shape[i])} for i in range(d)]
                    Xs = {tuple(maps[i][c[i]] for i in range(d)) for c in X}
                    sol, _ = tree_recover(Xs, d, tree, root=0)
                    scr += 1
                    scr_ok += bool(sol) and closed_under(Xs, [{v: r for r, v in enumerate(sol[0][i])} for i in range(d)])
        rows.append(dict(box=list(shape), tree=kind, tree_structured=n, solution_sets_agree=agree, closed=nclosed,
                         scrambles=scr, scrambles_recovered=scr_ok, seconds=round(time.time() - t, 1)))
        exp_n, exp_closed, exp_scr = {((2, 2, 3), "path"): (175, 175, 4200), ((2, 3, 3), "path"): (6625, 4819, 346968),
                                      ((2, 2, 2, 2), "path"): (343, 343, 5488), ((2, 2, 2, 2), "star"): (343, 343, 5488)}[(shape, kind)]
        report("EXHAUSTIVE", "box %s, %s: solution set == brute force on all %d tree-structured subsets" % ("x".join(map(str, shape)), kind, n),
               agree == n and scr_ok == scr and n == exp_n and nclosed == exp_closed and scr == exp_scr, "agree=%d/%d; %d closed x every relabelling = %d scrambles, %d recovered" % (agree, n, nclosed, scr, scr_ok))
    put("tree_exhaustive", rows)

    # Lambda: 20 seeded scrambles at each cap setting; the recovered order is admissible
    print("   Lambda from a scrambled bag of cells (SAMPLED: 20 scrambles per cap setting, seed 2026)")
    lam_rows = []
    for label, L in (("976", lam976), ("216", lam216)):
        t = time.time()
        d = 8
        A = alphabets(L, d)
        rnd = random.Random(2026)
        ok = exact_or_dual = 0
        tries = []
        for trial in range(20):
            perms = [rnd.sample(a, len(a)) for a in A]
            maps = [{a[r]: perms[i][r] for r in range(len(a))} for i, a in enumerate(A)]
            Xs = {tuple(maps[i][c[i]] for i in range(d)) for c in L}
            sol, tried = tree_recover(Xs, d, TREE, root=4)
            tries.append(tried)
            if not sol:
                continue
            ranks = [{v: r for r, v in enumerate(sol[0][i])} for i in range(d)]
            good = closed_under(Xs, ranks)
            ok += good
            true = [tuple(maps[i][v] for v in a) for i, a in enumerate(A)]
            dual = [tuple(reversed(o)) for o in true]
            exact_or_dual += all(sol[0][i] == true[i] for i in range(d)) or all(sol[0][i] == dual[i] for i in range(d))
        # how many orderings admit Lambda at all (the true labelling), by the DP enumerating every solution
        sols, _ = tree_recover(L, d, TREE, root=4, all_solutions=True)
        lam_rows.append(dict(cells=len(L), scrambles=20, recovered=ok, exact_or_dual=exact_or_dual,
                             admissible_orderings=len(sols), root_orders_tried_max=max(tries), seconds=round(time.time() - t, 1)))
        report("SAMPLED", "Lambda (%s cells): 20 of 20 scrambles recovered; admissible orderings = %d" % (label, len(sols)),
               ok == 20 and len(sols) == 16 and exact_or_dual == {"976": 3, "216": 0}[label],
               "recovered=%d exact-or-dual=%d admissible=%d root orders tried at most %d" % (ok, exact_or_dual, len(sols), max(tries)))
        # WHICH sixteen.  At 976: one global reversal x three ties of values with identical fibres --
        # n: 2 ~ 3 and e: 2 ~ 3 (because l, f <= 1) and 2S: 0 ~ 1 (because k >= 1).  At 216: the tie
        # 2S: 0 ~ 1 x the independent reversal of the three components {n,l}, {e,f}, {k,q,g,2S}, because
        # the tree edges l-k (k <= 4l+2) and f-g (g <= 4f+2) are vacuous at k <= 2.
        got = {tuple(s[i] for i in range(d)) for s in sols}
        nat = [tuple(a) for a in A]

        def swap(o, x, y):
            return tuple(y if v == x else x if v == y else v for v in o)

        def fibre(i, u):
            return {c[:i] + c[i + 1:] for c in L if c[i] == u}
        binding = {e: len({(c[e[0]], c[e[1]]) for c in L}) < len(A[e[0]]) * len(A[e[1]]) for e in TREE}
        pred = set()
        if label == "976":
            for bits in itertools.product((0, 1), repeat=3):
                o = list(nat)
                if bits[0]:
                    o[0] = swap(o[0], 2, 3)
                if bits[1]:
                    o[4] = swap(o[4], 2, 3)
                if bits[2]:
                    o[7] = swap(o[7], 0, 1)
                pred.add(tuple(o))
                pred.add(tuple(tuple(reversed(x)) for x in o))
            structure = fibre(0, 2) == fibre(0, 3) and fibre(4, 2) == fibre(4, 3) and fibre(7, 0) == fibre(7, 1) and all(binding.values())
            desc = "one global reversal x the ties n:2~3, e:2~3, 2S:0~1 (identical fibres); every tree edge binding"
        else:
            comps = [(0, 1), (4, 5), (2, 3, 6, 7)]
            for bits in itertools.product((0, 1), repeat=3):
                for tie in (0, 1):
                    o = list(nat)
                    if tie:
                        o[7] = swap(o[7], 0, 1)
                    for bt, comp in zip(bits, comps):
                        if bt:
                            for i in comp:
                                o[i] = tuple(reversed(o[i]))
                    pred.add(tuple(o))
            structure = (fibre(7, 0) == fibre(7, 1) and not binding[(1, 2)] and not binding[(5, 6)]
                         and all(binding[e] for e in TREE if e not in ((1, 2), (5, 6))))
            desc = "the tie 2S:0~1 x independent reversal of {n,l}, {e,f}, {k,q,g,2S}; edges l-k and f-g vacuous"
        put("lambda_%s_structure" % label, dict(description=desc, predicted=len(pred), equal=got == pred, binding_edges={str(e): b for e, b in binding.items()}))
        report("EXHAUSTIVE", "Lambda (%s): the 16 admissible systems are exactly %s" % (label, desc.split(";")[0]),
               got == pred and len(pred) == 16 and structure, "predicted=%d equal=%s" % (len(pred), got == pred))
    put("lambda_recovery", lam_rows)
    fact = [len(a) for a in alphabets(lam976, 8)]
    put("lambda_sum_fact", sum(math.factorial(k) for k in fact))
    put("lambda_prod_fact", math.prod(math.factorial(k) for k in fact))
    report("EXHAUSTIVE", "Lambda: sum |A_i|! = 94 against prod |A_i|! = 11,943,936",
           sum(math.factorial(k) for k in fact) == 94 and math.prod(math.factorial(k) for k in fact) == 11943936,
           "sum=%d prod=%d" % (sum(math.factorial(k) for k in fact), math.prod(math.factorial(k) for k in fact)))


def section_removal(CENSUS):
    print("\nJ. Interval removal (Lemma 9) -- Z3 over every sublattice S of the box and every a <= b")
    rows = []
    for shape in [(3, 3), (2, 2, 2), (2, 2, 3)]:
        t = time.time()
        cells = cells_of(shape)
        S = prover.subset_vars(cells, "s")
        closed = prover.closed(S, cells)
        bad = n = 0
        for a in cells:
            for b in cells:
                if not leq(a, b):
                    continue
                n += 1
                ok, _ = z3_prove(z3.Implies(z3.And(closed, S[a], S[b]),
                                            enc_remclosed(S, cells, a, b) == z3.And(enc_jp(S, cells, a), enc_mp(S, cells, b))))
                bad += not ok
        rows.append(dict(box=list(shape), pairs=n, failures=bad, seconds=round(time.time() - t, 1)))
        report("MACHINE-CHECKED", "S minus [a,b] closed <=> a join-prime and b meet-prime, box %s, all %d pairs a<=b"
               % ("x".join(map(str, shape)), n), bad == 0 and n == {(3, 3): 36, (2, 2, 2): 27, (2, 2, 3): 54}[shape],
               "2^%d sublattice candidates per pair" % len(cells))
    put("removal_z3", rows)

    print("   The largest proper sublattice of the Boolean box 2^d (Z3, cardinality); drop at the full box is arithmetic on the answer")
    rows = []
    for d in range(2, 7):
        t = time.time()
        cells = cells_of((2,) * d)
        S = prover.subset_vars(cells, "s")
        closed = prover.closed(S, cells)
        proper = z3.Or([z3.Not(S[c]) for c in cells])
        bound = 3 * 2 ** (d - 2)
        sat_above, _ = z3_sat(z3.And(closed, proper, z3.AtLeast(*[S[c] for c in cells], bound + 1)))
        sat_at, _ = z3_sat(z3.And(closed, proper, z3.AtLeast(*[S[c] for c in cells], bound)))
        drop = 2 ** d - bound
        rows.append(dict(d=d, bound=bound, attained=sat_at, exceeded=sat_above, drop_at_box=drop, seconds=round(time.time() - t, 1)))
        report("MACHINE-CHECKED", "2^%d: every proper sublattice has <= %d cells, %d is attained; drop(2^%d) = %d = 2^(d-2)"
               % (d, bound, bound, d, drop), (not sat_above) and sat_at and drop == 2 ** (d - 2), "2^%d subsets" % len(cells))
    put("max_sublattice_z3", rows)
    put("boolean_step_at_box", {r["d"]: r["drop_at_box"] for r in rows})

    # Corollary 2: every MAXIMAL proper sublattice of 2^d has exactly 3.2^(d-2) cells and there are
    # d(d-1) of them -- exhaustive over the closed subsets the census computed, d = 2, 3, 4
    print("   Every maximal proper sublattice of 2^d, d = 2..4, from the census's closed subsets")
    rows = []
    for shape in [(2, 2), (2, 2, 2), (2, 2, 2, 2)]:
        C = CENSUS[shape]
        closed, popc, N = C["closed"], C["popc"], len(C["cells"])
        full = (1 << N) - 1
        d = len(shape)
        cl = np.nonzero(closed)[0].astype(np.int64)
        cl = cl[(cl != full) & (cl != 0)]
        maxi = [int(m) for m in cl if len(cl[(cl & m) == m]) == 1]
        sizes = sorted({int(popc[m]) for m in maxi})
        rows.append(dict(d=d, closed_subsets=int(len(cl)), maximal=len(maxi), sizes=sizes))
        report("EXHAUSTIVE", "2^%d: %d maximal proper sublattices, every one of exactly %d = 3.2^(d-2) cells" % (d, len(maxi), 3 * 2 ** (d - 2)),
               len(maxi) == d * (d - 1) and sizes == [3 * 2 ** (d - 2)], "proper non-empty sublattices=%d sizes=%s" % (len(cl), sizes))
    put("maximal_sublattices", rows)
    # Rival's lower bound |K| >= (2/3)|L| is tight on the three-element chain
    chain = [(0,), (1,), (2,)]
    subl = [set(S) for r in (1, 2) for S in itertools.combinations(chain, r) if ref_closed_natural(list(S))]
    maxi = [S for S in subl if not any(S < T for T in subl)]
    put("three_chain_maximal", [sorted(S) for S in maxi])
    report("EXHAUSTIVE", "three-element chain: every maximal proper sublattice has 2 of its 3 elements (two thirds, tight)",
           len(maxi) == 3 and all(len(S) == 2 for S in maxi), "maximal=%d" % len(maxi))


def bell(n):
    """The Bell number B(n), by the Bell triangle (independent of any partition enumeration)."""
    row = [1]
    for _ in range(n):
        new = [row[-1]]
        for x in row:
            new.append(new[-1] + x)
        row = new
    return row[0]


def clauses_for(k, pts, idx):
    """Every clause of at most two literals over k Boolean variables, as a bitmask over pts."""
    out = []
    for i in range(k):
        for si in (0, 1):
            out.append(sum(1 << idx[p] for p in pts if p[i] != si))
            for j in range(i + 1, k):
                for sj in (0, 1):
                    out.append(sum(1 << idx[p] for p in pts if not (p[i] == si and p[j] == sj)))
    return out


def two_clause_closed(mask, clauses, full):
    """A relation (as a bitmask) equals the solution set of the 2-clauses it satisfies:
    Schaefer's characterisation of the bijunctive relations."""
    closure = full
    for c in clauses:
        if mask & ~c == 0:
            closure &= c
    return closure == mask


def partition_constraint(C, k):
    """The constancy set of the equality pattern of C: sigma constant on every block of the
    partition generated by { {i,j} : sigma_i = sigma_j for all sigma in C }."""
    parent = list(range(k))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    for i in range(k):
        for j in range(i + 1, k):
            if all(s[i] == s[j] for s in C):
                parent[find(i)] = find(j)
    blocks = {}
    for i in range(k):
        blocks.setdefault(find(i), []).append(i)
    B = list(blocks.values())
    return {s for s in itertools.product((0, 1), repeat=k) if all(len({s[i] for i in blk}) == 1 for blk in B)}, len(B)


def C_of(T, k):
    """The complement-closed C on k orientation variables with difference relation T (Lemma 7)."""
    return {s for s in itertools.product((0, 1), repeat=k) if tuple(s[0] ^ s[t] for t in range(1, k)) in T}


def pair_constraint(X, x, y):
    """C(x,y) of D9: the sigma for which the meet and the join determined by sigma both lie in X."""
    Xs = set(X)
    I = [i for i in range(len(x)) if x[i] != y[i]]
    OK = set()
    for s in itertools.product((0, 1), repeat=len(I)):
        j, m = list(x), list(x)
        for tt, i in enumerate(I):
            j[i], m[i] = (y[i], x[i]) if s[tt] else (x[i], y[i])
        if tuple(j) in Xs and tuple(m) in Xs:
            OK.add(s)
    return OK, I


def closed_under_op(R, op):
    R = set(R)
    return all(tuple(op(a[i], b[i]) for i in range(len(a))) in R for a in R for b in R)


def affine_closed(R):
    R = set(R)
    return all(tuple(a[i] ^ b[i] ^ c[i] for i in range(len(a))) in R for a in R for b in R for c in R)


def section_arity():
    print("\nK. The reorderability law (Lemmas 6-7, Theorems 7-8): pair constraints C, difference relations T, bijunctivity")
    # every pair constraint that ARISES in a box, at every arity: complement-closed, containing 0 and 1,
    # every difference relation containing 0 realised; bijunctivity counted on C (the constraint D9
    # defines) AND on T (the auxiliary difference relation)
    rows = []
    for shape in [(2, 2, 2), (2, 2, 2, 2)]:
        t = time.time()
        cells = cells_of(shape)
        d = len(shape)
        N = len(cells)
        types = {}
        total = {}
        nontriv = {}
        cc_checked = cc_ok = 0
        for mask in range(1, 1 << N):
            X = [cells[i] for i in range(N) if mask >> i & 1]
            for a in range(len(X)):
                for b in range(a + 1, len(X)):
                    OK, I = pair_constraint(X, X[a], X[b])
                    k = len(I)
                    cc_checked += 1
                    cc_ok += all(tuple(1 - b_ for b_ in s) in OK for s in OK) and tuple([0] * k) in OK and tuple([1] * k) in OK
                    T = frozenset(tuple(s[0] ^ s[tt] for tt in range(1, k)) for s in OK)
                    total[k] = total.get(k, 0) + 1
                    if len(T) < 2 ** (k - 1):
                        nontriv[k] = nontriv.get(k, 0) + 1
                    types.setdefault(k, {})
                    types[k][T] = types[k].get(T, 0) + 1
        per = {}
        for k in sorted(types):
            Ts = list(types[k])
            per[k] = dict(constraints=total[k], nontrivial=nontriv.get(k, 0), distinct=len(Ts),
                          contain_zero=all(tuple([0] * (k - 1)) in T for T in Ts),
                          bijunctive_T=sum(1 for T in Ts if majority_closed(T, k - 1)),
                          bijunctive_C=sum(1 for T in Ts if majority_closed(C_of(T, k), k)))
        rows.append(dict(box=list(shape), complement_checked=cc_checked, complement_closed=cc_ok, per_arity=per, seconds=round(time.time() - t, 1)))
        kmax = max(per)
        ok = (cc_ok == cc_checked and all(per[k]["contain_zero"] for k in per)
              and all(per[k]["distinct"] == 2 ** (2 ** (k - 1) - 1) for k in per)
              and all(per[k]["bijunctive_C"] == bell(k) for k in per)
              and all(per[k]["bijunctive_T"] == {1: 1, 2: 2, 3: 8, 4: 73}[k] for k in per))
        report("EXHAUSTIVE", "box %s: %d pair constraints, all complement-closed with 0 and 1; every relation containing 0 arises up to arity %d"
               % ("x".join(map(str, shape)), cc_checked, kmax), ok,
               "; ".join("arity %d: %d distinct, %d bijunctive on C, %d on T" % (k, per[k]["distinct"], per[k]["bijunctive_C"], per[k]["bijunctive_T"]) for k in sorted(per)))
    put("arity_census", rows)

    # The exact census at arity k = 2..5: every complement-closed C on k orientation variables containing
    # 0 and 1 (equivalently every T on k-1 difference variables containing 0).  Bijunctivity is decided
    # by the two-clause closure (Schaefer) for every k, and by majority-closure as well for k <= 4, the
    # two agreeing on every relation; every bijunctive C is verified to be the constancy set of a
    # partition of its k variables, and their number is the Bell number B(k).  Theorem 7's construction
    # is verified for every T at k <= 4: X = C realises T at the pair (0^k, 1^k).
    exact = {}
    EXP_T = {1: 2, 2: 8, 3: 73, 4: 1442}
    for k in range(2, 6):
        t = time.time()
        m = k - 1
        Tpts = list(itertools.product((0, 1), repeat=m))
        Cpts = list(itertools.product((0, 1), repeat=k))
        Tidx = {p: i for i, p in enumerate(Tpts)}
        Cidx = {p: i for i, p in enumerate(Cpts)}
        img = [Tidx[tuple(s[0] ^ s[tt] for tt in range(1, k))] for s in Cpts]
        clsT, clsC = clauses_for(m, Tpts, Tidx), clauses_for(k, Cpts, Cidx)
        fullT, fullC = (1 << len(Tpts)) - 1, (1 << len(Cpts)) - 1
        tot = bijT = bijC = transfer_fail = part_ok = disagree = constr_ok = blocks_seen = 0
        for Tm in range(1, 1 << len(Tpts)):
            if not Tm & 1:                      # the origin is Tpts[0]
                continue
            tot += 1
            Cm = 0
            for i in range(len(Cpts)):
                if Tm >> img[i] & 1:
                    Cm |= 1 << i
            bT = two_clause_closed(Tm, clsT, fullT)
            bC = two_clause_closed(Cm, clsC, fullC)
            bijT += bT
            bijC += bC
            transfer_fail += bC and not bT          # C bijunctive => T bijunctive must never fail
            if bC or k <= 4:
                Cset = {Cpts[i] for i in range(len(Cpts)) if Cm >> i & 1}
            if k <= 4:
                Tset = {Tpts[i] for i in range(len(Tpts)) if Tm >> i & 1}
                disagree += (majority_closed(Tset, m) != bT) + (majority_closed(Cset, k) != bC)
                # Theorem 7's construction: X = C, the pair (0^k, 1^k)
                OK, I = pair_constraint(sorted(Cset), tuple([0] * k), tuple([1] * k))
                constr_ok += (OK == Cset and len(I) == k and all(len({c[i] for c in Cset}) == 2 for i in range(k)))
            if bC:
                P, nb = partition_constraint(Cset, k)
                part_ok += P == Cset
        exact[m] = dict(arity=k, relations=tot, bijunctive_C=bijC, bijunctive_T=bijT, bell=bell(k),
                        partition_constraints=part_ok, transfer_failures=transfer_fail,
                        majority_vs_two_clause_disagreements=(disagree if k <= 4 else None),
                        construction_verified=(constr_ok if k <= 4 else None), seconds=round(time.time() - t, 1))
        report("EXHAUSTIVE", "arity %d: %d pair constraints; %d bijunctive = B(%d), every one a partition constraint; C bijunctive => T bijunctive"
               % (k, tot, bijC, k),
               tot == 2 ** (2 ** m - 1) and bijC == bell(k) and part_ok == bijC and transfer_fail == 0 and (k > 4 or disagree == 0),
               "majority == two-clause on all: %s" % ("yes" if k <= 4 else "two-clause only"))
        report("EXHAUSTIVE", "relations on %d difference variables containing 0: %d, of which %d bijunctive (arity %d)" % (m, tot, bijT, k),
               tot == 2 ** (2 ** m - 1) and bijT == EXP_T[m], "")
        if k <= 4:
            report("EXHAUSTIVE", "Theorem 7's construction at arity %d: X = C realises T at (0^k, 1^k) for all %d relations" % (k, tot),
                   constr_ok == tot, "")
    put("pair_constraint_exact", exact)
    # the bijunctive census on T only (kept for the figure's contrast line and the record)
    put("bijunctive_exact", {m: dict(relations_containing_zero=exact[m]["relations"], bijunctive=exact[m]["bijunctive_T"]) for m in exact})

    # The source plate's own parametrisation -- non-empty proper complement-closed subsets of {0,1}^3,
    # 14 of them, without the origin requirement -- measured for the provenance record, not printed.
    pairs3 = [((0, 0, 0), (1, 1, 1)), ((0, 0, 1), (1, 1, 0)), ((0, 1, 0), (1, 0, 1)), ((1, 0, 0), (0, 1, 1))]
    cnt = tot14 = 0
    for r in range(1, 4):
        for S in itertools.combinations(pairs3, r):
            R = set(itertools.chain.from_iterable(S))
            tot14 += 1
            cnt += majority_closed(R, 3)
    put("source_plate_parametrisation", dict(relations=tot14, majority_closed=cnt))
    print("     (the plate's own parametrisation, 14 non-empty proper complement-closed subsets of {0,1}^3: %d of %d majority-closed)" % (cnt, tot14))

    # The arity-3 witness: six cells of 2x2x2, every value used; at (000,111) the constraint IS the set.
    X3 = [(0, 0, 0), (1, 1, 1), (0, 0, 1), (1, 1, 0), (0, 1, 0), (1, 0, 1)]
    C3, I3 = pair_constraint(X3, (0, 0, 0), (1, 1, 1))
    maj3 = tuple((a & b) | (b & c) | (a & c) for a, b, c in zip((0, 0, 1), (0, 1, 0), (1, 1, 1)))
    T3 = {(s[0] ^ s[1], s[0] ^ s[2]) for s in C3}
    observed3 = all(len({c[i] for c in X3}) == 2 for i in range(3))
    put("arity3_witness", dict(X=X3, C=sorted(C3), majority_of_001_010_111=list(maj3), in_C=maj3 in C3,
                               T=sorted(T3), T_majority_closed=majority_closed(T3, 2),
                               C_horn=closed_under_op(C3, lambda a, b: a & b), C_dual_horn=closed_under_op(C3, lambda a, b: a | b),
                               C_affine=affine_closed(C3), C_zero_valid=(0, 0, 0) in C3, C_one_valid=(1, 1, 1) in C3))
    report("EXHAUSTIVE", "witness: X = {000,111,001,110,010,101} in 2x2x2 uses every value; at (000,111) C(x,y) = X, and T = {00,01,10}",
           observed3 and C3 == set(X3) and len(I3) == 3 and T3 == {(0, 0), (0, 1), (1, 0)}, "C=%s T=%s" % (sorted(C3), sorted(T3)))
    report("REFUTATION", "'every pair constraint at arity 3 is bijunctive': maj(001,010,111) = %s not in C, while T is majority-closed" % (maj3,),
           maj3 == (0, 1, 1) and maj3 not in C3 and not majority_closed(C3, 3) and majority_closed(T3, 2),
           "C majority-closed=%s T majority-closed=%s" % (majority_closed(C3, 3), majority_closed(T3, 2)))
    xor = {(a, b, a ^ b) for a in (0, 1) for b in (0, 1)}
    neq = {(0, 1), (1, 0)}
    report("EXHAUSTIVE", "the arity-3 witness C is 0-valid and 1-valid and neither bijunctive, Horn, dual Horn nor affine; XOR is not bijunctive; != is neither 0- nor 1-valid",
           (0, 0, 0) in C3 and (1, 1, 1) in C3 and not majority_closed(C3, 3)
           and not closed_under_op(C3, lambda a, b: a & b) and not closed_under_op(C3, lambda a, b: a | b) and not affine_closed(C3)
           and not majority_closed(xor, 3) and (0, 0) not in neq and (1, 1) not in neq, "")

    # The arity-4 witness: the 6-cell set in the box 2x2x2x2 and the relation it realises at the
    # pair (0000, 1111).  The relation is READ OFF the witness, never asserted: a first version of this
    # block named {000,110,101} and the witness in fact realises {000,011,101}, which is the same
    # relation with two difference variables exchanged.
    X = {(0, 0, 0, 0), (1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1)}
    OK, I = pair_constraint(sorted(X), (0, 0, 0, 0), (1, 1, 1, 1))
    T = frozenset(tuple(s[0] ^ s[tt] for tt in range(1, 4)) for s in OK)
    maj = tuple((a & b) | (b & c) | (a & c) for a, b, c in zip(*sorted(T)))
    put("one_in_three_witness_set", sorted(X))
    put("one_in_three", dict(relation=sorted(T), majority=list(maj), size=len(T),
                             majority_closed=majority_closed(T, 3), C_majority_closed=majority_closed(OK, 4)))
    report("EXHAUSTIVE", "witness: X = {0000,1111,1100,0011,1010,0101} realises a 3-element T at (0000,1111)",
           len(T) == 3 and T == frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1)}), "T=%s" % sorted(T))
    report("REFUTATION", "'every arising difference relation is bijunctive' fails at arity 4: majority of T gives %s, not in T; C not bijunctive either" % (maj,),
           maj not in T and not majority_closed(T, 3) and not majority_closed(OK, 4), "T=%s majority=%s" % (sorted(T), maj))
    # and T is exactly-one-of-three up to an XOR translation and coordinatewise complement:
    # T + (1,1,0) = {110,101,011} = exactly-two-of-three, whose complement is exactly-one-of-three.
    t = (1, 1, 0)
    Tt = frozenset(tuple(a ^ b for a, b in zip(u, t)) for u in T)
    two_of_three = frozenset({(1, 1, 0), (1, 0, 1), (0, 1, 1)})
    one_of_three = frozenset(tuple(1 - a for a in u) for u in two_of_three)
    put("one_in_three_translation", dict(t=list(t), translated=sorted(Tt),
                                         equals_two_of_three=Tt == two_of_three,
                                         complement=sorted(one_of_three)))
    report("EXHAUSTIVE", "T + (1,1,0) = exactly-two-of-three, whose complement is exactly-one-of-three",
           Tt == two_of_three and one_of_three == frozenset({(0, 0, 1), (0, 1, 0), (1, 0, 0)}),
           "T+t=%s" % sorted(Tt))


def majority_closed(T, m):
    T = set(T)
    return all(tuple((a[i] & b[i]) | (b[i] & c[i]) | (a[i] & c[i]) for i in range(m)) in T for a in T for b in T for c in T)


def section_rank_lemma():
    print("\nL. The counting lemma (Lemma 8): rank of a Jacobian never exceeds either dimension (exact arithmetic)")
    # A sampled corroboration in exact rationals: random integer polynomial maps p -> q, Jacobian at
    # a rational point, rank by Fraction Gaussian elimination; the defect dim q - rank >= dim q - dim p
    rnd = random.Random(3)
    n = ok = 0
    for _ in range(60):
        dp, dq = rnd.randint(1, 4), rnd.randint(1, 5)
        # q_j = sum of monomials of degree <= 2 with small integer coefficients
        coef = [[[rnd.randint(-2, 2) for _ in range(dp)] + [rnd.randint(-2, 2) for _ in range(dp * dp)] for _ in range(1)][0] for _ in range(dq)]
        pt = [Fraction(rnd.randint(-3, 3), rnd.randint(1, 3)) for _ in range(dp)]
        J = []
        for j in range(dq):
            row = []
            for i in range(dp):
                # d/dp_i of sum_a c_a p_a + sum_{a,b} c_ab p_a p_b
                v = Fraction(coef[j][i])
                for a in range(dp):
                    for b in range(dp):
                        c = coef[j][dp + a * dp + b]
                        if a == i:
                            v += c * pt[b]
                        if b == i:
                            v += c * pt[a]
                row.append(v)
            J.append(row)
        # exact rank
        M = [r[:] for r in J]
        rank = 0
        for col in range(dp):
            piv = next((r for r in range(rank, dq) if M[r][col] != 0), None)
            if piv is None:
                continue
            M[rank], M[piv] = M[piv], M[rank]
            for r in range(dq):
                if r != rank and M[r][col] != 0:
                    f = M[r][col] / M[rank][col]
                    M[r] = [a - f * b for a, b in zip(M[r], M[rank])]
            rank += 1
        n += 1
        ok += (rank <= min(dp, dq)) and (dq - rank >= dq - dp)
    put("rank_lemma_sampled", dict(maps=n, ok=ok, seed=3))
    report("SAMPLED", "60 random quadratic maps (seed 3): rank <= min(dim p, dim q), so D >= dim q - dim p",
           ok == n, "%d of %d" % (ok, n))


def verification_record():
    print("\n" + "=" * 100)
    counts = {}
    for line in LINES:
        tag = line.split("]")[0].strip("[ ").strip()
        counts[tag] = counts.get(tag, 0) + 1
    print("obligations by status: " + ", ".join("%s %d" % (k, v) for k, v in sorted(counts.items())))
    put("counts", counts)
    if FAILS:
        print("FAILED: %d" % len(FAILS))
        for f in FAILS:
            print("   " + f)
    else:
        print("all obligations discharged")
    print("=" * 100)


def selftest():
    """Negative controls: a false claim must be REFUTED, and the encoding guard must catch a
    wrong reference (already part of guards()).  Run after the main obligations."""
    print("\nSELFTEST -- negative controls")
    ok = True
    # (1) the withdrawn clause of the source's criterion, asserted as a claim: must be refuted
    shape = (3, 3)
    cells = cells_of(shape)
    X = prover.subset_vars(cells, "x")
    A0 = list(range(3))
    s, order = order_vars(A0, "s")
    P = enc_P(X, cells, 0, A0)
    cl = enc_closed_s(X, s, cells, 0)
    antis = z3.And([z3.Not(z3.And(P[(u, v)], P[(v, u)])) for u in A0 for v in A0 if u < v])
    proved, m = z3_prove(z3.Implies(z3.And(prover.observed(X, cells, shape), order, cl), antis))
    ok &= not proved
    print("  [%s] false claim 'closed under some order => P antisymmetric' is REFUTED (witness found)" % ("ok" if not proved else "XX"))
    # (2) a wrong nesting lemma: 'no nesting at all' must fail
    ok &= RESULTS["interval_family"]["weak_refuted"] == 1098
    print("  [%s] false reading of the nesting lemma is refuted on 1,098 sets" % ("ok" if RESULTS["interval_family"]["weak_refuted"] == 1098 else "XX"))
    # (3) a wrong step law: step = 2^(d-1) must fail on some box
    wrong = any(r["step"] != 2 ** (len(r["box"]) - 1) for r in RESULTS["census"])
    ok &= wrong
    print("  [%s] false step law 2^(d-1) is contradicted by the census" % ("ok" if wrong else "XX"))
    # (4) a wrong bijunctivity claim at arity 4
    ok &= RESULTS["bijunctive_exact"][3]["bijunctive"] < RESULTS["bijunctive_exact"][3]["relations_containing_zero"]
    print("  [%s] 'all arity-4 relations are bijunctive' is false: %d of %d" % ("ok" if ok else "XX",
          RESULTS["bijunctive_exact"][3]["bijunctive"], RESULTS["bijunctive_exact"][3]["relations_containing_zero"]))
    # (5) a wrong bijunctivity claim at arity 3, on the constraint D9 defines
    e3 = RESULTS["pair_constraint_exact"][2]
    ok5 = e3["bijunctive_C"] < e3["relations"]
    ok &= ok5
    print("  [%s] 'every arity-3 pair constraint is bijunctive' is false: %d of %d" % ("ok" if ok5 else "XX", e3["bijunctive_C"], e3["relations"]))
    print("SELFTEST %s" % ("PASS" if ok else "FAIL"))
    return ok


def main():
    t0 = time.time()
    print(__doc__.split("Writes results.json")[0].rstrip())
    print("=" * 100)
    print("Z3 %s, numpy %s, Python %s" % (z3.get_version_string(), np.__version__, sys.version.split()[0]))
    print("=" * 100)
    if not guards():
        print("GUARDS FAILED -- obligations not reported")
        return 1
    cells, L216, TREE, A = section_lambda()
    section_closure()
    section_example()
    section_diagnostic()
    section_one_axis()
    section_interval_characterisation()
    section_interval_lemma()
    CENSUS = section_census()
    section_projection_gap(CENSUS)
    section_d2_algorithm(CENSUS)
    section_tree(CENSUS, cells, L216, TREE)
    section_removal(CENSUS)
    section_arity()
    section_rank_lemma()
    section_amplification(cells)
    verification_record()
    put("seconds", round(time.time() - t0, 1))
    rc = 0 if not FAILS else 1
    if "--selftest" in sys.argv:
        rc |= 0 if selftest() else 1
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(RESULTS, f, indent=1, default=lambda o: list(o) if isinstance(o, (set, frozenset, tuple)) else str(o))
    print("\n%.1f s total; results.json written" % (time.time() - t0))
    return rc


if __name__ == "__main__":
    sys.exit(main())
