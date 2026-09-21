#!/usr/bin/env python3
"""check.py -- the machine checks behind paper 08, "Lambda_chem and Lambda_PCA: closing the
chemical properties".

Every number the paper prints is produced here or is marked CITED in the paper.  One line per
obligation, a summary at the end, exit 1 on any failure.

    python3 check.py              the obligations
    python3 check.py --selftest   the obligations plus the negative controls (a deliberately false
                                  claim must be REFUTED, a deliberately wrong encoding must be CAUGHT)

The object under test is the seated staircase operator, tools/cypher.py's op_order (R), imported
by path.  The property tables are read by path (as literals, via ast) from the instruments that
built the indexes; nothing is copied.  A fresh, independent staircase implementation (ref_R) is
written here for the encoding guard only.  Z3 obligations run through research/warp-drive/prover.py.

stdlib + z3 + numpy (numpy only for the 2^24 brute-force count, which cross-checks next-closure).
"""
import ast
import importlib.util
import itertools
import os
import random
import sys
import time
from fractions import Fraction

ROOT = "/home/user/Claude-Method-Works"
HERE = os.path.dirname(os.path.abspath(__file__))
RP = os.path.join(ROOT, "extracted/archives/restore-point-2-13")
INSTR = {
    "chem4": os.path.join(RP, "chem4.py"),            # the 42 properties on (kind, seat, PCA)
    "chem3": os.path.join(RP, "chem3.py"),            # the same 42 on (kind, seat, breadth)
    "chem_index": os.path.join(RP, "chem_index.py"),  # the routing list (residual -> property -> class)
    "phys_close": os.path.join(RP, "phys_close.py"),  # the 21 (+1 excluded) physical parameters
    "charge_index": os.path.join(RP, "charge_index.py"),  # the nine occurrences of the charge
    "dom_reg": os.path.join(RP, "dom_reg.py"),        # the merge on domain == regime
    "amp_index": os.path.join(RP, "amp_index.py"),    # the Slater-integral index on raw rank
    "merge": os.path.join(ROOT, "recovered/merge.py"),  # the merge on axis names (the recorded correction)
}

SELFTEST = "--selftest" in sys.argv
FAILS = []
COUNT = {"PROVED": 0, "EXHAUSTIVE": 0, "MACHINE-CHECKED": 0, "SAMPLED": 0, "CITED": 0, "GUARD": 0}
RESULTS = {}


def report(tag, status, name, ok, detail=""):
    COUNT[status] = COUNT.get(status, 0) + 1
    mark = "ok " if ok else "XX "
    print("  [%s] %-16s %-6s %-58s %s" % (mark, status, tag, name, detail))
    if not ok:
        FAILS.append((tag, name, detail))
    return ok


# ------------------------------------------------------------------ imports by path

def load_module(name, path, register=True):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    if register:
        sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


cy = load_module("cypher", os.path.join(ROOT, "tools/cypher.py"))
pv = load_module("prover", os.path.join(ROOT, "research/warp-drive/prover.py"))
import z3  # noqa: E402  (prover has already required it)


def load_literal(path, name):
    """The first top-level-or-nested assignment `name = <literal>` in the instrument at `path`,
    read as data.  The instrument is not executed."""
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) and node.targets[0].id == name:
            try:
                return ast.literal_eval(node.value)
            except ValueError:
                continue
    raise KeyError("%s not found as a literal in %s" % (name, path))


# ------------------------------------------------------------------ the operator under test

def E_cypher(cells, names, orders):
    """Defect of the cell set under the declared value orders, by the seated op_order.
    `orders[i]` is the list of raw values of coordinate i in increasing order."""
    ix = cy.Index("x", names, cells, value_order={n: o for n, o in zip(names, orders)})
    R, _ = cy.op_order(ix, {})
    return len(R) - len(ix.cells), R, ix


def ref_R(X, d):
    """Independent staircase closure, witness form, own box: x is admitted iff for every ordered
    pair i != j some y in X has y_j <= x_j and y_i >= x_i."""
    X = set(X)
    alph = [sorted({x[i] for x in X}) for i in range(d)]
    return {x for x in itertools.product(*alph)
            if all(any(y[j] <= x[j] and y[i] >= x[i] for y in X)
                   for i in range(d) for j in range(d) if i != j)}


def relabel(cells, perms):
    """Apply a permutation of the value codes on each axis: cell (a,b,c) -> (p0[a], p1[b], p2[c])."""
    return [tuple(perms[i][x[i]] for i in range(len(perms))) for x in cells]


def recode(cells):
    """Map the realised values of every axis onto 0..k-1 in their given order (the own-box
    alphabet).  Returns (recoded cells, the per-axis value lists)."""
    d = len(cells[0])
    alph = [sorted({x[i] for x in cells}) for i in range(d)]
    return [tuple(alph[i].index(x[i]) for i in range(d)) for x in cells], alph


def sweep(cells, use_symmetry=True):
    """min E over every ordering of the axes (a permutation of each axis's REALISED values), by the
    seated operator.  Returns (minE, n_orderings, n_minimising, n_closing, minimisers, defect_sets,
    sizes) where defect_sets is the set of frozensets of defect cells (in the recoded labels) over
    the minimising orderings.  With use_symmetry the last axis's permutations are halved by the
    global-reversal symmetry (Lemma 3 of the paper) and the counts doubled."""
    cells, alph = recode(cells)
    sizes = [len(a) for a in alph]
    d = len(sizes)
    names = ["c%d" % i for i in range(d)]
    best = None
    n = 0
    minimisers = []
    closing = 0
    defects = set()
    last = list(itertools.permutations(range(sizes[-1])))
    if use_symmetry:
        last = [p for p in last if p[0] < p[-1]]
    axes = [list(itertools.permutations(range(s))) for s in sizes[:-1]] + [last]
    for perms in itertools.product(*axes):
        cs = relabel(cells, perms)
        E, R, ix = E_cypher(cs, names, [list(range(s)) for s in sizes])
        n += 1
        if E == 0:
            closing += 1
        if best is None or E < best:
            best = E
            minimisers = [perms]
            defects = set()
        elif E == best:
            minimisers.append(perms)
        if E == best:
            held = set(cs)
            inv = [{perms[i][v]: v for v in range(sizes[i])} for i in range(d)]
            dset = frozenset(tuple(inv[i][x[i]] for i in range(d)) for x in R if x not in held)
            defects.add(dset)
    mult = 2 if use_symmetry else 1
    return best, n * mult, len(minimisers) * mult, closing * mult, minimisers, defects, sizes


# ------------------------------------------------------------------ the data

KIND = ["count", "symmetry", "size", "energy", "rate"]
SEAT = ["the nucleus", "the core", "the subvalence shell", "the valence shell", "the aggregate"]
PCA = ["P", "C", "A"]
SUB, VAL, CORE, NUC, AGG = 2, 3, 1, 0, 4

