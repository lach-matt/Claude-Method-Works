import itertools, json, sys
from gen import build

def elements(X,d=8):
    els=[]
    for i in range(d):
        for v in sorted({c[i] for c in X}):
            els.append(frozenset(k for k,c in enumerate(X) if c[i]==v))
    for i in range(d):
        for j in range(d):
            if i==j: continue
            m={}
            for c in X: m[c[j]]=max(m.get(c[j],-10**9),c[i])
            b=-10**9
            for t in sorted(m):
                if m[t]>b:
                    b=m[t]
                    els.append(frozenset(k for k,c in enumerate(X) if c[j]<=t and c[i]==b))
    els=list(set(els)); els.sort(key=len)
    keep=[]
    for e in els:
        if not any(k<=e for k in keep): keep.append(e)
    return keep

def min_cover(els, allowed=None):
    if allowed is not None:
        els=[frozenset(c for c in e if c in allowed) for e in els]
        if any(not e for e in els): return None  # infeasible
    cand=sorted(set().union(*els))
    cmap={c:i for i,c in enumerate(cand)}
    E=[frozenset(cmap[c] for c in e) for e in els]
    cov={ci:set() for ci in range(len(cand))}
    for ei,e in enumerate(E):
        for ci in e: cov[ci].add(ei)
    NE=len(E)
    found=[None]
    def bb(chosen,covered,k):
        if found[0]: return
        if len(covered)==NE: found[0]=chosen; return
        if len(chosen)==k: return
        unc=[ei for ei in range(NE) if ei not in covered]
        # bound: max coverage per cell
        ei=min(unc,key=lambda e:len(E[e]))
        for ci in sorted(E[ei],key=lambda c:-len(cov[c])):
            if ci not in chosen: bb(chosen|{ci},covered|cov[ci],k)
    for k in range(1,16):
        found[0]=None
        bb(frozenset(),frozenset(),k)
        if found[0]: return k
    return None

cp=tuple(map(int,sys.argv[1:6]))
X=build(*cp,lambda k:0,False)
els=elements(X)
allcells=set(range(len(X)))
k0=min_cover(els)
print(f"cap {cp}: cells {len(X)}  elements {len(els)}  SEED = {k0}")
conds={
 "s->s":  lambda c:c[1]==0 and c[5]==0,
 "s->p":  lambda c:c[1]==0 and c[5]==1,
 "p->s":  lambda c:c[1]==1 and c[5]==0,
 "p->p":  lambda c:c[1]==1 and c[5]==1,
 "null q=0": lambda c:c[3]==0,
 "full q=k": lambda c:c[3]==c[2],
 "corner3-type (l,k,q,f,g max; 2S min)": lambda c:(c[1]==max(x[1] for x in X) and c[2]==max(x[2] for x in X)
      and c[3]==c[2] and c[5]==max(x[5] for x in X) and c[6]==max(x[6] for x in X) and c[7]==0),
}
res={"cap":cp,"cells":len(X),"seed":k0,"universal":{}}
for name,p in conds.items():
    allowed={i for i,c in enumerate(X) if not p(c)}
    k1=min_cover(els,allowed)
    uni=(k1 is None) or (k1>k0)
    res["universal"][name]=bool(uni)
    print(f"   {name:38s} min w/o it = {k1}  -> {'UNIVERSAL' if uni else 'not universal'}")
json.dump(res,open(f"sweep_{cp[0]}{cp[1]}{cp[2]}{cp[3]}{cp[4]}.json","w"))