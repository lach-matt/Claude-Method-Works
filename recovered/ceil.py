import numpy as np, eldata as ed, itertools
from itertools import combinations
from collections import Counter
CAP=lambda l: 2*(2*l+1)
occ=set(ed.E.values())
def leq(a,b): return all(x<=y for x,y in zip(a,b))

def build(NMAX,LMAX):
    return [(n,l,k) for n in range(1,NMAX+1) for l in range(0,min(n,LMAX+1))
            for k in range(1,CAP(l)+1)]
def props(NMAX,LMAX):
    L=build(NMAX,LMAX); S=set(L)
    jn=lambda a,b: tuple(max(x,y) for x,y in zip(a,b))
    mt=lambda a,b: tuple(min(x,y) for x,y in zip(a,b))
    # closure
    cl=all(jn(a,b) in S and mt(a,b) in S for a,b in combinations(L,2))
    # 2n^2
    twon2=all(sum(CAP(l) for l in range(0,min(n,LMAX+1)))==2*n*n for n in range(1,NMAX+1))
    # parity
    ev=sum(1 for c in L if sum(c)%2==0)
    par=(ev==len(L)-ev)
    # rank symmetry
    rk=Counter(sum(c) for c in L)
    seq=[rk[i] for i in range(min(rk),max(rk)+1)]
    sym=(seq==seq[::-1])
    # min element
    mn=min(L)
    # reserved cells (occupied set fixed)
    res=sum(1 for c in L if c not in occ)
    # columns
    cols=[(n,l) for n in range(1,NMAX+1) for l in range(0,min(n,LMAX+1))]
    occols=set((n,l) for (n,l,k) in occ)
    # down-sets of column poset
    def cleq(a,b): return a[0]<=b[0] and a[1]<=b[1]
    ds=[0]
    order=sorted(cols)
    def enum(i,ch):
        if i==len(order): ds[0]+=1; return
        c=order[i]; enum(i+1,ch)
        if all(d in ch for d in cols if cleq(d,c) and d!=c): enum(i+1,ch|{c})
    if len(cols)<=30: enum(0,frozenset())
    else: ds[0]=None
    # ideal property of occupied set within this lattice
    ideal=not any(leq(y,x) and y not in occ for x in occ for y in L)
    # maximal occupied + covering
    maxel=[x for x in occ if not any(leq(x,y) and x!=y for y in occ)]
    nxt=set()
    for m in maxel:
        for d in range(3):
            c=list(m); c[d]+=1; c=tuple(c)
            if c in S and c not in occ: nxt.add(c)
    # Sperner: largest rank level
    return dict(cells=len(L), closed=cl, twon2=twon2, parity=par, ranksym=sym,
                minel=mn, reserved=res, cols=len(cols), downsets=ds[0],
                ideal=ideal, maxel=len(maxel), covering=len(nxt),
                maxrank=max(rk.values()))

print("="*100)
print("CEILING SENSITIVITY: which results survive a change of n_max and l_max?")
print("="*100)
cfgs=[(7,4),(8,4),(7,5),(8,5),(9,4),(7,3)]
res={}
for c in cfgs: res[c]=props(*c)
keys=['cells','closed','twon2','parity','ranksym','minel','reserved','cols',
      'downsets','ideal','maxel','covering','maxrank']
print(f"  {'property':<22}"+"".join(f"{str(c):>12}" for c in cfgs))
print("  "+"-"*(22+12*len(cfgs)))
for k in keys:
    vals=[res[c][k] for c in cfgs]
    inv = len(set(map(str,vals)))==1
    tag='  INVARIANT' if inv else '  contingent'
    print(f"  {k:<22}"+"".join(f"{str(v):>12}" for v in vals)+tag)