T42 = load_literal(INSTR["chem4"], "C")          # (name, kind, seat, pca) as held
T42_BREADTH = load_literal(INSTR["chem3"], "C")  # (name, kind, seat, breadth)
BREADTH = ["every species", "a block", "a period", "one subshell"]
ROUTING = load_literal(INSTR["chem_index"], "R")  # (residual, property, class, why)
CHEM11 = load_literal(INSTR["chem_index"], "CHEM")  # (property, supplies, class, measured)

TERM = "term symbol"
T42_FILLED = [(n, k, s, (1 if n == TERM else p)) for n, k, s, p in T42]  # the fill: term symbol -> C


def cells_of(table, seats):
    return sorted({(k, s, p) for _, k, s, p in table if s in seats})


def header(t):
    print()
    print("== " + t)


# ================================================================== A. the table
header("A. The property table (42 properties on kind x seat x PCA)")
ok = len(T42) == 42 and len({n for n, *_ in T42}) == 42
report("A1", "EXHAUSTIVE", "42 named properties, all distinct", ok, "%d rows" % len(T42))
byk = [sum(1 for _, k, _, _ in T42 if k == i) for i in range(5)]
bys = [sum(1 for _, _, s, _ in T42 if s == i) for i in range(5)]
byp = [sum(1 for _, _, _, p in T42 if p == i) for i in range(3)]
byp_f = [sum(1 for _, _, _, p in T42_FILLED if p == i) for i in range(3)]
report("A2", "EXHAUSTIVE", "by kind count/symmetry/size/energy/rate = 9/8/8/11/6",
       byk == [9, 8, 8, 11, 6], str(byk))
report("A3", "EXHAUSTIVE", "by seat nucleus/core/subvalence/valence/aggregate = 6/2/2/20/12",
       bys == [6, 2, 2, 20, 12], str(bys))
report("A4", "EXHAUSTIVE", "by dependency P/C/A = 16/10/16 as held, 15/11/16 filled",
       byp == [16, 10, 16] and byp_f == [15, 11, 16], "%s -> %s" % (byp, byp_f))
TWELVE = {"density", "melting point", "boiling point", "hardness", "crystal structure",
          "electrical conductivity", "thermal conductivity", "colour of the metal", "smell",
          "taste", "metallic character", "reactivity"}
agg = {n for n, _, s, _ in T42 if s == AGG}
report("A5", "EXHAUSTIVE", "the twelve bulk properties are exactly the aggregate seat",
       agg == TWELVE, "%d" % len(agg))
same = {n for n, *_ in T42} == {n for n, *_ in T42_BREADTH}
same_ks = all((k, s) == next((k2, s2) for n2, k2, s2, _ in T42_BREADTH if n2 == n)
              for n, k, s, _ in T42)
report("A6", "EXHAUSTIVE", "the breadth table names the same 42 with the same kind and seat",
       same and same_ks)
RESULTS.update(byk=byk, bys=bys, byp=byp, byp_f=byp_f)

# ================================================================== B. Lambda_chem closes
header("B. Lambda_chem: E = 0 on fourteen cells (subvalence + valence, term symbol -> charge)")
NAMES3 = ["kind", "seat", "pca"]
SV = cells_of(T42_FILLED, {SUB, VAL})
SV0 = cells_of(T42, {SUB, VAL})
report("B1", "EXHAUSTIVE", "fourteen distinct cells; thirteen before the fill",
       len(SV) == 14 and len(SV0) == 13, "%d / %d" % (len(SV), len(SV0)))
SVc, SV_alph = recode(SV)           # realised alphabet: four kinds (no 'rate'), two seats, three dependencies
KINDS_SV = [KIND[k] for k in SV_alph[0]]
report("B1b", "EXHAUSTIVE", "realised alphabet 4 kinds x 2 seats x 3 dependencies: box 24; 'rate' is unrealised",
       [len(a) for a in SV_alph] == [4, 2, 3] and 4 not in SV_alph[0], ", ".join(KINDS_SV))
t0 = time.time()
mE, nvis, nmin, nclose, mins, dsets, sizes_sv = sweep(SV)
report("B2", "EXHAUSTIVE", "min E over all 4! x 2! x 3! = 288 orderings of the realised values is 0",
       mE == 0 and nvis == 288, "E=%d, %d orderings, %d close (%.1fs)" % (mE, nvis, nclose, time.time() - t0))
report("B2b", "EXHAUSTIVE", "the 1,440 of the source = 288 x 5 (the unrealised 'rate' permuted with the four)",
       288 * 5 == 1440)
# a canonical closing order: seat = (subvalence < valence)
canon = None
for perms in mins:
    if perms[1] == (0, 1):
        canon = perms
        break
if canon is None:   # the halved sweep stored the reversed partner: reverse every axis (Lemma 3)
    canon = tuple(tuple(len(p) - 1 - v for v in p) for p in mins[0])
assert canon[1] == (0, 1)
# prefer the order the building instrument declared (kind count < size < symmetry < energy, A < P < C) when it closes
want_k = [KIND.index(x) for x in ("count", "size", "symmetry", "energy")]
pref = (tuple(want_k.index(SV_alph[0][v]) for v in range(4)), (0, 1), (0, 2, 1))
E_pref, _, _ = E_cypher(relabel(SVc, pref), NAMES3, [list(range(4)), [0, 1], list(range(3))])
if E_pref == 0:
    canon = pref
ORD_K = [KINDS_SV[k] for k in sorted(range(4), key=lambda k: canon[0][k])]
ORD_S = [SEAT[s] for s in (SUB, VAL)]
ORD_P = [PCA[p] for p in sorted(range(3), key=lambda p: canon[2][p])]
E_decl, R_decl, ix_decl = E_cypher(relabel(SVc, canon), NAMES3, [list(range(4)), [0, 1], list(range(3))])
report("B3", "EXHAUSTIVE", "E = 0 under the declared order (seated op_order), box 24",
       E_decl == 0 and ix_decl.box == 24,
       "kind %s; seat %s; PCA %s" % (" < ".join(ORD_K), " < ".join(ORD_S), " < ".join(ORD_P)))
RESULTS.update(ORD_K=ORD_K, ORD_S=ORD_S, ORD_P=ORD_P, canon=canon, nclose_sv=nclose, SV=SV, SV0=SV0, KINDS_SV=KINDS_SV)
chem_orders = []
for perms in itertools.product(itertools.permutations(range(4)), [(0, 1)], itertools.permutations(range(3))):
    cs = relabel(SVc, perms)
    E1, R1, ix1 = E_cypher(cs, NAMES3, [list(range(4)), [0, 1], list(range(3))])
    if E1 == 0:
        ko = [KINDS_SV[v] for v in sorted(range(4), key=lambda v: perms[0][v])]
        po = [PCA[v] for v in sorted(range(3), key=lambda v: perms[2][v])]
        chem_orders.append((ko, po))
        print("      closing order: kind %s; PCA %s" % (" < ".join(ko), " < ".join(po)))
