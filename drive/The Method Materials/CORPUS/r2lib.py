# r2lib.py — shared instrument library for Phase R2 (chat 74). Ruling 2 of chat 74.
# Every function below is lifted VERBATIM (by AST source segment) from the instrument named in its
# provenance comment, except two marked parameterisations: mi() takes N = len(xs) instead of the module
# constant, and ci_sets() takes the index X as its first argument. Instruments import this module by path:
#   import importlib.util, os; H=os.path.dirname(os.path.abspath(__file__))
#   s=importlib.util.spec_from_file_location('r2lib', os.path.join(H,'r2lib.py')); r2lib=importlib.util.module_from_spec(s); s.loader.exec_module(r2lib)
# and load the tower with r2lib.load_tower() (tower-2.py by path; never copied).
import os, sys, math, itertools, importlib.util, collections, hashlib
from collections import Counter, defaultdict
import numpy as np
H = os.path.dirname(os.path.abspath(__file__))

def load_tower():
    s = importlib.util.spec_from_file_location('tower2', os.path.join(H, 'tower-2.py')); T = importlib.util.module_from_spec(s); s.loader.exec_module(T); return T

def read_member(name, binary=False):
    return open(os.path.join(H, name), 'rb').read() if binary else open(os.path.join(H, name), encoding='utf-8').read()

