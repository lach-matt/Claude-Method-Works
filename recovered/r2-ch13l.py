# r2-ch13l.py — Phase R2, chat 83. COMPUTABLE batch for the section read of Chapter 15
# (main L4270-L4331, "Self-reference — alphabet, order, bounds").
# Deterministic: no wall-clock, no unseeded randomness. Imports r2lib by path (chat 74 ruling 2).
import importlib.util, os, itertools, collections, random
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))
s = importlib.util.spec_from_file_location('r2lib', os.path.join(H, 'r2lib.py'))
r2lib = importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
T = r2lib.load_tower()

# lifted VERBATIM from r2-ch12r.py (chat 76) — the tower at arbitrary caps; owed to r2lib per DEFERRED
def L8_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    return [(n, l, k, q, e, f, g, S2) for n in range(1, n_max + 1) for l in range(0, min(l_max, n - 1) + 1) for k in range(1, min(k_max, 4 * l + 2) + 1)
            for q in range(0, k + 1) for e in range(1, e_max + 1) for f in range(0, min(f_max, e - 1) + 1) for g in range(0, min(4 * f + 2, q) + 1) for S2 in range(0, k + 1)]

NAMES8 = ['n', 'l', 'k', 'q', 'e', 'f', 'g', '2S']
L8 = [tuple(c) for c in T.L8()]; L9 = [tuple(c) for c in T.L9()]; L10 = [tuple(c) for c in T.L10()]
P = print

def alpha(X):
    d = len(X[0]); return [sorted({x[i] for x in X}) for i in range(d)]

# ---------------------------------------------------------------- 1. the alphabet, and the 56 functions
P('=== 1. S1 alphabets and the count of envelope functions (L4273, L4278, L4290) ===')
A8 = alpha(L8)
P('|L8| = %d   alphabets: %s' % (len(L8), ', '.join('%s:%d%s' % (NAMES8[i], len(a), a) for i, a in enumerate(A8))))
for X, tag in ((L8, 'L8'), (L9, 'L9'), (L10, 'L10')):
    d = len(X[0]); P('%-4s d = %2d  ordered pairs i != j  =  d(d-1) = %3d envelope functions phi_ij' % (tag, d, d * (d - 1)))
P('L4290 prints "56 functions" for L8: measured %d  -> %s' % (8 * 7, 'AGREES' if 8 * 7 == 56 else 'DIFFERS'))

# ---------------------------------------------------------------- 2. R(X) = X, and stability under a second application
P('')
P('=== 2. the envelope set determines the index: R(X) = X exactly (L4283, L4290, L4329) ===')
for X, tag in ((L8, 'L8'), (L9, 'L9'), (L10, 'L10')):
    S = set(X); R = r2lib.Rset(X); R2 = r2lib.Rset(sorted(R))
    box = 1
    for a in alpha(X): box *= len(a)
    P('%-4s cells %6d  ambient box %9d  |R(X)| %6d  E(X) = |R(X)|-|X| = %d  R(R(X))==R(X) %s  R(X)==X %s'
      % (tag, len(S), box, len(R), len(R) - len(S), R2 == R, R == S))

# ---------------------------------------------------------------- 3. the four cap settings, and the 216-cell one
P('')
P('=== 3. cap settings (L1786 names 216, 976, 1,636, 2,394; L4312-4313 names two of them) ===')
found = {}
for n_max in range(1, 5):
    for e_max in range(1, 5):
        for l_max in range(0, 3):
            for k_max in range(1, 5):
                for f_max in range(0, 3):
                    c = (n_max, e_max, l_max, k_max, f_max); v = len(L8_at(c))
                    if v in (216, 976, 1636, 2394): found.setdefault(v, []).append(c)
for v in sorted(found):
    P('%5d cells at %d cap setting(s); smallest %s (n_max,e_max,l_max,k_max,f_max)' % (v, len(found[v]), found[v][0]))
CAP216 = found.get(216, [None])[0]
X216 = L8_at(CAP216) if CAP216 else []
if X216:
    R = r2lib.Rset(X216); P('216-cell index: |X| %d  |R(X)| %d  E = %d  R(X)==X %s' % (len(X216), len(R), len(R) - len(X216), R == set(X216)))

# ---------------------------------------------------------------- 4. the may-precede lemma (A.7) on the tower
P('')
P('=== 4. the Lemma of L4298-4300 ("if X closed and u < v on axis i then u may precede v") ===')
def fibres(X, i):
    d = len(X[0]); F = collections.defaultdict(list)
    for x in X: F[x[i]].append(tuple(x[j] for j in range(d) if j != i))
    return {u: np.array(sorted(set(v)), dtype=np.int64) for u, v in F.items()}
def enc(A, rad):
    w = np.cumprod(np.concatenate(([1], rad[:-1]))); return A @ w
def may_precede(Fu, Fv, rad):
    ku, kv = set(enc(Fu, rad).tolist()), set(enc(Fv, rad).tolist())
    mn = np.minimum(Fu[:, None, :], Fv[None, :, :]).reshape(-1, Fu.shape[1])
    mx = np.maximum(Fu[:, None, :], Fv[None, :, :]).reshape(-1, Fu.shape[1])
    bad_meet = int(sum(1 for t in enc(mn, rad).tolist() if t not in ku))
    bad_join = int(sum(1 for t in enc(mx, rad).tolist() if t not in kv))
    return bad_meet, bad_join