report("B3b", "EXHAUSTIVE", "closing orders with subvalence < valence: 8 (the other 8 are their reversals)",
       len(chem_orders) == 8, "PCA orders: %s" % sorted({" < ".join(po) for _, po in chem_orders}))
RESULTS["chem_orders"] = chem_orders

# encoding guard: the seated operator against the independent reference, on every relabelling
t0 = time.time()
bad = 0
tot = 0
for perms in itertools.product(itertools.permutations(range(4)), itertools.permutations(range(2)),
                               itertools.permutations(range(3))):
    cs = relabel(SVc, perms)
    E1, R1, ix1 = E_cypher(cs, NAMES3, [list(range(4)), [0, 1], list(range(3))])
    tot += 1
    if R1 != ref_R(cs, 3):
        bad += 1
report("G1", "GUARD", "seated op_order == independent reference on all 288 relabellings",
       bad == 0 and tot == 288, "%d/%d agree (%.1fs)" % (tot - bad, tot, time.time() - t0))
rnd = random.Random(8)
bad = 0
for _ in range(300):
    shape = rnd.choice([(3, 3), (4, 2, 3), (4, 6), (2, 4, 4), (3, 3, 3)])
    allc = list(itertools.product(*[range(n) for n in shape]))
    X = rnd.sample(allc, rnd.randint(2, min(len(allc), 9)))
    X, _ = recode(X)   # the seated operator reports cells in rank codes; compare on the same labels
    names = ["c%d" % i for i in range(len(shape))]
    E1, R1, ix1 = E_cypher(X, names, [sorted({x[i] for x in X}) for i in range(len(shape))])
    if R1 != ref_R(X, len(shape)):
        bad += 1
report("G2", "SAMPLED", "seated op_order == reference on 300 random subsets (seed 8)", bad == 0,
       "%d disagreements" % bad)

# the fourteen cells, grid and inequalities under the declared order
grid = {}
for n, k, s, p in T42_FILLED:
    if s in (SUB, VAL):
        grid.setdefault((canon[0][SV_alph[0].index(k)], canon[1][SV_alph[1].index(s)], canon[2][p]), []).append(n)
RESULTS["grid"] = grid
coded = sorted(grid)
# phi tables of the closed set: phi_ij(a) = max{ y_i : y in X, y_j <= a }
phi = {}
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        for a in range(ix_decl.alphabets[j][-1] + 1):
            cand = [y[i] for y in coded if y[j] <= a]
            phi[(i, j, a)] = max(cand) if cand else None
RESULTS["phi"] = phi
print("      phi tables (i <- j): " + "; ".join(
    "%s<-%s: %s" % (NAMES3[i], NAMES3[j], [phi[(i, j, a)] for a in range(ix_decl.alphabets[j][-1] + 1)])
    for i in range(3) for j in range(3) if i != j))
# closed iff X = {x in Box(X) : x_i <= phi_ij(x_j) all i != j}: verify directly
stair = {x for x in itertools.product(range(4), range(2), range(3))
         if all(x[i] <= phi[(i, j, x[j])] for i in range(3) for j in range(3) if i != j)}
report("B4", "EXHAUSTIVE", "the fourteen cells are exactly the lattice points of their staircases",
       stair == set(coded), "%d points" % len(stair))

# the family of closed subsets of the index itself: every one of the 2^14 subsets
t0 = time.time()
n_closed_sub = 0
closed_sizes = {}
for r in range(0, 15):
    for Y in itertools.combinations(coded, r):
        if r == 0:
            n_closed_sub += 1
            closed_sizes[0] = 1
            continue
        if ref_R(Y, 3) == set(Y):
            n_closed_sub += 1
            closed_sizes[r] = closed_sizes.get(r, 0) + 1
report("B5", "EXHAUSTIVE", "closed subsets among the 2^14 = 16,384 subsets of the fourteen cells",
       True, "%d closed (%.1fs)" % (n_closed_sub, time.time() - t0))
RESULTS["n_closed_sub14"] = n_closed_sub
RESULTS["closed_sizes14"] = closed_sizes


# ------------------------------------------------------------------ the closure family of a box
def nextclosure_count(shape, spanning_only=False):
    """Ganter's next-closure over the FIXED box: visits every closed subset of the box exactly once
    (R is a closure operator on the fixed box: Lemma 1 of the paper, machine-checked below).
    Bit-parallel R with precomputed witness masks.  Returns the number of closed subsets, or of
    those that realise every value of every coordinate."""
    cells = list(itertools.product(*[range(n) for n in shape]))
    d = len(shape)
    idx = {c: i for i, c in enumerate(cells)}
    n = len(cells)
    W = []
    for x in cells:
        ms = []
        for i in range(d):
            for j in range(d):
                if i == j:
                    continue
                m = 0
                for y in cells:
                    if y[j] <= x[j] and y[i] >= x[i]:
                        m |= 1 << idx[y]
                ms.append(m)
        W.append(ms)
    axis_masks = []
    for i in range(d):
        for v in range(shape[i]):
            m = 0
            for y in cells:
                if y[i] == v:
                    m |= 1 << idx[y]
            axis_masks.append(m)

    def R(X):
        out = 0
        for k in range(n):
            for m in W[k]:
                if not (X & m):
                    break
            else:
                out |= 1 << k
        return out

    def spans(X):
        return all(X & m for m in axis_masks)

    A = R(0)
    K = 1 if (not spanning_only or spans(A)) else 0
    full = (1 << n) - 1
    while A != full:
        for i in range(n - 1, -1, -1):
            if A >> i & 1:
                continue
            low = (1 << i) - 1
            B = R((A & low) | (1 << i))
            if (B & low) == (A & low):
                A = B
                if not spanning_only or spans(A):
                    K += 1
                break
        else:
            break
    return K


def brute_counts_numpy(shape, chunk=1 << 22):
    """Every subset of the box, visited: fixed-box closed count and own-box closed count."""
    import numpy as np
    cells = list(itertools.product(*[range(n) for n in shape]))
    N = len(cells)
    d = len(shape)
    idx = {c: i for i, c in enumerate(cells)}
    total = 1 << N
    W = {}
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            for x in cells:
                m = 0
                for y in cells:
                    if y[j] <= x[j] and y[i] >= x[i]:
                        m |= 1 << idx[y]
                W[(i, j, x)] = m
    A = {}
    for i in range(d):
        for v in range(shape[i]):
            m = 0
            for y in cells:
                if y[i] == v:
                    m |= 1 << idx[y]
            A[(i, v)] = m
    dt = np.uint64 if N > 32 else np.uint32
    n_fixed = n_own = 0
    for start in range(0, total, chunk):
        m = np.arange(start, min(start + chunk, total), dtype=dt)
        R = np.zeros_like(m)
        B = np.zeros_like(m)
        for x in cells:
            inR = np.ones(m.shape, dtype=bool)
            for i in range(d):
                for j in range(d):
                    if i != j:
                        inR &= (m & dt(W[(i, j, x)])) != 0
            R |= np.where(inR, dt(1 << idx[x]), dt(0))
            inB = np.ones(m.shape, dtype=bool)
            for i in range(d):
                inB &= (m & dt(A[(i, x[i])])) != 0
            B |= np.where(inB, dt(1 << idx[x]), dt(0))
        n_fixed += int(np.count_nonzero(R == m))
        n_own += int(np.count_nonzero((R & B) == m))
    return total, n_fixed, n_own