def md5(b):
    return hashlib.md5(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()

def lam9p(L9):
    """Λ₉′ = Λ₉ ∩ {2S′ ≤ 2f+1} (r2-ch12i.py)."""
    return [c for c in L9 if c[8] <= 2 * c[5] + 1]

def gG_index(T):
    """The 13,775-cell (g, G) index of MC L1306 (r2-ch12k.py): Λ₈ cells extended by G ∈ [g, 4f+2] and 2S′ ∈ [0, G]."""
    n_, l_, k_, q_, e_, f_, g_, S_, G_, Sp_ = range(10)
    X = [c + (G, S2p) for c in T.L8() for G in range(c[g_], 4 * c[f_] + 2 + 1) for S2p in range(0, G + 1)]
    return X

# ---- Λ₉ / Λ₉′ constants (r2-ch12i.py) ----
NAMES = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', '2S′']
SRC, TGT, Q = [0, 1, 2, 7], [4, 5, 6, 8], 3
EDGES9 = [(0, 1), (1, 2), (2, 3), (2, 7), (4, 5), (5, 6), (3, 6), (6, 8)]
EDGES9P = EDGES9 + [(5, 8)]

# ---- (g, G) index constants (r2-ch12k.py) ----
n_, l_, k_, q_, e_, f_, g_, S_, G_, Sp_ = range(10)
NAMES10 = ['n', 'ℓ', 'k', 'q', 'e', 'f', 'g', '2S', 'G', '2S′']
ARROWS = {'shell': (n_, e_), 'subshell': (l_, f_), 'occupancy': (k_, G_), 'spin': (S_, Sp_)}
DIST = {('shell', 'subshell'): 1, ('subshell', 'occupancy'): 1, ('occupancy', 'spin'): 1, ('subshell', 'spin'): 2, ('shell', 'occupancy'): 2, ('shell', 'spin'): 3}
EDGES10 = [(n_, l_), (l_, k_), (k_, q_), (k_, S_), (e_, f_), (f_, g_), (q_, g_), (g_, G_), (f_, G_), (G_, Sp_)]

# lifted verbatim from r2-ch12f.py (chat 73)
def build9(caps):
    N,E,LM,KM,FM = caps
    out=[]
    for n in range(1,N+1):
      for l in range(0,min(LM,n-1)+1):
        for k in range(1,min(KM,4*l+2)+1):
          for q in range(0,k+1):
            for e in range(1,E+1):
              for f in range(0,min(FM,e-1)+1):
                for g in range(0,min(4*f+2,q)+1):
                  for S2 in range(0,k+1):
                    for S2p in range(0,g+1):
                      out.append((n,l,k,q,e,f,g,S2,S2p))
    return out

# lifted verbatim from r2-ch12f.py (chat 73)
def src(c): return (c[0],c[1],c[2],c[7])

# lifted verbatim from r2-ch12f.py (chat 73)
def tgt(c): return (c[4],c[5],c[6],c[8])

# lifted verbatim from r2-ch12f.py (chat 73)
def leq(x,y): return all(a<=b for a,b in zip(x,y))

# lifted verbatim from r2-ch12f.py (chat 73)
def tarjan(nodes, adj):
    idx={}; low={}; st=[]; on=set(); comps=[]; counter=[0]
    def strong(v):
        idx[v]=low[v]=counter[0]; counter[0]+=1; st.append(v); on.add(v)
        for w in adj.get(v,()):
            if w not in idx: strong(w); low[v]=min(low[v],low[w])
            elif w in on: low[v]=min(low[v],idx[w])
        if low[v]==idx[v]:
            comp=[]
            while True:
                w=st.pop(); on.discard(w); comp.append(w)
                if w==v: break
            comps.append(comp)
    for v in nodes:
        if v not in idx: strong(v)
    return comps

# lifted verbatim from r2-ch12f.py (chat 73)
def analyse(caps, full=False):
    cells=build9(caps)
    objs=sorted({src(c) for c in cells}); O=set(objs)
    tg=sorted({tgt(c) for c in cells})
    ident=sum(1 for c in cells if src(c)==tgt(c))
    edges={}
    for c in cells:
        if tgt(c) in O: edges.setdefault((src(c),tgt(c)),0); edges[(src(c),tgt(c))]+=1
    raising=sum(1 for c in cells if tgt(c) in O and c[6]>c[2])
    raising_all=sum(1 for c in cells if c[6]>c[2])
    adj={}
    for (a,b) in edges: adj.setdefault(a,[]).append(b)
    comps=tarjan(objs, adj)
    comps=sorted(comps, key=lambda cp:-max(o[2] for o in cp))
    sizes=[(len(cp), sorted({o[2] for o in cp})) for cp in comps]
    complete=[all((a,b) in edges for a in cp for b in cp) for cp in comps]
    # quotient
    cid={o:i for i,cp in enumerate(comps) for o in cp}
    qedges={(cid[a],cid[b]) for (a,b) in edges if cid[a]!=cid[b]}
    nC=len(comps)
    chain = all(((i,j) in qedges) for i in range(nC) for j in range(i+1,nC))  # every earlier (higher k) reaches every later directly
    back = any((j,i) in qedges for i in range(nC) for j in range(i+1,nC))
    conserv_all=sum(1 for c in cells if c[6]==c[3])
    comp_cells=[c for c in cells if tgt(c) in O]
    conserv_comp=sum(1 for c in comp_cells if c[6]==c[3])
    rev_edges=sum(1 for (a,b) in edges if (b,a) in edges)
    rev_edges_noloop=sum(1 for (a,b) in edges if a!=b and (b,a) in edges)
    rev_cells=sum(edges[(a,b)] for (a,b) in edges if (b,a) in edges)
    intra=sum(1 for (a,b) in edges if cid[a]==cid[b])
    allcons=[o for o in objs if all(c[6]==c[3] for c in comp_cells if tgt(c)==o)]
    kmax=max(o[2] for o in objs)
    print(f'caps {caps}: |Λ9| {len(cells):,} | objects {len(objs)} | distinct targets {len(tg)} | identity cells {ident} | edges (ordered object pairs joined by ≥1 cell, target ∈ objects) {len(edges):,} of {len(objs)**2:,} | edges incl. non-object targets {len({(src(c),tgt(c)) for c in cells}):,} of {len(objs)*len(tg):,}')
    print(f'   steps raising k (g > k): among cells with object target {raising}, among all cells {raising_all} | SCCs {len(comps)} sizes/k {sizes} | complete digraph inside each SCC {complete} | quotient is a chain (i<j ⇒ edge) {chain}, any upward edge {back} | intra-SCC edges {intra}')
    print(f'   conservative (g = q): {conserv_all:,} of {len(cells):,} = {100*conserv_all/len(cells):.1f}% (every cell) | {conserv_comp:,} of {len(comp_cells):,} = {100*conserv_comp/len(comp_cells):.1f}% (composable cells) | reversible: edges with a reverse edge {rev_edges} (excluding loops {rev_edges_noloop}); cells whose (src,tgt) has a reverse {rev_cells:,}')
    print(f'   all-conservative objects: {len(allcons)} at k = {sorted({o[2] for o in allcons})} | objects at k_max = {kmax}: {sum(1 for o in objs if o[2]==kmax)} | every object receives a cell {all(any(tgt(c)==o for c in cells) for o in objs)}')
    return cells, objs, edges, comps

# lifted verbatim from r2-ch12d.py (chat 72)
def is_tree(nv,edges):
    adj=collections.defaultdict(set)
    for a,b in edges: adj[a].add(b); adj[b].add(a)
    seen={0}; st=[0]
    while st:
        u=st.pop()
        for w in adj[u]:
            if w not in seen: seen.add(w); st.append(w)
    return len(seen)==nv and len(edges)==nv-1

# lifted verbatim from r2-ch12i.py (chat 74)
def closure(X):
    A = np.array(X, dtype=np.int64); n = len(A)
    rad = A.max(axis=0) + 1; w = np.cumprod(np.concatenate(([1], rad[:-1])))
    key = np.sort(A @ w)
    Ai, Aj = A[:, None, :], A[None, :, :]
    J = (np.maximum(Ai, Aj) @ w).ravel(); Mt = (np.minimum(Ai, Aj) @ w).ravel()
    jl = int((~np.isin(J, key)).sum()); ml = int((~np.isin(Mt, key)).sum())
    return n * n, jl, ml

# lifted verbatim from r2-ch12i.py (chat 74)
def factor_q(X):
    A = defaultdict(set); B = defaultdict(set)
    for c in X:
        A[c[Q]].add(tuple(c[i] for i in SRC)); B[c[Q]].add(tuple(c[i] for i in TGT))
    return sum(len(A[v]) * len(B[v]) for v in A) - len(X)

# lifted verbatim from r2-ch12i.py (chat 74)
def ci(X, a, b, c):
    """Exact (uniform-law) conditional independence a ⊥ b | c tested on every product cell (v, av, bv),
    av in the support of a given c=v, bv likewise: N(v,av,bv)·N(v) == N(v,av)·N(v,bv).
    Returns (product cells, cells failing the count test, cells with empty support)."""
    Nc, Na, Nb, Nab = Counter(), Counter(), Counter(), Counter()
    for x in X:
        Nc[x[c]] += 1; Na[(x[c], x[a])] += 1; Nb[(x[c], x[b])] += 1; Nab[(x[c], x[a], x[b])] += 1
    cells = fails = empty = 0
    for v in Nc:
        As = sorted(av for (vv, av) in Na if vv == v); Bs = sorted(bv for (vv, bv) in Nb if vv == v)
        for av in As:
            for bv in Bs:
                cells += 1
                if Nab[(v, av, bv)] * Nc[v] != Na[(v, av)] * Nb[(v, bv)]: fails += 1
                if Nab[(v, av, bv)] == 0: empty += 1
    return cells, fails, empty

# lifted verbatim from r2-ch12i.py (chat 74)
def components(edges, removed, nodes=9):
    adj = defaultdict(set)
    for u, v in edges:
        if u not in removed and v not in removed: adj[u].add(v); adj[v].add(u)
    comp = {}
    for s in range(nodes):
        if s in removed or s in comp: continue
        stack = [s]; comp[s] = s
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in comp: comp[v] = s; stack.append(v)
    return comp

# lifted verbatim from r2-ch12i.py (chat 74)
def separates(edges, c, a, b):
    comp = components(edges, {c}); return comp[a] != comp[b]

# lifted verbatim from r2-ch12j.py (chat 74)
def support(X, i): return sorted({x[i] for x in X})

# lifted verbatim from r2-ch12j.py (chat 74)
def direct(X, b, a, agg=max):
    d = defaultdict(list)
    for x in X: d[x[a]].append(x[b])
    return {v: agg(vals) for v, vals in sorted(d.items())}

# lifted verbatim from r2-ch12j.py (chat 74)
def composed(X, b, a, c, agg=max):
    ca = defaultdict(set)
    for x in X: ca[x[a]].add(x[c])
    dc = direct(X, b, c, agg)
    return {v: agg(dc[w] for w in ws) for v, ws in sorted(ca.items())}

# lifted from r2-ch12k.py (chat 74); parameterised: N -> len(xs)
def mi(xs, ys):
    cx, cy, cxy = Counter(xs), Counter(ys), Counter(zip(xs, ys))
    return sum(v / len(xs) * math.log2(v * len(xs) / (cx[x] * cy[y])) for (x, y), v in cxy.items())

# lifted from r2-ch12k.py (chat 74); parameterised: X is the first argument
def ci_sets(X, A, B, C):
    """exact conditional independence of coordinate sets A ⊥ B | C on every product cell of every C-fibre"""
    Nc, Na, Nb, Nab = Counter(), Counter(), Counter(), Counter()
    for x in X:
        a, b, c = tuple(x[i] for i in A), tuple(x[i] for i in B), tuple(x[i] for i in C)
        Nc[c] += 1; Na[(c, a)] += 1; Nb[(c, b)] += 1; Nab[(c, a, b)] += 1
    cells = fails = 0
    byc = defaultdict(lambda: (set(), set()))
    for (c, a) in Na: byc[c][0].add(a)
    for (c, b) in Nb: byc[c][1].add(b)
    for c, (As, Bs) in byc.items():
        for a in As:
            for b in Bs:
                cells += 1
                if Nab[(c, a, b)] * Nc[c] != Na[(c, a)] * Nb[(c, b)]: fails += 1
    return cells, fails


# ---------------------------------------------------------------------------------------------
# Lifted in chat 82 (HANDOFF-34's standing instruction: a batch that copies functions verbatim is
# worse than the library carrying them).  Verbatim from r2-ch13j.py, which generalised them from
# r2-ch13h.py §3/§4 (chat 81); Rset came to r2-ch13h from r2-ch13g.py, and to that from r2-ch12r.py's
# Rbox.  Nothing here is called by any instrument banked before chat 82.
import itertools as _it
import numpy as _np


def Rset(X):
    """ℛ(X): every cell of the ambient box ∏ Âᵢ(X) with xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j (§6.1 L1540)."""
    A = _np.array(sorted(set(X)), dtype=_np.int64); d = A.shape[1]
    vals = [_np.unique(A[:, i]) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i == j: continue
            m = _np.full(int(A[:, j].max()) + 1, -1, dtype=_np.int64)
            for v in vals[j]: m[v] = A[A[:, j] <= v, i].max()
            phi[(i, j)] = m
    G = _np.array(_np.meshgrid(*vals, indexing='ij')).reshape(d, -1).T
    ok = _np.ones(len(G), dtype=bool)
    for (i, j), m in phi.items(): ok &= G[:, i] <= m[G[:, j]]
    return set(map(tuple, G[ok]))


def cover_model(cells):
    """§14.5.7's seed definition as a covering problem (§14.5.9 L3923–3925).  Elements are the value
    slots of the ambient box and the envelope steps (i, j, v) → top; a cell covers a step it witnesses;
    the sixth field of a 'phi' element says whether that step RAISES the envelope (the book's 102-element
    model at Λ₈ is the value slots plus the raising steps).  G ⊆ X covers everything ⟺ ℛ(G) = ℛ(X)."""
    cells = sorted(set(tuple(int(x) for x in c) for c in cells))
    A = _np.array(cells, dtype=_np.int64); n, d = A.shape
    vals = [sorted(set(int(v) for v in A[:, i])) for i in range(d)]
    elems = []; rows = []
    for i in range(d):
        for v in vals[i]:
            elems.append(('val', i, v, v)); rows.append(A[:, i] == v)
    for i in range(d):
        for j in range(d):
            if i == j: continue
            prev = -1
            for v in vals[j]:
                sel = A[:, j] <= v
                top = int(A[sel, i].max())
                elems.append(('phi', i, j, v, top, top > prev)); rows.append(sel & (A[:, i] == top))
                prev = max(prev, top)
    return cells, elems, _np.array(rows), vals


def cover_reduce(Mx):
    """Two exact reductions: drop element e when another element's candidate set is contained in e's;
    then drop any cell whose cover is contained in another cell's.  Returns (kept element indices,
    per-cell bitmasks, non-dominated masks, FULL)."""
    E, n = Mx.shape
    P = _np.packbits(Mx, axis=1)
    keep = []
    for e in range(E):
        sub = ~(P & ~P[e]).any(axis=1)
        dom = False
        for e2 in _np.flatnonzero(sub):
            e2 = int(e2)
            if e2 == e: continue
            if bool((P[e2] == P[e]).all()):
                if e2 < e: dom = True; break
            else:
                dom = True; break
        if not dom: keep.append(e)
    K = Mx[keep]
    masks = []
    for c in range(K.shape[1]):
        m = 0
        for t in _np.flatnonzero(K[:, c]): m |= 1 << int(t)
        masks.append(m)
    uniq = sorted(set(masks))
    nd = [m for m in uniq if m and not any(m != m2 and (m | m2) == m2 for m2 in uniq)]
    return keep, masks, nd, (1 << len(keep)) - 1


def exact_seed(nd, FULL, cap=16):
    """The minimum seed, by branch and bound on the reduced model.  Returns (size, witness masks).
    Settled seed(Λ₈) = 7, seed(Λ₉) = 8, seed(Λ₁₀) = 9 in chat 82."""
    CAND = {}
    def cands(e):
        if e not in CAND: CAND[e] = [m for m in nd if m >> e & 1]
        return CAND[e]
    best = [None]
    def bb(cov, chosen, limit):
        if cov == FULL:
            best[0] = list(chosen); return True
        if len(chosen) >= limit: return False
        rest = FULL & ~cov; pick = None
        while rest:
            b = rest & -rest; e = b.bit_length() - 1; rest ^= b
            c = cands(e)
            if pick is None or len(c) < len(pick): pick = c
            if len(pick) <= 1: break
        for m in pick:
            if bb(cov | m, chosen + [m], limit): return True
        return False
    for limit in range(1, cap + 1):
        best[0] = None
        if bb(0, [], limit): return limit, best[0]
    return None, None


def enum_min_covers(pool, FULL, size):
    """Every minimum cover, as a set of frozensets of cell-cover masks.  Pass the full mask list, not
    only the non-dominated ones, when the count of cell-level covers is what is wanted."""
    CAND = {}
    def cands(e):
        if e not in CAND: CAND[e] = [m for m in pool if m >> e & 1]
        return CAND[e]
    out = set()
    def rec(cov, chosen):
        if cov == FULL:
            if len(chosen) == size: out.add(frozenset(chosen))
            return
        if len(chosen) >= size: return
        rest = FULL & ~cov; pick = None
        while rest:
            b = rest & -rest; e = b.bit_length() - 1; rest ^= b
            c = cands(e)
            if pick is None or len(c) < len(pick): pick = c
            if len(pick) <= 1: break
        for m in pick:
            if m in chosen: continue
            rec(cov | m, chosen + [m])
    rec(0, [])
    return out


def closure_mask(cellsA, mask):
    """ℛ on a subset of a small ambient, by the same box sweep as Rset, on bitmasks.  Validated against
    Rset on every non-empty subset of the 8- and 9-cell ambients (r2-ch13h §4)."""
    if mask == 0: return 0
    X = [cellsA[i] for i in range(len(cellsA)) if mask >> i & 1]
    w = len(X[0])
    vs = [sorted({x[i] for x in X}) for i in range(w)]
    phi = {}
    for i in range(w):
        for j in range(w):
            if i == j: continue
            for v in vs[j]: phi[(i, j, v)] = max(x[i] for x in X if x[j] <= v)
    out = 0
    for n, c in enumerate(cellsA):
        if any(c[i] not in vs[i] for i in range(w)): continue
        if all(c[i] <= phi[(i, j, c[j])] for i in range(w) for j in range(w) if i != j): out |= 1 << n
    return out


def staircase(d, c):
    """Non-increasing d-tuples over {0..c−1}: the 'down-set, c' of §14.5.8 / §14.5.9, ℛ-closed, seeding
    at d + c − 1 exactly (chat 82).  The simplex reading Σx ≤ c−1 has the same cell counts and E > 0."""
    return [t for t in _it.product(range(c), repeat=d) if all(t[i] >= t[i + 1] for i in range(d - 1))]


# lifted VERBATIM from r2-ch12r.py (chat 76), owed to r2lib since chat 74, lifted in chat 83 by
# r2-ch13l.py, which needed the 216-cell cap setting of main L1786 and L4312. The tower at arbitrary
# caps: caps = (n_max, e_max, l_max, k_max, f_max); the canonical (3, 3, 1, 3, 1) returns Λ₈'s 976
# cells, (3, 3, 1, 4, 1) returns 1,636 and (4, 3, 1, 4, 1) returns 2,394. Its companion phi_at is NOT
# lifted: it depends on TERMS, which is still owed.
def L8_at(caps):
    n_max, e_max, l_max, k_max, f_max = caps
    return [(n, l, k, q, e, f, g, S2) for n in range(1, n_max + 1) for l in range(0, min(l_max, n - 1) + 1) for k in range(1, min(k_max, 4 * l + 2) + 1)
            for q in range(0, k + 1) for e in range(1, e_max + 1) for f in range(0, min(f_max, e - 1) + 1) for g in range(0, min(4 * f + 2, q) + 1) for S2 in range(0, k + 1)]


# ---------------------------------------------------------------------------------------------
# Lifted in chat 95 out of r2-ch14i.py (chat 94), which DEFERRED recorded as owed after they were
# copied a second time.  heading_line() is chat 88's exact-token resolver, carried through
# r2-ch14g.py; the other three are chat 94's.  Signatures changed on lift only in that the main
# lines list M is now an explicit first argument instead of a module global, so an instrument may
# hold more than one volume at once.  Bodies are otherwise verbatim.  r2lib did not import re.
import re as _re


def heading_line(M, sec):
    """Line (1-based) of the heading whose number is exactly sec.  Exact-token, never a numeric
    prefix: a prefix rule matches 23.1 inside 23.11.  Last hit wins, as in chat 88."""
    hits = []
    for i, t in enumerate(M, 1):
        m = _re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', t.strip())
        if m and m.group(1) == sec:
            hits.append(i)
    return hits[-1] if hits else None


def section_span(M, sec):
    """[start, end) of a section INCLUDING its subsections.

    Rank is not usable here: the book sets §25.6 and §25.6.1 at the same '###' depth, so a rank
    rule truncates a section at its own first subsection.  The span therefore runs to the next
    heading whose number is not a dotted extension of sec, compared component-wise so that 25.61
    is not read as a child of 25.6."""
    s = heading_line(M, sec)
    if s is None: return None
    want = sec.split('.')
    for i in range(s + 1, len(M) + 1):
        m = _re.match(r'^#{1,4} (\d+(?:\.\d+)*)\.? ', M[i - 1].strip())
        if not m: continue
        got = m.group(1).split('.')
        if got[:len(want)] != want:
            return (s, i)
    return (s, len(M) + 1)


def has_token(text, tok):
    """Word-bounded, case-insensitive containment count.  A bare substring test reads 'gain' out
    of 'against' and inverts the verdict (chat 92's class, hit again in chat 94)."""
    pat = r'(?<![A-Za-z])' + _re.escape(tok) + r'(?![A-Za-z])'
    return len(_re.findall(pat, text, _re.I))


def enclosing(M, ln):
    """Nearest heading above ln.  Appendix headings are lettered ('### A.12'), so a numeric-only
    pattern walks past them and mislabels an appendix line with the last numbered chapter."""
    for i in range(ln, 0, -1):
        m = _re.match(r'^#{2,4} ((?:[A-G]|\d+)(?:\.\d+)*)\.? ', M[i - 1])
        if m:
            n = m.group(1)
            return ('App ' if n[0].isalpha() else '') + n
    return '?'