for X, tag in ((L8, 'L8'), (L9, 'L9')):
    d = len(X[0]); A = alpha(X); tot = ok = 0; tot_rel = 0
    Ar = np.array(X, dtype=np.int64).max(axis=0) + 1
    for i in range(d):
        rad = np.array([Ar[j] for j in range(d) if j != i], dtype=np.int64)
        F = fibres(X, i); vals = A[i]
        rel = {}
        for u, v in itertools.permutations(vals, 2):
            bm, bj = may_precede(F[u], F[v], rad); rel[(u, v)] = (bm == 0 and bj == 0); tot_rel += 1
            if u < v:
                tot += 1; ok += 1 if rel[(u, v)] else 0
        tot_order = all(rel[(u, v)] != rel[(v, u)] for u, v in itertools.combinations(vals, 2))
        if tag == 'L8':
            P('  axis %-3s |A| %d  u<v pairs %2d all-satisfy %s   "may precede" antisymmetric on this axis %s'
              % (NAMES8[i], len(vals), sum(1 for u, v in itertools.combinations(vals, 2)), all(rel[(u, v)] for u, v in itertools.combinations(vals, 2)), tot_order))
    P('%-4s ordered pairs tested %3d;  u<v pairs %3d, satisfying the lemma %3d  -> lemma holds %s'
      % (tag, tot_rel, tot, ok, ok == tot))

# ---------------------------------------------------------------- 5. the d = 2 converse, exhaustively
P('')
P('=== 5. the d = 2 criterion, exhaustive (L4302 prints "120 sets; 274 of 274") ===')
def closed2(S):
    for x in S:
        for y in S:
            if (min(x[0], y[0]), min(x[1], y[1])) not in S or (max(x[0], y[0]), max(x[1], y[1])) not in S: return False
    return True
def mayprec2(S, m):
    F = collections.defaultdict(set)
    for a, b in S: F[a].add(b)
    rel = {}
    for u in range(m):
        for v in range(m):
            if u == v or u not in F or v not in F: continue
            rel[(u, v)] = all(min(p, q) in F[u] and max(p, q) in F[v] for p in F[u] for q in F[v])
    return F, rel
for m, c in ((3, 3), (4, 3)):
    cells = [(a, b) for a in range(m) for b in range(c)]
    n_sets = tested = crit_yes = actually = mismatch = relabel_closed = 0
    for mask in range(1, 1 << len(cells)):
        S = frozenset(cells[i] for i in range(len(cells)) if mask >> i & 1)
        sup = sorted({a for a, _ in S})
        if len(sup) < 2: continue
        tested += 1
        idx = {u: i for i, u in enumerate(sup)}
        S2 = frozenset((idx[a], b) for a, b in S)
        F, rel = mayprec2(S2, len(sup))
        tot = all(rel.get((u, v), False) != rel.get((v, u), False) for u, v in itertools.combinations(range(len(sup)), 2))
        yes = False
        for perm in itertools.permutations(range(len(sup))):
            rk = {u: perm[u] for u in range(len(sup))}
            if closed2(frozenset((rk[a], b) for a, b in S2)): yes = True; break
        crit_yes += tot; actually += yes; mismatch += (tot != yes)
        if tot:
            # the criterion's own relabelling: order u by the number of v it may precede
            score = {u: sum(1 for v in range(len(sup)) if v != u and rel.get((u, v), False)) for u in range(len(sup))}
            rk = {u: len(sup) - 1 - score[u] for u in score}
            relabel_closed += closed2(frozenset((rk[a], b) for a, b in S2))
    P('A0 x A1 = %d x %d : %6d sets with >=2 values on A0;  criterion says closed-under-some-order %6d;  brute force %6d;  mismatches %d;  criterion order actually closes %6d of %6d'
      % (m, c, tested, crit_yes, actually, mismatch, relabel_closed, crit_yes))

# ---------------------------------------------------------------- 6. the constraint graph is a tree
P('')
P('=== 6. the constraint graph (L4309, L4326) ===')
# the seven Heaviside constraints of tower-2.py L8(): l<=n-1, k<=4l+2, q<=k, 2S<=k, g<=q, g<=4f+2, f<=e-1
E = [(0, 1), (1, 2), (2, 3), (2, 7), (3, 6), (6, 5), (5, 4)]
P('edges %s' % [(NAMES8[a], NAMES8[b]) for a, b in E])
P('nodes 8, edges %d, is_tree %s' % (len(E), r2lib.is_tree(8, E)))
adj = collections.defaultdict(set)
for a, b in E: adj[a].add(b); adj[b].add(a)
par = {0: None}; order = [0]; st = [0]
while st:
    u = st.pop()
    for w in sorted(adj[u]):
        if w not in par: par[w] = u; order.append(w); st.append(w)