def ownbox_count(shape):
    """Own-box closed subsets of the box = for every sub-box (a choice of realised values on
    each axis), the closed subsets of that sub-box that realise all of it; plus the empty set."""
    tot = 1  # the empty set
    for sub in itertools.product(*[range(1, n + 1) for n in shape]):
        # a sub-box is determined up to relabelling by the number of values realised per axis;
        # the number of ways to choose those values is a product of binomials
        ways = 1
        for n, k in zip(shape, sub):
            from math import comb
            ways *= comb(n, k)
        tot += ways * nextclosure_count(sub, spanning_only=True)
    return tot


header("C. The family of closed subsets of the boxes")
t0 = time.time()
tot24, fx24, own24 = brute_counts_numpy((4, 6))
nc24 = nextclosure_count((4, 6))
oc24 = ownbox_count((4, 6))
report("C1", "EXHAUSTIVE", "4x6 box: every one of 2^24 subsets visited; closed counts agree with next-closure",
       tot24 == 1 << 24 and fx24 == nc24 and own24 == oc24,
       "fixed-box %d, own-box %d (%.1fs)" % (fx24, own24, time.time() - t0))
tot20, fx20, own20 = brute_counts_numpy((4, 5))
report("C1b", "EXHAUSTIVE", "4x5 box (Lambda_PCA realised): every one of 2^20 subsets visited; agrees with next-closure",
       fx20 == nextclosure_count((4, 5)) and own20 == ownbox_count((4, 5)), "fixed-box %d, own-box %d" % (fx20, own20))
RESULTS.update(fx20=fx20, own20=own20)
tot6, fx6, own6 = brute_counts_numpy((2, 3))
report("C2", "EXHAUSTIVE", "2x3 box: brute force == next-closure (fixed %d, own %d)" % (fx6, own6),
       fx6 == nextclosure_count((2, 3)) and own6 == ownbox_count((2, 3)))
t0 = time.time()
nc30 = nextclosure_count((4, 2, 3))
oc30 = ownbox_count((4, 2, 3))
report("C3", "EXHAUSTIVE", "4x2x3 box (Lambda_chem): closed subsets by next-closure",
       nc30 > 0, "fixed-box %d, own-box %d of 2^24 (%.1fs)" % (nc30, oc30, time.time() - t0))
t0 = time.time()
tot24b, fx24b, own24b = brute_counts_numpy((4, 2, 3))
report("C3b", "EXHAUSTIVE", "4x2x3 box: every one of 2^24 subsets visited; counts agree with next-closure",
       fx24b == nc30 and own24b == oc30, "fixed-box %d, own-box %d (%.1fs)" % (fx24b, own24b, time.time() - t0))
nc32 = nextclosure_count((2, 4, 4))
report("C4", "EXHAUSTIVE", "2x4x4 box (Lambda_amp): closed subsets by next-closure", nc32 > 0,
       "fixed-box %d" % nc32)
RESULTS.update(fx24=fx24, own24=own24, nc30=nc30, oc30=oc30, nc32=nc32)


# ------------------------------------------------------------------ Z3: the closure family
def staircase_closed(X, S, cells, d, shape):
    """Every monotone staircase system that realises every value is closed under R.
    f_ij : chain j -> {-1, ..., |A_i|-1} monotone; X := {x : x_i <= f_ij(x_j) for all i != j}."""
    f = {}
    cons = []
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            for a in range(shape[j]):
                v = z3.Int("f_%d_%d_%d" % (i, j, a))
                f[(i, j, a)] = v
                cons += [v >= -1, v <= shape[i] - 1]
                if a > 0:
                    cons.append(f[(i, j, a - 1)] <= v)
    defX = [X[x] == z3.And([x[i] <= f[(i, j, x[j])] for i in range(d) for j in range(d) if i != j])
            for x in cells]
    hyp = z3.And(cons + defX + [pv.observed(X, cells, shape)])
    return z3.Implies(hyp, z3.And([pv.in_R(X, x, cells, d) == X[x] for x in cells]))


def staircase_hyp(X, S, cells, d, shape):
    f = {}
    cons = []
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            for a in range(shape[j]):
                v = z3.Int("f_%d_%d_%d" % (i, j, a))
                f[(i, j, a)] = v
                cons += [v >= -1, v <= shape[i] - 1]
                if a > 0:
                    cons.append(f[(i, j, a - 1)] <= v)
    defX = [X[x] == z3.And([x[i] <= f[(i, j, x[j])] for i in range(d) for j in range(d) if i != j])
            for x in cells]
    return z3.And(cons + defX + [pv.observed(X, cells, shape)])


def strictly_inside(X, S, cells, d, shape):
    return z3.Or([z3.Not(X[c]) for c in cells])


def idempotent(X, S, cells, d, shape):
    """observed X  =>  R(R(X)) = R(X), with S := R(X)."""
    hyp = z3.And(pv.observed(X, cells, shape), z3.And([S[c] == pv.in_R(X, c, cells, d) for c in cells]))
    return z3.Implies(hyp, z3.And([pv.in_R(S, c, cells, d) == S[c] for c in cells]))


def extensive_monotone(X, S, cells, d, shape):
    """X subset R(X); and X subset S implies R(X) subset R(S)."""
    ext = z3.And([z3.Implies(X[c], pv.in_R(X, c, cells, d)) for c in cells])
    mono = z3.Implies(pv.contains(X, S, cells),
                      z3.And([z3.Implies(pv.in_R(X, c, cells, d), pv.in_R(S, c, cells, d)) for c in cells]))
    return z3.And(ext, mono)


header("D. Machine checks (Z3 %s), guards first" % z3.get_version_string())
BOXES = [(4, 2, 3), (4, 5), (4, 6), (2, 4, 4)]


def ref_R_fixed(X, box, d):
    return {x for x in itertools.product(*box)
            if all(any(y[j] <= x[j] and y[i] >= x[i] for y in X) for i in range(d) for j in range(d) if i != j)}


def ref_R_wrong(X, box, d):
    """the deliberately wrong reference for the negative control: drops one pair direction."""
    return {x for x in itertools.product(*box)
            if all(any(y[j] <= x[j] and y[i] >= x[i] for y in X) for i in range(d) for j in range(d) if i < j)}


