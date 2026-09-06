import itertools, sys
from gen import build
sys.setrecursionlimit(100000)

def Rn_count(X, d=8):   # verbatim logic from bank cycle7.py Rn
    X=list(X); A=[sorted({c[i] for c in X}) for i in range(d)]
    def env(i,j):
        m={}
        for c in X: m[c[j]]=max(m.get(c[j],-10**9),c[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return sum(1 for x in itertools.product(*A)
               if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))

def elements(X, d=8):
    """envelope steps + alphabet slots; returns list of frozensets of cell-indices covering each"""
    idx={c:i for i,c in enumerate(X)}
    els=[]
    # alphabet slots
    for i in range(d):
        for v in sorted({c[i] for c in X}):
            els.append(frozenset(k for k,c in enumerate(X) if c[i]==v))
    # envelope steps: for each (i,j), minimal t at each new running-max level V
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in X: m[c[j]]=max(m.get(c[j],-10**9),c[i])
            b=-10**9
            for t in sorted(m):
                if m[t]>b:
                    b=m[t]; V=b
                    els.append(frozenset(k for k,c in enumerate(X) if c[j]<=t and c[i]==V))
    # dedupe & remove supersets (dominated elements)
    els=list(set(els))
    els.sort(key=len)
    keep=[]
    for e in els:
        if not any(k<e for k in keep): keep.append(e)
    return keep

X=build(3,3,1,3,1, lambda k:0, False)
d=8
print("cells:", len(X))
print("E(Lambda8) =", Rn_count(X,d)-len(X))
els=elements(X)
print("cover elements after reduction:", len(els))
# exact B&B minimum cover
cellsets={}
for ei,e in enumerate(els):
    for c in e: cellsets.setdefault(c,set()).add(ei)
best=[None]
def bb(chosen, covered):
    if best[0] is not None and len(chosen)>=best[0][0]: return
    if len(covered)==len(els):
        best[0]=(len(chosen),tuple(sorted(chosen))); return
    # pick uncovered element with fewest candidates
    rem=[ei for ei in range(len(els)) if ei not in covered]
    ei=min(rem,key=lambda e:len(els[e]))
    for c in sorted(els[ei], key=lambda c:-len(cellsets.get(c,()))):
        bb(chosen|{c}, covered|cellsets.get(c,set()))
bb(set(),set())
print("SEED SIZE (exact B&B):", best[0][0])
import json
json.dump({"seed_size":best[0][0],"one_cover":[X[c] for c in best[0][1]]},open("seed8.json","w"))