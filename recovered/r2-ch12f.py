# r2-ch12f.py — Phase R2, main §12.11.0.1 "The clock in the constraint" (chat 73). Beside tower-2.py.
# Λ9 rebuilt from §7.1's seven constraints with the caps (n, e, ℓ, k, f) named at MC L1286; the book's caps (3,3,1,3,1)
# reproduce tower-2.py's L9 cell for cell. Every claim measured on all cells / all 1,654² ordered pairs.
import sys, itertools
sys.setrecursionlimit(10000)
from tower_2 import L9 as T9  # tower-2.py copied to tower_2.py for import (identical bytes)

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

def src(c): return (c[0],c[1],c[2],c[7])
def tgt(c): return (c[4],c[5],c[6],c[8])

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

cells, objs, edges, comps = analyse((3,3,1,3,1), full=True)
T=T9(); print(f'tower-2.py L9 identical to build9((3,3,1,3,1)): {sorted(T)==sorted(cells)}')
# --- J(Λ9), length, down-set word length ---
S=set(cells); d=9
def leq(x,y): return all(a<=b for a,b in zip(x,y))
rank=lambda c: sum(c)
cells_sorted=sorted(cells, key=rank)
# lower covers via coordinatewise: y covers x iff y-x is a unit vector and both in S? Not in general (constraints); use rank grading: x<y with rank diff 1 and x ≤ y.
byrank={}
for c in cells: byrank.setdefault(rank(c),[]).append(c)
lower={c:[] for c in cells}
for r in sorted(byrank):
    for y in byrank[r]:
        for x in byrank.get(r-1,()):
            if leq(x,y): lower[y].append(x)
J=[c for c in cells if len(lower[c])==1]
ranks=sorted(byrank); print(f'Λ9 ranks {ranks[0]}..{ranks[-1]} = length {ranks[-1]-ranks[0]} | join-irreducibles (exactly one lower cover) {len(J)} | graded by coordinate sum (every cover raises rank by 1): {all(all(rank(y)-rank(x)==1 for x in lower[y]) for y in cells)} | Λ8 for comparison: 17 (r2-ch12c)')
# --- pair census on all ordered pairs ---
idx={c:i for i,c in enumerate(cells)}; n=len(cells)
comp_unord=0
for i in range(n):
    x=cells[i]
    for j in range(i+1,n):
        y=cells[j]
        if leq(x,y) or leq(y,x): comp_unord+=1
print(f'ordered pairs {n*n:,} = 1,654² | comparable unordered x<y {comp_unord:,} | ordered both orientations {2*comp_unord:,} = {100*2*comp_unord/(n*n):.1f}% | with x = y added {2*comp_unord+n:,}')
# composition reachability on cells: a→b iff tgt(a) = src(b); closure by bitmask iteration
bysrc={}
for c in cells: bysrc.setdefault(src(c),[]).append(idx[c])
succ=[bysrc.get(tgt(c),[]) for c in cells]
nedges=sum(len(s) for s in succ)
reach=[0]*n
for i in range(n):
    m=0
    for j in succ[i]: m|=1<<j
    reach[i]=m
changed=True; it=0
while changed:
    changed=False; it+=1
    for i in range(n):
        m=reach[i]; new=m
        # OR in reach of every direct successor
        for j in succ[i]: new|=reach[j]
        if new!=m: reach[i]=new; changed=True
paths=sum(bin(m).count('1') for m in reach)
refl=sum(1 for i in range(n) if reach[i]>>i & 1)
print(f'composability edges a→b {nedges:,} | pairs joined by a composition path (length ≥ 1) {paths:,} = {100*paths/(n*n):.1f}% (closure iterations {it}) | of which a→a (a on a cycle) {refl:,} | path pairs with a ≠ b {paths-refl:,}')
# both: ordered (a,b), a≠b, path a→b and (a ≤ b or b ≤ a); split by orientation
both_le=0; both_ge=0
for i in range(n):
    m=reach[i]; a=cells[i]
    j=0
    while m:
        if m&1 and j!=i:
            b=cells[j]
            if leq(a,b): both_le+=1
            elif leq(b,a): both_ge+=1
        m>>=1; j+=1
both=both_le+both_ge
print(f'in both (path a→b and comparable, a ≠ b) {both:,} = {100*both/(n*n):.2f}% of all pairs | a < b {both_le:,}, a > b {both_ge:,} | with a = b on a cycle added {both+refl:,}')
print(f'shares: both / comparable-ordered {100*both/(2*comp_unord):.1f}% | both / path pairs {100*both/paths:.1f}% | both / all pairs {100*both/(n*n):.2f}% | neither contains the other: comparable-not-joined {2*comp_unord-both:,}, joined-not-comparable {paths-refl-both:,}')
# --- variation ---
for caps in [(4,4,1,6,1),(4,4,2,6,2),(5,5,2,6,2)]:
    analyse(caps)