tot, bad = pv.encoding_matches(ref_R_fixed, BOXES, trials=300, seed=5)
report("G3", "GUARD", "in_R (witness form) == independent staircase on 300 random instances",
       bad == 0, "%d cells compared, %d disagree" % (tot, bad))
tot, badw = pv.encoding_matches(ref_R_wrong, BOXES, trials=300, seed=5)
report("G4", "GUARD", "negative control: the guard CATCHES a deliberately wrong reference",
       badw > 0, "%d disagreements" % badw)
for shape in BOXES:
    nv = pv.non_vacuous(shape, staircase_hyp, strictly_inside)
    report("G5", "GUARD", "non-vacuity: a staircase system strictly inside %s exists" % (shape,), nv)
    nv2 = pv.non_vacuous(shape, lambda X, S, c, d, sh: pv.observed(X, c, sh), strictly_inside)
    report("G6", "GUARD", "non-vacuity: an observed X strictly inside %s exists" % (shape,), nv2)
for shape in BOXES:
    ok = pv.prove("staircase systems are closed %s" % (shape,), shape, staircase_closed, quiet=True)
    report("D1", "MACHINE-CHECKED", "every monotone staircase system over %s is closed (all 2^%d X)" %
           (shape, len(pv.cells_of(shape))), ok)
for shape in BOXES:
    ok = pv.prove("closure operator %s" % (shape,), shape, extensive_monotone, quiet=True)
    ok2 = pv.prove("idempotent %s" % (shape,), shape, idempotent, quiet=True)
    report("D2", "MACHINE-CHECKED", "R is extensive, monotone and idempotent over %s" % (shape,), ok and ok2)

# ================================================================== E. the boundary
header("E. The boundary: E climbs as foreign seats are added (min over every ordering)")
SEATSETS = [("subvalence + valence", {SUB, VAL}), ("+ the core", {SUB, VAL, CORE}),
            ("+ the nucleus", {SUB, VAL, CORE, NUC}), ("+ the aggregate", {SUB, VAL, CORE, AGG}),
            ("all five", {SUB, VAL, CORE, NUC, AGG})]
BOUND = []
for label, seats in SEATSETS:
    row = {"label": label}
    for tag, table in (("filled", T42_FILLED), ("held", T42)):
        cs = cells_of(table, seats)
        ns = len(seats)
        t0 = time.time()
        mE_b, nvis_b, nmin_b, nclose_b, mins_b, dsets_b, sizes_b = sweep(cs)
        row[tag] = (len(cs), mE_b, nvis_b, nclose_b, dsets_b, sizes_b)
        print("      %-22s %-6s %2d cells  box %s  min E = %2d  over %6d orderings  (%.1fs)" %
              (label, tag, len(cs), "x".join(map(str, sizes_b)), mE_b, nvis_b, time.time() - t0))
    BOUND.append(row)
printed = [(14, 0), (15, 3), (20, 8), (21, 11), (26, 19)]
got_mixed = [(BOUND[0]["filled"][0], BOUND[0]["filled"][1])] + [(r["held"][0], r["held"][1]) for r in BOUND[1:]]
got_filled = [(r["filled"][0], r["filled"][1]) for r in BOUND]
got_held = [(r["held"][0], r["held"][1]) for r in BOUND]
report("E1", "EXHAUSTIVE", "printed sequence 14/0, 15/3, 20/8, 21/11, 26/19 = filled first row + held rows",
       got_mixed == printed, str(got_mixed))
report("E2", "EXHAUSTIVE", "held table (term symbol -> P): 13/1, 15/3, 20/8, 21/11, 26/19",
       got_held == [(13, 1), (15, 3), (20, 8), (21, 11), (26, 19)], str(got_held))
mono = all(got_filled[i][1] < got_filled[i + 1][1] for i in range(4))
report("E3", "EXHAUSTIVE", "filled table: E climbs strictly with every foreign seat added", mono, str(got_filled))
RESULTS.update(BOUND=BOUND, got_filled=got_filled, got_held=got_held)

# ================================================================== F. the last cell
header("F. The last cell before the fill (thirteen cells, term symbol on P)")
mE0, nvis0, nmin0, nclose0, mins0, dsets0, sizes0 = sweep(SV0)
report("F1", "EXHAUSTIVE", "all 288 orderings (1,440 with the unrealised kind) give min E = 1 and none reaches 0",
       mE0 == 1 and nclose0 == 0 and nvis0 == 288, "min E=%d, %d minimising" % (mE0, nmin0))
SV0c, SV0_alph = recode(SV0)
cellA = (SV0_alph[0].index(1), SV0_alph[1].index(VAL), 1)   # (symmetry, the valence shell, C)
cellB = (SV0_alph[0].index(1), SV0_alph[1].index(SUB), 2)   # (symmetry, the subvalence shell, A)
report("F2", "EXHAUSTIVE", "every minimising ordering has a single defect cell, and it is one of two",
       dsets0 == {frozenset({cellA}), frozenset({cellB})},
       "(symmetry, valence, C) or (symmetry, subvalence, A): %s" % str([sorted(x) for x in dsets0]))
# how many minimising orderings give each (full sweep, no symmetry halving)
nA = nB = 0
for perms in itertools.product(itertools.permutations(range(4)), itertools.permutations(range(2)),
                               itertools.permutations(range(3))):
    cs = relabel(SV0c, perms)
    E1, R1, ix1 = E_cypher(cs, NAMES3, [list(range(4)), [0, 1], list(range(3))])
    if E1 == 1:
        inv = [{perms[i][v]: v for v in range(len(perms[i]))} for i in range(3)]
        x = next(iter(set(R1) - set(cs)))
        cell = tuple(inv[i][x[i]] for i in range(3))
        nA += cell == cellA
        nB += cell == cellB
report("F2b", "EXHAUSTIVE", "of the minimising orderings, how many put the defect at each cell",
       nA + nB == nmin0 and nA > 0 and nB > 0, "(symmetry, valence, C): %d; (symmetry, subvalence, A): %d" % (nA, nB))
altSV = sorted(set(SV0) | {(1, SUB, 2)})
mE_alt, nv_alt, nm_alt, nc_alt, _, _, _ = sweep(altSV)
report("F2c", "EXHAUSTIVE", "the alternative fill (symmetry, subvalence, A) would also close at fourteen cells",
       mE_alt == 0 and len(altSV) == 14, "%d of %d orderings close" % (nc_alt, nv_alt))
RESULTS.update(nA=nA, nB=nB, nc_alt=nc_alt)
four = [n for n, k, s, p in T42 if k == 1 and s == VAL]
report("F3", "EXHAUSTIVE", "four symmetry-of-valence properties held, all on P or A before the fill",
       len(four) == 4 and all(p != 1 for n, k, s, p in T42 if k == 1 and s == VAL), ", ".join(four))
