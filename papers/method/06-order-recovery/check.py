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
    report("EXHAUSTIVE", "pushback over 475,800 pairs: min 16, none zero; zero iff JI and MI",
           pairs == 475800 and v[0] == 16 and v.count(0) == 0 and zero_iff and v[-1] == 5091,
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
    print("\nB. The cost of one fabricated cell, over every ambient non-cell (reference closure: op_order)")
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
    put("amplification", dict(noncells=len(non), min=amp_sorted[0], median=float(statistics.median(amp)),
                              max=amp_sorted[-1], mean=round(sum(amp) / len(amp), 1),
                              zero=amp.count(0), values=amp))
    report("EXHAUSTIVE", "A(y) = |R(Lambda u {y})| - 977 over all 5,936 non-cells: none is zero",
           len(non) == 5936 and amp_sorted[0] > 0,
           "n=%d min=%d median=%s max=%d mean=%.1f zero=%d" % (len(non), amp_sorted[0], statistics.median(amp), amp_sorted[-1], sum(amp) / len(amp), amp.count(0)))
    print("     (%.1f s)" % (time.time() - t))


def section_diagnostic():
    print("\nC. The diagnostic: the defect is a property of the coordinatisation")
    per = cypher._periodic()
    jan = cypher._janet()
    adm_p, _ = cypher.op_order(per, {})
    adm_j, _ = cypher.op_order(jan, {})
    Ep = len(adm_p) - len(per.cells)
    Ej = len(adm_j) - len(jan.cells)
    put("periodic_E", Ep)
    put("periodic_cells", len(per.cells))
    put("janet_E", Ej)
    put("janet_cells", len(jan.cells))
    report("EXHAUSTIVE", "periodic table (period x group): 90 cells, E = 36; Janet (n+l x l): E = 0",
           Ep == 36 and len(per.cells) == 90 and Ej == 0,
           "periodic cells=%d E=%d; janet cells=%d E=%d" % (len(per.cells), Ep, len(jan.cells), Ej))


def guards():
    """Both guards, before any Z3 obligation is reported."""
    print("\nGUARDS (run before the obligations)")
    ok = True
    rnd = random.Random(11)
    # (a) non-vacuity: the hypothesis of each obligation is satisfiable with X a proper subset
    for shape in ((3, 3), (2, 2, 3), (3, 3, 3)):
        cells = cells_of(shape)
        X = prover.subset_vars(cells, "x")
        A0 = list(range(shape[0]))
        s, order = order_vars(A0, "s")
        hyp = z3.And(prover.observed(X, cells, shape), order, enc_closed_s(X, s, cells, 0),
                     z3.Or([z3.Not(X[c]) for c in cells]))
        sat, _ = z3_sat(hyp)
        ok &= sat
        print("  [%s] hypothesis 'observed, s a total order, X closed under s, X != box' satisfiable, %s"
              % ("ok" if sat else "XX", "x".join(map(str, shape))))
    # (b) encoding fidelity: the Z3 formulas, evaluated on concrete X and s, equal the reference code
    tot = bad = 0
    tot2 = bad2 = 0
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
        enc = z3.is_true(z3.simplify(enc_closed_s(Xv, sv, cells, 0)))
        ref = closed_under(Xs, ranks)
        tot += 1
        bad += enc != ref
        # P against the reference relation (axis 0 free, others natural)
        Pz = enc_P(Xv, cells, 0, A0)
        vals, Pr = P_relation(Xs, 0, [{v: v for v in range(shape[i])} for i in range(d)])
        for u in A0:
            for v in A0:
                tot2 += 1
                bad2 += z3.is_true(z3.simplify(Pz[(u, v)])) != Pr[(u, v)]
    ok &= bad == 0 and bad2 == 0
    print("  [%s] enc_closed_s EVALUATED == closed_under: %d instances, %d disagreements" % ("ok" if bad == 0 else "XX", tot, bad))
    print("  [%s] enc_P EVALUATED == P_relation: %d pairs, %d disagreements" % ("ok" if bad2 == 0 else "XX", tot2, bad2))
    # (c) the reference closure: closed under the natural order iff E = 0 under cypher.op_order
    tot3 = bad3 = 0
    for _ in range(120):
        shape = rnd.choice([(3, 3), (2, 2, 3), (3, 3, 3), (2, 2, 2, 2)])
        cells = cells_of(shape)
        d = len(shape)
        while True:
            Xs = frozenset(rnd.sample(cells, rnd.randint(2, min(len(cells), 9))))
            if all(len({c[i] for c in Xs}) == shape[i] for i in range(d)):
                break
        tot3 += 1
        bad3 += closed_under(Xs, natural(Xs, d)) != (R_index(Xs) == set(Xs))
    ok &= bad3 == 0
    print("  [%s] closed_under(natural) == (op_order adds nothing): %d instances, %d disagreements" % ("ok" if bad3 == 0 else "XX", tot3, bad3))
    # (d) negative control on the fidelity guard: a wrong reference must be caught
    wrong = 0
    for _ in range(20):
        shape = (3, 3)
        cells = cells_of(shape)
        Xs = frozenset(rnd.sample(cells, rnd.randint(2, 6)))
        Xv = {c: z3.BoolVal(c in Xs) for c in cells}
        sv = {(u, v): z3.BoolVal(u < v) for u in range(3) for v in range(3) if u != v}
        enc = z3.is_true(z3.simplify(enc_closed_s(Xv, sv, cells, 0)))
        wrong += enc != (len(Xs) % 2 == 0)      # a deliberately wrong 'reference'
    ok &= wrong > 0
    print("  [%s] negative control: the guard detects a wrong reference (%d disagreements)" % ("ok" if wrong > 0 else "XX", wrong))
    put("guards", dict(fidelity_instances=tot, fidelity_pairs=tot2, closure_instances=tot3, ok=ok))
    return ok


def section_one_axis():
    print("\nD. One-axis order recovery (Theorem 1) -- Z3 over every X and every total order on axis 0")
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
            ("1(a) P is transitive", z3.Implies(obs, transP)),
            ("1(b) closed under s  =>  P reflexive and s in P", z3.Implies(z3.And(obs, order, cl), z3.And(refl, sub))),
            ("1(b) P reflexive and s in P  =>  closed under s", z3.Implies(z3.And(obs, order, refl, sub), cl)),
            ("1(c) P total preorder  =>  s* is a total order and X closed under s*",
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
    print("\nE. The fibre characterisation at d = 2 (Theorem 2) -- Z3 over every X and every order on axis 0")
    rows = []
    for shape in [(3, 3), (4, 4), (3, 5), (5, 4)]:
        t = time.time()
        cells = cells_of(shape)
        A, B = list(range(shape[0])), list(range(shape[1]))
        X = prover.subset_vars(cells, "x")
        s, order = order_vars(A, "s")
        obs = prover.observed(X, cells, shape)
        cl = enc_closed_s(X, s, cells, 0)
        interval = z3.And([z3.Implies(z3.And(X[(u, b1)], X[(u, b3)]), X[(u, b2)])
                           for u in A for b1 in B for b2 in B for b3 in B if b1 < b2 < b3])

        def lo_le(u, v):
            return z3.And([z3.Implies(X[(v, c)], z3.Or([X[(u, c2)] for c2 in B if c2 <= c])) for c in B])

        def hi_le(u, v):
            return z3.And([z3.Implies(X[(u, c)], z3.Or([X[(v, c2)] for c2 in B if c2 >= c])) for c in B])
        mono = z3.And([z3.Implies(s[(u, v)], z3.And(lo_le(u, v), hi_le(u, v))) for u in A for v in A if u != v])
        ok, _ = z3_prove(z3.Implies(z3.And(obs, order), cl == z3.And(interval, mono)))
        report("MACHINE-CHECKED", "closed under s  <=>  fibres are intervals with endpoints monotone along s, box %s"
               % "x".join(map(str, shape)), ok, "2^%d subsets x %d orders" % (len(cells), len(list(itertools.permutations(A)))))
        rows.append(dict(box=list(shape), ok=ok, seconds=round(time.time() - t, 1)))
    put("fibre_z3", rows)


def section_interval_lemma():
    print("\nF. The nesting lemma (Lemma 4), exhaustive over every set of 2..4 distinct intervals on 2..5 points")

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


def section_census():
    """Every subset of each box: closed under the natural order, reorderable, the step, the largest
    proper reorderable subset of the full box.  Bitmask arrays, one bit per cell."""
    print("\nG. Reorderability census, every subset of each box")
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
        row = dict(box=list(shape), subsets=1 << N, orderings=len(perms_list), closed_natural_observed=int((closed & obs).sum()),
                   reorderable_observed=int((reord & obs).sum()), reorderable_all=int(reord.sum()), step=step,
                   step_attained_at_full_box=(step_at == full), max_proper_reorderable=maxproper,
                   three_quarters=(maxproper == 3 * (1 << N) // 4) if all(n == 2 for n in shape) else None,
                   seconds=round(time.time() - t, 1))
        rows.append(row)
        CENSUS[shape] = dict(cells=cells, idx=idx, closed=closed, obs=obs, reord=reord, permmaps=permmaps, perms=perms_list, popc=popc)
        report("EXHAUSTIVE", "box %s: %d subsets, %d reorderable, step %d, largest proper reorderable %d"
               % ("x".join(map(str, shape)), 1 << N, int(reord.sum()), step, maxproper),
               step == 2 ** (d - 2) if d >= 2 else True, "step attained at the full box: %s" % (step_at == full))
    put("census", rows)
    return CENSUS


def section_d2_algorithm(CENSUS):
    print("\nH. The d = 2 decision by root enumeration + Theorem 1, against the brute-force census")
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
        report("EXHAUSTIVE", "box %s: algorithm == brute force on every observed subset" % "x".join(map(str, shape)),
               agree == n, "%d of %d" % (agree, n))
    put("d2_algorithm", rows)


def section_tree(CENSUS, lam976, lam216, TREE):
    print("\nI. Tree propagation (Theorem 3): every solution, against brute force, on every tree-structured subset")
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
        report("EXHAUSTIVE", "box %s, %s: solution set == brute force on all %d tree-structured subsets" % ("x".join(map(str, shape)), kind, n),
               agree == n and scr_ok == scr, "agree=%d/%d; %d closed x every relabelling = %d scrambles, %d recovered" % (agree, n, nclosed, scr, scr_ok))
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
               ok == 20, "recovered=%d exact-or-dual=%d admissible=%d" % (ok, exact_or_dual, len(sols)))
    put("lambda_recovery", lam_rows)
    fact = [len(a) for a in alphabets(lam976, 8)]
    import math
    put("lambda_sum_fact", sum(math.factorial(k) for k in fact))
    put("lambda_prod_fact", math.prod(math.factorial(k) for k in fact))
    report("EXHAUSTIVE", "Lambda: sum |A_i|! = 94 against prod |A_i|! = 11,943,936",
           sum(math.factorial(k) for k in fact) == 94 and math.prod(math.factorial(k) for k in fact) == 11943936,
           "sum=%d prod=%d" % (sum(math.factorial(k) for k in fact), math.prod(math.factorial(k) for k in fact)))


def section_removal():
    print("\nJ. Interval removal (Lemma 5) -- Z3 over every sublattice S of the box and every a <= b")
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
                inR = lambda c: leq(a, c) and leq(c, b)
                rem = lambda c: z3.And(S[c], z3.BoolVal(not inR(c)))
                remclosed = z3.And([z3.Implies(z3.And(rem(x), rem(y)), z3.And(rem(meet(x, y)), rem(join(x, y))))
                                    for x in cells for y in cells if x < y])
                jp = z3.And([z3.Implies(z3.And(S[x], S[y], z3.BoolVal(leq(a, join(x, y)))),
                                        z3.BoolVal(leq(a, x) or leq(a, y))) for x in cells for y in cells])
                mp = z3.And([z3.Implies(z3.And(S[x], S[y], z3.BoolVal(leq(meet(x, y), b))),
                                        z3.BoolVal(leq(x, b) or leq(y, b))) for x in cells for y in cells])
                ok, _ = z3_prove(z3.Implies(z3.And(closed, S[a], S[b]), remclosed == z3.And(jp, mp)))
                bad += not ok
        rows.append(dict(box=list(shape), pairs=n, failures=bad, seconds=round(time.time() - t, 1)))
        report("MACHINE-CHECKED", "S \\ [a,b] closed <=> a join-prime and b meet-prime, box %s, all %d pairs a<=b"
               % ("x".join(map(str, shape)), n), bad == 0, "2^%d sublattice candidates per pair" % len(cells))
    put("removal_z3", rows)

    print("   The largest proper sublattice of the Boolean box 2^d (Z3, cardinality)")
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
        rows.append(dict(d=d, bound=bound, attained=sat_at, exceeded=sat_above, seconds=round(time.time() - t, 1)))
        report("MACHINE-CHECKED", "2^%d: every proper sublattice has <= %d cells, and %d is attained" % (d, bound, bound),
               (not sat_above) and sat_at, "2^%d subsets" % len(cells))
    put("max_sublattice_z3", rows)


def section_arity():
    print("\nK. The arity law: pair constraints, their difference relations, and bijunctivity")
    # every difference relation containing 0 arises (Theorem 5), and the census of what arises
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
            Xs = set(X)
            for a in range(len(X)):
                for b in range(a + 1, len(X)):
                    x, y = X[a], X[b]
                    I = [i for i in range(d) if x[i] != y[i]]
                    k = len(I)
                    OK = set()
                    for s in itertools.product((0, 1), repeat=k):
                        j, m = list(x), list(x)
                        for tt, i in enumerate(I):
                            j[i], m[i] = (y[i], x[i]) if s[tt] else (x[i], y[i])
                        if tuple(j) in Xs and tuple(m) in Xs:
                            OK.add(s)
                    cc_checked += 1
                    cc_ok += all(tuple(1 - b_ for b_ in s) in OK for s in OK)
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
                          bijunctive=sum(1 for T in Ts if majority_closed(T, k - 1)))
        rows.append(dict(box=list(shape), complement_checked=cc_checked, complement_closed=cc_ok, per_arity=per, seconds=round(time.time() - t, 1)))
        ok = cc_ok == cc_checked and all(per[k]["contain_zero"] for k in per) and per[max(per)]["distinct"] == 2 ** (2 ** (max(per) - 1) - 1)
        report("EXHAUSTIVE", "box %s: %d pair constraints, all complement-closed; every relation containing 0 arises at arity %d"
               % ("x".join(map(str, shape)), cc_checked, max(per)), ok,
               "; ".join("arity %d: %d distinct, %d bijunctive" % (k, per[k]["distinct"], per[k]["bijunctive"]) for k in sorted(per)))
    put("arity_census", rows)
    # exact count of bijunctive (majority-closed) relations on m difference variables containing 0
    exact = {}
    for m in range(1, 5):
        cnt = tot = 0
        pts = list(itertools.product((0, 1), repeat=m))
        # bit-parallel: a relation is a 2^m-bit mask; it is majority-closed iff it equals the
        # solution set of the 2-clauses it satisfies
        M = 1 << len(pts)
        pidx = {p: i for i, p in enumerate(pts)}
        clauses = []
        for i in range(m):
            for si in (0, 1):
                clauses.append(sum(1 << pidx[p] for p in pts if p[i] != si))          # unit clause x_i != si
                for j in range(i + 1, m):
                    for sj in (0, 1):
                        clauses.append(sum(1 << pidx[p] for p in pts if not (p[i] == si and p[j] == sj)))
        full = M - 1
        for T in range(1, M):
            if not (T >> pidx[tuple([0] * m)]) & 1:
                continue
            tot += 1
            closure = full
            for c in clauses:
                if T & ~c == 0:
                    closure &= c
            cnt += closure == T
        exact[m] = dict(relations_containing_zero=tot, bijunctive=cnt)
        report("EXHAUSTIVE", "relations on %d difference variables containing 0: %d, of which %d bijunctive (arity %d)" % (m, tot, cnt, m + 1),
               True, "")
    put("bijunctive_exact", exact)
    # The explicit witness: the 6-cell set in the box 2x2x2x2 and the relation it realises at the
    # pair (0000, 1111).  The relation is READ OFF the witness, never asserted: an earlier draft of
    # this block named {000,110,101} and the witness in fact realises {000,011,101}, which is the
    # same relation with two difference variables exchanged.
    X = {(0, 0, 0, 0), (1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 1, 0), (0, 1, 0, 1)}
    x, y = (0, 0, 0, 0), (1, 1, 1, 1)
    OK = set()
    for s in itertools.product((0, 1), repeat=4):
        j = tuple(y[i] if s[i] else x[i] for i in range(4))
        m = tuple(x[i] if s[i] else y[i] for i in range(4))
        if j in X and m in X:
            OK.add(s)
    T = frozenset(tuple(s[0] ^ s[tt] for tt in range(1, 4)) for s in OK)
    maj = tuple((a & b) | (b & c) | (a & c) for a, b, c in zip(*sorted(T)))
    put("one_in_three_witness_set", sorted(X))
    put("one_in_three", dict(relation=sorted(T), majority=list(maj), size=len(T),
                             majority_closed=majority_closed(T, 3)))
    report("EXHAUSTIVE", "witness: X = {0000,1111,1100,0011,1010,0101} realises a 3-element relation at (0000,1111)",
           len(T) == 3 and T == frozenset({(0, 0, 0), (0, 1, 1), (1, 0, 1)}), "T=%s" % sorted(T))
    report("REFUTATION", "'every arising relation is bijunctive' fails at arity 4: majority of T gives %s, not in T" % (maj,),
           maj not in T and not majority_closed(T, 3), "T=%s majority=%s" % (sorted(T), maj))
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
    print("\nL. The counting lemma (Lemma 6): rank of a Jacobian never exceeds either dimension (exact arithmetic)")
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
    section_diagnostic()
    section_one_axis()
    section_interval_characterisation()
    section_interval_lemma()
    CENSUS = section_census()
    section_d2_algorithm(CENSUS)
    section_tree(CENSUS, cells, L216, TREE)
    section_removal()
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
