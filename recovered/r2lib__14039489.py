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