# the ground-term table is CITED (NIST ASD); the one decidable statement about it:
TERMS = {20: ["1S0", "3D1", "3F2", "3F2"], 38: ["1S0", "3D1", "3F2", "3F2"],
         56: ["1S0", "3F2", "3H4"], 88: ["1S0", "1S0", "3H4o"]}
report("F4", "CITED", "ground terms of the Ne = 20 and Ne = 38 sequences are identical (NIST ASD values)",
       TERMS[20] == TERMS[38])
changes = {ne: len(set(t)) > 1 for ne, t in TERMS.items()}
report("F5", "CITED", "the ground term changes with charge in every sequence but none is constant",
       all(changes.values()), str(changes))
RESULTS.update(mins0=mins0, four=four, nmin0=nmin0)

# ================================================================== G. routing by residual
header("G. Routing by residual")
props = {n: (k, s, p) for n, k, s, p in T42_FILLED}
breadth = {n: b for n, _, _, b in T42_BREADTH}
cls11 = {}
for prop, supplies, cls, meas in CHEM11:
    cls11.setdefault(prop, set()).add(cls)
ROUTE = []
okall = True
for res, prop, cls, why in ROUTING:
    k, s, p = props[prop]
    okrow = (s in (SUB, VAL)) and (cls in cls11.get(prop, set()))
    okall &= okrow
    ROUTE.append((res, prop, KIND[k], SEAT[s], PCA[p], BREADTH[breadth[prop]], cls))
    print("      %-30s -> %-22s (%s, %s, %s)  breadth: %s  class: %s" % (res, prop, KIND[k], SEAT[s], PCA[p],
                                                                         BREADTH[breadth[prop]], cls))
report("G7", "EXHAUSTIVE", "four residuals route to a property in the closed seats with its recorded class",
       okall and len(ROUTING) == 4)
RESULTS["ROUTE"] = ROUTE

# ================================================================== H. Lambda_PCA
header("H. Lambda_PCA: physics (+) charge (+) amplitude on (source, domain == regime)")
P22 = load_literal(INSTR["phys_close"], "P")      # (name, source, domain, arity, real?)
SRC = ["mathematics", "standard", "literature", "this work"]
DOM4 = ["universal", "all elements", "a region", "one species"]
P21 = [p for p in P22 if p[4]]
excluded = [p[0] for p in P22 if not p[4]]
report("H1", "EXHAUSTIVE", "22 listed, one excluded as a property of the method, 21 parameters of real atoms",
       len(P22) == 22 and len(P21) == 21 and excluded == ["5σ threshold"], ", ".join(excluded))
ph_cells = sorted({(s, d) for _, s, d, _, _ in P21})
src_order = [SRC.index(x) for x in ["standard", "mathematics", "literature", "this work"]]
dom_present = sorted({d for _, d in ph_cells})
E_ph, R_ph, ix_ph = E_cypher(ph_cells, ["source", "domain"], [src_order, dom_present])
report("H2", "EXHAUSTIVE", "Lambda_phys on (source, domain): 7 cells, E = 0, box %d" % ix_ph.box,
       len(ph_cells) == 7 and E_ph == 0 and ix_ph.box == 12)
mEp, nvp, nmp, ncp, _, _, _ = sweep(ph_cells)
report("H3", "EXHAUSTIVE", "Lambda_phys: closing orderings among all 4! x 3! = 144", mEp == 0,
       "%d of %d close" % (ncp, nvp))
ph3 = sorted({(s, d, a) for _, s, d, a, _ in P21})
mE3, nv3, nm3, nc3, _, _, _ = sweep(ph3)
report("H4", "EXHAUSTIVE", "with arity as a third axis: 12 cells, min E = 7 over all orderings",
       len(ph3) == 12 and mE3 == 7, "min E=%d over %d" % (mE3, nv3))

CH = load_literal(INSTR["charge_index"], "CH")   # (occurrence, role, carrier, sign, regime)
ROLE = ["screening", "decay base", "decay rate", "ordering"]
CARR = ["u", "c itself", "Ne", "the configuration"]
SIGN = ["lowers", "raises"]
REG = ["neutral", "low", "hydrogenic"]
ch_cells = sorted({(ROLE.index(r), CARR.index(c), SIGN.index(s), REG.index(g)) for _, r, c, s, g in CH})
E_ch, _, ix_ch = E_cypher(ch_cells, ["role", "carrier", "sign", "regime"],
                          [list(range(4)), list(range(4)), [0, 1], [0, 1, 2]])
report("H5", "EXHAUSTIVE", "Lambda_charge: nine occurrences, nine distinct cells, E = 0 under the declared order",
       len(CH) == 9 and len(ch_cells) == 9 and E_ch == 0, "box %d" % ix_ch.box)
by_reg = [sum(1 for _, r, c, s, g in CH if g == x) for x in REG]
report("H6", "EXHAUSTIVE", "occurrences by regime neutral/low/hydrogenic = 2/3/4", by_reg == [2, 3, 4], str(by_reg))

PH = load_literal(INSTR["dom_reg"], "PH")   # (source, merged domain) for the 21
CHm = load_literal(INSTR["dom_reg"], "CH")  # (source, merged domain) for the 9
D6 = ["universal", "all elements", "neutral", "low", "hydrogenic", "one species"]  # the instrument's coding
# reconcile with phys_close: source codes must agree; domains agree under 'a region' -> 'low' except where noted
agree_src = all(a == b for (a, _), (_, b, *_) in zip(PH, P21))
map_dom = {0: 0, 1: 1, 2: 3, 3: 5}
dom_diff = [(P21[i][0], DOM4[P21[i][2]], D6[PH[i][1]]) for i in range(21) if map_dom[P21[i][2]] != PH[i][1]]
report("H7", "EXHAUSTIVE", "merge table vs parameter table: sources agree on 21/21; domains on 20/21",
       agree_src and len(dom_diff) == 1, "differs: %s" % dom_diff)
RESULTS["dom_diff"] = dom_diff
pca_cells = sorted(set(PH) | set(CHm))
DOM6 = ["universal", "all elements", "low", "neutral", "hydrogenic", "one species"]  # the closing order
d_order = [D6.index(x) for x in DOM6]
E_pca, R_pca, ix_pca = E_cypher(pca_cells, ["source", "domain"], [src_order, d_order])
report("H8", "EXHAUSTIVE", "Lambda_PCA: 9 cells, E = 0 under source standard<math<lit<this work, domain univ<all<low<neutral<hydro; box 20 ('one species' unrealised)",
       len(pca_cells) == 9 and E_pca == 0 and ix_pca.box == 20, "box %d" % ix_pca.box)
mult = {}
for s, d in list(PH) + list(CHm):
    mult[(s, d)] = mult.get((s, d), 0) + 1
