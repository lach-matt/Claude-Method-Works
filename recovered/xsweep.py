from itertools import product, permutations, combinations
def opR(X,d):
    X=set(X); vals=[sorted({x[i] for x in X}) for i in range(d)]
    def env(i,j):
        m={}
        for x in X: m[x[j]]=max(m.get(x[j],-10**9),x[i])
        b,o=-10**9,{}
        for t in sorted(m): b=max(b,m[t]); o[t]=b
        return o
    phi={(i,j):env(i,j) for i in range(d) for j in range(d) if i!=j}
    return {x for x in product(*vals) if all(x[i]<=phi[(i,j)][x[j]] for i in range(d) for j in range(d) if i!=j)}
def minE(cells,axes,cap=20000):
    b=None;k=0
    for p in product(*[permutations(range(a)) for a in axes]):
        cs={tuple(p[i].index(x[i]) for i in range(len(axes))) for x in cells}
        E=len(opR(cs,len(axes)))-len(cs)
        b=E if b is None else min(b,E)
        if b==0: return 0
        k+=1
        if k>cap: break
    return b
NMAX=4
LEV=[(n,l,tj) for n in range(1,NMAX+1) for l in range(n)
     for tj in ([1] if l==0 else [2*l-1,2*l+1])]
def e1(h,f):
    return f[0]>h[0] and abs(f[1]-h[1])==1 and abs(f[2]-h[2])<=2
CELLS=[(h,f) for h in LEV for f in LEV if e1(h,f)]
# coordinate POOL — each is read off the cell, none adjoined to the others
P={
 "n_hole":      lambda h,f: h[0],
 "l_hole":      lambda h,f: h[1],
 "2j_hole":     lambda h,f: h[2],
 "n_fill":      lambda h,f: f[0],
 "l_fill":      lambda h,f: f[1],
 "2j_fill":     lambda h,f: f[2],
 "dn":          lambda h,f: f[0]-h[0],
 "dl":          lambda h,f: f[1]-h[1],
 "d2j":         lambda h,f: f[2]-h[2],
 "jtype_hole":  lambda h,f: 1 if h[2]==2*h[1]+1 else 0,
 "jtype_fill":  lambda h,f: 1 if f[2]==2*f[1]+1 else 0,
}
names=list(P)
res=[]
for tri in combinations(names,3):
    cells={tuple(P[t](h,f) for t in tri) for h,f in CELLS}
    axes=[len({c[i] for c in cells}) for i in range(3)]
    rel={i:{v:k for k,v in enumerate(sorted({c[i] for c in cells}))} for i in range(3)}
    cells={tuple(rel[i][c[i]] for i in range(3)) for c in cells}
    if max(axes)>6: continue
    E=minE(cells,axes)
    res.append((E,len(cells),axes[0]*axes[1]*axes[2],tri))
res.sort()
print(f"{'coordinates':<40}{'cells':>6}{'box':>6}{'minE':>6}")
for E,n,box,tri in res[:12]:
    print(f"{' x '.join(tri):<40}{n:>6}{box:>6}{E:>6}")
print(f"\ntotal 3-coordinate systems tried: {len(res)}")
print(f"systems reaching E = 0 : {sum(1 for r in res if r[0]==0)}")
print(f"systems reaching E = 1 : {sum(1 for r in res if r[0]==1)}")