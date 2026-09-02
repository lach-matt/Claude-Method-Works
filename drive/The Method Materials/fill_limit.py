#!/usr/bin/env python3
"""fill_limit.py — the tower fill-limit: what morphism-admissibility alone decides, computed.

Answers REQUEST-to-method-project-FILL-LIMIT.md (book-build chat 61, MC-33) against
§12.11.0.11 / R 333.  Admissibility is taken as the corpus states it (A.morph, §18.4.1):
a new coordinate t with range [lo(x), hi(x)] on cell x is admissible iff lo and hi are
lattice morphisms of the stage below, which makes the new stage a sublattice of its box
(E = 0).  Three continuations of Λ13 are built from the tower's OWN axis-types:

  P  repeated projection cap      t_i ∈ [0, g]              (the 2S' ≤ g type, iterated)
  Q  descending chain             t_1 ∈ [0, g], t_i ∈ [0, t_{i-1}]   (the v ≥ 2S' type, iterated)
  T  translated cap, growing      t_i ∈ [0, g + M_i], M_i = M0·2^(i-1)  (the 2K ≤ 2Jc + 2f_max type)

Route 1: closed form over the g-distribution of Λ13 (multiplicities depend on g only).
Route 2: direct enumeration of cells at small depth, and the exhaustive closure test
         E(X) = |R(X)| − |X| against every cell of the ambient box (the §14.1 test), run
         first on the tower itself (must reproduce R 249: E = 0) and then on the continuations.

Zeno: every segment is bounded and closed before the next opens; results go to a file and
are reported by shape (§H.11).
"""
import sys, math, itertools, importlib.util, time
from collections import Counter
import numpy as np

HERE = __import__('os').path.dirname(__import__('os').path.abspath(__file__))
spec = importlib.util.spec_from_file_location('tower_1', HERE + '/tower-1.py')
tower = importlib.util.module_from_spec(spec); spec.loader.exec_module(tower)

OUT = open(HERE + '/FILL-LIMIT-RESULTS.txt', 'w')
def emit(*a):
    s = ' '.join(str(x) for x in a); print(s); OUT.write(s + '\n'); OUT.flush()

G = 6   # index of coordinate g in every stage (n0 l1 k2 q3 e4 f5 g6 2S7 | ...)

# ------------------------------------------------------------------ closure test (§14.1)
def box_of(X):
    return [sorted(set(c[i] for c in X)) for i in range(len(X[0]))]

def E_of(X, max_box=4_000_000):
    """E(X) = |R(X)| − |X|, R(X) = cells of the ambient box all of whose 2-projections are
    realised in X (Bergman / Baker–Pixley: a sublattice of a product of chains is determined
    by its two-fold projections).  Exhaustive over the box; refuses above max_box."""
    A = box_of(X); d = len(A)
    boxsize = math.prod(len(a) for a in A)
    if boxsize > max_box:
        return None, boxsize
    idx = [{v: k for k, v in enumerate(a)} for a in A]
    Xi = np.array([[idx[i][c[i]] for i in range(d)] for c in X], dtype=np.int16)
    grids = np.indices([len(a) for a in A]).reshape(d, -1).astype(np.int16)   # d × box
    mask = np.ones(boxsize, dtype=bool)
    for i in range(d):
        for j in range(i + 1, d):
            T = np.zeros((len(A[i]), len(A[j])), dtype=bool)
            T[Xi[:, i], Xi[:, j]] = True
            mask &= T[grids[i], grids[j]]
    return int(mask.sum()) - len(X), boxsize

def sublattice(X):
    """Direct test: closed under componentwise max and min over all pairs (|X| ≤ ~4000)."""
    S = set(X); Xa = np.array(X, dtype=np.int16); n = len(X)
    if n > 4000: return None
    for a in range(n):
        J = np.maximum(Xa[a], Xa[a:]); M = np.minimum(Xa[a], Xa[a:])
        for row in itertools.chain(map(tuple, J), map(tuple, M)):
            if row not in S: return False
    return True

# ------------------------------------------------------------------ continuations
def cont_P(X, m):   # t_i ∈ [0, g]
    for _ in range(m):
        X = [c + (t,) for c in X for t in range(0, c[G] + 1)]
    return X
def cont_Q(X, m):   # t_1 ∈ [0, g], t_i ∈ [0, t_{i-1}]
    for i in range(m):
        cap = G if i == 0 else len(X[0]) - 1
        X = [c + (t,) for c in X for t in range(0, c[cap] + 1)]
    return X
def cont_T(X, m, M0):   # t_i ∈ [0, g + M_i], M_i = M0·2^(i-1)
    for i in range(m):
        Mi = M0 * 2 ** i
        X = [c + (t,) for c in X for t in range(0, c[G] + Mi + 1)]
    return X

def fill_of(X):
    return len(X) / math.prod(len(a) for a in box_of(X))

# ================================================================== SEGMENT 1 — the tower
t0 = time.time()
emit('SEGMENT 1 — tower rebuild from tower-1.py (§12.11.1 axis definitions)')
emit(' D      cells          box      fill%    ratio')
stages = {}; prev = None
for D in range(8, 14):
    X = tower.STAGES[D](); stages[D] = X
    b = math.prod(len(a) for a in box_of(X)); f = len(X) / b
    emit(f'{D:2d} {len(X):10,d} {b:14,d} {100*f:8.4f}  {"" if prev is None else f"{f/prev:.4f}"}')
    prev = f
L13 = stages[13]; box13 = math.prod(len(a) for a in box_of(L13)); fill13 = len(L13) / box13
gdist = Counter(c[G] for c in L13)
emit('g-distribution over Λ13 (cells by g = 0..3):', [gdist[g] for g in range(4)],
     ' sum =', sum(gdist.values()))