table = [[mult.get((SRC.index(sname), D6.index(dname)), 0) for dname in DOM6] for sname in ["standard", "mathematics", "literature", "this work"]]
printed_pca = [[5, 0, 0, 0, 0, 0], [3, 1, 0, 0, 0, 0], [0, 7, 1, 0, 0, 0], [0, 2, 5, 2, 4, 0]]
report("H9", "EXHAUSTIVE", "the multiplicity table 5 / 3,1 / 7,1 / 2,5,2,4 (30 = 21 + 9)", table == printed_pca and sum(map(sum, table)) == 30,
       str(table))
RESULTS["pca_table"] = table
RESULTS["pca_names"] = {}
for (s, d), (name, *_) in zip(PH, P21):
    RESULTS["pca_names"].setdefault((s, d), []).append(name)
for (s, d), (occ, *_) in zip(CHm, CH):
    RESULTS["pca_names"].setdefault((s, d), []).append("charge: " + occ)
# every closing ordering, and where low sits relative to neutral in each
t0 = time.time()
mEm, nvm, nmm, ncm, minsm, _, sizes_m = sweep(pca_cells, use_symmetry=False)
low_before_neutral = 0
univ_first = 0
for perms in minsm:
    ps, pd = perms
    # orient so that 'universal' precedes 'one species' ... the domain axis carries five realised values
    # (one species is absent) so orient by universal (code 0) before hydrogenic (code 4)
    if pd[0] < pd[4]:
        univ_first += 1
        if pd[3] < pd[2]:   # low (code 3) before neutral (code 2)
            low_before_neutral += 1
report("H10", "EXHAUSTIVE", "closing orderings among 4! x 5! = 2,880 (17,280 with the unrealised value); in every one oriented universal-first, low precedes neutral",
       mEm == 0 and nvm == 2880 and low_before_neutral == univ_first and univ_first > 0,
       "%d close; %d universal-first, %d with low < neutral (%.1fs)" % (ncm, univ_first, low_before_neutral, time.time() - t0))
SRC_ORDERED = ["standard", "mathematics", "literature", "this work"]
for perms in minsm:
    ps, pd = perms
    if pd[0] < pd[4]:
        so = [SRC[v] for v in sorted(range(4), key=lambda v: ps[v])]
        do = [D6[v] for v in sorted(range(5), key=lambda v: pd[v])]
        RESULTS.setdefault("pca_orders", []).append((so, do))
        print("      closing order: source %s; domain %s" % (" < ".join(so), " < ".join(do)))
report("H10b", "EXHAUSTIVE", "both universal-first closing orders read standard < mathematics < literature < this work",
       all(so == ["standard", "mathematics", "literature", "this work"] for so, _ in RESULTS["pca_orders"]))
RESULTS.update(ncm=ncm, univ_first=univ_first)
# in every closing ordering, is 'one species' (unrealised) free? the realised domain alphabet has 5 values
# the floor form
L = lambda s: s // 2
U = lambda s: s + s // 3
floor_cells = {(s, d) for s in range(4) for d in range(6) if L(s) <= d <= U(s)}
coded_pca = {(src_order.index(s), d_order.index(d)) for s, d in pca_cells}
report("H11", "EXHAUSTIVE", "L(s) = floor(s/2) <= d <= U(s) = s + floor(s/3) on 4 x 6 gives exactly the nine cells",
       floor_cells == coded_pca, "%d cells" % len(floor_cells))
# the amplitude index adds no cell to the merge (three_merge.py's reading)
amp_as_pc = {(SRC.index("mathematics"), D6.index("universal")), (SRC.index("mathematics"), D6.index("all elements"))}
report("H12", "EXHAUSTIVE", "Lambda_amp read on (source, domain) is two cells already in the merge",
       amp_as_pc <= set(pca_cells))
# the recorded correction: the merge on axis NAMES
PHn = load_literal(INSTR["merge"], "PH")
CHn = load_literal(INSTR["merge"], "CH")
mE_n1, nv_n1, *_ = sweep(sorted(set(PHn)))
Mn = set()
for r, c, s, g in CHn:
    Mn.add((r, g, c))
for k, d, a in PHn:
    Mn.add((min(k, 3), d, min(a, 3)))
mE_n2, nv_n2, *_ = sweep(sorted(Mn))
report("H13", "EXHAUSTIVE", "the name-merge: the earlier Lambda_phys has E = 6 (13 cells) and the merge E = 11 (18 cells)",
       mE_n1 == 6 and len(set(PHn)) == 13 and mE_n2 == 11 and len(Mn) == 18,
       "E=%d over %d; merged E=%d over %d" % (mE_n1, nv_n1, mE_n2, nv_n2))

# ================================================================== I. Lambda_amp
header("I. Lambda_amp: the Slater integrals of the diagonal pairs")


def slater_list(l1, l2):
    """The direct and exchange ranks that exist for a subshell pair: F^k, k even, 0..2min(l,l');
    G^k, k = |l-l'|, |l-l'|+2, ..., l+l'.  Slater 1929, Condon & Shortley 1935."""
    F = list(range(0, 2 * min(l1, l2) + 1, 2))
    G = list(range(abs(l1 - l2), l1 + l2 + 1, 2))
    return F, G