P('rooted at n: ' + ', '.join('%s<-%s' % (NAMES8[c], NAMES8[par[c]]) for c in order if par[c] is not None))
sep = [(NAMES8[c], NAMES8[a], NAMES8[b]) for c in range(8) for a, b in itertools.combinations(range(8), 2)
       if a != c and b != c and r2lib.components(E, {c}, nodes=8)[a] != r2lib.components(E, {c}, nodes=8)[b]]
P('cut vertices separating some pair: %s' % sorted({t[0] for t in sep}))
P('non-tree constraints among the seven: %d' % (len(E) - 7))

# ---------------------------------------------------------------- 7. order recovery by propagation along the tree
P('')
P('=== 7. recovery from a scrambled bag: L4312 "20 of 20, at two cap settings, on 216 and 976 cells" ===')
def recover(X, E, cap_nodes=400000):
    """Root the tree, fix the root by brute force, extend along the tree with backtracking.
    A child order is accepted iff the 2-D projection onto (parent, child) is closed under the two
    orders — the d = 2 criterion of L4302, which is the only local test §15.4 offers."""
    d = len(X[0]); A = [sorted({x[i] for x in X}) for i in range(d)]
    proj = {}
    for a, b in E:
        proj[(a, b)] = frozenset((x[a], x[b]) for x in X); proj[(b, a)] = frozenset((x[b], x[a]) for x in X)
    adj = collections.defaultdict(set)
    for a, b in E: adj[a].add(b); adj[b].add(a)
    par = {0: None}; seq = [0]; st = [0]
    while st:
        u = st.pop()
        for w in sorted(adj[u]):
            if w not in par: par[w] = u; seq.append(w); st.append(w)
    sols = []; nodes = [0]
    def ok_pair(p, c, rp, rc):
        S = frozenset((rp[a], rc[b]) for a, b in proj[(p, c)])
        return closed2(S)
    def go(k, rank):
        nodes[0] += 1
        if nodes[0] > cap_nodes: return
        if k == len(seq): sols.append(dict(rank)); return
        ax = seq[k]
        for perm in itertools.permutations(range(len(A[ax]))):
            rk = {v: perm[i] for i, v in enumerate(A[ax])}
            if par[ax] is not None and not ok_pair(par[ax], ax, rank[par[ax]], rk): continue
            rank[ax] = rk; go(k + 1, rank); del rank[ax]
            if len(sols) > 200: return
    go(0, {})
    return sols, nodes[0], A
def scramble(X, seed):
    rnd = random.Random(seed); d = len(X[0]); A = [sorted({x[i] for x in X}) for i in range(d)]
    pi = []
    for a in A:
        lab = list(range(len(a))); rnd.shuffle(lab); pi.append({v: lab[i] for i, v in enumerate(a)})
    return [tuple(pi[i][x[i]] for i in range(d)) for x in X], pi
for X, tag in ((X216, '216 cells'), (L8, '976 cells')):
    if not X: continue
    good = glob_ok = trials = 0; costs = []; local_only = 0
    for seed in range(20):
        Y, pi = scramble(X, seed); trials += 1
        sols, nodes, A = recover(Y, E); costs.append(nodes)
        if not sols: continue
        good += 1
        hit = False; bad_local = 0
        for r in sols:
            Z = [tuple(r[i][y[i]] for i in range(len(y))) for y in Y]
            if r2lib.Rset(Z) == set(Z): hit = True
            else: bad_local += 1
        glob_ok += hit; local_only += bad_local
    Asz = [len(a) for a in alpha(X)]
    import math
    P('%-9s trials %2d  an order found %2d of %2d  a found order closes globally %2d of %2d  candidate orders passing every local test but failing closure %d  search nodes min/max %d/%d'
      % (tag, trials, good, trials, glob_ok, trials, local_only, min(costs), max(costs)))
    P('%-9s alphabet sizes %s  sum|A_i|! = %d   prod|A_i|! = %d   (L4315: cost is the sum, never the product)'
      % (tag, Asz, sum(math.factorial(z) for z in Asz), int(np.prod([math.factorial(z) for z in Asz], dtype=object))))

# ---------------------------------------------------------------- 8. the figure's stated bound, and the failed methods
P('')
P('=== 8. Figure 15.1 caption (L4321) and the two failed methods (L4317) ===')
P('q <= k on every cell of L8: %s  (q attains k on %d cells; q ranges %s, k ranges %s)'
  % (all(c[3] <= c[2] for c in L8), sum(1 for c in L8 if c[3] == c[2]), (min(c[3] for c in L8), max(c[3] for c in L8)), (min(c[2] for c in L8), max(c[2] for c in L8))))
P('L4317 prints "0 of 12", then "42%% and 25%%" with no denominator.')
for num in range(0, 13):
    if abs(num / 12 * 100 - 42) < 0.5: P('  42%% is %d/12 = %.2f%% (rounded)' % (num, num / 12 * 100))
    if abs(num / 12 * 100 - 25) < 0.5: P('  25%% is %d/12 = %.2f%% (exact)' % (num, num / 12 * 100))
P('neither method is specified in the section; the two rates are not re-measurable from the text (13j-07 class).')
