import itertools, json, sys
from gen import build

def Rn_count(S,d=8):
    S=list(S); A=[sorted({c[i] for c in S}) for i in range(d)]
    def env(i,j):
        m={}
        for c in S: m[c[j]]=max(m.get(c[j],-10**9),c[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return sum(1 for x in itertools.product(*A)
               if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j))

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

def all_min_covers(X,d=8,cap_sols=200000):
    els=elements(X,d)
    cand=sorted(set().union(*els))
    cmap={c:i for i,c in enumerate(cand)}
    E=[frozenset(cmap[c] for c in e) for e in els]
    cov={ci:set() for ci in range(len(cand))}
    for ei,e in enumerate(E):
        for ci in e: cov[ci].add(ei)
    NE=len(E); trunc=[False]
    def search(k):
        sols=set()
        def bb(chosen,covered):
            if len(sols)>=cap_sols: trunc[0]=True; return
            if len(covered)==NE: sols.add(tuple(sorted(chosen))); return
            if len(chosen)==k: return
            unc=[ei for ei in range(NE) if ei not in covered]
            ei=min(unc,key=lambda e:len(E[e]))
            for ci in E[ei]:
                if ci not in chosen: bb(chosen|{ci},covered|cov[ci])
        bb(frozenset(),frozenset())
        return sorted(sols)
    for k in range(1,15):
        sols=search(k)
        if sols: return len(els),cand,k,sols,trunc[0]
    return len(els),cand,None,[],False

def census(X,cand,sols):
    covers=[[X[cand[ci]] for ci in s] for s in sols]
    N=len(covers)
    def frac(pred): return sum(1 for cv in covers if any(pred(c) for c in cv))
    kmaxes={}
    out={
      "s->s": frac(lambda c:c[1]==0 and c[5]==0),
      "s->p": frac(lambda c:c[1]==0 and c[5]==1),
      "p->s": frac(lambda c:c[1]==1 and c[5]==0),
      "p->p": frac(lambda c:c[1]==1 and c[5]==1),
      "null q=0": frac(lambda c:c[3]==0),
      "full q=k": frac(lambda c:c[3]==c[2]),
    }
    common=set(sols[0])
    for s in sols[1:]: common&=set(s)
    return N,out,[X[cand[ci]] for ci in sorted(common)]

def bits(c,X):
    A=[sorted({x[i] for x in X}) for i in range(8)]
    return "".join("1" if c[i]==A[i][-1] else "0" if c[i]==A[i][0] else "." for i in range(8))

CAPS=[(2,2,1,3,1),(3,3,1,3,1),(4,4,1,3,1),(3,3,2,6,2)]
R={}
for cp in CAPS:
    X=build(*cp,lambda k:0,False)
    E0=Rn_count(X)-len(X)
    ne,cand,k,sols,trunc=all_min_covers(X)
    N,ch,comm=census(X,cand,sols)
    R[str(cp)]={"cells":len(X),"E":E0,"elements":ne,"seed":k,"covers":N,"truncated":trunc,
                "channels":ch,"universal_cells":[(c,bits(c,X)) for c in comm]}
    print(f"cap {cp}: cells {len(X)}  E={E0}  seed={k}  covers={N}{' (TRUNC)' if trunc else ''}")
    for name,v in ch.items(): print(f"   {name:10s} {v}/{N} {'U' if v==N else ''}")
    print(f"   universal cells: {len(comm)}")
    for c in comm: print(f"     {c}  {bits(c,X)}")
json.dump(R,open("sweep.json","w"),default=str)