tri = sorted({(kind, l, k // 2) for l in range(4) for kind, ks in enumerate(slater_list(l, l)) for k in ks})
E_amp, _, ix_amp = E_cypher(tri, ["kind", "l", "i"], [[0, 1], list(range(4)), list(range(4))])
report("I1", "EXHAUSTIVE", "the diagonal pairs l/l, l = s..f, on (kind, l, position i): 20 cells, E = 0, box 32",
       len(tri) == 20 and E_amp == 0 and ix_amp.box == 32)
report("I2", "EXHAUSTIVE", "the twenty cells are exactly {(kind, l, i) : 0 <= i <= l}",
       set(tri) == {(kd, l, i) for kd in (0, 1) for l in range(4) for i in range(l + 1)})
mEa, nva, nma, nca, _, _, _ = sweep(tri)
report("I3", "EXHAUSTIVE", "closing orderings among 2! x 4! x 4! = 1,152", mEa == 0, "%d of %d close" % (nca, nva))
PAIRS = load_literal(INSTR["amp_index"], "PAIRS")
raw = set()
for nm, l1, l2, ne in PAIRS:
    F, G = slater_list(l1, l2)
    raw |= {(k, 0, l2) for k in F} | {(k, 1, l2) for k in G}
for l in range(4):
    F, G = slater_list(l, l)
    raw |= {(k, 0, l) for k in F} | {(k, 1, l) for k in G}
ks = sorted({c[0] for c in raw})
raw_coded = sorted({(ks.index(a), b, c) for a, b, c in raw})
mEr, nvr, nmr, ncr, minsr, dsr, _ = sweep(raw_coded)
defect_raw = {tuple((ks[x[0]], ["F", "G"][x[1]], "spdf"[x[2]]) for x in sorted(s)) for s in dsr}
report("I4", "EXHAUSTIVE", "indexed on the raw rank k: 21 cells, min E = 1 over all %d orderings, one defect cell" % nvr,
       len(raw_coded) == 21 and mEr == 1 and len(defect_raw) == 1 and all(len(x) == 1 for x in defect_raw),
       "defect: %s (the source prints F^1 at p; see SOURCES)" % str(sorted(defect_raw)))
report("I4b", "EXHAUSTIVE", "the reproduced defect cell is G^1 at an s rival, a rank parity forbids there too",
       defect_raw == {((1, "G", "s"),)}, "%d of %d orderings minimise" % (nmr, nvr))
s_s = slater_list(0, 0)
f_f = slater_list(3, 3)
report("I5", "EXHAUSTIVE", "s/s has F0 and G0 only (one independent radial quantity); f/f has four F and four G",
       s_s == ([0], [0]) and len(f_f[0]) == 4 and len(f_f[1]) == 4)


def threej_sq(j1, j2, j3, m1, m2, m3):
    """(j1 j2 j3; m1 m2 m3)^2 exactly, by Racah's formula, as a Fraction."""
    from math import factorial as fac
    if m1 + m2 + m3 != 0 or not (abs(j1 - j2) <= j3 <= j1 + j2):
        return Fraction(0)
    delta = Fraction(fac(j1 + j2 - j3) * fac(j1 - j2 + j3) * fac(-j1 + j2 + j3), fac(j1 + j2 + j3 + 1))
    pref = fac(j1 + m1) * fac(j1 - m1) * fac(j2 + m2) * fac(j2 - m2) * fac(j3 + m3) * fac(j3 - m3)
    s = Fraction(0)
    for k in range(0, j1 + j2 + j3 + 2):
        args = [k, j1 + j2 - j3 - k, j1 - m1 - k, j2 + m2 - k, j3 - j2 + m1 + k, j3 - j1 - m2 + k]
        if min(args) < 0:
            continue
        den = 1
        for a in args:
            den *= fac(a)
        s += Fraction((-1) ** k, den)
    return delta * pref * s * s


ok = all(threej_sq(l, 0, l, 0, 0, 0) == Fraction(1, 2 * l + 1) for l in range(0, 9))
report("I6", "EXHAUSTIVE", "(l 0 l; 0 0 0)^2 = 1/(2l+1) exactly (Fraction), l = 0..8", ok)
# an independent identity check of the 3j implementation: orthogonality sum_m (j j 0; m -m 0)^2 = 1/(2j+1)... and
# the parity zero (l 1 l; 0 0 0) = 0
ok2 = all(threej_sq(l, 1, l, 0, 0, 0) == 0 for l in range(1, 6)) and threej_sq(1, 1, 2, 0, 0, 0) == Fraction(2, 15)
report("I7", "EXHAUSTIVE", "3j implementation: (l 1 l; 0 0 0) = 0 by parity, (1 1 2; 0 0 0)^2 = 2/15", ok2)

# ================================================================== J. the reversal symmetry (Lemma 3)
header("J. Lemma 3: E is invariant under reversing every axis at once")
rnd = random.Random(3)
bad = 0
for _ in range(200):
    shape = rnd.choice([(4, 2, 3), (4, 6), (3, 3, 3)])
    allc = list(itertools.product(*[range(n) for n in shape]))
    X = rnd.sample(allc, rnd.randint(2, 10))
    d = len(shape)
    Xr = [tuple(shape[i] - 1 - x[i] for i in range(d)) for x in X]
    if len(ref_R(X, d)) != len(ref_R(Xr, d)):
        bad += 1
report("J1", "SAMPLED", "|R(X)| = |R(reversed X)| on 200 random subsets (seed 3)", bad == 0, "%d failures" % bad)
# and exhaustively on the 1,440 orderings of the fourteen cells: the halved sweep equals the full sweep
mE_full, nv_full, nm_full, nc_full, _, _, _ = sweep(SV, use_symmetry=False)
report("J2", "EXHAUSTIVE", "the halved sweep reproduces the full sweep on the fourteen cells",
       (mE_full, nv_full, nc_full) == (mE, nvis, nclose), "%d close of %d" % (nc_full, nv_full))

# ================================================================== negative controls
if SELFTEST:
    header("SELFTEST: negative controls")
    # a deliberately false claim: the thirteen cells before the fill close.  Must be refuted.
    E13, _, _ = E_cypher(relabel(SV0c, canon), NAMES3, [list(range(4)), [0, 1], list(range(3))])
    refuted = E13 != 0
    report("N1", "GUARD", "negative control: 'the thirteen cells close at E = 0' is REFUTED", refuted, "E = %d" % E13)
    # a deliberately false z3 claim: every OBSERVED subset is closed.  Must be sat (counterexample).
    false_claim = lambda X, S, c, d, sh: z3.Implies(pv.observed(X, c, sh), z3.And([pv.in_R(X, x, c, d) == X[x] for x in c]))
    ok_false = pv.prove("false: every observed X is closed (3x3)", (3, 3), false_claim, quiet=True)
    report("N2", "GUARD", "negative control: 'every observed subset is closed' is REFUTED by Z3", not ok_false)
    # the wrong reference is caught (already G4); a wrong floor form must fail
    Lw = lambda s: s // 2
    Uw = lambda s: s + s // 2
    wrong = {(s, d) for s in range(4) for d in range(6) if Lw(s) <= d <= Uw(s)}
    report("N3", "GUARD", "negative control: U(s) = s + floor(s/2) does NOT give the nine cells", wrong != coded_pca)

# ================================================================== summary
print()
print("summary: " + ", ".join("%s %d" % (k, v) for k, v in COUNT.items() if v))
if FAILS:
    print("FAILED: %d" % len(FAILS))
    for f in FAILS:
        print("  ", f)
    sys.exit(1)
print("all obligations discharged")

if True:
    import json
    dump = {k: v for k, v in RESULTS.items() if k in ("byk", "bys", "byp", "byp_f", "ORD_K", "ORD_S", "ORD_P",
                                                     "nclose_sv", "fx24", "own24", "nc30", "oc30", "nc32",
                                                     "got_filled", "got_held", "n_closed_sub14", "ncm", "univ_first", "fx20", "own20", "nA", "nB", "nc_alt",
                                                     "pca_table", "ROUTE", "dom_diff", "nmin0", "four", "pca_orders", "chem_orders")}
    dump["grid"] = {"%d,%d,%d" % k: v for k, v in RESULTS["grid"].items()}
    dump["closed_sizes14"] = RESULTS["closed_sizes14"]
    dump["pca_names"] = {"%d,%d" % k: v for k, v in RESULTS["pca_names"].items()}
    json.dump(dump, open(os.path.join(HERE, "figures", "check-results.json"), "w"), indent=1, ensure_ascii=False)
    print("results dumped to figures/check-results.json")