emit('closure of the tower (must reproduce R 249, E = 0):')
for D in range(8, 12):
    E, b = E_of(stages[D]); emit(f'  Λ{D}: E = {E}  (box {b:,}; sublattice = {sublattice(stages[D])})')
emit(f'segment 1 closed ({time.time()-t0:.1f}s)')

# ================================================================== SEGMENT 2 — closed forms
t0 = time.time()
emit('\nSEGMENT 2 — closed-form limits over the g-distribution of Λ13')
c = [gdist[g] for g in range(4)]
def P_cells(m): return sum(c[g] * (g + 1) ** m for g in range(4))
def Q_cells(m): return sum(c[g] * math.comb(g + m, m) for g in range(4))
def T_cells(m, M0): return sum(c[g] * math.prod(g + M0 * 2 ** i + 1 for i in range(m)) for g in range(4))
def T_box(m, M0): return box13 * math.prod(M0 * 2 ** i + 4 for i in range(m))

emit(' m   P: ratio      fill%        Q: ratio      fill%')
for m in list(range(1, 13)) + [20, 40, 80]:
    Pr = P_cells(m) / (4 * P_cells(m - 1)); Pf = P_cells(m) / (box13 * 4 ** m)
    Qr = Q_cells(m) / (4 * Q_cells(m - 1)); Qf = Q_cells(m) / (box13 * 4 ** m)
    emit(f'{m:3d}   {Pr:.6f}  {100*Pf:.6f}%    {Qr:.6f}  {100*Qf:.3e}%')
LP = c[3] / box13
emit(f'P: L = c3/box13 = {c[3]:,}/{box13:,} = {100*LP:.6f}%  (positive; ratio → 1, Σ(1−ratio) < ∞)')
emit(f'Q: L = 0 (cells grow as a cubic in m, box as 4^m; ratio → 1/4, Σ(1−ratio) = ∞)')
emit(' T: M0     L_T/fill13 (product to convergence)   L_T%')
for M0 in (4, 16, 64, 256, 1024):
    prod = 1.0; m = 0
    while True:
        m += 1; Mi = M0 * 2 ** (m - 1)
        # weighted mean of g at this depth is bounded in [0,3]; use exact weights
        w = [c[g] * math.prod(g + M0 * 2 ** i + 1 for i in range(m - 1)) for g in range(4)]
        gbar = sum(g * w[g] for g in range(4)) / sum(w)
        r = (Mi + 1 + gbar) / (Mi + 4); prod *= r
        if 1 - r < 1e-12: break
    emit(f'    {M0:5d}   {prod:.8f}                          {100*fill13*prod:.6f}%   (lower bound 1−6/M0 = {1-6/M0:.6f})')
emit(f'fill13 = {100*fill13:.6f}%  — T approaches it from below as M0 → ∞; never attains it')
emit(f'segment 2 closed ({time.time()-t0:.1f}s)')

# ================================================================== SEGMENT 3 — direct route on Λ13
t0 = time.time()
emit('\nSEGMENT 3 — direct enumeration on Λ13 (route 2 against segment 2)')
def lazy_P(X, m):   # direct enumeration of the cells, counted without storing them
    return sum(1 for c in X for ts in itertools.product(range(c[G] + 1), repeat=m))
def lazy_Q(X, m):
    def walk(cap, k):
        return 1 if k == 0 else sum(walk(t, k - 1) for t in range(cap + 1))
    return sum(walk(c[G], m) for c in X)
def lazy_T(X, m, M0):
    return sum(1 for c in X for ts in itertools.product(*[range(c[G] + M0 * 2 ** i + 1) for i in range(m)]))
tmax = max(c[G] for c in L13)
for m in (1, 2):
    nP, nQ = lazy_P(L13, m), lazy_Q(L13, m)
    emit(f'  m={m}: P cells {nP:,} vs closed form {P_cells(m):,} ({nP==P_cells(m)})'
         f'  |  Q cells {nQ:,} vs {Q_cells(m):,} ({nQ==Q_cells(m)})'
         f'  | new axes realise {tmax+1} values each, box = box13·4^{m} = {box13*4**m:,}')
nT = lazy_T(L13, 1, 4)
emit(f'  T(M0=4), m=1: cells {nT:,} vs {T_cells(1,4):,} ({nT==T_cells(1,4)}); axis realises {tmax+4+1} values, box {T_box(1,4):,}')
emit(f'segment 3 closed ({time.time()-t0:.1f}s)')

# ================================================================== SEGMENT 4 — closure of the continuations
t0 = time.time()
emit('\nSEGMENT 4 — exhaustive closure test E = |R(X)| − |X| on the continuations (small depth)')
for base in (8, 9, 10, 11):
    for name, fn in (('P', lambda X, m: cont_P(X, m)), ('Q', lambda X, m: cont_Q(X, m)),
                     ('T4', lambda X, m: cont_T(X, m, 4))):
        for m in (1, 2, 3):
            X = fn(stages[base], m); E, b = E_of(X)
            if E is None:
                emit(f'  Λ{base}+{name}^{m}: box {b:,} above bound — not run (refused, §2.9)'); break
            sub = sublattice(X) if len(X) <= 4000 else '-'
            emit(f'  Λ{base}+{name}^{m}: cells {len(X):,} box {b:,} fill {100*len(X)/b:.4f}%  E = {E}  sublattice = {sub}')
emit(f'segment 4 closed ({time.time()-t0:.1f}s)')
OUT.close()
