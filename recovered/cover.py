import itertools, json, sys
from gen import build

def envelope_elements(X,d=8):
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

def solve(X, d=8, kmax=12):
    els=envelope_elements(X,d)
    cand=sorted(set().union(*els))
    cmap={c:i for i,c in enumerate(cand)}
    E=[frozenset(cmap[c] for c in e) for e in els]
    cov={ci:set() for ci in range(len(cand))}
    for ei,e in enumerate(E):
        for ci in e: cov[ci].add(ei)
    NE=len(E)
    def search(k):
        sols=[]
        def bb(chosen,covered,start_ok):
            if len(covered)==NE:
                sols.append(tuple(sorted(chosen))); return len(sols)<50000
            if len(chosen)==k: return True
            rem=min((e for ei,e in enumerate(E) if ei not in covered_set(covered)),key=len,default=None)
            # pick uncovered element with fewest candidates
            unc=[ei for ei in range(NE) if ei not in covered]
            ei=min(unc,key=lambda e:len(E[e]))
            # bound: remaining elements need coverage; simple bound: if k-len(chosen)==0 handled above
            for ci in E[ei]:
                if ci in chosen: continue
                if not bb(chosen|{ci}, covered|cov[ci], True): return False
            return True
        def covered_set(c): return c
        bb(frozenset(),frozenset(),True)
        # dedupe (different branch orders can find same set)
        return sorted(set(sols))
    for k in range(1,kmax+1):
        sols=search(k)
        if sols:
            return els,cand,k,sols
    return els,cand,None,[]

X=build(3,3,1,3,1, lambda k:0, False)
els,cand,k,sols=solve(X)
print("elements after reduction:",len(els))
print("candidate cells:",len(cand))
print("SEED SIZE:",k,"| minimum covers found (exact, deduped):",len(sols))
covers=[[X[cand[ci]] for ci in s] for s in sols]
json.dump({"seed":k,"n_covers":len(sols),"covers":covers},open("covers8.json","w"))
# universal cells
if sols:
    common=set(sols[0])
    for s in sols[1:]: common&=set(s)
    print("cells common to ALL minimum covers:",len(common))
    for ci in sorted(common): print("  ",X[cand[ci]])